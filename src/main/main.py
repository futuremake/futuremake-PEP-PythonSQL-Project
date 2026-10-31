import csv
import os
import sqlite3

# Resolve the resources folder relative to this file, so paths work
# no matter what directory the script is run from.
_RESOURCES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'resources')

# Connect to the SQLite in-memory database
conn = sqlite3.connect(':memory:')

# A cursor object to execute SQL commands
cursor = conn.cursor()


def main():

    # users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        userId INTEGER PRIMARY KEY,
                        firstName TEXT,
                        lastName TEXT
                      )'''
                   )

    # callLogs table (with FK to users table)
    cursor.execute('''CREATE TABLE IF NOT EXISTS callLogs (
        callId INTEGER PRIMARY KEY,
        phoneNumber TEXT,
        startTime INTEGER,
        endTime INTEGER,
        direction TEXT,
        userId INTEGER,
        FOREIGN KEY (userId) REFERENCES users(userId)
    )''')

    # You will implement these methods below. They just print TO-DO messages for now.
    load_and_clean_users(os.path.join(_RESOURCES_DIR, 'users.csv'))
    load_and_clean_call_logs(os.path.join(_RESOURCES_DIR, 'callLogs.csv'))
    write_user_analytics(os.path.join(_RESOURCES_DIR, 'userAnalytics.csv'))
    write_ordered_calls(os.path.join(_RESOURCES_DIR, 'orderedCalls.csv'))

    # Helper method that prints the contents of the users and callLogs tables. Uncomment to see data.
    # select_from_users_and_call_logs()

    # Close the cursor and connection. main function ends here.
    cursor.close()
    conn.close()


# TODO: Implement the following 4 functions. The functions must pass the unit tests to complete the project.


# This function will load the users.csv file into the users table, discarding any records with incomplete data
def load_and_clean_users(file_path):

    # print("TODO: load_users")

    # Ernest's Solution 1:

    # Extract: loading the raw data file into a pandas dataframe
    df = pd.read_csv(file_path, sep=",", encoding="utf-8")

    # Function Variables
    rows_read = len(df)
    skipped_rows = []
    conn = sqlite3.connect(':memory:')

    # Inspecting the Extracted Data
    print(df.head())

    # Accessing a row
    print(df.loc[0])

    # Accessing a column in the row
    print(df.loc[0]["firstName"])

    # Transform: Read each Row in the dataframe
    for num in range(rows_read):

        # If the row has too much or too little values, drop it
        if len(df.loc[0]) != 2:
            skipped_rows.append(df.loc[num])
            df = df.drop([num])

    # Check how many rows were dropped 
    print("Number of rows skipped: ", len(skipped_rows))

    # If the Transformation was successful, say it
    print("Invalid user records removed!")

    # Load: Send the Transformed data into the SQL database
    df_sql = df.to_sql(name="users", connection=conn, if_exists="replace", index_label="id")

    # If everything went well, say so
    print(df_sql, " records were allowed into the database\'s 'users' table!")

    # Close the connection
    conn.close()


# This function will load the callLogs.csv file into the callLogs table, discarding any records with incomplete data
def load_and_clean_call_logs(file_path):

    # print("TODO: load_call_logs")

    # Ernest's Solution:

    # Extract: loading the Raw data file into a panda's dataframe
    df = pd.read_csv("callLogs.csv", sep=",", encoding="utf-8")

    # Function Variables
    rows_read = len(df)
    skipped_rows = []

    # Inspecting the Extracted Data
    print(df.head())

    # Accessing a row
    print(df.loc[0])

    # Accessing a column in a row
    print(df.loc[0][""])

    # Transform: Read each record in the dataframe
    for num in range(rows_read):

        # If the record has too much or too little values, drop it
        if len(df.loc[num]) != 5:
            skipped_rows.append(df.loc[num])
            df = df.drop([num])

    # Check how many records were dropped
    print("Number of records dropped: ", len(skipped_rows))
    # If the Transformation was successful, say so

    # Load the cleaned data into the "call_logs" database table

    # If everything went well, say so

    # Close the connection
    


# This function will write analytics data to testUserAnalytics.csv - average call time, and number of calls per user.
# You must save records consisting of each userId, avgDuration, and numCalls
# example: 1,105.0,4 - where 1 is the userId, 105.0 is the avgDuration, and 4 is the numCalls.
def write_user_analytics(csv_file_path):

    print("TODO: write_user_analytics")


# This function will write the callLogs ordered by userId, then start time.
# Then, write the ordered callLogs to orderedCalls.csv
def write_ordered_calls(csv_file_path):

    print("TODO: write_ordered_calls")



# No need to touch the functions below!------------------------------------------

# This function is for debugs/validation - uncomment the function invocation in main() to see the data in the database.
def select_from_users_and_call_logs():

    print()
    print("PRINTING DATA FROM USERS")
    print("-------------------------")

    # Select and print users data
    cursor.execute('''SELECT * FROM users''')
    for row in cursor:
        print(row)

    # new line
    print()
    print("PRINTING DATA FROM CALLLOGS")
    print("-------------------------")

    # Select and print callLogs data
    cursor.execute('''SELECT * FROM callLogs''')
    for row in cursor:
        print(row)


def return_cursor():
    return cursor


if __name__ == '__main__':
    main()