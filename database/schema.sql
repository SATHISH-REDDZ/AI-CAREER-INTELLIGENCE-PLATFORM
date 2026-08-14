-- =====================================================
-- AI Career Intelligence Platform Database Schema
-- =====================================================

PRAGMA foreign_keys = ON;

-- ==============================================
-- USERS
-- ==============================================

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    full_name TEXT NOT NULL,

    email TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL,

    role TEXT DEFAULT 'user',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==============================================
-- RESUMES
-- ==============================================

CREATE TABLE IF NOT EXISTS resumes (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    file_name TEXT,

    resume_score REAL,

    ats_score REAL,

    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
        REFERENCES users(id)
);

-- ==============================================
-- JOBS
-- ==============================================

CREATE TABLE IF NOT EXISTS jobs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT,

    company TEXT,

    salary TEXT,

    location TEXT,

    description TEXT
);

-- ==============================================
-- CHAT HISTORY
-- ==============================================

CREATE TABLE IF NOT EXISTS conversations (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    question TEXT,

    answer TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id)
        REFERENCES users(id)
);