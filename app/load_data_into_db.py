import mysql.connector

def load_data(db_connection, data, table_name, columns_in_table, columns, batch_size):
    """
    Load data in batches into a given table in mysql.

    Args:
        data (list): A list containing the data to load.
        batch_size (int): The number of records to include in each batch.

    Returns:
        None
    """

    try:
        with db_connection.cursor() as cursor:
            for i in range(0, len(data), batch_size):
                batch = data[i:i+batch_size]
                insert_sql = f"""
                INSERT IGNORE INTO {table_name} ({', '.join(columns_in_table)})
                VALUES ({', '.join(['%s']*len(columns_in_table))})
                """

                data_batches = [
                    [
                        tuple(row[col] for col in columns)
                        for row in batch
                    ]
                ]

                for batch in data_batches:
                    cursor.executemany(insert_sql, batch)

                db_connection.commit()

                start_range = i + 1
                end_range = min(i + batch_size, len(data))
                print(f"Inserted {start_range} - {end_range} rows.")

                if start_range <= 10000 <= end_range:
                    print(f"Inserted {start_range} - {end_range} rows.")

        print(f"Data insertion for {table_name} completed successfully.")

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
    except Exception as e:
        print(f"Error: {e}")

