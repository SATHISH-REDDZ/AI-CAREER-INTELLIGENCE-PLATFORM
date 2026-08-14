"""
=========================================================
AI Career Intelligence Platform
Export Service
=========================================================
"""

import json
from services.report_service import ReportService


class ExportService:
    """
    Data & Analytics Export Service Logic
    """

    @staticmethod
    def export_report_to_json(user_id: int, resume_id: int = None) -> str:
        """
        Export candidate career report to formatted JSON string.
        """
        report_res = ReportService.generate_career_report(user_id, resume_id)
        if not report_res["success"]:
            return json.dumps({"error": report_res["message"]})

        return json.dumps(report_res["report"], indent=2)
