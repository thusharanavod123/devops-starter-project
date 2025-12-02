"""Health check endpoints."""
from flask import Blueprint, jsonify
from app.services.cache_service import CacheService
from app.utils.logger import setup_logger

bp = Blueprint('health', __name__)
logger = setup_logger(__name__)
cache_service = CacheService()


@bp.route('/health', methods=['GET'])
def health_check():
    """Basic health check endpoint.
    
    Returns:
        JSON response with health status
    """
    return jsonify({
        'status': 'healthy',
        'service': 'devops-showcase-api',
        'version': '1.0.0'
    }), 200


@bp.route('/health/ready', methods=['GET'])
def readiness_check():
    """Readiness check - verifies dependencies are available.
    
    Returns:
        JSON response with readiness status
    """
    checks = {
        'redis': cache_service.check_connection()
    }
    
    all_ready = all(checks.values())
    status_code = 200 if all_ready else 503
    
    return jsonify({
        'ready': all_ready,
        'checks': checks
    }), status_code


@bp.route('/health/live', methods=['GET'])
def liveness_check():
    """Liveness check - verifies application is running.
    
    Returns:
        JSON response with liveness status
    """
    return jsonify({
        'alive': True
    }), 200
