import datetime
import random
import time
print()
print('Ticket status',' ',' ','Ticket Reservation',' ',' ',
      ' Sign In',' ',' ','Sign Out',' ',' ',' Sign Up (Or) Rigister',' ')
print()
date=datetime.datetime.now()
BusNo=["AP16 5121","AP16 1465","AP16 1646",
           "AP16 2797","AP16 6554","AP16 6598","AP16 8495",
           "AP16 1646","AP16 2654","AP16 5287","AP16 1265",
           "AP16 4564","AP16 4565","AP16 2565","AP16 5494"]
Name=["Venkata Rao","Raju","Ravi","Rahual",
               "Venkatesh","gopal","Monu","Venky",
               "Gopi","Sathish","SaiBabu","Vijay",
               "sandeep","Deepak","Sudhaker"]
Phone=["9985465745","9985463506","7382899471","9985546231",
       "8754321245","7895421022","8545454712","8854531520","9985462152",
       "7584628264","8895421214","9965848475","9985874521","7757541254",
       "7899865467"]
ids=['198765','465442','33218','46734','876215','32166','216767']
BusNumber=random.choice(BusNo)
BusDriverName=random.choice(Name)
DriverPhoneNumber=random.choice(Phone)
ids=random.choice(ids)
Destinations=[]
Destinationgoings=[]
Passengernames=[]
Passengerages=[]
Emails=[]
UserName=[]
Password=[]

class TicketReservation:
    def TicketStatus(self):
        if len(UserName)==0:
            print()
            print('please login website..')
            print()
            print('information is not avilable server is updating..... ')
            print()
        else:
            print('\t\t\t\t\tCheck Ticket Status')
            x = 0
            print('Ticket :', ids)
            print("Date:",date)
            print("From Destination",Destinations)
            print("Going Destination",Destinationgoings)
            print('Name :', Passengernames[0])
            print('age :', Passengerages[0])
            print('Email id :', Emails[0])
            print("Bus Number::", BusNumber)
            print("Bus Driver Name::", BusDriverName)
            print("Driver Phone Number::", DriverPhoneNumber)
    def Ticket(self):
        if len(UserName)==0:
            print()
            print('\t\t Please Login ')
            print()
            print('\t\t Login Page And Book Tickects')
            username=input('Enter your username::')
            password=input('Enter your password::')
            if username in UserName:
                if password in Password:
                    print('\t\t Ticket Reservation Application Form')
                    print()
                    people=int(input("Enter No of Tickets::"))
                    print()
                    for i in range(people):
                        i+=1
                        from_Dest=input("From Destination::")
                        Destinations.append(from_Dest)

                        going_Dest=input("Going Destination::")
                        Destinationgoings.append(going_Dest)

                        name=input('Enter Your Name::')
                        Passengernames.append(name)

                        age=input('Enter your Age:')
                        Passengerages.append(age)

                        Email=input('Enter your Email::')
                        Emails.append(Email)

                        print("Bus Number::", BusNumber)
                        print("Bus Driver Name::", BusDriverName)
                        print("Driver Phone Number::", DriverPhoneNumber)
                        print()
                        print('Your Ticket Is Updating..... please check your ticket status.')
                else:
                    print('\t\t wrong password {}'.format(password))
                    print('\t\t Create New account ')
            else:
                print('\t\t wrong username {}'.format(username))
                print('\t\t Create New Account')
        else:
            print('\t\t Ticket Reservation Application Form')
            print()
            people = int(input("Enter No of Tickets::"))
            print()
            for i in range(people):
                i += 1
                from_Dest = input("From Destination::")
                Destinations.append(from_Dest)

                going_Dest = input("Going Destination::")
                Destinationgoings.append(going_Dest)

                name = input('Enter Your Name::')
                Passengernames.append(name)

                age = input('Enter your Age:')
                Passengerages.append(age)

                Email = input('Enter your Email::')
                Emails.append(Email)

                print("Bus Number::", BusNumber)
                print("Bus Driver Name::", BusDriverName)
                print("Driver Phone Number::", DriverPhoneNumber)
                print()
                print('Your Ticket Is Updating..... please check your ticket status.')
    def SignIn(self):
        print()
        username = input('Enter your username::')
        password = input('Enter your password::')
        print()
        if username in UserName:
            if password in Password:
                print('you signed your account ')
            else:
                print('wrong password {} or'.format(password))
                print('create new account and login again')
                print()
        else:
            print('wrong username {}'.format(username))
            print('create new account and login again')
            print()
    def SignUp(self):
        print('\t \t \t\tCreate New Account')
        username = input('Enter User Name::')
        UserName.append(username)
        password = input('Enter your New password::')
        password2 = input('Enter Conform password::')
        if password == password2:
            print()
            print('you created your account ', username)
            Password.append(password)
            print('Thank you.......')
        else:
            print('Create New Account')
while True:
    print('1.Ticket status')
    print('2.Ticket Reservation')
    print('3.Sign In')
    print('4.Sign Out')
    print('5.Sign Up (Or) Rigister')
    print()
    choice=int(input('Select your choice::'))
    t=TicketReservation()
    if choice==1:
        t.TicketStatus()
    elif choice==2:
        t.Ticket()
    elif choice==3:
        t.SignIn()
    elif choice==4:
        string=''
        user=string.join(UserName)
        print()
        print("Your Account is loging outing.......", user)
        time.sleep(1.5)
        print()
        print("your account is loged out.......", user)
        print()
        time.sleep(1.0)
        print('Thank you to Visiting our website......')
        break
    elif choice==5:
        t.SignUp()
    else:
        print('')
        print('choice correct option',choice)
        print()



