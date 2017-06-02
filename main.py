print 'Let\'s get started'




#Taking spy name and displaying a welcome message.
#.................................................
spy_name = raw_input("What is your name? ")
spy_name = spy_name.strip()                                                                         #Removes extra whitespaces.

if len(spy_name)>0:                                                                                 #Checking for blank name.
    print 'Welcome ' + spy_name + '. Glad to have you back with us.'
else:
    print "Please enter a valid name. "                                                              #First input in app so exit will be better than asking again.
    exit()




#Ask salutation for the spy and error handling.
#.............................................
loop_count = 0
while(True):                                                                                         #loop for handling invalid input cases.
    if loop_count > 4:                                                                               #escaping from infinite cases. If someone do knowingly.
        print "You are too DUMB to be a SPY or your keyboard need to be repaired, Bye bye."
        exit()

    loop_count = loop_count + 1
    spy_salutation = raw_input("What should we call you (Mr. or Ms.)? ")                              #Asking salutation.
    spy_salutation = spy_salutation.strip()                                                          #Removing extra whitespaces.
    if len(spy_salutation)>0:
        spy_name = spy_salutation + " " +spy_name                                                    #updating spy name with salutation.
        print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."
        break
    else:
        print "Please enter a valid salutation."




#Ask spy for his/her age.
#........................
loop_count = 0
while(True):                                                                                           #loop for handling invalid input cases.
    if loop_count > 4:                                                                                 #escaping from infinite cases. If someone do knowingly.
        print "You are too DUMB to be a SPY or your keyboard need to be repaired, Bye bye."
        exit()

    loop_count = loop_count + 1
    spy_age = raw_input("What is your age? ")                                                           #asking age.
    spy_age = spy_age.replace(" ", "")                                                                  #Removing extra whitespaces.
    try:
        spy_age = int(spy_age)                                                                          #updating spy age and handling if not an integer.
        break
    except:
        print "Please enter a valid age."

if spy_age <= 12 and spy_age >= 50:                                                                     #age should be between 12 and 50.
    print "Sorry you are not of the correct age to be a spy "
    exit()




#Ask spy for his/her rating
#..........................
loop_count = 0
while(True):                                                                                            #loop for handling invalid input cases.
    if loop_count > 4:                                                                                  #escaping from infinite cases. If someone do knowingly
        print "You are too DUMB to be a SPY or your keyboard need to be repaired, Bye bye."
        exit()

    loop_count = loop_count + 1
    spy_rating = raw_input("What is your spy rating? ")                                                 #asking spy_rating.
    spy_rating = spy_rating.replace(" ","")                                                             #Removing extra whitespaces.
    try:
        spy_rating = float(spy_rating)                                                                  #updating spy age and handling if not an integer.
        if spy_rating < 10.0:                                                                           #handling if spy_rating entered is greater than 10.
            break
        else:
            print "We are expecting rating out of 10"
    except:
        print "Please enter a valid rating."


if spy_rating > 4.5:                                                                                    #Complementry message according to spy_rating.
    print "Great ace!"
elif spy_rating > 3.5 and spy_rating <=4.5:
    print "You are one of the good ones."
elif spy_rating >= 2.5 and spy_rating <=3.5:
    print "You can always do better."
else:
    print "We acn always use somebody to help in the office."




#Now we have all basic information about spy.
#...........................................
spy_is_online = True

print "Authentication complete. Welcome %s, age: %d and rating of: %.2f. Proud to have you onboard" % (spy_name, spy_age, spy_rating)