#Author Markus Lu A01224733

#Get and return the appropriate messgae for the given level.
def get_lvl_message(lvl):
    filename = r'messages\message_' + str(lvl) +'.txt'
    with open(filename,'r') as data:
        message = data.read()
        print(f'\n{message}\n')