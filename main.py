import app.extract_data as e_data
from app.database_connector import get_db_connection, close_db_connection
from app.create_tables import create_tables
from app.load_data_into_db import load_data

import os

DATA_FOLDER = "data/"

def main():

    db_connection = get_db_connection("localhost", "testuser", "test1", "test")
    batch_size = 10000

    if db_connection:
        try:
            print("Connected to the database")
            create_tables(db_connection)
            extraction = e_data.DataExtraction()

            file_path_recipe = os.path.join(DATA_FOLDER, "RAW_recipes_sample.csv")
            file_path_users = os.path.join(DATA_FOLDER, "RAW_users_sample.csv")
            file_path_interactions= os.path.join(DATA_FOLDER, "RAW_interactions_sample.csv")

            data_recipe = extraction.extract_data_from_csv(file_path_recipe, 'id')
            data_users = extraction.extract_data_from_csv(file_path_users, 'user id')
            data_interactions = extraction.extract_data_from_csv(file_path_interactions, 'user_id')

            columns_in_table_recipe = ['recipe_id', 'minutes', 'name', 'contributor_id', 'submitted_date', 'tags', 'nutrition', 'n_steps', 'steps', 'description', 'ingredients', 'n_ingredients']
            columns_recipe = ['id', 'minutes', 'name', 'contributor_id', 'submitted', 'tags', 'nutrition', 'n_steps', 'steps', 'description', 'ingredients', 'n_ingredients']
            load_data(db_connection, data_recipe, 'recipes', columns_in_table_recipe, columns_recipe, batch_size)

            columns_in_table_users = ['user_id', 'encoded_id', 'first_name', 'last_name', 'sex', 'email', 'phone', 'birth', 'job_title']
            columns_user = ['user id', 'encoded id', 'first name', 'last name', 'Sex', 'email', 'phone', 'date of birth', 'job title']
            load_data(db_connection, data_users, 'users', columns_in_table_users, columns_user, batch_size)

            columns_in_table_interactions = ['user_id', 'recipe_id', 'date', 'rating', 'review']
            columns_interactions = ['user_id', 'recipe_id', 'date', 'rating', 'review']
            load_data(db_connection, data_interactions, 'interactions', columns_in_table_interactions, columns_interactions, batch_size)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            close_db_connection(db_connection)
            print("Database connection closed")

if __name__ == "__main__":
    main()