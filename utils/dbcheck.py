# from DB_Connection import DatabaseUtil

# # Set up the database connection
# DATABASE_URL = "mysql+pymysql://root:sarthak1@localhost:3306/students_db"
# db_util = DatabaseUtil(DATABASE_URL)

# # Reflect the table from the database
# students_table = db_util.reflect_table('students')  # Replace 'students' with your actual table name

# # Query using SQLAlchemy Core
# with db_util.engine.connect() as connection:
#     # Execute a SELECT query on the reflected table
#     query = students_table.select()
#     result = connection.execute(query)
    
#     # Iterate over the result set
#     for row in result:
#         print(row)

# # Dispose the engine after use
# db_util.close()


import pandas as pd
from DB_Connection import DatabaseUtil

# Set up the database connection
DATABASE_URL = "mysql+pymysql://root:sarthak1@localhost:3306/students_db"
db_util = DatabaseUtil(DATABASE_URL)

# Reflect the table from the database
students_table = db_util.reflect_table('students')  # Replace 'students' with your actual table name

# Query using SQLAlchemy Core
with db_util.engine.connect() as connection:
    # Execute a SELECT query on the reflected table
    query = students_table.select()
    result = connection.execute(query)
    
    # Convert the result to a pandas DataFrame
    df = pd.DataFrame(result.fetchall())
    
    # Set column names
    df.columns = result.keys()
    
    # Write the DataFrame to a CSV file
    df.to_csv('students_data.csv', index=False)
    
    print(f"Data has been written to students_data.csv")

# Dispose the engine after use
db_util.close()
