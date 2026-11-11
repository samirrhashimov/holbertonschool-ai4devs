import sqlite3


def get_user(conn, username):
    """Return the user row that matches the given username."""
    cursor = conn.cursor()
    # FIX: parameterized query, input is never part of the SQL text
    cursor.execute("SELECT id, username FROM users WHERE username = ?", (username,))
    return cursor.fetchall()


def main():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER, username TEXT)")
    conn.execute("INSERT INTO users VALUES (1, 'alice')")
    conn.execute("INSERT INTO users VALUES (2, 'bob')")

    assert get_user(conn, "alice") == [(1, "alice")]
    assert get_user(conn, "bob") == [(2, "bob")]
    assert get_user(conn, "' OR '1'='1") == []  # injection no longer works
    print("All 3 test cases passed")


if __name__ == "__main__":
    main()