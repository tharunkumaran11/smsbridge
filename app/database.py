import sqlite3

DATABASE_NAME = "smsbridge.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sms_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            phone TEXT NOT NULL,

            message TEXT NOT NULL,

            status TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    conn.commit()
    conn.close()


def save_sms(phone, message, status):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sms_history (
            phone,
            message,
            status
        )
        VALUES (?, ?, ?)
    """, (phone, message, status))

    conn.commit()
    conn.close()


def get_sms_history():

    conn = get_connection()

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM sms_history
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]