loop_count = 0
while (True):
    if loop_count > 4:
        print "You are too DUMB to be a SPY or your keyboard need to be repaired, Bye bye."
        exit()

    loop_count = loop_count + 1
    spy_rating = raw_input("What is your spy rating? ")
    spy_rating = spy_rating.replace(" ", "")
    try:
        spy_rating = float(spy_rating)
        if spy_rating < 10.0:
            break
        else:
            print "We are expecting rating out of 10"
    except:
        print "Please enter a valid rating."

print spy_rating
print type(spy_rating)