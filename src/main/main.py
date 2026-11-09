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
    select_from_users_and_call_logs()

    # Close the cursor and connection. main function ends here.
    cursor.close()
    conn.close()


# TODO: Implement the following 4 functions. The functions must pass the unit tests to complete the project.


# This function will load the users.csv file into the users table, discarding any records with incomplete data
def load_and_clean_users(file_path):

    # print("TODO: load_users")

    # Ernest's Solution 1:
    print("---------------------------------------------------------------------------")
    print("User Story 1: Get user data into the user table\n")

    # Extract: get the raw data from the users.csv
    print("Beginning Extraction...\n")    

    # Declare variables
    file_headers = []
    file_data = []
    file_data_2 = []
    file_data_3 = []

    # Open the "users.csv" file for Extraction
    with open(file_path, "r") as user_file:
        
        # Check if the data was read
        content = user_file.read()
        # print(content)

        # Getting the file headers
        user_file.seek(0)
        file_headers = [user_file.readline().replace("\n", '').split()]
        # print(file_headers)

        # Getting the file data rows
        file_data = user_file.readlines()
        # print(file_data)

    # Transform: Transform the data into a form that can be
    #            entered into the database
    print("Beginning Transformation...\n")

    for line in file_data:

        # # Method 1
        # line = line.replace('\n', '')
        # temp_tup = (line.split(","))
        # # print(temp_tup)


        # Method 2
        line = line.replace('\n', '')
        line_2 = line.split(",")
        line_3 = []

        for col in line_2:
            line_3.append(col.strip())

        # temp_tup = (line_3[0], line_3[1])
        # print(temp_tup)

        if len(line_3) != 2:
            continue

        if (line_3[0] == '') | (line_3[1] == ''):
            continue
        
        file_data_2.append(line_3)

    # print(file_data_2)

    # Load: enter the data into the database
    print("Beginning Loading...\n")
    for i, val in enumerate(file_data_2):
        file_data_3.append((i+1, val[0], val[1]))
        
    cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", file_data_3)

    # If the operation was a success, say so.
    print("Population of user table complete!\n")


# This function will load the callLogs.csv file into the callLogs table, discarding any records with incomplete data
def load_and_clean_call_logs(file_path):

    # print("TODO: load_call_logs")

    # Ernest's Solution 2:
    print("---------------------------------------------------------------------------")
    print("User Story 2: Get call data into the calLogs table\n")
    
    # Declare variables
    file_headers = []
    file_data = []
    file_data_2 = []
    file_data_3 = []
    
    # Extract: load the data from the csv file
    print("Beginning Extraction...\n")

    # Opening the callLogs file for Extraction
    with open(file_path, "r") as log_file:
        content = log_file.read()
        # print(content)

        # Getting the file headers
        log_file.seek(0)
        file_headers = log_file.readline().replace("\n", '').split(",")
        # print(file_headers)

        # Getting the main file data
        file_data = log_file.readlines()
        # print(file_data)


    # Transform: transform the data, cleaning it of faulty records
    #           and making it transferable into an SQL database
    print("Beginning Transformation...\n")
    
    for line in file_data:
        
        line = line.replace("\n", '')
        temp_tup = line.split(",")

        if len(temp_tup) != 5:
            continue

        if (temp_tup[0] == '') | (temp_tup[1] == '') | (temp_tup[2] == '') | (temp_tup[3] == '') | (temp_tup[4] == ''):
            continue

        # print(temp_tup)
        file_data_2.append(temp_tup)

    # Load: download the data into the database 
    print("Beginning Loading...\n")

    for i, val in enumerate(file_data_2):
        # print((i, val[0], val[1], val[2], val[3], val[4]))
        file_data_3.append((i, val[0], val[1], val[2], val[3], val[4]))

    cursor.executemany("INSERT INTO callLogs VALUES (?, ?, ?, ?, ?, ?)", file_data_3)

    # If the operation was a success, say so.
    print("Congratulations! you have populated the callLogs table! :)\n")


