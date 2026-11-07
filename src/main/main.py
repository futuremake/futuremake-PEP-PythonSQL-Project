import csv
import os
import sqlite3

# Ernest's Imports
# import pandas as pd
import math

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
    select_from_users_and_call_logs()

    # Close the cursor and connection. main function ends here.
    cursor.close()
    conn.close()


# TODO: Implement the following 4 functions. The functions must pass the unit tests to complete the project.


# This function will load the users.csv file into the users table, discarding any records with incomplete data
def load_and_clean_users(file_path):

    # print("TODO: load_users")

    # Ernest's Solution 1:
    
    # # Trial 1:
    # # Extract: loading the raw data file into a pandas dataframe
    # df = pd.read_csv(file_path, sep=",", encoding="utf-8")

    # # Function Variables
    # rows_read = len(df)
    # skipped_rows = []
    # conn = sqlite3.connect(':memory:')

    # # Inspecting the Extracted Data
    # print(df.head())

    # # Accessing a row
    # print(df.loc[0])

    # # Accessing a column in the row
    # print(df.loc[0]["firstName"])

    # # Transform: Read each Row in the dataframe
    # for num in range(rows_read):

    #     # If the row has too much or too little values, drop it
    #     if len(df.loc[num]) != 2:
    #         skipped_rows.append(df.loc[num])
    #         df = df.drop([num])
    #         continue
            
    #     # If the row has any missing values, drop it
    #     for col in len(df.loc[num]):
    #         if df.loc[num][col] == '':
    #             skipped_rows.append(df.loc[num])
    #             df = df.dropna(axis=0)
    #             continue

    # # Check how many rows were dropped 
    # print("Number of rows skipped: ", len(skipped_rows))

    # # If the Transformation was successful, say it
    # print("Invalid user records removed!")

    # # Load: Send the Transformed data into the SQL database
    # df_sql = df.to_sql(name="users", connection=conn, if_exists="replace", index_label="id")

    # # If everything went well, say so
    # print(df_sql, " records were allowed into the database\'s 'users' table!")

    # # Close the connection
    # conn.close()


    # Trial 2
    # Extract: get the raw data from the users.csv
    
    # Declare variables
    file_headers = []
    file_data = []
    file_data_2 = []
    file_data_3 = []

    with open(file_path, "r") as user_file:
        
        # Check if the data was read
        content = user_file.read()
        print(content)

        # Getting the file headers
        user_file.seek(0)
        file_headers = [user_file.readline().replace("\n", '').split()]
        print(file_headers)
        
        

        # Getting the file data rows
        file_data = user_file.readlines()
        print(file_data)

    # Transform: Transform the data into a form that can be
    #            entered into the database
    for line in file_data:
        line = line.replace('\n', '')
        temp_tup = (line.split(","))
        # print(temp_tup)

        if len(temp_tup) != 2:
            continue

        if (temp_tup[0] == '') | (temp_tup[1] == ''):
            continue
    
        file_data_2.append(temp_tup)

    print(file_data_2)


    # Load: enter the data into the database
    for i, val in enumerate(file_data_2):
        file_data_3.append((i+1, val[0], val[1]))
        
    cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", file_data_3)

    print("population of user table complete!")

    # cursor.close()
    # conn.close()


# This function will load the callLogs.csv file into the callLogs table, discarding any records with incomplete data
def load_and_clean_call_logs(file_path):

    print("TODO: load_call_logs")

    # Ernest's Solution:

    # # Trial 1:
    # # Extract: loading the Raw data file into a panda's dataframe
    # df = pd.read_csv(file_path, sep=",", encoding="utf-8")

    # # Function Variables
    # rows_read = len(df)
    # skipped_rows = []

    # # Inspecting the Extracted Data
    # print(df.head())

    # # Accessing a row
    # print(df.loc[0])

    # # Accessing a column in a row
    # print(df.loc[0]["phoneNumber"])

    # # Transform: Read each record in the dataframe
    # for num in range(rows_read):

    #     # If the record has too much or too little values, drop it
    #     if len(df.loc[num]) != 5:
    #         skipped_rows.append(df.loc[num])
    #         df = df.drop([num])

    #     # If the record has missing values, drop it
    #     for col in len(df.loc[num]):
    #         if df.loc[num][col] == '':
    #             skipped_rows.append(df.loc[num])
    #             df = df.drop([num])

    # # Check how many records were dropped
    # print("Number of records dropped: ", len(skipped_rows))
    
    # # If the Transformation was successful, say so
    # print("The Transformation was a success!")
    
    # # Load the cleaned data into the "callLogs" database table
    # df_sql = df.to_sql(name="callLogs", connection=conn, if_exists='replace', index_label="id")

    # # If everything went well, say so
    # print(df_sql, " records were added into the database table 'callLogs!'")
    
    # # Close the connection
    # conn.close()

    
    # Trial 2:
    
    # Declare variables
    file_headers = []
    file_data = []
    file_data_2 = []
    file_data_3 = []
    
    # Extract: load the data from the csv file
    with open(file_path, "r") as log_file:
        content = log_file.read()
        print(content)

        # Getting the file headers
        log_file.seek(0)
        file_headers = log_file.readline().replace("\n", '').split(",")
        print(file_headers)

        # Getting the main file data
        file_data = log_file.readlines()
        print(file_data)


    # Transform: transform the data, cleaning it of faulty records
    #           and making it transferable into an SQL database
    for line in file_data:
        
        line = line.replace("\n", '')
        temp_tup = line.split(",")

        if len(temp_tup) != 5:
            continue

        if (temp_tup[0] == '') | (temp_tup[1] == '') | (temp_tup[2] == '') | (temp_tup[3] == '') | (temp_tup[4] == ''):
            continue

        print(temp_tup)
        file_data_2.append(temp_tup)

    # Load: download the data into the database    
    for i, val in enumerate(file_data_2):
        print((i, val[0], val[1], val[2], val[3], val[4]))
        file_data_3.append((i, val[0], val[1], val[2], val[3], val[4]))

    cursor.executemany("INSERT INTO callLogs VALUES (?, ?, ?, ?, ?, ?)", file_data_3)

    print("Congradulations! you have populated the callLogs table! :)")


