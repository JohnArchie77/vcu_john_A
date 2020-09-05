def check_users(current_us, new_us):
    pass
    current_us = ['chris', 'haritha', 'sally', 'darnell', 'superman']
    new_us = ['george', 'ringo', 'superman', 'hannibal']
    new_list = []
    for current_us in current_us:
        new_list.append(current_us.lower())

available = [itm.lower() for itm in current_us]
for new_us in new_us:
    if new_us.lower() in current_us:
        print("Sorry, can not use that user name")
    else:
            print("That user name is available ")


if __name__=="__main__":
    current_us = ['chris', 'haritha', 'sally', 'darnell', 'superman']
    new_us = ['george', 'ringo', 'superman', 'hannibal']
    check_users(current_us, new_us)