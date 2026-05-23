import sqlite3


DB_NAME = "lost_items.db"


def connect_db():
    connection = sqlite3.connect(DB_NAME)
    return connection


def create_table():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lost_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            description TEXT,
            last_location TEXT,
            date_last_seen TEXT,
            status TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_item():
    item_name = input("Item name: ")
    description = input("Description: ")
    last_location = input("Last known location: ")
    date_last_seen = input("Date last seen (YYYY-MM-DD): ")
    status = input("Status (Lost/Found): ")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO lost_items 
        (item_name, description, last_location, date_last_seen, status)
        VALUES (?, ?, ?, ?, ?)
    """, (item_name, description, last_location, date_last_seen, status))

    connection.commit()
    connection.close()

    print("Item added successfully.")


def view_items():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM lost_items")
    items = cursor.fetchall()

    connection.close()

    if len(items) == 0:
        print("No items found.")
    else:
        for item in items:
            print("-------------------------")
            print("ID:", item[0])
            print("Item Name:", item[1])
            print("Description:", item[2])
            print("Last Location:", item[3])
            print("Date Last Seen:", item[4])
            print("Status:", item[5])


def search_item():
    keyword = input("Enter item name to search: ")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM lost_items
        WHERE item_name LIKE ?
    """, ("%" + keyword + "%",))

    items = cursor.fetchall()

    connection.close()

    if len(items) == 0:
        print("No matching items found.")
    else:
        for item in items:
            print("-------------------------")
            print("ID:", item[0])
            print("Item Name:", item[1])
            print("Description:", item[2])
            print("Last Location:", item[3])
            print("Date Last Seen:", item[4])
            print("Status:", item[5])


def update_item():
    item_id = input("Enter the ID of the item to update: ")
    new_location = input("New last known location: ")
    new_status = input("New status (Lost/Found): ")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE lost_items
        SET last_location = ?, status = ?
        WHERE id = ?
    """, (new_location, new_status, item_id))

    connection.commit()
    connection.close()

    print("Item updated successfully.")


def delete_item():
    item_id = input("Enter the ID of the item to delete: ")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM lost_items
        WHERE id = ?
    """, (item_id,))

    connection.commit()
    connection.close()

    print("Item deleted successfully.")


def search_by_date_range():
    start_date = input("Start date (YYYY-MM-DD): ")
    end_date = input("End date (YYYY-MM-DD): ")

    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM lost_items
        WHERE date_last_seen BETWEEN ? AND ?
    """, (start_date, end_date))

    items = cursor.fetchall()

    connection.close()

    if len(items) == 0:
        print("No items found in that date range.")
    else:
        for item in items:
            print("-------------------------")
            print("ID:", item[0])
            print("Item Name:", item[1])
            print("Description:", item[2])
            print("Last Location:", item[3])
            print("Date Last Seen:", item[4])
            print("Status:", item[5])


def main():
    create_table()

    while True:
        print()
        print("GPS Lost Item Tracker")
        print("1. Add new item")
        print("2. View all items")
        print("3. Search item by name")
        print("4. Update item location/status")
        print("5. Delete item")
        print("6. Search by date range")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            search_item()
        elif choice == "4":
            update_item()
        elif choice == "5":
            delete_item()
        elif choice == "6":
            search_by_date_range()
        elif choice == "7":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")


main()