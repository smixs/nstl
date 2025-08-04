#!/usr/bin/env python3
"""
Instagram Account Analysis Script
Analyzes Instagram JSON data and generates comprehensive markdown report
"""

import json
import pandas as pd
from datetime import datetime
from collections import Counter
import re
import sys
from pathlib import Path

class InstagramAnalyzer:
    def __init__(self, json_file):
        """Initialize analyzer with JSON data"""
        with open(json_file, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.df = pd.DataFrame(self.data)
        self.account_name = self.data[0]['ownerUsername'] if self.data else 'Unknown'
        self.full_name = self.data[0]['ownerFullName'] if self.data else 'Unknown'
        
    def analyze_engagement(self):
        """Calculate engagement metrics"""
        total_posts = len(self.df)
        total_likes = self.df['likesCount'].sum()
        total_comments = self.df['commentsCount'].sum()
        avg_likes = self.df['likesCount'].mean()
        avg_comments = self.df['commentsCount'].mean()
        
        # Engagement per post
        self.df['engagement'] = self.df['likesCount'] + self.df['commentsCount']
        avg_engagement = self.df['engagement'].mean()
        
        # Top and worst performing posts
        top_posts = self.df.nlargest(5, 'engagement')[['caption', 'engagement', 'likesCount', 'commentsCount', 'timestamp']]
        worst_posts = self.df.nsmallest(5, 'engagement')[['caption', 'engagement', 'likesCount', 'commentsCount', 'timestamp']]
        
        return {
            'total_posts': total_posts,
            'total_likes': total_likes,
            'total_comments': total_comments,
            'avg_likes': round(avg_likes, 2),
            'avg_comments': round(avg_comments, 2),
            'avg_engagement': round(avg_engagement, 2),
            'top_posts': top_posts,
            'worst_posts': worst_posts
        }
    
    def analyze_content_types(self):
        """Analyze different content types"""
        content_types = self.df['type'].value_counts().to_dict()
        
        # Carousel analysis
        carousel_posts = self.df[self.df['childPosts'].apply(lambda x: len(x) > 0)]
        carousel_engagement = carousel_posts['engagement'].mean() if len(carousel_posts) > 0 else 0
        
        return {
            'types': content_types,
            'carousel_count': len(carousel_posts),
            'carousel_avg_engagement': round(carousel_engagement, 2)
        }
    
    def analyze_hashtags(self):
        """Analyze hashtag usage and performance"""
        all_hashtags = []
        hashtag_engagement = {}
        
        for _, post in self.df.iterrows():
            hashtags = post['hashtags']
            engagement = post['engagement']
            all_hashtags.extend(hashtags)
            
            for tag in hashtags:
                if tag not in hashtag_engagement:
                    hashtag_engagement[tag] = []
                hashtag_engagement[tag].append(engagement)
        
        # Calculate average engagement per hashtag
        hashtag_avg_engagement = {
            tag: round(sum(engagements) / len(engagements), 2)
            for tag, engagements in hashtag_engagement.items()
        }
        
        # Sort by usage and engagement
        hashtag_counts = Counter(all_hashtags)
        top_hashtags = hashtag_counts.most_common(15)
        top_performing_hashtags = sorted(hashtag_avg_engagement.items(), key=lambda x: x[1], reverse=True)[:10]
        
        return {
            'total_unique': len(hashtag_counts),
            'top_used': top_hashtags,
            'top_performing': top_performing_hashtags
        }
    
    def analyze_posting_patterns(self):
        """Analyze posting frequency and timing"""
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        self.df['date'] = self.df['timestamp'].dt.date
        self.df['hour'] = self.df['timestamp'].dt.hour
        self.df['day_of_week'] = self.df['timestamp'].dt.day_name()
        self.df['month'] = self.df['timestamp'].dt.month_name()
        
        # Posting frequency
        date_range = (self.df['timestamp'].max() - self.df['timestamp'].min()).days
        posts_per_week = len(self.df) / (date_range / 7) if date_range > 0 else 0
        
        # Best posting times
        hour_engagement = self.df.groupby('hour')['engagement'].agg(['mean', 'count'])
        best_hours = hour_engagement.nlargest(5, 'mean')
        
        # Best days
        day_engagement = self.df.groupby('day_of_week')['engagement'].mean().sort_values(ascending=False)
        
        return {
            'date_range_days': date_range,
            'posts_per_week': round(posts_per_week, 2),
            'best_hours': best_hours,
            'best_days': day_engagement.head(),
            'posting_by_month': self.df['month'].value_counts()
        }
    
    def analyze_captions(self):
        """Analyze caption patterns and language"""
        caption_lengths = self.df['caption'].str.len()
        
        # Language detection (simple approach - checking for Cyrillic vs Latin)
        def detect_language(text):
            if not text:
                return 'unknown'
            cyrillic = len(re.findall(r'[а-яА-ЯёЁ]', text))
            latin = len(re.findall(r'[a-zA-Z]', text))
            if cyrillic > latin:
                return 'russian/uzbek_cyrillic'
            elif latin > cyrillic:
                return 'uzbek_latin/english'
            else:
                return 'mixed'
        
        self.df['language'] = self.df['caption'].apply(detect_language)
        language_dist = self.df['language'].value_counts()
        
        # Caption length vs engagement
        self.df['caption_length'] = caption_lengths
        length_categories = pd.cut(self.df['caption_length'], bins=[0, 500, 1000, 2000, 5000], 
                                  labels=['Short', 'Medium', 'Long', 'Very Long'])
        length_engagement = self.df.groupby(length_categories, observed=False)['engagement'].mean()
        
        return {
            'avg_length': round(caption_lengths.mean(), 0),
            'max_length': caption_lengths.max(),
            'min_length': caption_lengths.min(),
            'language_distribution': language_dist.to_dict(),
            'length_vs_engagement': length_engagement.to_dict()
        }
    
    def analyze_comments(self):
        """Analyze comments and user interactions"""
        total_comments = self.df['commentsCount'].sum()
        posts_with_comments = len(self.df[self.df['commentsCount'] > 0])
        
        # Extract all comments
        all_comments = []
        for _, post in self.df.iterrows():
            if post['latestComments']:
                all_comments.extend(post['latestComments'])
        
        # Comment patterns
        comment_texts = [c['text'] for c in all_comments if 'text' in c]
        
        # Common questions (contains ?)
        questions = [c for c in comment_texts if '?' in c]
        
        return {
            'total_comments': total_comments,
            'posts_with_comments': posts_with_comments,
            'comment_rate': round(posts_with_comments / len(self.df) * 100, 2),
            'sample_questions': questions[:5] if questions else [],
            'total_questions': len(questions)
        }
    
    def generate_report(self, output_file='instagram_analysis.md'):
        """Generate comprehensive markdown report"""
        engagement = self.analyze_engagement()
        content = self.analyze_content_types()
        hashtags = self.analyze_hashtags()
        patterns = self.analyze_posting_patterns()
        captions = self.analyze_captions()
        comments = self.analyze_comments()
        
        report = f"""# Instagram Analysis Report: @{self.account_name}

*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*
*Account: {self.full_name} (@{self.account_name})*

## 📊 Executive Summary

- **Total Posts Analyzed**: {engagement['total_posts']}
- **Date Range**: {patterns['date_range_days']} days
- **Average Engagement**: {engagement['avg_engagement']} interactions per post
- **Posting Frequency**: {patterns['posts_per_week']} posts per week

## 💹 Engagement Metrics

### Overall Performance
- **Total Likes**: {engagement['total_likes']:,}
- **Total Comments**: {engagement['total_comments']:,}
- **Average Likes per Post**: {engagement['avg_likes']}
- **Average Comments per Post**: {engagement['avg_comments']}
- **Engagement Rate**: ~{round((engagement['avg_engagement'] / 10000) * 100, 2)}% (assuming ~10K followers)

### Top 5 Performing Posts
"""
        
        # Add top posts
        for idx, row in engagement['top_posts'].iterrows():
            caption_preview = row['caption'][:100] + '...' if len(row['caption']) > 100 else row['caption']
            report += f"\n{idx+1}. **{int(row['engagement'])} interactions** ({int(row['likesCount'])} likes, {int(row['commentsCount'])} comments)\n"
            report += f"   - Caption: {caption_preview}\n"
            report += f"   - Date: {pd.to_datetime(row['timestamp']).strftime('%Y-%m-%d') if pd.notna(row['timestamp']) else 'N/A'}\n"
        
        report += f"""

## 📝 Content Analysis

### Content Types Distribution
"""
        for content_type, count in content['types'].items():
            percentage = round(count / engagement['total_posts'] * 100, 1)
            report += f"- **{content_type}**: {count} posts ({percentage}%)\n"
        
        report += f"""
- **Carousel Posts**: {content['carousel_count']} (avg engagement: {content['carousel_avg_engagement']})

### Caption Analysis
- **Average Caption Length**: {captions['avg_length']:.0f} characters
- **Language Distribution**:
"""
        for lang, count in captions['language_distribution'].items():
            report += f"  - {lang}: {count} posts\n"
        
        report += f"""

### Caption Length vs Engagement
"""
        for length, eng in captions['length_vs_engagement'].items():
            report += f"- **{length}**: {eng:.1f} avg engagement\n"
        
        report += f"""

## #️⃣ Hashtag Analysis

- **Total Unique Hashtags**: {hashtags['total_unique']}

### Most Used Hashtags
"""
        for tag, count in hashtags['top_used'][:10]:
            report += f"1. #{tag} - used {count} times\n"
        
        report += """

### Best Performing Hashtags (by avg engagement)
"""
        for tag, avg_eng in hashtags['top_performing']:
            report += f"1. #{tag} - {avg_eng} avg engagement\n"
        
        report += f"""

## 📅 Posting Patterns

- **Posts per Week**: {patterns['posts_per_week']}

### Best Posting Times (by engagement)
"""
        for hour, stats in patterns['best_hours'].iterrows():
            report += f"- **{hour}:00**: {stats['mean']:.1f} avg engagement ({int(stats['count'])} posts)\n"
        
        report += """

### Best Days of Week
"""
        for day, eng in patterns['best_days'].items():
            report += f"- **{day}**: {eng:.1f} avg engagement\n"
        
        report += f"""

## 💬 Comment Analysis

- **Total Comments**: {comments['total_comments']}
- **Posts with Comments**: {comments['posts_with_comments']} ({comments['comment_rate']}%)
- **Questions in Comments**: {comments['total_questions']}

### Sample Questions from Audience
"""
        for i, question in enumerate(comments['sample_questions'], 1):
            report += f"{i}. {question}\n"
        
        report += """

## 🎯 Key Insights & Recommendations

### Strengths
1. **Consistent Posting Schedule** - {:.1f} posts per week shows good consistency
2. **High-Quality Content** - Average engagement of {:.0f} indicates resonating content
3. **Strategic Hashtag Use** - {} unique hashtags shows diverse reach strategies

### Areas for Improvement
1. **Increase Comment Rate** - Only {:.1f}% of posts receive comments
2. **Optimize Posting Times** - Focus on peak engagement hours
3. **Content Diversification** - Experiment with different content types

### Action Items
- [ ] Create more carousel posts (higher engagement)
- [ ] Respond to all questions in comments to boost engagement
- [ ] Test posting during peak hours: {}:00-{}:00
- [ ] Use top-performing hashtags more consistently
- [ ] Increase caption length for better storytelling

---
*Note: This analysis is based on public data. For complete insights including saves, shares, and reach, access to Instagram Insights is required.*
""".format(
            patterns['posts_per_week'],
            engagement['avg_engagement'],
            hashtags['total_unique'],
            comments['comment_rate'],
            patterns['best_hours'].index[0] if len(patterns['best_hours']) > 0 else 'N/A',
            patterns['best_hours'].index[0] + 2 if len(patterns['best_hours']) > 0 else 'N/A'
        )
        
        return report
    
    def save_report(self, output_file='instagram_analysis.md'):
        """Save the report to file"""
        report = self.generate_report()
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report saved to {output_file}")
        
    def export_data_summary(self, output_file='instagram_data_summary.csv'):
        """Export summary data to CSV for further analysis"""
        summary_df = self.df[['timestamp', 'type', 'likesCount', 'commentsCount', 'engagement', 
                             'caption_length', 'language', 'day_of_week', 'hour']]
        summary_df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"Data summary exported to {output_file}")


def main():
    """Main execution function"""
    if len(sys.argv) < 2:
        print("Usage: python analyze_instagram.py <json_file> [output_file]")
        sys.exit(1)
    
    json_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not Path(json_file).exists():
        print(f"Error: File {json_file} not found")
        sys.exit(1)
    
    try:
        analyzer = InstagramAnalyzer(json_file)
        
        if output_file:
            analyzer.save_report(output_file)
        else:
            # Auto-generate filename based on account name
            account_name = analyzer.account_name.replace('@', '')
            output_file = f"{account_name}_analysis.md"
            analyzer.save_report(output_file)
        
        # Also export CSV summary
        csv_file = output_file.replace('.md', '_data.csv')
        analyzer.export_data_summary(csv_file)
        
    except Exception as e:
        print(f"Error analyzing data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()