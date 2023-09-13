from mysql.connector import Error

def create_tables(db_connection):
    """
    Create tables in a MySQL database.
    """
    try:

        cursor = db_connection.cursor()

        create_table_query = [
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id INT PRIMARY KEY,
            encoded_id VARCHAR(255),
            first_name VARCHAR(255) COLLATE utf8mb4_unicode_ci,
            last_name VARCHAR(255) COLLATE utf8mb4_unicode_ci,
            sex VARCHAR(255),
            email VARCHAR(255) COLLATE utf8mb4_unicode_ci,
            phone VARCHAR(255),
            birth DATE,
            job_title VARCHAR(255)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS recipes (
            recipe_id INT PRIMARY KEY,
            minutes INT,
            name VARCHAR(255) COLLATE utf8mb4_unicode_ci,
            contributor_id INT,
            submitted_date DATETIME, 
            tags TEXT,
            nutrition TEXT,
            n_steps INT, 
            steps TEXT,
            description TEXT,
            ingredients TEXT,
            n_ingredients INT
        );
        """, 
        """
        CREATE TABLE IF NOT EXISTS interactions (
            interaction_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            recipe_id INT,
            date DATETIME, 
            rating INT, 
            review TEXT,
            FOREIGN KEY (user_id) REFERENCES users (user_id),
            FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id)
        );
        """
        ]

        for query in create_table_query:
            cursor.execute(query)
            db_connection.commit() 

    except Error as e:
        print("Error:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()