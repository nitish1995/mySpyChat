from spy_details import default_spy

status_messages = []
friends = []




#this method will input all data if user does not select default.
#...................................................................................................................................................................................
def basic_info():
    new_spy = {
        'name': None,
        'salutation': None,
        'age': 0,
        'rating': 0.0,
        'is_online': False
    }

    #Taking spy name and displaying a welcome message.
    #.................................................
    loop_count = 0
    while(True):                                                                                            #loop for handling invalid input cases.
        if loop_count > 4:                                                                                  #escaping from infinite cases. If someone do knowingly.
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Bye bye."
            exit()

        loop_count = loop_count + 1
        new_spy['name'] = raw_input("What is your name? ")
        new_spy['name'] = new_spy['name'].strip()                                                           #Removes extra whitespaces.
        if len(new_spy['name'])>0:                                                                          #Checking for blank name.
            print 'Welcome ' + new_spy['name'] + '. Glad to have you back with us.'
            break
        else:
            print "Please enter a valid name. "
    #.................................................




    #Ask salutation for the spy and error handling.
    #.............................................
    loop_count = 0
    while(True):                                                                                            #loop for handling invalid input cases.
        if loop_count > 4:                                                                                  #escaping from infinite cases. If someone do knowingly.
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Bye bye."
            exit()

        loop_count = loop_count + 1
        new_spy['salutation'] = raw_input("What should we call you (Mr. or Ms.)? ")                                         #Asking salutation.
        new_spy['salutation'] = new_spy['salutation'].strip()                                                               #Removing extra whitespaces.
        if len(new_spy['salutation'])>0:
            new_spy['name'] = new_spy['salutation'] + " " +new_spy['name']                                                  #updating spy name with salutation.
            print "Alright " + new_spy['name'] + ". I'd like to know a little bit more about you before we proceed..."
            break
        else:
            print "Please enter a valid salutation."
    #.............................................




    #Ask spy for his/her age.
    #........................
    loop_count = 0
    while(True):                                                                                           #loop for handling invalid input cases.
        if loop_count > 4:                                                                                 #escaping from infinite cases. If someone do knowingly.
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Bye bye."
            exit()

        loop_count = loop_count + 1
        new_spy['age'] = raw_input("What is your age? ")                                                    #asking age.
        new_spy['age'] = new_spy['age'].replace(" ", "")                                                    #Removing extra whitespaces.
        try:
            new_spy['age'] = int(new_spy['age'])                                                            #updating spy age and handling if not an integer.
            break
        except:
            print "Please enter a valid age."

    if new_spy['age'] <= 12 or new_spy['age'] >= 50:                                                        #age should be between 12 and 50.
        print "Sorry you are not of the correct age to be a spy "
        exit()
    #........................




    #Ask spy for his/her rating
    #..........................
    loop_count = 0
    while(True):                                                                                            #loop for handling invalid input cases.
        if loop_count > 4:                                                                                  #escaping from infinite cases. If someone do knowingly
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Bye bye."
            exit()

        loop_count = loop_count + 1
        new_spy['rating'] = raw_input("What is your spy rating? ")                                           #asking spy_rating.
        new_spy['rating'] = new_spy['rating'].replace(" ","")                                                #Removing extra whitespaces.
        try:
            new_spy['rating'] = float(new_spy['rating'])                                                      #updating spy age and handling if not a float.
            if new_spy['rating'] < 10.0:                                                                      #handling if spy_rating entered is greater than 10.
                break
            else:
                print "We are expecting rating out of 10"
        except:
            print "Please enter a valid rating."

    if new_spy['rating'] > 4.5:                                                                               #Complementry message according to spy_rating.
        print "Great ace!"
    elif new_spy['rating'] > 3.5 and new_spy['rating'] <=4.5:
        print "You are one of the good ones."
    elif new_spy['rating'] >= 2.5 and new_spy['rating'] <=3.5:
        print "You can always do better."
    else:
        print "We can always use somebody to help in the office."
    #.........................




    #Now we have all basic information about spy.
    #...........................................
    new_spy['is_online'] = True
    return (new_spy)
    #...........................................

#End of basic_info() method.......................................................................................................................................................





