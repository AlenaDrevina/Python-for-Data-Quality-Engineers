import datetime
import random

class PrintMessage:
    def __init__(self, message):
        self.message = message

    def print_message(self):                   # create a method which inserts the formatted text into text file newsfeed05
        ptf = open("newsfeed05.txt", "a")      # open file to add
        print(self.message, file=ptf)
        ptf.close()                            # close file

class News:
    def __init__(self, news_msg, location):
        self.news_msg = news_msg               # news_info
        self.location = location               # location where it has happened

    def news_message(self):                    # create a method which creates a news (text, city, time)
        message = f'News ----------------------------\n{self.news_msg}\n{self.location}, {datetime.datetime.now().strftime("%d/%m/%y %H:%M")}\n---------------------------------\n\n'
        self.ptf = PrintMessage(message)
        ptf = self.ptf
        ptf.print_message()


class Advertising:
    def __init__(self, adv_message, actual_until=None):
        self.adv_message = adv_message
        self.actual_until = actual_until

    def advertising(self):                     # create a method which creates an advertisement (text, expiration day, how many days left)
        message = f'Private Ad -----------------------\n{self.adv_message}\nActual until: {self.actual_until}, {(datetime.datetime.strptime(self.actual_until, "%d/%m/%y") - datetime.datetime.now()).days} days left\n----------------------------------\n\n'
        self.ptf = PrintMessage(message)
        ptf = self.ptf
        ptf.print_message()


class WhatIs:
    def __init__(self, answer):
        self.answer = answer

    def ask_question(self):                   # create an interactive method with indicating possibility using random
        rand_num_list = [random.randrange(1, 100) for i in range(1)]
        question = f'How do you think? ----------------\nTomorrow it will be rainy in your city?\nYour answer - "{self.answer}",\nprobability will be {rand_num_list[0]} %\n----------------------------------\n\n'
        self.prt = PrintMessage(question)
        prt = self.prt
        prt.print_message()

class WhoIs:
    def __init__(self, birthday):
        self.birthday = birthday

    def ask_birthday(self):                   # ask the name to congratulate with today's birthday
        birth = f'Congratulation-------------------\nHappy birthday to {self.birthday}!\nWishing you a wonderful year of\ngood health,happiness and success!\n{datetime.date.today()}\n----------------------------------\n\n'
        self.prt = PrintMessage(birth)
        prt = self.prt
        prt.print_message()

class Guess:
    def __init__(self, guessing):
        self.guessing = guessing

    def ask_future(self):                   # create an interactive method with indicating possibility using random elements from list
        test_list = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'As I see it, yes',
                        'Most likely', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
                        'Don\'t count on it', 'My reply is no', 'My sources say no', 'Very doubtful']
        random_test_list = random.randint(0, len(test_list) - 1)
        prediction = f'Ask me about your future? --------\nYour question - "{self.guessing}",\nWitch\'s answer will be - {test_list[random_test_list]}\n----------------------------------\n\n'
        self.prt = PrintMessage(prediction)
        prt = self.prt
        prt.print_message()

class Choice:  # ask a user what data he wants to print and then call a class and insert the data into file using inserting method
    def __init__(self, flag):
        self.flag = flag

    def choose_message_type(self):
        if self.flag == '1':
            self.news = News(input('Please enter news text\n'), input('Please enter location\n'))
            news_mess = self.news
            news_mess.news_message()
        elif self.flag == '2':
            self.advng = Advertising(input('Please enter advertisement text\n'), input('Please enter expire date in the format dd/mm/yy\n'))
            adv_message = self.advng
            adv_message.advertising()
        elif self.flag == '3':
            self.question = WhatIs(input('Tomorrow it will be rainy in your city? Please enter your assumption\n'))
            question_mess = self.question
            question_mess.ask_question()
        elif self.flag == '4':
            self.birthday = WhoIs(input('Write the name of the person who has today\'s birthday\n'))
            answer_birthday = self.birthday
            answer_birthday.ask_birthday()
        elif self.flag == '5':
            self.guessing = Guess(input('Ask me about your near future\n'))
            question_divination = self.guessing
            question_divination.ask_future()
        else:
            print('Your choice is not correct')


make_your_choice = Choice(input('Please enter your choice:\n1 - News\n2 - Private Ad\n3 - Prediction\n4 - Congratulation\n5 - Divination\n\n'))
make_your_choice.choose_message_type()