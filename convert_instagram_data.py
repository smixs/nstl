#!/usr/bin/env python3
"""
Instagram Data Converter
Converts Instagram JSON data to multiple formats for different analysis needs
"""

import json
import pandas as pd
import sqlite3
from pathlib import Path
from datetime import datetime
import sys

class InstagramDataConverter:
    def __init__(self, json_file):
        """Initialize with JSON data"""
        with open(json_file, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.account_name = self.data[0]['ownerUsername'] if self.data else 'unknown'
        
    def to_flat_csv(self, output_file=None):
        """Convert to flat CSV for basic metrics analysis"""
        if not output_file:
            output_file = f"{self.account_name}_metrics.csv"
            
        # Extract flat data
        flat_data = []
        for post in self.data:
            flat_data.append({
                'post_id': post['id'],
                'timestamp': post['timestamp'],
                'type': post['type'],
                'likes': post['likesCount'],
                'comments': post['commentsCount'],
                'engagement': post['likesCount'] + post['commentsCount'],
                'caption_length': len(post['caption']),
                'hashtag_count': len(post['hashtags']),
                'is_carousel': len(post.get('childPosts', [])) > 0,
                'url': post['url']
            })
        
        df = pd.DataFrame(flat_data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"✅ Flat CSV saved to: {output_file}")
        return df
    
    def to_detailed_csv(self, output_dir=None):
        """Convert to multiple CSV files preserving relationships"""
        if not output_dir:
            output_dir = f"{self.account_name}_detailed"
        
        Path(output_dir).mkdir(exist_ok=True)
        
        # 1. Posts table
        posts_data = []
        for post in self.data:
            posts_data.append({
                'post_id': post['id'],
                'shortcode': post['shortCode'],
                'timestamp': post['timestamp'],
                'type': post['type'],
                'caption': post['caption'],
                'likes': post['likesCount'],
                'comments': post['commentsCount'],
                'url': post['url'],
                'is_sponsored': post.get('isSponsored', False),
                'comments_disabled': post.get('isCommentsDisabled', False)
            })
        
        posts_df = pd.DataFrame(posts_data)
        posts_df.to_csv(f"{output_dir}/posts.csv", index=False, encoding='utf-8')
        
        # 2. Hashtags table
        hashtags_data = []
        for post in self.data:
            for tag in post.get('hashtags', []):
                hashtags_data.append({
                    'post_id': post['id'],
                    'hashtag': tag
                })
        
        if hashtags_data:
            hashtags_df = pd.DataFrame(hashtags_data)
            hashtags_df.to_csv(f"{output_dir}/hashtags.csv", index=False, encoding='utf-8')
        
        # 3. Comments table
        comments_data = []
        for post in self.data:
            for comment in post.get('latestComments', []):
                comments_data.append({
                    'post_id': post['id'],
                    'comment_id': comment.get('id', ''),
                    'username': comment.get('ownerUsername', ''),
                    'text': comment.get('text', ''),
                    'timestamp': comment.get('timestamp', ''),
                    'likes': comment.get('likesCount', 0)
                })
        
        if comments_data:
            comments_df = pd.DataFrame(comments_data)
            comments_df.to_csv(f"{output_dir}/comments.csv", index=False, encoding='utf-8')
        
        print(f"✅ Detailed CSVs saved to: {output_dir}/")
        
    def to_parquet(self, output_file=None):
        """Convert to Parquet for efficient storage and analysis"""
        if not output_file:
            output_file = f"{self.account_name}_data.parquet"
        
        # Create comprehensive dataframe
        df = pd.DataFrame(self.data)
        
        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Add calculated fields
        df['engagement'] = df['likesCount'] + df['commentsCount']
        df['caption_length'] = df['caption'].str.len()
        df['hashtag_count'] = df['hashtags'].apply(len)
        df['is_carousel'] = df['childPosts'].apply(lambda x: len(x) > 0)
        
        # Save to parquet
        df.to_parquet(output_file, engine='auto', compression='snappy')
        print(f"✅ Parquet file saved to: {output_file}")
        
    def to_sqlite(self, output_file=None):
        """Convert to SQLite database for complex queries"""
        if not output_file:
            output_file = f"{self.account_name}_data.db"
        
        conn = sqlite3.connect(output_file)
        
        # 1. Create posts table
        posts_data = []
        for post in self.data:
            posts_data.append({
                'post_id': post['id'],
                'shortcode': post['shortCode'],
                'timestamp': post['timestamp'],
                'type': post['type'],
                'caption': post['caption'],
                'likes': post['likesCount'],
                'comments': post['commentsCount'],
                'engagement': post['likesCount'] + post['commentsCount'],
                'url': post['url'],
                'is_sponsored': post.get('isSponsored', False),
                'comments_disabled': post.get('isCommentsDisabled', False)
            })
        
        posts_df = pd.DataFrame(posts_data)
        posts_df.to_sql('posts', conn, if_exists='replace', index=False)
        
        # 2. Create hashtags table
        hashtags_data = []
        for post in self.data:
            for tag in post.get('hashtags', []):
                hashtags_data.append({
                    'post_id': post['id'],
                    'hashtag': tag
                })
        
        if hashtags_data:
            hashtags_df = pd.DataFrame(hashtags_data)
            hashtags_df.to_sql('hashtags', conn, if_exists='replace', index=False)
        
        # 3. Create comments table
        comments_data = []
        for post in self.data:
            for comment in post.get('latestComments', []):
                comments_data.append({
                    'post_id': post['id'],
                    'comment_id': comment.get('id', ''),
                    'username': comment.get('ownerUsername', ''),
                    'text': comment.get('text', ''),
                    'timestamp': comment.get('timestamp', ''),
                    'likes': comment.get('likesCount', 0)
                })
        
        if comments_data:
            comments_df = pd.DataFrame(comments_data)
            comments_df.to_sql('comments', conn, if_exists='replace', index=False)
        
        # Create indexes for better performance
        conn.execute('CREATE INDEX IF NOT EXISTS idx_posts_timestamp ON posts(timestamp)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_posts_engagement ON posts(engagement)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_hashtags_tag ON hashtags(hashtag)')
        
        # Create useful views
        conn.execute('''
            CREATE VIEW IF NOT EXISTS post_performance AS
            SELECT 
                DATE(timestamp) as date,
                COUNT(*) as posts,
                AVG(likes) as avg_likes,
                AVG(comments) as avg_comments,
                AVG(engagement) as avg_engagement
            FROM posts
            GROUP BY DATE(timestamp)
        ''')
        
        conn.execute('''
            CREATE VIEW IF NOT EXISTS hashtag_performance AS
            SELECT 
                h.hashtag,
                COUNT(DISTINCT h.post_id) as usage_count,
                AVG(p.engagement) as avg_engagement
            FROM hashtags h
            JOIN posts p ON h.post_id = p.post_id
            GROUP BY h.hashtag
            ORDER BY avg_engagement DESC
        ''')
        
        conn.commit()
        conn.close()
        
        print(f"✅ SQLite database saved to: {output_file}")
        print("   Sample queries:")
        print("   - SELECT * FROM posts ORDER BY engagement DESC LIMIT 10;")
        print("   - SELECT * FROM hashtag_performance LIMIT 20;")
        print("   - SELECT * FROM post_performance ORDER BY date;")
    
    def create_analysis_package(self, output_dir=None):
        """Create a complete analysis package with all formats"""
        if not output_dir:
            output_dir = f"{self.account_name}_analysis_package"
        
        Path(output_dir).mkdir(exist_ok=True)
        
        print(f"\n📦 Creating complete analysis package for @{self.account_name}...\n")
        
        # 1. Keep original JSON
        json_file = f"{output_dir}/raw_data.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
        print(f"✅ JSON preserved: {json_file}")
        
        # 2. Create flat CSV for quick analysis
        self.to_flat_csv(f"{output_dir}/metrics.csv")
        
        # 3. Create detailed CSVs
        self.to_detailed_csv(f"{output_dir}/detailed")
        
        # 4. Create Parquet for efficient processing
        try:
            self.to_parquet(f"{output_dir}/data.parquet")
        except Exception as e:
            print(f"⚠️  Parquet creation skipped (install pyarrow if needed): {e}")
        
        # 5. Create SQLite for complex queries
        self.to_sqlite(f"{output_dir}/data.db")
        
        # 6. Create README
        readme_content = f"""# Instagram Analysis Package: @{self.account_name}

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## 📁 Files Included:

### 1. raw_data.json
- Original complete data
- Use for: Custom analysis, archiving

### 2. metrics.csv
- Flat file with key metrics
- Use for: Excel, Google Sheets, quick charts
- Columns: post_id, timestamp, type, likes, comments, engagement, etc.

### 3. detailed/
- posts.csv: All posts with captions
- hashtags.csv: Post-hashtag relationships
- comments.csv: All comments data
- Use for: Relational analysis, pivot tables

### 4. data.parquet
- Compressed columnar format
- Use for: Python/Pandas analysis, big data tools
- 70-90% smaller than CSV

### 5. data.db
- SQLite database with indexed tables
- Use for: SQL queries, complex analysis
- Tables: posts, hashtags, comments
- Views: post_performance, hashtag_performance

## 🔍 Quick Start Queries:

### Excel/Sheets (metrics.csv):
- Pivot table by type
- Chart engagement over time
- Filter top posts

### Python (Parquet):
```python
import pandas as pd
df = pd.read_parquet('data.parquet')
df.groupby('type')['engagement'].mean()
```

### SQL (data.db):
```sql
-- Top hashtags
SELECT * FROM hashtag_performance LIMIT 10;

-- Best posting times
SELECT strftime('%H', timestamp) as hour, 
       AVG(engagement) as avg_eng
FROM posts 
GROUP BY hour 
ORDER BY avg_eng DESC;
```

## 📊 Recommended Tools:

- **Quick View**: Excel, Google Sheets → metrics.csv
- **Deep Analysis**: Python, R → data.parquet
- **BI Tools**: Tableau, Power BI → data.db or metrics.csv
- **Custom Apps**: Any language → raw_data.json
"""
        
        with open(f"{output_dir}/README.md", 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print(f"\n✅ Complete analysis package created in: {output_dir}/")
        print("   Check README.md for usage instructions")


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_instagram_data.py <json_file> [format]")
        print("Formats: csv, detailed, parquet, sqlite, all")
        sys.exit(1)
    
    json_file = sys.argv[1]
    format_type = sys.argv[2] if len(sys.argv) > 2 else 'all'
    
    converter = InstagramDataConverter(json_file)
    
    if format_type == 'csv':
        converter.to_flat_csv()
    elif format_type == 'detailed':
        converter.to_detailed_csv()
    elif format_type == 'parquet':
        converter.to_parquet()
    elif format_type == 'sqlite':
        converter.to_sqlite()
    elif format_type == 'all':
        converter.create_analysis_package()
    else:
        print(f"Unknown format: {format_type}")
        print("Available formats: csv, detailed, parquet, sqlite, all")


if __name__ == "__main__":
    main()