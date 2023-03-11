import datetime
import random
from HW_module_4_task3 import text_decomposition_for_correctness as normalize
import os

class PrintMessage:
    def __init__(self, message):
        self.message = message

    # create a method which inserts the formatted text into text file
    def print_message(self):
        ptf = open("Module6_paste.txt", "a")      # open file to add
        print(self.message, file=ptf)
        ptf.close()                            # close file

class News:
    def __init__(self, news_msg, location):
        self.news_msg = news_msg               # news_info
        self.location = location               # location where it has happened

    # create a method which creates a news (text, city, time)
    def news_message(self):
        message = f'News ----------------------------\n{self.news_msg}\n{self.location},' \
                  f'{datetime.datetime.now().strftime("%d/%m/%y %H:%M")}\n' \
                  f'---------------------------------\n\n'
        PrintMessage(normalize(message)).print_message()

class Advertising:
    def __init__(self, adv_message, actual_until=None):
        self.adv_message = adv_message
        self.actual_until = actual_until

    # create a method which creates an advertisement (text, expiration day, how many days left)
    def advertising(self):
        message = f'Private Ad -----------------------\n{self.adv_message}\n' \
                  f'Actual until: {self.actual_until},' \
                  f'{(datetime.datetime.strptime(self.actual_until, "%d/%m/%y") - datetime.datetime.now()).days}days left\n' \
                  f'----------------------------------\n\n'
        PrintMessage(normalize(message)).print_message()

class Guess:
    def __init__(self, guessing):
        self.guessing = guessing

    # create an interactive method with indicating possibility using random elements from list
    def ask_future(self):
        test_list = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'As I see it, yes',
                        'Most likely', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
                        'Don\'t count on it', 'My reply is no', 'My sources say no', 'Very doubtful']
        random_test_list = random.randint(0, len(test_list) - 1)
        prediction = f'Ask me about your future? --------\n' \
                     f'Your question - "{self.guessing}",\n' \
                     f'Witch\'s answer will be - {test_list[random_test_list]}\n' \
                     f'----------------------------------\n\n'
        PrintMessage(normalize(prediction)).print_message()

class FromAnotherSource:

    # create a method which makes another directories and reads a file from that directory OR use the default one
    def read_file(self):
        original_path = os.path.dirname(os.path.realpath(__file__))
        print(f'Your default directory is "{os.getcwd()}"')
        is_true = True
        while is_true:
            answer = int(input(
                f'If you want to ingest your file from default directory - enter 1, if you want to change it - enter 2: '))
            if answer == 1:
                while True:
                    try:
                        file_name = input('Enter the file name with its format: ')
                        with open(file_name, "r", encoding='utf-8') as source:
                            f_contents = source.readlines()
                        print('Okay, such file exists')
                        path_for_remove = str(file_name)
                        is_true = False
                        break
                    except FileNotFoundError:
                        print('No file with such name. Try again')
                    except PermissionError:
                        print('No file with such name. Try again')
            elif answer == 2:
                while True:
                    try:
                        change_path = input('Enter the file path: ')
                        if not os.path.isdir(change_path):
                            os.mkdir(change_path)
                        os.chdir(change_path)
                        print(f'Now you directory is "{os.getcwd()}"')
                        break
                    except SyntaxError:
                        print('You made a mistake. Try again')
                    except FileNotFoundError:
                        print('You made a mistake. Try again')
                while True:
                    try:
                        file_name = input('Enter the file name with its format: ')
                        with open(file_name, "r", encoding='utf-8') as source:
                            f_contents = source.readlines()
                        print('Such file exists')
                        path_for_remove = os.path.join(str(change_path), str(file_name))
                        os.chdir(original_path)
                        is_true = False
                        break
                    except FileNotFoundError:
                        print('No file with such name. Try again')
                    except PermissionError:
                        print('No file with such name. Try again')
            else:
                print('Try again here')
        num_records = int(input("Enter records num:\n"))
        count = 0
        for i, line in enumerate(f_contents):
            if line == '\n':
                count += 1
                if count == 2 * num_records:
                    f_contents_new = f_contents[:i + 1]
                    break
        return f_contents_new, path_for_remove


# ask a user what data he wants to print and then call a class and insert the data into file using inserting method
if __name__ == "__main__":
    while True:
        print('Please enter your choice:', '1 - News', '2 - Private Ad', '3 - Divination','4 - Add data from another file', '5 - Nothing', sep='\n')
        flag = input('Choose the appropriate number: ')
        if flag == '1':
            news = News(input('Please enter news text\n'),
                        input('Please enter location\n'))
            news_mess = news
            news_mess.news_message()
        elif flag == '2':
            advng = Advertising(input('Please enter advertisement text\n'),
                                input('Please enter expire date in the format dd/mm/yy\n'))
            adv_message = advng
            adv_message.advertising()
        elif flag == '3':
            guessing = Guess(input('Ask me about your near future\n'))
            question_divination = guessing
            question_divination.ask_future()
        elif flag == '4':
            f_contents_new, path_for_remove = FromAnotherSource().read_file()
            with open("Module6_paste.txt", "a", encoding='utf-8') as file:
                file.writelines(f_contents_new)
            print(f'This file {path_for_remove} will be removed now\n')
            os.remove(path_for_remove)
        elif flag == '5':
            print('That is all.')
            break
        else:
            print('Try again')