# This function will write analytics data to testUserAnalytics.csv - average call time, and number of calls per user.
# You must save records consisting of each userId, avgDuration, and numCalls
# example: 1,105.0,4 - where 1 is the userId, 105.0 is the avgDuration, and 4 is the numCalls.
def write_user_analytics(csv_file_path):

    # print("TODO: write_user_analytics")

    # Ernest's Solution 3:
    print("---------------------------------------------------------------------------")
    print("User Story 3: Saving user analytics data into userAnalytics.csv\n")

    # Variable Declaration:
    content = ""
    content_data = []
    analysis_array = []
    
    dict_1 = {}
    dict_2 = {}


    # Extract: Get the data from the SQL "callLogs" table,
    #          Transformed as much as possible
    print("Beginning Extraction...\n")

    content = cursor.execute("""SELECT userID, 
                                    AVG(startTime) AS avgStartTime,
                                    AVG(endTime) As avgEndTime, 
                                    COUNT(phoneNumber) AS numCalls
                                FROM callLogs
                                GROUP BY userID;
                            """)
    # print("Content 1 Info:")
    content_data = cursor.fetchall()
    # print(content_data)

    # Transform: Transform the data into a form that can go into a CSV
    #            File
    print("Beginning Transformation...\n")

    for record in content_data:
        temp_dur = (record[2] * 1.0) - (record[1] * 1.0)
        # print("Call Duration:", temp_dur)
        temp_tup = []
        temp_tup.append(record[0])
        temp_tup.append(temp_dur)
        temp_tup.append(record[3])
        # print("Information Prepped for loading:", temp_tup)
        analysis_array.append(temp_tup)

    # Load: Load the data into the chosen CSV File
    print("Beginning Loading...\n")

    # Trial 1
    # with open(csv_file_path, "a") as analy_file:
    #     for record in analysis_array:
    #         # print(record)
    #         analy_file.write(f"{record[0]},{record[1]},{record[2]}\n")


    # Trial 2
    with open(csv_file_path, "a", encoding="utf-8") as analy_file:

        # Skipping the first line
        # analy_file.seek(1)
        # next(analy_file)

        for record in analysis_array:
            # print(record)
            analy_file.write(f"{record[0]},{record[1]},{record[2]}\n")    


    # If the operation was successful, say so
    print("User data successfully analyzed, and saved!")
    

# This function will write the callLogs ordered by userId, then start time.
# Then, write the ordered callLogs to orderedCalls.csv
def write_ordered_calls(csv_file_path):

    # print("TODO: write_ordered_calls")

    # Ernest's Solution 4:
    # Trial 2: Working without pandas
    print("---------------------------------------------------------------------------")
    print("User Story 4: Saving order call logs into orderedCalls.csv\n")

    # Variable Declarations
    content_data = []
    transform_array = []
    transform_array_2 = []


    # Extract: Get the information from the "callLogs" table
    print("Beginning Extraction...\n")

    cursor.execute("""SELECT phoneNumber, startTime, endTime, direction, userID 
                      FROM callLogs
                      ORDER BY userID, startTime;
    """)
    content_data = cursor.fetchall()
    # print("Extracted content data:", content_data)

    # Transform: Transform the data into a form that can go into a CSV table
    print("Beginning Transformation...\n")

    for record in content_data:
        temp_tup = []
        temp_tup.append(record[0])
        temp_tup.append(record[1])
        temp_tup.append(record[2])
        temp_tup.append(record[3])
        temp_tup.append(record[4])
        # print("Record to add to the pre-loading list:", temp_tup)
        transform_array.append(temp_tup)

    for i, record in enumerate(transform_array):
        temp_tup = []
        temp_tup.append(i)
        temp_tup.append(record[0])
        temp_tup.append(record[1])
        temp_tup.append(record[2])
        temp_tup.append(record[3])
        temp_tup.append(record[4])
        # print("Record to add to the main loading list:", temp_tup)
        transform_array_2.append(temp_tup)

    # print("The Main List: ", transform_array_2)

    # Load: Load the information into the CSV table
    print("Beginning Loading...\n")
    
    with open(csv_file_path, "a") as order_file:
        for record in transform_array_2:
            # print(record)
            order_file.write(f"{record[0]},{record[1]},{record[2]},{record[3]},{record[4]},{record[5]}\n")

    # If the operation was successful, say so.
    print("The operation to save ordered calls was a complete success!")



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