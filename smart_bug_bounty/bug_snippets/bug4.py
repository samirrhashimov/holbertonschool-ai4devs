import sqlite3


def get_user(conn, username):
    """Return the user row that matches the given username."""
    cursor = conn.cursor()
    # BUG: SQL injection, user input is concatenated into the query
    query = "SELECT id, username FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


def main():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER, username TEXT)")
    conn.execute("INSERT INTO users VALUES (1, 'alice')")
    conn.execute("INSERT INTO users VALUES (2, 'bob')")

    print(get_user(conn, "alice"))       # Expected: [(1, 'alice')]
    print(get_user(conn, "' OR '1'='1"))  # Returns ALL users (exploit)


if __name__ == "__main__":
    main()