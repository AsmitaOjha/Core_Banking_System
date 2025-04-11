from dotenv import load_dotenv
import os
import sys
import mysql.connector
from datetime import datetime
import glob

def get_db_config():
    return{
        'user': os.getenv('DB_USERNAME'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'database': os.getenv('DB_DATABASE')

    }

def init_migrations_table(cursor):
    cursor.execute(""" CREATE TABLE IF NOT EXISTS migrations (
                   id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(255) NOT NULL
                   )
                   """)
    
def generate(name):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f"migrations/{timestamp}_{name}.sql"
    os.makedirs('migrations',exist_ok=True)
    open(filename, 'a').close()
    print(f"Created migration: {filename}")

def migrate():
    print(get_db_config())
    db= mysql.connector.connect(**get_db_config())
    cursor = db.cursor()
    init_migrations_table(cursor)

    executed_migrations = []
    cursor.execute("SELECT name FROM migrations")
    cursor.fetchall()
    for (name,) in cursor:
        executed_migrations.append(name)


    migration_files = sorted(glob.glob("migrations/*.sql"))


    for file_path in migration_files:
        filename = os.path.basename(file_path)
        if filename not in executed_migrations:
            print(f"Migrating: {filename}")
            with open(file_path, 'r') as f:
                sql = f.read()
                cursor.execute(sql)
                cursor.execute("INSERT INTO migrations (name) VALUES (%s)", (filename,))
                db.commit()
                cursor.fetchall()
                print(f"Executed: {filename}")
    cursor.close()
    db.close()

if __name__ == "__main__":
    load_dotenv()

    if len(sys.argv) < 2:
        print("Usage: python script.py [generate|migrate] [migration_name]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "generate":
        if len(sys.argv) != 3:
            print("Usage: python script.py generate <migration_name>")
            sys.exit(1)
        generate(sys.argv[2])
    elif command == "migrate":
        migrate()
    else:
        print("Invalid command. Use 'generate' or 'migrate'")