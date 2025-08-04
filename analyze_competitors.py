#!/usr/bin/env python3
"""
Скрипт для анализа больших результатов поиска конкурентов
и сохранения их в структурированный MD файл
"""

import json
import re
from datetime import datetime
from typing import Dict, List, Any

def extract_instagram_handle(text: str) -> str:
    """Извлекает Instagram хэндл из текста"""
    instagram_pattern = r'@([A-Za-z0-9_.]+)|instagram\.com/([A-Za-z0-9_.]+)'
    matches = re.findall(instagram_pattern, text, re.IGNORECASE)
    if matches:
        return matches[0][0] or matches[0][1]
    return ""

def extract_telegram_handle(text: str) -> str:
    """Извлекает Telegram хэндл из текста"""
    telegram_pattern = r't\.me/([A-Za-z0-9_]+)|@([A-Za-z0-9_]+)'
    matches = re.findall(telegram_pattern, text, re.IGNORECASE)
    if matches:
        return matches[0][0] or matches[0][1]
    return ""

def extract_key_metrics(text: str) -> Dict[str, Any]:
    """Извлекает ключевые метрики из текста"""
    metrics = {
        'followers': 0,
        'posts_count': 0,
        'engagement_rate': 0,
        'mentions_influencers': []
    }
    
    # Поиск количества подписчиков
    followers_pattern = r'(\d+(?:\.\d+)?[KkМм]?)\s*(?:подписчик|follower|subscriber)'
    followers_match = re.search(followers_pattern, text, re.IGNORECASE)
    if followers_match:
        followers_str = followers_match.group(1)
        # Конвертация K/М в числа
        if 'K' in followers_str.upper():
            metrics['followers'] = int(float(followers_str.replace('K', '').replace('k', '')) * 1000)
        elif 'М' in followers_str.upper():
            metrics['followers'] = int(float(followers_str.replace('М', '').replace('M', '')) * 1000000)
        else:
            metrics['followers'] = int(float(followers_str))
    
    # Поиск упоминаний инфлюенсеров
    influencer_pattern = r'(?:блогер|blogger|influencer|амбассадор)\s+([А-Яа-я\s]+)'
    influencers = re.findall(influencer_pattern, text, re.IGNORECASE)
    metrics['mentions_influencers'] = list(set(influencers))
    
    return metrics

def analyze_content_strategy(text: str) -> Dict[str, List[str]]:
    """Анализирует контентную стратегию"""
    strategy = {
        'content_types': [],
        'key_themes': [],
        'ugc_mentions': False,
        'promo_mechanics': []
    }
    
    # Типы контента
    if re.search(r'видео|video|reel|сторис|stories', text, re.IGNORECASE):
        strategy['content_types'].append('Видео контент')
    if re.search(r'карусель|carousel|фото|photo', text, re.IGNORECASE):
        strategy['content_types'].append('Фото контент')
    if re.search(r'инфографик|infographic', text, re.IGNORECASE):
        strategy['content_types'].append('Инфографика')
    
    # Ключевые темы
    if re.search(r'рецепт|recipe|готов|cook', text, re.IGNORECASE):
        strategy['key_themes'].append('Рецепты')
    if re.search(r'совет|advice|tip|рекоменд', text, re.IGNORECASE):
        strategy['key_themes'].append('Советы по уходу')
    if re.search(r'развитие|development|рост|growth', text, re.IGNORECASE):
        strategy['key_themes'].append('Развитие ребенка')
    
    # UGC контент
    strategy['ugc_mentions'] = bool(re.search(r'ugc|пользовательский контент|отзыв', text, re.IGNORECASE))
    
    # Промо механики
    if re.search(r'конкурс|contest|giveaway|розыгрыш', text, re.IGNORECASE):
        strategy['promo_mechanics'].append('Конкурсы и розыгрыши')
    if re.search(r'скидк|discount|промо|promo', text, re.IGNORECASE):
        strategy['promo_mechanics'].append('Скидки и промо')
    
    return strategy