# This function will write analytics data to testUserAnalytics.csv - average call time, and number of calls per user.
# You must save records consisting of each userId, avgDuration, and numCalls
# example: 1,105.0,4 - where 1 is the userId, 105.0 is the avgDuration, and 4 is the numCalls.
def write_user_analytics(csv_file_path):

    print("TODO: write_user_analytics")

    # # Create the connection(s) with the database
    # conn = sqlite3.connect(':memory:')
    # cursor = conn.cursor()

    # Extract the appropriate data from the database with an SQL Query
    

    # # Trial 1:
    # res = cursor.execute(
    #     """SELECT userId, AVG(startTime) AS avgStartTime, AVG(endTime) AS avgEndTime, SUM(userID) as numCalls
    #         FROM callLogs
    #         GROUP BY userId, avgStartTime, avgEndTime, numCalls;
    #     """
    # )


    # # Trial 2:
    # sql = (
    #     """SELECT userId, AVG(startTime) AS avgStartTime, AVG(endTime) AS avgEndTime, SUM(userID) as numCalls
    #          FROM callLogs
    #          GROUP BY userId, avgStartTime, avgEndTime, numCalls;
    #      """
    # )

    # retre_logs_df = pd.read_sql(sql, conn)

    # # inspect the retrieved database data
    # print(retre_logs_df)

    # # clean up the data
    # avgDurationArray = []

    # for row in range(len(ret_logs_df)):
    #     avgDur = (ret_logs_df[avgStartTime] + ret_logs_df[avgEndTime] / 2)
    #     avgDurationArray.append(avgDur)

    # avgDur_df = pd.dataframe(data=avgDurationArray columns=["avgDuration"])

    # userId_df = retre_logs_df.loc[:, [userID]]

    # sol_df = merge ()


    # # Trial 3:
    # sql = (
    #     """SELECT userId, AVG(startTime) AS avgStartTime
    #          FROM callLogs
    #          GROUP BY userId;
    #      """
    # )

    # sql_2 = (
    #     """SELECT userId, AVG(endTime) AS avgEndTime
    #          FROM callLogs
    #          GROUP BY userId;
    #      """
    # )

    # sql_3 = (
    #     """SELECT userId, count(userID) AS numCalls
    #          FROM callLogs
    #          GROUP BY userId;
    #      """
    # )

    # # Trial 4:
    # sql = (
    #     """SELECT userID, 
    #             avgDuration = AVG(SUM(startTime) + SUM(endTime)),
    #             COUNT(phoneNumber) as numCalls
    #         FROM callLogs,
    #         GROUP BY userID;
    #     """
    # ) 

    # retre_data_df = pd.read_sql(sql, conn)
    # print(retre_data_df)

    # # Load the data into the 'userAnalytics.csv' file
    # retre_data_df.to_csv(csv_file_path)

    # # if the operation was successful, say so
    # print("The data was successfully downloaded for analysis!")

    # # Close the cursor and the connection
    # cursor.close()
    # conn.close()


    # Trial 5
    # Variable Declaration:
    content = ""
    content_2 = ""
    dict_1 = {}
    dict_2 = {}


    # Extract: Get the data from the SQL "callLogs" table
    #          Transformed as much as possible
    
    # content = cursor.execute("""SELECT userID, 
    #                                 AVG(SUM(endTime) - SUM(startTime)) AS avgDuration, 
    #                                 COUNT(phoneNumber) AS numCalls
    #                             FROM callLogs
    #                             GROUP BY userID;        
    #                         """)
    
    content = cursor.execute("""SELECT userID, 
                                    SUM(startTime) AS sumStartTime, 
                                    COUNT(phoneNumber) AS numCalls
                                FROM callLogs
                                GROUP BY userID;        
                            """)
    


    print(content)

    # Transform: Transform the data into a form that can go into a CSV
    #            File



    # Load: Load the data into the chosen CSV File


# This function will write the callLogs ordered by userId, then start time.
# Then, write the ordered callLogs to orderedCalls.csv
def write_ordered_calls(csv_file_path):

    print("TODO: write_ordered_calls")

    # # Ernest's Solution:

    # # Create the connection(s) with the database
    # conn = sqlite3.connect(':memory:')
    # cursor = conn.cursor()

    # # Extract the Data from the Database with a SQL Query
    # sql = (
    #     """SELECT callId, phoneNumber, startTime, endTime, direction, userId
    #         FROM callLogs
    #         ORDER BY userId, startTime;
    #     """
    # )

    # retre_data_df = pd.read_sql(sql, conn)
    # print(retre_data_df)
    
    # # Load the data into the 'orderedCalls.csv' file
    # retre_data_df.to_csv(csv_file_path)

    # # If the operation was successful, say so
    # print("The call logs were successfully downloaded and ordered for analysis!")

    # # Close the cursor and the connection
    # cursor.close()
    # conn.close()




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