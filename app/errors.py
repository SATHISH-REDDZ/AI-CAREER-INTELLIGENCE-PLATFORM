"""
=========================================================
AI Career Intelligence Platform
Global Error Handlers
=========================================================
"""

from flask import Flask, jsonify


def register_error_handlers(app: Flask) -> None:
    """
    Register global error handlers.
    """

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": "Bad Request",
            "message": str(error)
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": "Unauthorized",
            "message": "Authentication required."
        }), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": "Forbidden",
            "message": "Access denied."
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": "Not Found",
            "message": "Requested resource not found."
        }), 404

    @app.errorhandler(413)
    def request_entity_too_large(error):
        return jsonify({
            "success": False,
            "error": "Payload Too Large",
            "message": "File exceeds maximum permitted upload size."
        }), 413

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            "success": False,
            "error": "Unprocessable Entity",
            "message": "Invalid request payload format."
        }), 422

    @app.errorhandler(429)
    def too_many_requests(error):
        return jsonify({
            "success": False,
            "error": "Too Many Requests",
            "message": "Rate limit exceeded. Please try again later."
        }), 429

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": "Internal Server Error",
            "message": "An unexpected error occurred. Please try again later."
        }), 500

    @app.errorhandler(Exception)
    def handle_unexpected_exception(error):
        if app.debug or app.testing:
            raise error
        return jsonify({
            "success": False,
            "error": "Internal Server Error",
            "message": "An unexpected error occurred."
        }), 500