def process_search_results(results: List[Dict[str, Any]], brand_name: str) -> str:
    """Обрабатывает результаты поиска и создает MD отчет"""
    report = f"## {brand_name}\n\n"
    report += f"*Дата анализа: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n"
    
    # Сводная информация
    report += "### 📊 Сводная информация\n\n"
    
    all_instagram_handles = []
    all_telegram_handles = []
    all_metrics = []
    all_strategies = []
    
    for idx, result in enumerate(results):
        text = result.get('text', '')
        url = result.get('url', '')
        
        # Извлекаем данные
        instagram = extract_instagram_handle(text)
        telegram = extract_telegram_handle(text)
        metrics = extract_key_metrics(text)
        strategy = analyze_content_strategy(text)
        
        if instagram:
            all_instagram_handles.append(instagram)
        if telegram:
            all_telegram_handles.append(telegram)
        
        all_metrics.append(metrics)
        all_strategies.append(strategy)
        
        # Добавляем детальную информацию
        report += f"\n#### Источник {idx + 1}: {url}\n"
        report += f"**Краткое содержание:** {text[:300]}...\n\n"
        
        if instagram or telegram:
            report += "**Социальные сети:**\n"
            if instagram:
                report += f"- Instagram: @{instagram}\n"
            if telegram:
                report += f"- Telegram: @{telegram}\n"
            report += "\n"
        
        if metrics['followers'] > 0:
            report += f"**Метрики:**\n"
            report += f"- Подписчики: {metrics['followers']:,}\n"
            if metrics['mentions_influencers']:
                report += f"- Упомянутые инфлюенсеры: {', '.join(metrics['mentions_influencers'])}\n"
            report += "\n"
    
    # Общий анализ
    report += "\n### 🎯 Ключевые выводы\n\n"
    
    # Социальные сети
    if all_instagram_handles:
        report += f"**Instagram аккаунты:** @{', @'.join(set(all_instagram_handles))}\n"
    if all_telegram_handles:
        report += f"**Telegram каналы:** @{', @'.join(set(all_telegram_handles))}\n"
    
    # Контентная стратегия
    report += "\n**Используемые типы контента:**\n"
    all_content_types = []
    for strategy in all_strategies:
        all_content_types.extend(strategy['content_types'])
    for content_type in set(all_content_types):
        report += f"- {content_type}\n"
    
    # Темы
    report += "\n**Ключевые темы:**\n"
    all_themes = []
    for strategy in all_strategies:
        all_themes.extend(strategy['key_themes'])
    for theme in set(all_themes):
        report += f"- {theme}\n"
    
    # UGC
    ugc_count = sum(1 for s in all_strategies if s['ugc_mentions'])
    if ugc_count > 0:
        report += f"\n**UGC контент:** Используется (найдено в {ugc_count} источниках)\n"
    
    report += "\n---\n\n"
    
    return report

def save_to_chunks(content: str, base_filename: str, chunk_size: int = 10000):
    """Сохраняет контент по частям в отдельные файлы"""
    chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]
    
    for idx, chunk in enumerate(chunks):
        filename = f"{base_filename}_part{idx+1}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(chunk)
        print(f"Сохранено: {filename}")

# Пример использования
if __name__ == "__main__":
    # Здесь будут результаты от Firecrawl
    sample_results = [
        {
            "url": "https://example.com/nutrilak",
            "text": "Nutrilak Узбекистан имеет 45K подписчиков в Instagram @nutrilak_uz. Активно работают с блогерами..."
        }
    ]
    
    # Обработка результатов
    report = process_search_results(sample_results, "Nutrilak")
    
    # Сохранение полного отчета
    with open('competitor_analysis_nutrilak.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    # Если отчет большой, сохраняем по частям
    if len(report) > 10000:
        save_to_chunks(report, 'competitor_analysis_nutrilak')