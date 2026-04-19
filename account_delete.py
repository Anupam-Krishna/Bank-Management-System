def account_delete():
    import mysql.connector
    connectionobject=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='bankmanagement')
    cursor=connectionobject.cursor()
    print('='*44)
    print('\t','DELETE AN ACCOUNT')
    print('='*44)
    user = input('Enter your username: ')
    pas = input('Enter your password: ')
    query = "SELECT * FROM details WHERE User = %s"
    cursor.execute(query, (user,))
    result = cursor.fetchone()
    if result:
        if result[6] == pas:
            delete_query = "DELETE FROM details WHERE User = %s"
            cursor.execute(delete_query, (user,))
            connectionobject.commit()
            print("Account deleted successfully.")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username not found. Please try again.")



    
            







    

    
