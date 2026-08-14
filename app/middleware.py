"""
=========================================================
AI Career Intelligence Platform
Application Middleware
=========================================================

This module registers middleware that executes
before and after every request.
=========================================================
"""

import time

from flask import Flask, g, request


from werkzeug.middleware.proxy_fix import ProxyFix


def register_middleware(app: Flask) -> None:
    """
    Register application middleware & reverse proxy HTTPS support.
    """
    # HTTPS Proxy Header Fix for reverse proxies (Render, Cloud Run, Nginx)
    app.wsgi_app = ProxyFix(
        app.wsgi_app,
        x_for=1,
        x_proto=1,
        x_host=1,
        x_prefix=1
    )

    @app.before_request
    def before_request():
        """
        Executes before every request.
        """
        g.start_time = time.time()

    @app.after_request
    def after_request(response):
        """
        Executes after every request.
        """

        # Prevent AttributeError if before_request was skipped
        start_time = getattr(g, "start_time", None)

        if start_time is not None:
            execution_time = time.time() - start_time
        else:
            execution_time = 0.0

        print(
            f"[{request.method}] "
            f"{request.path} "
            f"{response.status_code} "
            f"{execution_time:.4f}s"
        )

        # Security Headers
        response.headers["X-Frame-Options"] = "SAMEORIGIN"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-XSS-Protection"] = "1; mode=block"

        return response