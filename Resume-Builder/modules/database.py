import sqlite3

DB_NAME = "data/database.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        resume_name TEXT NOT NULL,

        analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        overall_score INTEGER,

        ats_score INTEGER,

        job_match INTEGER,

        content_quality INTEGER,

        resume_structure INTEGER,

        matched_skills TEXT,

        missing_skills TEXT
    )
    """)

    conn.commit()
    conn.close()