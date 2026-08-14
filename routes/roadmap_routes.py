"""
=========================================================
AI Career Intelligence Platform
Roadmap Routes
=========================================================
"""

from flask import Blueprint
from controllers.roadmap_controller import RoadmapController
from utils.decorators import login_required

roadmap_bp = Blueprint(
    "roadmap",
    __name__,
    url_prefix="/api/roadmap"
)


@roadmap_bp.route("", methods=["GET"])
@login_required
def get_roadmap():
    return RoadmapController.get_roadmap()
