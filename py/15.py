import sqlite3

class DatabaseManager:
    def __init__(self, db_name = 'example.db'):
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        """Initialize database with tables"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    age INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    content TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                    )
                ''')

    def create_user(self, name, email, age):
        """Create a new user"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (name, email, age)
                    VALUES (?, ?, ?)
                ''', (name, email, age))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
            return None

    def create_post(self, user_id, title, content):
        """Create a new post"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO posts (user_id, title, content)
                VALUES (?, ?, ?)
            ''', (user_id, title, content))
            return cursor.lastrowid

    def get_all_users(self):
        """Get all users"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            return cursor.fetchall()

    def get_user_posts(self, user_id):
        """Get posts by user"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT p.id, p.title, p.content, p.created_at
                FROM posts p
                WHERE p.user_id = ?
                ORDER BY p.created_at DESC
            ''', (user_id,))
            return cursor.fetchall()

    def delete_user(self, user_id):
        """Delete user and their posts"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM posts WHERE user_id = ?', (user_id,))
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            return cursor.rowcount > 0

def display_menu():
        """Display the main menu"""
        print("\n" + "="*40)
        print("         DATABASE MANAGER")
        print("="*40)
        print("1. Create User")
        print("2. View All Users")
        print("3. Create Post")
        print("4. View User Posts")
        print("5. Delete User")
        print("6. Exit")
        print("-"*40)

def main():
        """Main interactive CLI function"""
        db = DatabaseManager()

        while True:
            display_menu()
            choice = input("Enter your choice(1-6): ").strip()

            if choice == "1":
                print("\n---Create New User ---")
                name = input("Enter name: ").strip()
                email = input("Enter emaiil: ").strip()
                try:
                    age = int(input("Enter age: ").strip())
                    user_id = db.create_user(name,email,age)
                    if user_id:
                        print(f"✓ User created succesfully! ID: {user_id}")
                    else:
                        print("✗ Failed to create user")
                except ValueError:
                    print("✗ Invalid age. Please enter correctly.")

            elif choice =='2' :
                print ("\n--- All Users ---")
                users = db.get_all_users()
                if users:
                    for user in users:
                        print(f"ID: {user[0]} | Name: {user[1]} | Email: {user[2]} | Age: {user[3]}")
                else:
                    print("No users found.")

            elif choice == "3":
                print("\n---Create New Post---")    
                try:
                    user_id = int(input("Enter user ID: ").strip())
                    title = input("Enter post title: ").strip()
                    content = input("Enter post content: ").strip()
                    post_id = db.create_post(user_id, title, content)
                    if post_id:
                        print(f"✓ Post created succesfully! ID: {post_id}")
                    else:
                        print("✗ Failed to create post")
                except ValueError:
                    print("✗ Invalid user ID. Please enter a number.")

            elif choice == "4":
                print("\n---View User Posts---")
                try:
                    user_id = int(input("Enter user ID: ").strip())
                    posts = db.get_user_posts(user_id)
                    if posts:
                        for post in posts:
                            print(f"\nPost ID: {post[0]}")
                            print(f"Title: {post[1]}")
                            print(f"Content: {post[2]}")
                            print(f"Created: {post[3]}")
                            print("-" * 30)
                    else:
                        print("No posts found for this user.")
                except ValueError:
                    print("✗ Invalid user ID. Please enter a number")


            elif choice == "5":
                print("\n---Delete User---")
                try:
                    user_id = int(input("Enter user ID to delete: ").strip())
                    confirm = input(f"Are you sure you want to delete {user_id}? (y/N): ").strip().lower()
                    if confirm == 'y':
                        if db.delete_user(user_id):
                            print("✓ User deleted succesfully!")
                        else:
                            print("✗ User not found or deletion failed")
                    else:
                        print("✗ Deletion cancelled.")
                except ValueError:
                    print("✗ Invalid user ID. Please enter a number.")

            elif choice == "6":
                print("\nGoodbye!!!!")
                break

            else:
                print("✗ Invalid choice, Please enter 1-6.")

            input("\n Press Enter to Continue...")

if __name__ == "__main__":
    main()
                        
                              
