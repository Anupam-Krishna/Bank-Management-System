def depo_with():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="bankmanagement")
    mycursor = mydb.cursor()
    def deposit(username, password, amount):
        sql_check = "SELECT * FROM details WHERE User = %s AND Passwd = %s"
        val_check = (username, password)
        mycursor.execute(sql_check, val_check)
        result = mycursor.fetchone()
        if result:
            sql = "UPDATE details SET Balance = Balance + %s WHERE User = %s AND Passwd = %s"
            val = (amount, username, password)
            mycursor.execute(sql, val)
            mydb.commit()
            print("AMOUNT SUCCESSFULLY DEPOSITED")
        else:
            print("Username and password combination does not exist.")

        
    def withdraw(username, password, amount):
        sql_check = "SELECT * FROM details WHERE User = %s AND Passwd = %s"
        val_check = (username, password)
        mycursor.execute(sql_check, val_check)
        result = mycursor.fetchone()
        if result:
            check_balance_sql = "SELECT Balance FROM details WHERE User = %s AND Passwd = %s"
            val = (username, password)
            mycursor.execute(check_balance_sql, val)
            result = mycursor.fetchone()
            if result[0] >= amount:
                update_sql = "UPDATE details SET Balance = Balance - %s WHERE User = %s AND Passwd = %s"
                val = (amount, username, password)
                mycursor.execute(update_sql, val)
                mydb.commit()
                print("AMOUNT SUCCESSFULLY WITHDRAWN")
            else:
                print("Not enough balance for the withdrawal.")
        else:
            print("Username and password combination does not exist.")

        
    print("="*44)
    print('\t','DEPOSIT OR WITHDRAW')
    print("="*44)
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    choice = input("Do you want to deposit[D] or withdraw[W]: ")

    if choice == 'D':
        amount = float(input("Enter the amount you want to deposit: "))
        deposit(username, password, amount)
    elif choice == 'W':
        amount = float(input("Enter the amount you want to withdraw: "))
        withdraw(username, password, amount)
    else:
        print("Invalid choice.")

        
    
    

