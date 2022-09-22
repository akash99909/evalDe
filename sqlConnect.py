import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='demo_sample',
                                         user='root',
                                         password='03051998@Sanu')

    conn = sqlite3.connect('test.db')
    conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

    conn.commit()

    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
        print ("ID = ", row[0])
        print ("NAME = ", row[1])
        print ("ADDRESS = ", row[2])
        print ("SALARY = ", row[3], "\n")

    temp = cursor.execute("SELECT s1,s2 from de_accelerator")
    sum = 0
    for row,row1 in temp:
        sum = sum+int(row1[0])
        print ("row1 = ", row[0],"row2=",row1[0])
    print(sum)