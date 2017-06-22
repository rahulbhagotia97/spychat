from spy_details import spy, Spy, ChatMessage, STATUS_MESSAGES,\
    block_menu, friends_menu, menu_choices, block_list
from steganography.steganography import Steganography
from datetime import datetime
from function import add_friend,select_a_friend , read_chat
begin = 'Press any key to open the application'
any_key = raw_input(begin)

print 'The game is ON !!!'

question = 'Do you want to continue as ' + spy.salutation + ' ' + spy.name + ' (Y/N)? '
existing = raw_input(question)

while (existing.upper() != 'Y') and (existing.upper() != 'N'):
    print 'Invalid Input'
    existing = raw_input(question)


def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:
        password_test = getpass.getpass(prompt='Please enter your password again to continue ')

        while password_test != initial_password:

            print('The password is incorrect..!!!')
            password_test = getpass.getpass(prompt='Please enter the right password to continue ')

        else:
            print('\n')

        print 'Authentication complete. \nWelcome! ' + spy.name + ' \nAge: ' \
              + str(spy.age) + ' \nRating: ' + str(spy.rating) + ' \nSpy Chat mai aapka swaagat hai'

        show_menu = True

        while show_menu:
            menu()
    else:
        print 'Sorry you are not of the correct age to be a spy'


def menu():
    menu_choice = raw_input(menu_choices)

    if len(menu_choice) > 0:
        menu_choice = int(menu_choice)

        if menu_choice == 1:
            add_status()
        elif menu_choice == 2:
            add_friend()
        elif menu_choice == 3:
            send_message()
        elif menu_choice == 4:
            read_message()
        elif menu_choice == 5:
            read_chat_history()
        elif menu_choice == 6:
            print 'Application Closed'
        else:
            show_menu = False


def add_status():

    updated_status_message = None

    if spy.current_status_message != None:

        print 'Your current status message is %s \n' % spy.current_status_message
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % updated_status_message
    else:
        print 'You current don\'t have a status update'

    return updated_status_message


def add_friend():

    new_friend = Spy('', '', 0, 0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)


def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name,
                                                                friend.age, friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text, True)

    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"


def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text, False)

    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"


def read_chat_history():

    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)

if existing.upper() == "Y":
    initial_password = 'lessordinary'
    start_chat(spy)
else:

    spy = Spy('', '', 0, 0.0)

    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = int(raw_input("What is your age?"))

        spy.rating = float(raw_input("What is your spy rating?"))
        initial_password = getpass.getpass(prompt='Enter a password for your SpyChat account ')

        start_chat(spy)
    else:
        print 'Please add a valid spy name'
