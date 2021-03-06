# https://mariadb-corporation.github.io/mariadb-connector-python/module.html  #exceptions


import dbcreds
import mariadb
import sys 

def connect():
      return mariadb.connect(
         user = dbcreds.user,
         password = dbcreds.password,
         host = dbcreds.host,
         port = dbcreds.port,
         database = dbcreds.database
    )

def Insert_blog():
    conn  = None
    cursor = None

    try:
        conn = connect()
        cursor = conn.cursor()
        content = input("Write your new post: ")
        cursor.execute("INSERT INTO blog_post(username, content, id) VALUES (?, ?, NULL)", [username, content])
        conn.commit()
        print("success")
    except Exception as ex:
        print(ex)
    else:
        if cursor != None:
            cursor.close()
        if conn != None:
            conn.rollback()
            conn.close() 


       
def Select_blog():
    conn  = None
    cursor = None
    rows = []


    try: 
         conn = connect()
         cursor = conn.cursor()
         cursor.execute("SELECT * FROM blog_post")
         rows = cursor.fetchall()
         row_count = cursor.rowcount
         print("returned " + str(row_count) + " row")
         for row in rows:
             print(row)
        #  print(rows)
                                  
    except Exception as ex:
        print(ex)


    else:
        if cursor != None:
            cursor.close()
        if conn != None:
            conn.rollback()
            conn.close()    
   

        return rows 
       


def login():
    conn  = None
    cursor = None

    try:
        conn = connect()
        cursor = conn.cursor()
        username = input("enter your username: ")
        password = input("enter your password: ")
        if username != "" and password != "":
            try:
                cursor.execute("SELECT * FROM users WHERE username = ? and password = ? limit 1", [username, password])
                rows = cursor.fetchall()[0]
                row_count = cursor.rowcount
                print(row_count, "user detected")
                if cursor.rowcount == 1:
                    id = rows[0]
                    name = rows[1]
                    password = rows[2]
                else:
                    print("error")
                    pass    

            except:
                print("invalid username or password")
                login()
            else:
                pass
        print(rows)
    except Exception as ex:
        print(ex)
    else:
        if cursor != None:
            cursor.close()
        if conn != None:
            conn.rollback()
            conn.close()    
   

        return rows 
rows = login()        


while True:
    print("welcome to my first blog site!")
    username = input("username: ")
    option = input(" 1. your new post: , 2. see others post: , 3. Exit ")



        
    if option == "1":
       Insert_blog()
    elif option == "2":
       Select_blog()
    elif option == "3":
        print("Good Bye!!")
        break   
    else:
       print("something went wrong") 

       