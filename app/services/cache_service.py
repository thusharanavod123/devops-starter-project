"""Redis cache service."""
import json
import redis
from app.config import Config
from app.utils.logger import setup_logger

logger = setup_logger(__name__)


class CacheService:
    """Redis cache service for application."""
    
    def __init__(self):
        """Initialize Redis connection."""
        try:
            self.redis_client = redis.Redis(
                host=Config.REDIS_HOST,
                port=Config.REDIS_PORT,
                db=Config.REDIS_DB,
                decode_responses=True
            )
            logger.info("Redis connection established")
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {str(e)}")
            self.redis_client = None
    
    def get(self, key):
        """Get value from cache.
        
        Args:
            key: Cache key
            
        Returns:
            Cached value or None
        """
        if not self.redis_client:
            return None
        
        try:
            value = self.redis_client.get(key)
            if value:
                return json.loads(value)
            return None
        except Exception as e:
            logger.error(f"Cache get error: {str(e)}")
            return None
    
    def set(self, key, value, ttl=300):
        """Set value in cache.
        
        Args:
            key: Cache key
            value: Value to cache
            ttl: Time to live in seconds (default: 300)
            
        Returns:
            True if successful, False otherwise
        """
        if not self.redis_client:
            return False
        
        try:
            serialized_value = json.dumps(value)
            self.redis_client.setex(key, ttl, serialized_value)
            return True
        except Exception as e:
            logger.error(f"Cache set error: {str(e)}")
            return False
    
    def delete(self, key):
        """Delete key from cache.
        
        Args:
            key: Cache key
            
        Returns:
            True if successful, False otherwise
        """
        if not self.redis_client:
            return False
        
        try:
            self.redis_client.delete(key)
            return True
        except Exception as e:
            logger.error(f"Cache delete error: {str(e)}")
            return False
    
    def check_connection(self):
        """Check if Redis connection is alive.
        
        Returns:
            True if connected, False otherwise
        """
        if not self.redis_client:
            return False
        
        try:
            self.redis_client.ping()
            return True
        except Exception as e:
            logger.error(f"Redis health check failed: {str(e)}")
            return False
