from spy_details import default_spy, Spy, ChatMessage, friends, special_words
from steganography.steganography import Steganography
from datetime import datetime

status_messages = []





#this method will input all data if user does not select default.(no parameter, return type new_spy)
#...................................................................................................................................................................................
def basic_info():
    new_spy = Spy("", "", 0, 0.0)                                                                                       # Object of type Spy class.

    #Taking spy name and displaying a welcome message.
    #.................................................
    loop_count = 0
    while(True):                                                                                                        # loop for handling invalid input cases.
        if loop_count > 4:                                                                                              # escaping from infinite cases. If someone do knowingly.
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Bye bye."
            exit()

        loop_count = loop_count + 1
        new_spy.name = raw_input("Please tell me your name? ")
        new_spy.name = new_spy.name.strip()                                                                             # Removes extra whitespaces.
        if len(new_spy.name) > 0:                                                                                       # Checking for blank name.
            print 'Welcome ' + new_spy.name + '. Glad to have you back with us.'
            break
        else:
            print "Please enter a valid name. "
    #.................................................




    #Ask salutation for the spy and error handling.
    #.............................................
    loop_count = 0
    while(True):                                                                                                        # loop for handling invalid input cases.
        if loop_count > 4:                                                                                              # escaping from infinite cases. If someone do knowingly.
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Bye bye."
            exit()

        loop_count = loop_count + 1
        new_spy.salutation = raw_input("What should we call you (Mr. or Ms.)? ")                                        # Asking salutation.
        new_spy.salutation = new_spy.salutation.strip()                                                                 # Removing extra whitespaces.
        if len(new_spy.salutation) > 0:
            new_spy.name = new_spy.salutation + " " +new_spy.name                                                       # updating spy name with salutation.
            print "Alright " + new_spy.name + ". I'd like to know a little bit more about you before we proceed..."
            break
        else:
            print "Please enter a valid salutation."
    #.............................................




    #Ask spy for his/her age.
    #........................
    loop_count = 0
    while(True):                                                                                                        # loop for handling invalid input cases.
        if loop_count > 4:                                                                                              # escaping from infinite cases. If someone do knowingly.
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Bye bye."
            exit()

        loop_count = loop_count + 1
        new_spy.age = raw_input("What is your age? ")                                                                   # asking age.
        new_spy.age = new_spy.age.replace(" ", "")                                                                      # Removing extra whitespaces.
        try:
            new_spy.age = int(new_spy.age)                                                                              # updating spy age and handling if not an integer.
            break
        except:
            print "Please enter a valid age."

    if new_spy.age <= 12 or new_spy.age >= 50:                                                                          # age should be between 12 and 50.
        print "Sorry you are not of the correct age to be a spy "
        exit()
    #........................




    #Ask spy for his/her rating
    #..........................
    loop_count = 0
    while(True):                                                                                                        # loop for handling invalid input cases.
        if loop_count > 4:                                                                                              # escaping from infinite cases. If someone do knowingly
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Bye bye."
            exit()

        loop_count = loop_count + 1
        new_spy.rating = raw_input("What is your spy rating? ")                                                         # asking spy_rating.
        new_spy.rating = new_spy.rating.replace(" ", "")                                                                # Removing extra whitespaces.
        try:
            new_spy.rating = float(new_spy.rating)                                                                      # updating spy age and handling if not a float.
            if new_spy.rating <= 5.0:                                                                                   # handling if spy_rating entered is greater than 5.
                break
            else:
                print "We are expecting rating out of 5."
        except:
            print "Please enter a valid rating."

    if new_spy.rating > 4.5:                                                                                            # Complementry message according to spy_rating.
        print "Great ace!"
    elif 3.5 < new_spy.rating <= 4.5:
        print "You are one of the good ones."
    elif 2.5 <= new_spy.rating <= 3.5:
        print "You can always do better."
    else:
        print "We can always use somebody to help in the office."
    #.........................

    return new_spy

#End of basic_info() method.......................................................................................................................................................





