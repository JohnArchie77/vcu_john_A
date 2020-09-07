def check_users(current_us, new_us):
    pass
    current_us = ['chris', 'haritha', 'sally', 'darnell', 'superman','john']
    new_us = ['george', 'ringo', 'superman', 'hannibal','John']

    current_us = [itm.lower() for itm in current_us]
    for new_us in new_us:
        if new_us.lower() in current_us:
            print("Sorry, can not use that user name")
        else:
            print("That user name is available ")


if __name__=="__main__":
    current_us = ['chris', 'haritha', 'sally', 'darnell', 'superman','john']
    new_us = ['george', 'ringo', 'superman', 'hannibal','John']
    check_users(current_us, new_us)