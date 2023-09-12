import csv
import mysql.connector

def load_recipes_data(data, batch_size):
    try:
        # Connect to the MySQL database
        with mysql.connector.connect(
            host="localhost",
            user="testuser",
            password="test1",
            database="test"
        ) as db_connection:
            with db_connection.cursor() as cursor:
                for i in range(0, len(data), batch_size):
                    batch = data[i:i+batch_size]

                    # SQL insert statement for a batch of rows
                    insert_sql = """
                    INSERT IGNORE INTO recipes (recipe_id, minutes, name, contributor_id, submitted_date, tags, nutrition, n_steps, steps, description, ingredients, n_ingredients)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """

                    'INSERT IGNORE INTO recipes (recipe_id, minutes, name, contributor_id, submitted_date, tags, nutrition, n_steps, steps, description, ingredients, n_ingredients) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                    # Execute the insert statement with the current batch of data
                    cursor.executemany(insert_sql, [
                        (
                            row['id'],
                            row['minutes'],
                            row['name'],
                            row['contributor_id'],
                            row['submitted'],
                            row['tags'],
                            row['nutrition'],
                            row['n_steps'],
                            row['steps'],
                            row['description'],
                            row['ingredients'],
                            row['n_ingredients']
                        )
                        for row in batch
                    ])

                    db_connection.commit()

                    start_range = i + 1
                    end_range = min(i + batch_size, len(data))
                    print(f"Inserted {start_range} - {end_range} rows.")

                    # Check if 10,000-10,200 rows have been inserted
                    if start_range <= 10000 <= end_range:
                        print(f"Inserted {start_range} - {end_range} rows.")

        print("Data insertion completed successfully.")

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
    except Exception as e:
        print(f"Error: {e}")

