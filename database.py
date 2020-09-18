import sqlite3

# for single-user applications, generally
# only one connection is needed. so, it
# can be opened first as a global variable.
connection = sqlite3.connect("data.db")
# This will allow the cursor to hold a list of rows,
# like a dictionary, rather than a list of tuples.
# This allows for named access, like a dictionary.
connection.row_factory = sqlite3.Row

def create_table():
    # `with` is a context manager. it will automatically commit
    # the transaction at the end of the block.
    with connection:
        # `execute` creates a transaction
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);"
        )

def close_connection():
    connection.close()

def add_entry(entry_content: str, entry_date: str):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?, ?);", 
            (entry_content, entry_date)
        )


def get_entries():
    cursor = connection.execute("SELECT * FROM entries;")
    
    return cursor
