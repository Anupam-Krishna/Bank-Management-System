def create_account():
    import mysql.connector
    connectionobject=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='bankmanagement')
    cursor=connectionobject.cursor()
    import random
    print('='*44)
    print('\t','CREATE AN ACCOUNT')
    print('='*44)
    name=input('Enter your name: ')
    age=int(input('Enter your age: '))
    if age<18:
        print('Only age above 18 can create account')
    else:
        mob=int(input('Enter your mobile number: '))
        add=input('Enter your address: ')
        user=input('Enter your username: ')
        pas=input('Enter your password(DO NOT SHARE): ')
        z=random.randint(10000,99999)
        x=random.randint(1000,9999)
        print(x)
        y=int(input('Enter the number shown above for security purposes: '))
        if y!=x:
            print('Account creation failed!!!')
        else:
            balance=0
            sql = "INSERT INTO details VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (z, name, age, add, mob, user, pas, balance)
            print('ACCOUNT CREATION SUCCESSFUL')
            print('Your account number is: ',z)
            cursor.execute(sql, val)
            connectionobject.commit()        
