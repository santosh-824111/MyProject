import pyodbc

# SQL Server से कनेक्शन पाने वाला फंक्शन
def get_connection():
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=AI_DataBase;Trusted_Connection=yes')
        return conn
    except Exception as e:
        print("❌ Connection Error:", e)
        return None

# 1️⃣ Add Product
def add_product():
    name = input("🔹 Product Name: ")
    category = input("🔹 Category: ")
    price = float(input("🔹 Price: "))
    quantity = int(input("🔹 Quantity: "))
    
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Products (productName, category, price, quantity) VALUES (?, ?, ?, ?)",
            (name, category, price, quantity)
        )
        conn.commit()
        print("✅ Product added successfully.")
        conn.close()

# 2️⃣ View All Products
def view_all_products():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        print("\n📋 All Products:")
        for row in rows:
            print(f"ID: {row.productId} | Name: {row.productName} | Category: {row.category} | Price: {row.price} | Qty: {row.quantity}")
        conn.close()

# 3️⃣ Search Product By ID
def search_product_by_id():
    pid = int(input("🔍 Enter Product ID to Search: "))
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products WHERE productId = ?", (pid,))
        row = cursor.fetchone()
        if row:
            print(f"✅ Found: {row.productName} | Category: {row.category} | Price: {row.price} | Quantity: {row.quantity}")
        else:
            print("❌ Product not found.")
        conn.close()

# 4️⃣ Update Product
def update_product():
    pid = int(input("✏️ Enter Product ID to Update: "))
    name = input("🔹 New Product Name: ")
    category = input("🔹 New Category: ")
    price = float(input("🔹 New Price: "))
    quantity = int(input("🔹 New Quantity: "))
    
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Products
            SET productName = ?, category = ?, price = ?, quantity = ?
            WHERE productId = ?
        """, (name, category, price, quantity, pid))
        
        if cursor.rowcount:
            print("✅ Product updated.")
        else:
            print("❌ Product ID not found.")
        conn.commit()
        conn.close()

# 5️⃣ Delete Product
def delete_product():
    pid = int(input("🗑️ Enter Product ID to Delete: "))
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Products WHERE productId = ?", (pid,))
        
        if cursor.rowcount:
            print("✅ Product deleted.")
        else:
            print("❌ Product ID not found.")
        conn.commit()
        conn.close()

# 📋 Menu System
def main():
    while True:
        print("\n===============================")
        print("📦 PRODUCT MANAGEMENT SYSTEM")
        print("===============================")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product by ID")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")
        
        choice = input("➡️ Enter your choice (1-6): ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            view_all_products()
        elif choice == '3':
            search_product_by_id()
        elif choice == '4':
            update_product()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            print("👋 Exiting program. Bye!")
            break
        else:
            print("❌ Invalid input. Please enter 1-6.")

# Main call
if __name__ == "__main__":
    main()
