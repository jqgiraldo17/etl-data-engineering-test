import mysql.connector
from mysql.connector import Error

try:

    db_connection = mysql.connector.connect(
        host="localhost",
        user="testuser",
        password="test1",
        database="test"
    )

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
        birth VARCHAR(255),
        job_title VARCHAR(255)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS recipes (
        recipe_id INT PRIMARY KEY,
        minutes INT,
        name VARCHAR(255) COLLATE utf8mb4_unicode_ci,
        contributor_id INT,
        submitted_date DATE, 
        tags VARCHAR(255) COLLATE utf8mb4_unicode_ci,
        nutrition VARCHAR(255) COLLATE utf8mb4_unicode_ci,
        n_steps INT, 
        steps VARCHAR(255) COLLATE utf8mb4_unicode_ci,
        description VARCHAR(255) COLLATE utf8mb4_unicode_ci,
        ingredients VARCHAR(255) COLLATE utf8mb4_unicode_ci,
        n_ingredients INT
    );
    """, 
    """
    CREATE TABLE IF NOT EXISTS interactions (
        interaction_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        recipe_id INT,
        date DATE, 
        rating INT, 
        review VARCHAR(255) COLLATE utf8mb4_unicode_ci,
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
    if 'db_connection' in locals():
        db_connection.close()
