import sqlite3
import os
from datetime import datetime, UTC

DB_NAME = "test_users.db"


# ------------------ CONNECTION ------------------

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # allows dict-like access
    return conn


# ------------------ INIT ------------------

def init_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age INTEGER,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ------------------ CREATE ------------------

def create_user(name, email, age=None):
    if not name or not email:
        raise ValueError("Name and email are required")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (name, email, age, created_at)
            VALUES (?, ?, ?, ?)
        """, (name, email, age, datetime.now(UTC).isoformat()))

        conn.commit()
        return cursor.lastrowid

    except sqlite3.IntegrityError:
        raise ValueError("Email already exists")

    finally:
        conn.close()


# ------------------ READ ------------------

def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()

    return dict(row) if row else None


def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()

    return dict(row) if row else None


def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


# ------------------ UPDATE ------------------

def update_user(user_id, name=None, email=None, age=None):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if user exists
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    if not cursor.fetchone():
        conn.close()
        return False

    fields = []
    values = []

    if name is not None:
        fields.append("name = ?")
        values.append(name)

    if email is not None:
        fields.append("email = ?")
        values.append(email)

    if age is not None:
        fields.append("age = ?")
        values.append(age)

    if not fields:
        conn.close()
        return False

    values.append(user_id)

    try:
        cursor.execute(
            f"UPDATE users SET {', '.join(fields)} WHERE id = ?",
            tuple(values)
        )
        conn.commit()
        return True

    except sqlite3.IntegrityError:
        raise ValueError("Email already exists")

    finally:
        conn.close()


# ------------------ DELETE ------------------

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

    deleted = cursor.rowcount > 0
    conn.close()

    return deleted


def delete_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users")
    conn.commit()
    conn.close()


# ------------------ DROP ------------------

def drop_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
