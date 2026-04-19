def main():
    while True:
        print('='*44)
        print('\t','WELCOME TO AM DIGITAL BANK')
        print('='*44)
        print('\t','\t','HOME')
        print('\t','------------------------')
        print('\t','1: About Us')
        print('\t','2: Deposit/Withdrawal')
        print('\t','3: Create An Account')
        print('\t','4: Delete An Account')
        print('\t','5: Account Details')
        print('\t','6: Exit Digital Bank')
        print('\t','------------------------')
        x=int(input('Please select an option: '))
        if x==1:
            import about_us
            about_us.about_us()
            print()
        elif x==2:
            import depo_with
            depo_with.depo_with()
            print()
        elif x==3:
            import create_account
            create_account.create_account()
            print()
        elif x==4:
            import account_delete
            account_delete.account_delete()
            print()
        elif x==5:
            import account_details
            account_details.account_details()
            print()
        elif x==6:
            print('\t','THANK YOU FOR USING OUR DIGITAL BANKING SYSTEM')
            break
main()