#This method will input new friend's detail.
#.................................................................................................................................................................................
def friend_info(user_spy_rating):
    new_friend = {
        "name": None,
        "salutation": None,
        "age": 0,
        "rating": 0,
        "is_online": False
    }


    # Taking friend's name.
    # .................................................

    loop_count = 0
    while (True):                                                                                            # loop for handling invalid input cases.
        if loop_count > 4:                                                                                   # escaping from infinite cases. If someone do knowingly.
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Try again."
            return (new_friend)

        loop_count = loop_count + 1
        new_friend['name'] = raw_input("Please add your friend's name: ")
        new_friend['name'] = new_friend['name'].strip()                                                       # Removes extra whitespaces.
        if len(new_friend['name']) > 0:                                                                       # Checking for blank name.
            break
        else:
            new_friend['name'] = None
            print "Please enter a valid name. "
    # .................................................




    # Ask salutation for the friend and error handling.
    # .............................................
    loop_count = 0
    while (True):                                                                                            # loop for handling invalid input cases.
        if loop_count > 4:                                                                                   # escaping from infinite cases. If someone do knowingly.
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Try again."
            return (new_friend)

        loop_count = loop_count + 1
        new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")                                        # Asking salutation.
        new_friend['salutation'] = new_friend['salutation'].strip()                                           # Removing extra whitespaces.
        if len(new_friend['salutation']) > 0:
            new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']                          # updating friend name with salutation.
            break
        else:
            new_friend['salutation'] = None
            print "Please enter a valid salutation."
    # .............................................




    # Ask spy for friend's age.
    # ........................
    loop_count = 0
    while (True):                                                                                            # loop for handling invalid input cases.
        if loop_count > 4:                                                                                   # escaping from infinite cases. If someone do knowingly.
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Try again."
            return (new_friend)

        loop_count = loop_count + 1
        new_friend['age'] = raw_input("Age? ")                                                                # asking age.
        new_friend['age'] = new_friend['age'].replace(" ", "")                                                # Removing extra whitespaces.
        try:
            new_friend['age'] = int(new_friend['age'])                                                        # updating friend age and handling if not an integer.
            break
        except:
            new_friend['age'] = 0
            print "Please enter a valid age."

    if new_friend['age'] <= 12 or new_friend['age'] >= 50:                                                     # age should be between 12 and 50.
        new_friend['age'] = 0
        print "Sorry your friend is not of the correct age to be a spy "
        return (new_friend)
    # ........................




    # Ask spy for friends rating
    # ..........................
    loop_count = 0
    while (True):                                                                                              # loop for handling invalid input cases.
        if loop_count > 4:                                                                                     # escaping from infinite cases. If someone do knowingly.
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Try again."
            return (new_friend)

        loop_count = loop_count + 1
        new_friend['rating'] = raw_input("Spy rating? ")                                                        # asking spy_rating.
        new_friend['rating'] = new_friend['rating'].replace(" ", "")                                            # Removing extra whitespaces.
        try:
            new_friend['rating'] = float(new_friend['rating'])                                                                # updating spy age and handling if not a float.
            if new_friend['rating'] > user_spy_rating and new_friend['rating'] <=10:                                          # handling if spy_rating entered is greater than 10.
                break
            elif new_friend['rating'] <= user_spy_rating:
                new_friend['rating'] = 0
                print "Can not be your friend rating is less. "
                break
            else:
                new_friend['rating'] = 0
                print "We are expecting rating out of 10"
        except:
            new_friend['rating'] = 0
            print "Please enter a valid rating."


    # Now we have all basic information about friend.
    # ...........................................
    new_friend['is_online'] = True
    return (new_friend)
#End of friend info method........................................................................................................................................................





