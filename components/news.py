import feedparser
from flask import current_app


def parse_rss():
    rss_url = current_app.config.get('RSS_URL')
    return feedparser.parse(rss_url)


def get_headlines():
    num_headlines = current_app.config.get('NUM_HEADLINES')
    headlines = []
    feed = parse_rss()

    for i in range(0, num_headlines):
        headlines.append(feed['items'][i]['title'])
    return headlines




