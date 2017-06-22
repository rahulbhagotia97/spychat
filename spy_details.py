from datetime import datetime
STATUS_MESSAGES = ['You know the rules of the game.'
                   'Report Back to me when this all makes sense.'
                   'This is the best bad idea we have ,sir. by far']
friends_menu = '\n1. Add a friend' \
               '\n2. Remove a friend' \
               '\n3. Block a friend' \
               '\n4. Go back to main menu'
block_menu = '\n1. Block a contact' \
             '\n2. Unblock a contact' \
             '\n3. Go back to previous menu' \
             '\n4. Go back to main menu'
menu_choices = "\nwhat u want to do ?'"
             "\n 1. Update status "\
             "\n 2. Friend settings "\
             "\n 3. send a secret message "\
             "\n 4. read a secret message "\
             "\n 5. read chats from a user "\
             "\n 6. Close application \n"
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('bond', 'Mr.', 24, 4.7)

friend_one = Spy('Raja', 'Mr.', 4.9, 27)
friend_two = Spy('Mata Hari', 'Ms.', 4.39, 21)
friend_three = Spy('No', 'Dr.', 4.95, 37)


friends = [friend_one, friend_two, friend_three]