#Add status method update the status.
#.................................................................................................................................................................................
def add_status(current_status_message):
    if current_status_message != None:
        print "Your current status message is " + current_status_message
    else:
        print 'You don\'t have any status message currently.'
    loop_count = 0
    while True:
        if loop_count > 4:
            print "Too many wrong attempt, This is a spy chat not a Game."
            break
        loop_count = loop_count + 1

        default = raw_input("Do you want to select from the older status (y/n)? or Want to go the main menu (1)?  ")
        default = default.replace(" ", "")
        default = default.upper()

        if default == "Y" or default == "YES":                                                               # In case of selecting from older status.
            if(len(status_messages)>0):
                item_position = 1
                for message in status_messages:
                    print "%d.%s"%(item_position,message)
                    item_position = item_position + 1
                try:
                    message_selection = int(raw_input("Choose from the above messages. "))
                    current_status_message =status_messages[message_selection - 1]
                    break
                except:
                    print "Invalid Input."
            else:
                print "You don/'t have any previous Status message."
                break

        elif default == "N" or default == "NO":                                                             # To update with new status.
            new_status_message = raw_input("What status message do you want to set?")
            new_status_message = new_status_message.strip()
            if len(new_status_message) > 0:
                current_status_message = new_status_message
                status_messages.append(current_status_message)
                break
            else:
                print "Can not set a blank status message."

        elif default == "1":
            break

        else:
            print "Please provide valid input (Y/N) "

    return current_status_message

#End of add status method.........................................................................................................................................................





#Select a friend in friend list.
#..................................................................................................................................................................................
def select_friend():
    item_number = 0
    num_of_friend = len(friends)
    friend_choice = 0
    if num_of_friend > 0:
        for friend in friends:
            print '%d. %s  online_status = %s' % ((item_number + 1),friend['name'],friend['is_online'])
            item_number = item_number + 1
        friend_choice = raw_input("Select from above frinds: ")
        friend_choice = friend_choice.strip()
        try:
            friend_choice = int(friend_choice)
            if friend_choice > 0 and friend_choice <= num_of_friend:
                friend_choice_position = friend_choice - 1
                return friend_choice_position
            elif friend_choice == 0:
                print "What Do you want to contact GOD!"
                return None
            else:
                print "I think that number is not in the list."
                return None
        except:
            print  "Please enter a valid input"
            return None
    else:
        print "You have no friends in your friend list"
        return None
#End of select a friend method.....................................................................................................................................................





#Send message method will send message.............................................................................................................................................
#..................................................................................................................................................................................
def send_message():
    index = select_friend()
    if index != None:
        print "selected friend %s aged %d with rating %.2f is online" %(friends[index]["name"], friends[index]["age"], friends[index]["rating"])
#End of send_message method........................................................................................................................................................





#Add friend method will add new friend.
#.................................................................................................................................................................................
def add_friend(user_spy_rating):
    new_friend = friend_info(user_spy_rating)
    if new_friend['rating'] != 0:
        friends.append(new_friend)
        print "friend added successfully. "
    return len(friends)


#End of add friend method.........................................................................................................................................................





#Start chat method provide menu for the app.
#.................................................................................................................................................................................
def start_chat(spy):
    current_status_message = None
    show_menu = True
    menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"

    while show_menu:
        menu_choice = raw_input(menu_choices)
        menu_choice = menu_choice.strip()

        if (menu_choice == "1"):
            current_status_message = add_status(current_status_message)
            if current_status_message != None:
                print "Status updated successfully "+current_status_message

        elif(menu_choice == "2"):
            total_friend = add_friend(spy['rating'])
            if total_friend > 1:
                print "You have total %d friends in your friend list"%(total_friend)
            else:
                print "You have %d friend in your friend list"%(total_friend)

        elif(menu_choice == "3"):
            send_message()
        #elif(menu_choice == "4"):
         #   read_message()
        #elif(menu_choice == "5"):
         #   read_chat
        elif menu_choice == "6":
            show_menu = False
        else:
            print "Please provide valid input."

#End of start chat and menu method................................................................................................................................................





#start of chat application start of applictaion.
# .....................................................................................................................................................
print 'Let\'s get started'

question_string = "Continue as "+ default_spy["salutation"] +" "+default_spy["name"]+"(Y/N)? "              #Ask to start with default user details.
existing = raw_input(question_string)                                                                       #handling input.
existing = existing.replace(" ","")
existing = existing.upper()

if existing == "Y" or existing == "YES":                                                                    #In case of default, using default values.
    spy = default_spy
    spy['name'] = spy['salutation']+spy['name']
elif existing == "N" or existing == "NO":                                                                   #calling basic_info method to input values.
    spy = basic_info()
else:
    print "Please provide valid input (Y/N) "
    exit()


print "Authentication complete. Welcome %s, age: %d and rating of: %.2f. Proud to have you onboard" % (spy['name'], spy['age'], spy['rating'])
start_chat(spy)


#end of chat applictaion.................................................................................................................................