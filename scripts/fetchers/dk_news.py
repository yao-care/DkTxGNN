#!/usr/bin/env python3
"""Denmark health news fetcher via Google News RSS.

Fetches health news from Danish sources via Google News RSS feed.
"""

import re
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from typing import Optional

import requests

# Google News RSS for Denmark health news
GOOGLE_NEWS_RSS = "https://news.google.com/rss/search?q=health+medicine+denmark&hl=en&gl=DK&ceid=DK:en"

# Danish health news sources (English)
DANISH_HEALTH_SOURCES = [
    "https://www.thelocal.dk/tag/health/feed/",
    "https://cphpost.dk/category/health/feed/",
]

# Health-related keywords to filter news
HEALTH_KEYWORDS = [
    "health", "medicine", "drug", "treatment", "therapy", "clinical trial",
    "hospital", "patient", "disease", "cancer", "diabetes", "heart",
    "pharmaceutical", "FDA", "EMA", "approval", "study", "research",
    "vaccine", "medication", "prescription", "healthcare", "diagnosis",
    "symptom", "cure", "prevention", "epidemic", "pandemic", "outbreak",
]


def fetch_google_news_rss(url: str = GOOGLE_NEWS_RSS) -> list[dict]:
    """Fetch news from Google News RSS feed."""
    headers = {"User-Agent": "Mozilla/5.0 (compatible; DkTxGNN/1.0)"}

    try:
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching RSS: {e}")
        return []

    articles = []

    try:
        root = ET.fromstring(resp.content)
        for item in root.findall(".//item"):
            title = item.findtext("title", "")
            link = item.findtext("link", "")
            pub_date = item.findtext("pubDate", "")
            description = item.findtext("description", "")

            if title and link:
                articles.append({
                    "title": title,
                    "url": link,
                    "published": pub_date,
                    "description": description,
                    "source": "Google News Denmark",
                })
    except ET.ParseError as e:
        print(f"Error parsing RSS: {e}")

    return articles


def filter_health_news(articles: list[dict]) -> list[dict]:
    """Filter articles to only include health-related news."""
    health_articles = []

    for article in articles:
        text = f"{article.get('title', '')} {article.get('description', '')}".lower()
        if any(kw in text for kw in HEALTH_KEYWORDS):
            health_articles.append(article)

    return health_articles


def fetch_danish_health_news() -> list[dict]:
    """Fetch all Danish health news."""
    all_articles = []

    # Fetch from Google News
    google_articles = fetch_google_news_rss()
    all_articles.extend(google_articles)

    # Fetch from Danish sources
    for source_url in DANISH_HEALTH_SOURCES:
        try:
            articles = fetch_google_news_rss(source_url)
            all_articles.extend(articles)
        except Exception as e:
            print(f"Error fetching {source_url}: {e}")

    # Filter for health-related content
    health_articles = filter_health_news(all_articles)

    # Remove duplicates by URL
    seen_urls = set()
    unique_articles = []
    for article in health_articles:
        if article["url"] not in seen_urls:
            seen_urls.add(article["url"])
            unique_articles.append(article)

    return unique_articles


if __name__ == "__main__":
    articles = fetch_danish_health_news()
    print(f"Fetched {len(articles)} health news articles")

    for article in articles[:5]:
        print(f"\n- {article['title']}")
        print(f"  {article['url']}")
