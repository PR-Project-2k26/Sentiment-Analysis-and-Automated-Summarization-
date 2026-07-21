import sqlite3

DB_NAME = "data/database.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def save_analysis(
    resume_name,
    overall_score,
    ats_score,
    job_match,
    content_quality,
    resume_structure,
    matched_skills,
    missing_skills
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO analysis_history(

            resume_name,

            overall_score,

            ats_score,

            job_match,

            content_quality,

            resume_structure,

            matched_skills,

            missing_skills

        )

        VALUES(?,?,?,?,?,?,?,?)
        """,

        (

            resume_name,

            overall_score,

            ats_score,

            job_match,

            content_quality,

            resume_structure,

            ",".join(sorted(matched_skills)),

            ",".join(sorted(missing_skills))

        )
    )

    conn.commit()

    conn.close()

def get_analysis_history():

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                resume_name,
                analysis_date,
                overall_score,
                ats_score,
                job_match,
                content_quality,
                resume_structure
            FROM analysis_history
            ORDER BY analysis_date DESC
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

def get_latest_two():

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                resume_name,
                analysis_date,
                overall_score,
                ats_score,
                job_match,
                content_quality,
                resume_structure,
                matched_skills,
                missing_skills

            FROM analysis_history

            ORDER BY analysis_date DESC

            LIMIT 2
        """)

        rows = cursor.fetchall()

        conn.close()

        return rows

def get_dashboard_stats():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            MAX(overall_score)
        FROM analysis_history
    """)

    total, best = cursor.fetchone()

    cursor.execute("""
        SELECT overall_score
        FROM analysis_history
        ORDER BY analysis_date DESC
        LIMIT 1
    """)

    latest = cursor.fetchone()

    conn.close()

    return {
        "total": total or 0,
        "best": best or 0,
        "latest": latest[0] if latest else 0
    }