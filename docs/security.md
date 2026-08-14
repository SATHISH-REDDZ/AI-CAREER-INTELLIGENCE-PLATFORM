# Security & Safety Audit - AI Career Intelligence Platform

## Security Guidelines & Verification Checklist

- [x] **Password Protection**: Passwords are hashed using bcrypt with dynamic salts before storage.
- [x] **JWT Security**: Auth tokens use SHA-256 HMAC signing with configurable `JWT_SECRET_KEY` secret keys.
- [x] **File Upload Validation**:
  - Whitelist validation for extension (`.pdf`, `.docx`).
  - MIME type checking via `magic`/`filetype`.
  - Max payload limit enforced (`MAX_CONTENT_LENGTH = 16MB`).
  - Safe filename sanitization using `secure_filename`.
- [x] **Injection Prevention**: All database queries use parameterized SQLAlchemy ORM models, eliminating SQL injection.
- [x] **XSS & CSRF Protection**: Jinja2 auto-escaping on web templates; secure headers set in middleware.
- [x] **Secret Isolation**: Sensitive secrets kept strictly inside `.env` (git-ignored); template provided in `.env.example`.
- [x] **Error Handling**: Production environment (`DEBUG=False`) suppresses internal stack trace output and returns structured JSON errors.
