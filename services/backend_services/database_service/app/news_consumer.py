import logging
from datetime import datetime
from typing import Dict, Any, Optional

from .messaging_client import MessagingClient
from .database_manager import DatabaseManager

logger = logging.getLogger(__name__)

class NewsConsumer:
    def __init__(self, messaging_client: MessagingClient, database_manager: DatabaseManager):
        self.messaging_client = messaging_client
        self.database_manager = database_manager

    async def start(self):
        """Subscribe to the news article topic."""
        await self.messaging_client.subscribe(
            topic="news.streaming.article",
            callback=self.handle_news_article
        )
        logger.info("Subscribed to 'news.streaming.article' topic.")

    async def stop(self):
        """Unsubscribe from the news article topic."""
        await self.messaging_client.unsubscribe("news.streaming.article")
        logger.info("Unsubscribed from 'news.streaming.article' topic.")

    async def handle_news_article(self, article_data: Dict[str, Any]):
        """Handle an incoming news article message."""
        try:
            if not article_data:
                logger.warning("Received an empty news article message.")
                return

            # Map the incoming data to the NewsArticle model
            article_to_insert = {
                'publisher': article_data.get('source'),
                'title': article_data.get('title'),
                'content': article_data.get('content'),
                'published_at': datetime.fromtimestamp(article_data.get('published_at')),
                'related_tickers': article_data.get('related_symbols'),
                'article_type': article_data.get('article_type'),
                'sentiment': article_data.get('sentiment')
            }

            await self.database_manager.insert_news_article(article_to_insert)
        except Exception as e:
            logger.error(f"Failed to handle news article message: {e}")