#This method will input new friend's detail(no parameter and return type of Spy class new friend.)
#.................................................................................................................................................................................
def friend_info(user_spy_rating):
    new_friend = Spy("", "", 0, 6.0)                                                                                    # new friend of type Spy class.


    # Asking for friend's name.
    # .................................................

    loop_count = 0
    while True:                                                                                                         # loop for handling invalid input cases.
        if loop_count > 4:                                                                                              # escaping from infinite cases. If someone do knowingly.
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Try again."
            return new_friend
        loop_count = loop_count + 1

        new_friend.name = raw_input("Please add your friend's name: ")
        new_friend.name = new_friend.name.strip()                                                                       # Removes extra whitespaces.
        if len(new_friend.name) > 0:                                                                                    # Checking for blank name.
            break
        else:
            new_friend.name = ""
            print "Please enter a valid name. "
    # .................................................




    # Ask salutation for the friend and error handling.
    # .............................................
    loop_count = 0
    while True:                                                                                                         # loop for handling invalid input cases.
        if loop_count > 4:                                                                                              # escaping from infinite cases. If someone do knowingly.
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Try again."
            return new_friend
        loop_count = loop_count + 1

        new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")                                                     # Asking salutation.
        new_friend.salutation = new_friend.salutation.strip()                                                           # Removing extra whitespaces.
        if len(new_friend.salutation) > 0:
            new_friend.name = new_friend.salutation + " " + new_friend.name                                             # updating friend name with salutation.
            break
        else:
            new_friend.salutation = ""
            print "Please enter a valid salutation."
    # .............................................




    # Ask spy for friend's age.
    # ........................
    loop_count = 0
    while True:                                                                                                         # loop for handling invalid input cases.
        if loop_count > 4:                                                                                              # escaping from infinite cases. If someone do knowingly.
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Try again."
            return new_friend
        loop_count = loop_count + 1

        new_friend.age = raw_input("Age? ")                                                                             # asking age.
        new_friend.age = new_friend.age.replace(" ", "")                                                                # Removing extra whitespaces.
        try:
            new_friend.age = int(new_friend.age)                                                                        # updating friend age and handling if not an integer.
            break
        except:
            new_friend.age = 0
            print "Please enter a valid age."

    if new_friend.age <= 12 or new_friend.age >= 50:                                                                    # age should be between 12 and 50.
        new_friend.age = 0
        print "Sorry your friend is not of the correct age to be a spy "
        return new_friend
    # ........................




    # Ask spy for friends rating
    # ..........................
    loop_count = 0
    while True:                                                                                                         # loop for handling invalid input cases.
        if loop_count > 4:                                                                                              # escaping from infinite cases. If someone do knowingly.
            print "You are too DUMB to be a SPY or your keyboard need to be repaired, Try again."
            return new_friend
        loop_count = loop_count + 1

        new_friend.rating = raw_input("Spy rating? ")                                                                   # asking spy_rating.
        new_friend.rating = new_friend.rating.replace(" ", "")                                                          # Removing extra whitespaces.
        try:
            new_friend.rating = float(new_friend.rating)                                                                # updating spy age and handling if not a float.
            if user_spy_rating <= new_friend.rating <= 5:                                                               # handling if spy_rating entered is greater than 5.
                break
            elif new_friend.rating < user_spy_rating:                                                                   # If friends rating is less than spy.
                new_friend.rating = 6
                print "Can not be your friend rating is less. "
                break
            else:
                new_friend.rating = 6
                print "We are expecting rating out of 5"
        except:
            new_friend.rating = 6                                                                                       # Not entered a float Value.
            print "Please enter a valid rating."

    # ............................
    return new_friend

#End of friend info method........................................................................................................................................................





#Add friend method will add new friend(take spy rating and return total friend in list)
#.................................................................................................................................................................................
def add_friend(user_spy_rating):
    new_friend = friend_info(user_spy_rating)                                                                           # This will call friend_info to enter new friend.
    if new_friend.rating != 6:                                                                                          # Checking if info collected or not.
        friends.append(new_friend)                                                                                      # Adding to list.
        print "friend added successfully. "
    return len(friends)                                                                                                 # Number of friends.


#End of add friend method.........................................................................................................................................................





#Update_avg method will update avg words spoken by friends.
#.................................................................................................................................................................................
def update_avg(sender,text):
    friends[sender].sent_chats = friends[sender].sent_chats + 1                                                         # Updating total chats.
    text = text.split()
    text = len(text)                                                                                                    # Calculating new message length.
    friends[sender].total_words = friends[sender].total_words + text

    avg_words = friends[sender].total_words / friends[sender].sent_chats                                                # calculating avg words.

    if avg_words > 100:
        print "%s was speaking too much, so deleted from your friends list." % friends[sender].name                     # Deleting if speaking too much.
        del friends[sender]

#End of update_avg method.........................................................................................................................................................





#Check_special method will check for special word in message.
#.................................................................................................................................................................................
def check_special(text):
    contained = False
    text = text.upper()                                                                                                 # converting all text to upper for better matcing.

    for special_word in special_words:
        found = text.find(special_word)                                                                                 # Checking for special words.
        if found != -1:
            contained = True
            break
    return contained

#End of check_special method......................................................................................................................................................





