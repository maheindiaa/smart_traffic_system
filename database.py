import sqlite3


def create_table():

    conn = sqlite3.connect("traffic.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS traffic_reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        direction TEXT,
        vehicles INTEGER,
        emergency INTEGER
    )
    """)

    conn.commit()
    conn.close()

def save_report(direction, vehicles, emergency):

    conn = sqlite3.connect("traffic.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO traffic_reports(
            direction,
            vehicles,
            emergency
        )
        VALUES (?, ?, ?)
        """,
        (
            direction,
            vehicles,
            emergency
        )
    )

    conn.commit()

    conn.close()

def get_reports():

    conn = sqlite3.connect("traffic.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM traffic_reports"
    )

    data = cursor.fetchall()

    conn.close()

    return data