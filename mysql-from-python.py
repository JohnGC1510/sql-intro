import pymysql
import datetime

# Connect to the database
connection = pymysql.connect(host="localhost", db="Chinook")

try:
    """
    Lesson 1
    run a query
    cursors are objects that allow us to interact with databases
    they provide methods for accessing sql queries and providing results
    the defualt cursor returns data as a tuple.
    pymysql.cursors.DictCursor returns the data as a dictionary.
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    connection.close()
    """
    with connection.cursor() as cursor:
        # Lesson 2
        # insert empty table
        # cursor.execute("""CREATE TABLE IF NOT EXISTS
        # Friends(name char(20), age int, DOB datetime);""")
        # Lesson 3
        # insert single row into table
        # row = ("Bob", 21, "1990-02-06 23:05:43")
        # cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        # connection.commit()
        # Lesson 4
        # Insert Multiple rows into table
        """
        row = [("Bob", 21, "1990-02-06 23:05:43"),
               ("Jim", 56, "1995-05-10 14:45:32"),
               ("Fred", 102, "1902-04-12 23:12:12")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
        """
        # Lesson 5 - Updating values in a table
        """
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Bob';")
        or cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
        (23,'Bob'))
        connection.commit()
        """
        # Update multiple rows
        """
        rows =[(23,'Bob'),
             (24,'Jim)
             (120, 'Fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name =%s;",
        rows)
        connection.commmit()
        """
        # Delete Rows
        """
        cursor.execute("DELETE FROM Friends WHERE name = %s;", 'Jim')
        connection.commit()
        """
        # Delete Multiple Rows
        """
            names = ['Jim','Bob']
            names_string = ",".join(['%s']*len(names))
            cursor.execute("DELETE FROM Friends WHERE name in ({});".format(names_string), names)
        """
finally:
    connection.close()