#Add status method update the status.(one parameter of type string current status. one retuen type of string current status.)
#.................................................................................................................................................................................
def add_status(current_status_message):
    if current_status_message is not None:
        print "Your current status message is " + current_status_message                                                # displaying cureent status message.
    else:
        print 'You don\'t have any status message currently.'
    loop_count = 0
    while True:                                                                                                         # Loop to handle too many invalid cases.
        if loop_count > 4:
            print "Too many wrong attempt, This is a spy chat not a Game."
            break
        loop_count = loop_count + 1

        default = (raw_input("Do you want to select from the older status (y/n)? or Want to go the main menu (1)?  ")).replace(" ", "").upper()

        if default == "Y" or default == "YES":                                                                          # In case of selecting from older status.
            if len(status_messages) > 0:                                                                                # If there are old statuses.
                item_position = 1
                for message in status_messages:                                                                         # printing older messages.
                    print "%d.%s" % (item_position, message)
                    item_position = item_position + 1
                message_selection = (raw_input("Choose from the above messages. ")).strip()
                try:
                    message_selection = int(message_selection)                                                          # checking for selected status message.
                    if message_selection > 0:
                        current_status_message = status_messages[message_selection - 1]
                        break
                    else:
                        print "Invalid Input"                                                                           # handling index out of bond and non-integer.
                except:
                    print "Invalid Input."
            else:
                print "You don/'t have any previous Status message."
                break

        elif default == "N" or default == "NO":                                                                         # To update with new status.
            new_status_message = raw_input("What status message do you want to set? ")
            new_status_message = new_status_message.strip()
            if len(new_status_message) > 0:                                                                             # checking for blank input.
                current_status_message = new_status_message
                status_messages.append(current_status_message)
                break
            else:
                print "Can not set a blank status message."

        elif default == "1":                                                                                            # return to main menu
            break

        else:
            print "Please provide valid input (Y/N) "                                                                   # if user input anything else than required.

    return current_status_message

#End of add status method.........................................................................................................................................................





#Select a friend in friend list(No parameter and return a index in list of friends.)
#..................................................................................................................................................................................
def select_friend():
    item_number = 0                                                                                                     # Iterrative variable for for loop.
    num_of_friend = len(friends)                                                                                        # Number of total friends.
    if num_of_friend > 0:                                                                                               # Checking for no friends
        for friend in friends:
            print '%d. %s  online_status = %s' % ((item_number + 1), friend.name, friend.is_online)                     # Printing every friend.
            item_number = item_number + 1
        friend_choice = raw_input("Select from above friends: ")
        friend_choice = friend_choice.replace(" ", "")                                                                  # Handling Input.
        try:
            friend_choice = int(friend_choice)
            if 0 < friend_choice <= num_of_friend:
                friend_choice_position = friend_choice - 1
                return friend_choice_position
            elif friend_choice == 0:
                print "What Do you want to contact GOD!"
                return None
            else:
                print "I think that number is not in the list."
                return None
        except:
            print "Please enter a valid input"
            return None
    else:
        print "You have no friends in your friend list"
        return None
#End of select a friend method.....................................................................................................................................................





#Send message method will send message(No parameter and no return type).
#..................................................................................................................................................................................
def send_message():
    friend_choice = select_friend()                                                                                     # select a friend.
    if friend_choice is not None:                                                                                       # Checking if friend selected or not.
        loop_count = 0
        while True:
            if loop_count > 10:
                print "Too many wrong attempt, Please try after sometime."                                              # Loop for handling invalid cases.
                break
            loop_count = loop_count + 1

            original_image = raw_input("What is the name of the image? ")                                               # Asking for image file.
            original_image = original_image.strip()
            if len(original_image) > 0:                                                                                 # Checking for blank input.
                output_path = 'output.jpg'
                text = raw_input("What do you want to say?")                                                            # asking for secret message.
                text_modified = text.strip()
                if len(text_modified) > 0:                                                                              # if message is not blank
                    try:
                        Steganography.encode(original_image, output_path, text)
                        new_chat = ChatMessage(text, True)
                        friends[friend_choice].chats.append(new_chat)                                                   # Adding to chat history
                        print ("Your secret message is ready!")
                        break
                    except:
                        print "File not Found (Please select a valid image file). Try Again."                           # Handling file not found error.
                else :
                    question = raw_input("Do you want to send a blank message? (y/n)")                                  # Asking for blank message to send.
                    question = question.replace(" ", "")
                    question = question.upper()
                    if question == "Y" or question == "YES":
                        try:
                            Steganography.encode(original_image, output_path, text)
                            new_chat = ChatMessage(text, True)
                            friends[friend_choice].chats.append(new_chat)
                            print ("Your secret message is ready!")
                            break
                        except:
                            print "File not Found (Please select a valid image file). Try Again."
                    elif question == "N" or question == "NO":
                        break
                    else :
                        print "Invalid input (y/n)"
            else:
                print "Please enter a valid file name. "
