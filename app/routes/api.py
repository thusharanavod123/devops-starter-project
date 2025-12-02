"""Main API endpoints."""
from flask import Blueprint, jsonify, request
from app.services.cache_service import CacheService
from app.utils.logger import setup_logger
from app.utils.metrics import request_counter, request_duration

bp = Blueprint('api', __name__, url_prefix='/api')
logger = setup_logger(__name__)
cache_service = CacheService()


@bp.route('/', methods=['GET'])
@request_counter
@request_duration
def index():
    """API index endpoint.
    
    Returns:
        JSON response with API information
    """
    return jsonify({
        'message': 'Welcome to DevOps Showcase API',
        'version': '1.0.0',
        'endpoints': {
            'health': '/health',
            'api': '/api',
            'metrics': '/metrics'
        }
    }), 200


@bp.route('/data', methods=['GET'])
@request_counter
@request_duration
def get_data():
    """Get sample data with caching.
    
    Returns:
        JSON response with sample data
    """
    cache_key = 'sample_data'
    
    # Try to get from cache
    cached_data = cache_service.get(cache_key)
    if cached_data:
        logger.info("Cache hit for sample_data")
        return jsonify({
            'data': cached_data,
            'source': 'cache'
        }), 200
    
    # Generate new data
    logger.info("Cache miss for sample_data, generating new data")
    data = {
        'items': [
            {'id': 1, 'name': 'Item 1', 'value': 100},
            {'id': 2, 'name': 'Item 2', 'value': 200},
            {'id': 3, 'name': 'Item 3', 'value': 300}
        ]
    }
    
    # Store in cache
    cache_service.set(cache_key, data, ttl=300)
    
    return jsonify({
        'data': data,
        'source': 'database'
    }), 200


@bp.route('/echo', methods=['POST'])
@request_counter
@request_duration
def echo():
    """Echo endpoint for testing.
    
    Returns:
        JSON response echoing the request body
    """
    data = request.get_json()
    logger.info(f"Echo request received: {data}")
    
    return jsonify({
        'echo': data,
        'message': 'Data received successfully'
    }), 200
