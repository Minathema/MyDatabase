import re

def username():
    condition = False
    global user_name
    while condition == False:
        user_n = input("Please add your name: ")
        if user_n == "" or user_n.isspace() == True:
            user_name = "(blank)"
            #print (user_name)
            return user_name
            condition = True
        else:
            if (user_n.replace(" ", "")).isalpha() == False:
                print ("This is not a valid username")
            else:
                user_name = ((user_n).upper()).lstrip()
                #print (user_name)
                return user_name
                condition = True

def mobilenumber():
    condition = False
    global mobile_number
    while condition == False:
        mobile_n = input("Please add your mobile number: ")
        if mobile_n == "" or mobile_n.isspace() == True:
            mobile_number = "(blank)"
            #print (mobile_number)
            return mobile_number
            condition = True
        else:
            mobile_n = mobile_n.replace(" ", "")
            if mobile_n.isnumeric() == False or len(mobile_n) != 10:
                print ("This is not a valid mobile number")
            else:
                mobile_number = mobile_n
                #print (mobile_number)
                return mobile_number
                condition = True

def email():
    condition = False
    global email_address
    while condition == False:
        email_add = input("Please add your email address: ")
        if email_add == "" or email_add.isspace() == True:
            email_address = "(blank)"
            #print (email_address)
            return email_address
            condition = True
        else:
            email_add = (email_add.replace(" ", "")).lower()
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_add)
            if match == None:
                print ("This is not a valid email address")
            else:
                email_address = email_add
                #print (email_address)
                return email_address

def homeaddress():
    condition = False
    global home_address
    while condition == False:
        home_add = input("Please add your home address: ")
        if home_add == "" or home_add.isspace() == True:
            home_address = "(blank)"
            #print (home_address)
            return home_address
            condition = True
        elif home_add.isnumeric() == True:
            print ("This is not a valid home address")
        elif bool(re.search(r'\d', home_add)) == False:
            print ("This is not a valid home address")
        else:
            home_address = (home_add.upper()).lstrip()
            #print (home_address)
            return home_address
            condition = True

def profile():
    entry = []
    if user_name == "(blank)" and mobile_number == "(blank)" \
       and email_address == "(blank)" and home_address == "(blank)" :
       print ("Profile was not created")
    else:
        entry.append(user_name)
        entry.append(mobile_number)
        entry.append(email_address)
        entry.append(home_address)
        print ("Profile was created successfully")
        print ('\n'.join(entry))

username()
mobilenumber()
email()
homeaddress()
profile()
