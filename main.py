print 'Let\'s get started'



#Taking spy name and displaying a welcome message.
#.................................................
spy_name = raw_input("What is your name?")
spy_name = spy_name.strip()                                                                         #Removes extra whitespaces.

if len(spy_name)>0:                                                                                 #Checking for blank name.
    print 'Welcome ' + spy_name + '. Glad to have you back with us.'
else:
    print "Please enter a valid name."                                                              #First input in app so exit will be better than asking again.
    exit()



#Ask salutation for the spy and error handling.
#.............................................
loop_count = 0
while(True):                                                                                         #loop for handling invalid input cases.
    if loop_count > 4:                                                                               #escaping from infinite cases. If someone do knowingly.
        print "You are too DUMB to be a SPY, Bye bye."
        exit()

    loop_count = loop_count + 1
    spy_salutation = raw_input("What should we call you (Mr. or Ms.)?")                              #Asking salutation.
    spy_salutation = spy_salutation.strip()                                                          #Removing extra whitespaces.
    if len(spy_salutation)>0:
        spy_name = spy_salutation + " " +spy_name                                                    #updating spy name with salutation.
        print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."
        break
    else:
        print "Please enter a valid salutation."
