def account_details():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="bankmanagement")
    mycursor = mydb.cursor()
    def view_details(username, password):
        sql = "SELECT * FROM details WHERE User = %s AND Passwd = %s"
        val = (username, password)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result:
            print(f"Account details for {username}:")
            print("Account Number:", result[0])
            print("Name:", result[1])
            print("Age:", result[2])
            print("Address:", result[3])
            print("Mobile Number:", result[4])
            print("Balance:", result[7])
        else:
            print("Account not found.")
    print("="*44)
    print('\t','ACCOUNT DETAILS')
    print("="*44)
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    view_details(username, password)
    

    
    
