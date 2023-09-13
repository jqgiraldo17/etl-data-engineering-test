import pytest
from unittest.mock import MagicMock 
from app.database_connector import get_db_connection
from app.create_tables import create_tables
from app.load_data_into_db import load_data



@pytest.fixture
def db_connection_mocked():
    """
    This test evaluates the connection with the database. 

    Returns:
        The mocked connection.
    """
    mocked_connection = MagicMock()
    get_db_connection.return_value = mocked_connection
    
    yield mocked_connection

def test_create_tables(db_connection_mocked):
    """
    This tests the create_table() function. Creates two tables and check the columns.

    Args:
         db_connection_mocked: A mocked database connection.
    """
    create_tables(db_connection_mocked)

    cursor = db_connection_mocked.cursor()
    cursor.execute.return_value = None  
    
    cursor.fetchall.return_value = [('table1',), ('table2',)]  

    assert ('table1',) in cursor.fetchall()
    assert ('table2',) in cursor.fetchall()

    cursor.execute.side_effect = [
        None,  
        [('column1', 'int'), ('column2', 'varchar')],  
        None,  
        [('column3', 'int'), ('column4', 'varchar')]  
    ]

    
    cursor.execute('DESCRIBE table1')
    assert len(cursor.fetchall()) == 2  

    cursor.execute('DESCRIBE table2')
    assert len(cursor.fetchall()) == 2  


def test_data_insertion(db_connection_mocked):
    """
    This tests the insertion that is part of the function load_data(). 
    Inserts data into a table in the database..

    Args:
         db_connection_mocked: A mocked database connection.
    """
    
    data = [{"col1": 1, "col2": 2}, {"col1": 3, "col2": 4}]
    batch_size = 2
    table_name = "table"
    columns_in_table = ["col1", "col2"]
    columns = ["col1", "col2"]

    cursor = db_connection_mocked.cursor()
    cursor.executemany.return_value = 2

    sql = "INSERT INTO {} ({}) VALUES ({})".format(
        table_name, ",".join(columns_in_table), ",".join(["%s"] * len(columns))
    )

    cursor.executemany(sql, data)
    db_connection_mocked.commit()

    cursor.executemany.assert_called_once()
    assert cursor.rowcount is not None
    db_connection_mocked.commit.assert_called_once()

def test_load_data(db_connection_mocked):
    """
    Tests the function load_data(). 

    Args:
         db_connection_mocked: A mocked database connection.
    """
    
    data = [{"col1": 1, "col2": 2}, {"col1": 3, "col2": 4}]
    batch_size = 2
    table_name = "table"
    columns_in_table = ["col1", "col2"]
    columns = ["col1", "col2"]

    cursor = db_connection_mocked.cursor()
    cursor.executemany.return_value = 2

    with db_connection_mocked.cursor() as cursor:
        load_data(db_connection_mocked, data, table_name, columns_in_table, columns, batch_size)

    assert cursor.executemany.called