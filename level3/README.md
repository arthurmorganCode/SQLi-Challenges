Level 3 - SQL Injection: Extracting Database Name
Overview:

In this level, we perform a character-by-character SQL Injection attack to extract the name of the database. First, we determine the length of the database name, and then we extract each character individually using conditional logic.
Steps:

    Finding the Length of the Database Name:

    To find the length of the database name, we used the following SQL payload:

    sql

yahoo' and 1=if((length(database())) = 6,1,2)#

    This payload checks if the length of the database name is 6 characters.
    If the length is 6, it returns true (1); otherwise, it returns false (2).
    In this case, we discovered that the length of the database name is indeed 6 characters.

Extracting the Characters of the Database Name:

Once we knew the length of the database name, we wrote a Python script to extract the database name character by character using the ascii() and substring() functions in SQL.

# request.py

        This script loops through the length of the database name and extracts each character by sending conditional SQL queries.
        For each position in the name, it checks all ASCII characters from 32 to 126 until it finds a match.

    Final Database Name: After running the script, we successfully retrieved the database name.

Key Concepts:

    SQL Injection: A technique where we inject SQL queries into user inputs to manipulate the database.
    Character-by-character extraction: Using SQL's substring() and ascii() functions to extract data from the database one character at a time.
    Conditional logic: Using if statements to guide the attack and identify correct characters




Monitoring Requests via Burp Suite:

To monitor the SQL Injection requests and responses, I created a Python script that sends the requests through Burp Suite. This allows us to inspect and analyze each request in real time using Burp's intercepting proxy
# request-burp.py