#End of send_message method........................................................................................................................................................





#Read message method will read message(No parameter and no retuen type.)
#....................................................................................................................................................................................
def read_message():
    sender = select_friend()                                                                                            # Select a friend.
    if sender is not None:
        loop_count = 0
        while True:
            if loop_count > 10:
                print "Too many wrong attempt, Please try after sometime."                                              # Loop fro handling too many invalid inputs
                break
            loop_count = loop_count + 1

            output_path = raw_input("What is the name of the file? ")                                                   # Asking for output file.
            output_path = output_path.strip()
            if len(output_path) > 0:                                                                                    # Checking for blank file name.
                try:
                    secret_text = Steganography.decode(output_path)
                    secret_text = secret_text.strip()
                    if check_special(secret_text):                                                                      # Checking for special words.
                        print "!!!!EMERGENCY!!!!"
                    print "Message = %s" % secret_text
                    if len(secret_text) == 0:                                                                           # Decoding Message.
                        print "Your friend has sent you a blank message"
                    new_chat = ChatMessage(secret_text, False)                                                          # saving in chat History.
                    friends[sender].chats.append(new_chat)
                    print "Your secret message has been saved!"
                    update_avg(sender, secret_text)
                    break
                except:
                    print "File Not Found (Please select a valid image file). Try Again. "
            else:
                print "Please enter a valid file name. "

#End of read message method..........................................................................................................................................................





#Read chat method this will read chat from selected friend.(no parameter and return type.)
#.....................................................................................................................................................................................
def read_chat():
    sender = select_friend()                                                                                            # Select a friend.
    if sender is not None:
        if len(friends[sender].chats) > 0:                                                                              # Checking if there are no chat history.
            counter = 0
            for chat in friends[sender].chats:
                counter = counter + 1
                time_of_message = chat.time                                                                             # printing chat history.
                if chat.sent_by_me:
                    status = "sent"
                else:
                    status = "recieved"
                print "%d. " % counter + time_of_message.strftime("%d-%m-%y %H:%M:%S") + " " + status + "  '" + chat.message + "'"

        else:
            print ("No chat history from selected friend")


#.....................................................................................................................................................................................





#Start chat method provide menu for the app(one parameter of type Spy class, no return type.)
#.................................................................................................................................................................................
def start_chat(spy):
    current_status_message = None
    show_menu = True
    menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"

    while show_menu:
        menu_choice = (raw_input(menu_choices)).strip()                                                                 # Asking for a input in menu.

        if menu_choice == "1":                                                                                          # Calling status update if 1.
            spy.current_status_message = add_status(spy.current_status_message)
            if spy.current_status_message is not None:
                print "Status updated successfully "+spy.current_status_message

        elif menu_choice == "2":                                                                                        # Calling add friend if 2.
            total_friend = add_friend(spy.rating)
            if total_friend > 1:
                print "You have total %d friends in your friend list" % total_friend
            else:
                print "You have %d friend in your friend list" % total_friend

        elif menu_choice == "3":                                                                                        # Calling send message if 3.
            send_message()
        elif menu_choice == "4":                                                                                        # Calling read message if 4.
            read_message()
        elif menu_choice == "5":                                                                                        # Calling read caht if 5.
            read_chat()
        elif menu_choice == "6":                                                                                        # Exit from applicatoon.
            show_menu = False
        else:                                                                                                           # handling invalid inputs.
            print "Please provide valid input."

#End of start chat and menu method................................................................................................................................................





#start of chat application start of applictaion.
# ................................................................................................................................................................................
print "Welcome to spy_chat. (version 1.0)"
print 'Let\'s get started'

question_string = "Continue as " + default_spy.name + "(Y/N)? "                                                         # Ask to start with default user details.
existing = (raw_input(question_string)).replace(" ", "").upper()                                                        # handling input.

if existing == "Y" or existing == "YES":                                                                                # In case of default, using default values.
    spy = default_spy
elif existing == "N" or existing == "NO":                                                                               # Calling basic_info method to input values.
    spy = basic_info()
else:
    print "Please provide valid input (Y/N) "
    exit()


print "Authentication complete. Welcome %s, age: %d and rating of: %.2f. Proud to have you onboard" % (spy.name, spy.age, spy.rating)
start_chat(spy)


#end of chat applictaion.................................................................................................................................