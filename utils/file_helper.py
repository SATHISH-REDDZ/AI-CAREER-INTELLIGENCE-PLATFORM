"""
=========================================================
AI Career Intelligence Platform
File Helper Utilities
=========================================================
"""

import os
import uuid
from pathlib import Path

from flask import current_app
from werkzeug.utils import secure_filename


def allowed_file(filename: str) -> bool:
    """
    Check whether the uploaded file has an allowed extension.
    """

    if "." not in filename:
        return False

    extension = filename.rsplit(".", 1)[1].lower()

    return (
        extension in
        current_app.config["ALLOWED_EXTENSIONS"]
    )


def generate_unique_filename(filename: str) -> str:
    """
    Generate a unique filename.
    """

    extension = filename.rsplit(".", 1)[1].lower()

    return (
        f"{uuid.uuid4().hex}.{extension}"
    )


def save_uploaded_file(file) -> tuple:
    """
    Save uploaded file to disk.
    """

    print("\n========== FILE HELPER ==========")

    filename = secure_filename(file.filename)

    print("Original Filename :", filename)

    unique_filename = generate_unique_filename(
        filename
    )

    print("Unique Filename :", unique_filename)

    upload_folder = Path(
        current_app.config["UPLOAD_FOLDER"]
    )

    print("Upload Folder :", upload_folder)

    upload_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = upload_folder / unique_filename

    print("Saving File To :", file_path)

    file.save(file_path)

    print("File Saved Successfully")

    file_size = os.path.getsize(file_path)

    print("File Size :", file_size)

    return (
        unique_filename,
        str(file_path),
        file_size
    )