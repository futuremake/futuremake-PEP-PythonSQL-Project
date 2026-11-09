# PEP-PYTHONSQL-PROJECT - Revature - Python SQL API with File I/O

By Developer Ernest Niiquaye

Started on October 31st, 2026, Saturday, at 5pm.

In this Project, Developer Ernest Niiquaye will demonstrate the skills that he learned throughout Revature's Pre-Training 8-Week Codding Bootcamp. Those skills Include: 
1. Python, 
2. SQL, 
4. Sqlite3, 
5. Creating/reading/writing to files,
6. Big Data,
7. Data Warehousing,
8. Data Lake,
9. Extract-Transform-Load (ETL), and
10. Extract-Load-Transform (ELT).

First: the developer will extract data about callers and their calls from csv files, clean/transform it, then put it into Relational SQL Database tables. 

Second: the developer will extract the "Call Log" data from the database, transform it for analysis, then load it into a CSV file. 

Third: finally, the developer will extract the "Call Log" data from the database, in assending order by "userID" and the number of calls a user made. Then, the developer would transform it, giving each record a "callID" Finally, the developer would load the ordered data into a CSV file, for analysis and storage. 


## October 31st, 2026, Saturday

1. The project was started. The "Pandas" library was used to write the functions in "src/main/main.py", but the Assignment does not allow outside libraries to be downloaded, imported, and used. The only outside library allowed was SQLlite3. The developer will take a break on the project for now and work on other tasks, while finding another way to accomplish the task.


## November 7th, 2026, Saturday

1. The Developer returned to the Project. On a Revature professor's suggestion to work without the "Pandas" library, the developer went back to the learning material, and reviewed creating/reading/writing to files, and creating/manipulating/extracting data in databases in Python. That information enabled the developer to complete the functions "load_and_clean_users()", and "load_and_clean_call_logs()".

## November 8th, 2026 Sunday

1. The Developer continued to complete the functions "write_user_analytics()" and "write_ordered_calls()", using SQLlite3, and Python's native file reading and writing functionality.

2. The code output to the console was cleaned up, and comments were added in "main.py". However, the outputs to "orderedCalls.csv" and "userAnalytics.csv" could be looked at.

3. The data output to "userAnalytics" in the "avgDuration" section was faulty, because the formula to calulate it was faulty. Fixing the formulas in the SQL Query and during Transformation fixed the data in the "avgDuration" section.

4. The project code was tested using "lab_test.py". the tests revealed a flaw with cleaning user data before loading into the database. The flaw was fixed.

## November 9th, 2026 Monday

1. The reason why the "ProjectTests.test_user_analytics_are_correct" test failed was because the file that the data was output to in the tests "testUserAnalytics.csv" had an extra empty line at the end. The function "writeUserAnalytics()" appends data to the end of the file. So, when the tests evaluated the "testUserAnalytics.csv" file, it saw that empty space and declared the test failed. Simply removing the space from "testUserAnalytics.csv" enabled the test to pass. Also, in "main.py", in function "writeUserAnalytics()", when loading the data into the csv file, the encoding was explictly set to "utf-8" to ensure the encoding is the same across all computer systems.

