"""
=========================================================
AI Career Intelligence Platform
Chatbot API Routes
=========================================================
"""

import os
from flask import Blueprint, request, jsonify, current_app, session
from chatbot.chatbot import CareerChatbotEngine
from chatbot.history import ChatHistoryManager
from chatbot.feedback import ChatFeedback
from chatbot.session_manager import SessionManager
from services.pdf_service import PDFService
from werkzeug.utils import secure_filename

chatbot_bp = Blueprint(
    "chatbot_api",
    __name__,
    url_prefix="/api/chatbot"
)


@chatbot_bp.route("/ask", methods=["POST"])
def ask_chatbot():
    """
    Main endpoint for asking questions to the AI Career Advisor.
    Supports query text, model selection, persona prompt selection, active resume text, and context building.
    """
    try:
        data = request.get_json() or {}
        query = data.get("query", "").strip()

        if not query:
            return jsonify({
                "success": False,
                "message": "Query string is required."
            }), 400

        user_id = session.get("user_id") or data.get("user_id") or 1
        model = data.get("model", "Gemini")
        persona = data.get("persona", "Career Advisor")
        target_role = data.get("target_role", "")
        resume_text = data.get("resume_text", "") or session.get("active_resume_text", "")

        result = CareerChatbotEngine.ask(
            user_id=user_id,
            query=query,
            resume_text=resume_text,
            model=model,
            persona=persona,
            target_role=target_role
        )

        return jsonify(result), 200

    except Exception as err:
        print("Error in /api/chatbot/ask route:", err)
        return jsonify({
            "success": False,
            "message": f"An error occurred while processing chatbot query: {str(err)}"
        }), 500


@chatbot_bp.route("/history", methods=["GET"])
def get_history():
    """
    Retrieve stored user conversation history.
    """
    try:
        user_id = session.get("user_id") or request.args.get("user_id") or 1
        limit = int(request.args.get("limit", 50))
        history = ChatHistoryManager.get_user_conversations(user_id=user_id, limit=limit)
        return jsonify({
            "success": True,
            "history": history
        }), 200
    except Exception as err:
        return jsonify({
            "success": False,
            "message": str(err)
        }), 500


@chatbot_bp.route("/clear", methods=["POST"])
def clear_history():
    """
    Clear active session chat memory.
    """
    try:
        user_id = session.get("user_id") or 1
        SessionManager.reset_session(user_id)
        session.pop("active_resume_text", None)
        return jsonify({
            "success": True,
            "message": "Chat history cleared successfully."
        }), 200
    except Exception as err:
        return jsonify({
            "success": False,
            "message": str(err)
        }), 500


@chatbot_bp.route("/feedback", methods=["POST"])
def record_feedback():
    """
    Record user feedback (thumbs up / thumbs down / rating / comment) for a response.
    """
    try:
        data = request.get_json() or {}
        user_id = session.get("user_id") or data.get("user_id") or 1
        query = data.get("query", "")
        response_text = data.get("response", "")
        rating = data.get("rating", 5)
        feedback_type = data.get("feedback_type", "thumbs_up")
        comment = data.get("comment", "")
        conversation_id = data.get("conversation_id")

        res = ChatFeedback.record_feedback(
            user_id=user_id,
            query=query,
            response=response_text,
            rating=rating,
            feedback_type=feedback_type,
            comment=comment,
            conversation_id=conversation_id
        )
        return jsonify(res), 200

    except Exception as err:
        return jsonify({
            "success": False,
            "message": str(err)
        }), 500


@chatbot_bp.route("/upload-resume", methods=["POST"])
def upload_resume_attachment():
    """
    Parse uploaded resume file (PDF/DOCX) and store extracted text in active session context.
    """
    try:
        if "file" not in request.files:
            return jsonify({"success": False, "message": "No file uploaded."}), 400

        file = request.files["file"]
        if not file or not file.filename:
            return jsonify({"success": False, "message": "Invalid file."}), 400

        upload_dir = current_app.config.get("UPLOAD_FOLDER", "uploads/resumes")
        os.makedirs(upload_dir, exist_ok=True)

        filename = secure_filename(file.filename)
        filepath = os.path.join(upload_dir, filename)
        file.save(filepath)

        extracted_text = PDFService.extract_text(filepath)
        session["active_resume_text"] = extracted_text

        return jsonify({
            "success": True,
            "filename": filename,
            "extracted_text_preview": extracted_text[:300],
            "word_count": len(extracted_text.split()),
            "message": f"Resume '{filename}' parsed and attached to chatbot context."
        }), 200

    except Exception as err:
        return jsonify({"success": False, "message": str(err)}), 500


@chatbot_bp.route("/prompts", methods=["GET"])
def get_prompts():
    """
    Return list of prompt starter cards for the frontend.
    """
    prompts = [
        {
            "id": "ats_audit",
            "title": "ATS Resume Audit",
            "icon": "fa-file-lines",
            "color": "#10b981",
            "prompt": "Audit my resume for ATS compliance and highlight key missing skills."
        },
        {
            "id": "star_interview",
            "title": "Mock Interview Prep",
            "icon": "fa-user-tie",
            "color": "#a855f7",
            "prompt": "Ask me a technical interview question for a Python Backend Engineer role."
        },
        {
            "id": "learning_roadmap",
            "title": "8-Week Tech Roadmap",
            "icon": "fa-road",
            "color": "#3b82f6",
            "prompt": "Create an 8-week learning roadmap to master Backend API & AI Engineering."
        },
        {
            "id": "cover_letter",
            "title": "Tailored Cover Letter",
            "icon": "fa-envelope-open-text",
            "color": "#f59e0b",
            "prompt": "Write a compelling cover letter for a Software Developer position."
        }
    ]
    return jsonify({"success": True, "prompts": prompts}), 200
