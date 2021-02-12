import dbcreds
import mariadb


def Insert_blog():
    content = input("Write your new post: ")
    conn = mariadb.connect(
         user = dbcreds.user,
         password = dbcreds.password,
         host = dbcreds.host,
         port = dbcreds.port,
         database = dbcreds.database
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO blog_post(username, content, id) VALUES (?, ?, NULL)", [username, content])
    conn.commit()
    print("success")
    cursor.close()
    conn.close()

  
    
def Select_blog():
    conn = mariadb.connect(
         user = dbcreds.user,
         password = dbcreds.password,
         host = dbcreds.host,
         port = dbcreds.port,
         database = dbcreds.database
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog_post")
    rows = cursor.fetchall()
    print(rows)
    cursor.close()
    conn.close()

while True:
    print("welcome to Dhwani's first blog site!")
    username = input("username: ")
    option = input("1. your new post: , 2. see others post: , 3. Exit ")

    if option == "1":
       Insert_blog()
    elif option == "2":
       Select_blog()
    elif option == "3":
        print("Good Bye!!")
        break   
    else:
       print("something went wrong") 

       