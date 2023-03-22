import os
import re
import datetime
import random
import json
from HW_module_6 import News, Advertising, Guess, FromAnotherSource
from HW_module_7 import WordsCount, LettersCount

class FileInsert:

    # create a method which inserts the text into Module6_paste.txt
    def inserting(self, text):
        with open("Module6_paste.txt", "a", encoding='utf-8') as file:
            for line in text:
                file.write(line)

class FromJson(FileInsert):

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
                        with open(file_name, "r", encoding='utf-8') as read_file:
                            lict_of_dicts = json.load(read_file)
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
                        with open(file_name, "r", encoding='utf-8') as read_file:
                            lict_of_dicts = json.load(read_file)
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
                print('Try again')
        return lict_of_dicts, path_for_remove

    def publishing(self):
        lict_of_dicts, path_for_remove = self.read_file()

        insert_into_file = []
        try:
            for i, d in enumerate(lict_of_dicts):
                data = []
                if d["type"] == 'News':
                    if len(d["text"]) > 0 and len(d["location"]) > 0 and len(d["date"]) > 0:
                        data.append('News ----------------------------'+'\n')
                        data.append(d["text"] + "\n")
                        data.append(d["location"] + ', ' + str(d["date"]) + "\n")
                        data.append('---------------------------------' + "\n\n\n")
                        insert_into_file.append(data)
                elif d["type"] == 'Private Ad':
                    if len(d["text"]) > 0 and len(d["date"]) > 0:
                        data.append('Private Ad -----------------------'+'\n')
                        data.append(d["text"] + "\n")
                        data.append(str(d["date"]) + "\n")
                        data.append('---------------------------------' + "\n\n\n")
                        insert_into_file.append(data)
                elif d["type"] == 'Ask me about your future?':
                    if len(d["question"]) > 0 and len(d["conclusion"]) > 0:
                        data.append('Ask me about your future? ----------------'+'\n')
                        data.append(d["question"] + "\n")
                        data.append(d["conclusion"] + "\n")
                        data.append('---------------------------------' + "\n\n\n")
                        insert_into_file.append(data)
                else:
                    print('Some unknown type of records was found')
                    insert_into_file = 'Empty'
                    break
        except KeyError:
            print('Some important field is absent for block #', i + 1, sep='')
            insert_into_file = 'Empty'

        return insert_into_file, path_for_remove


# ask a user what data he wants to print and then call a class and insert the data into file using inserting method
if __name__ == "__main__":
    while True:
        print('Please enter your choice:', '1 - News', '2 - Private Ad', '3 - Divination',
              '4 - Add data from another file', '5 - Add data from json file', '6 - Nothing', sep='\n')
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
            data, path_for_remove = FromJson().publishing()
            print(data)
            print(path_for_remove)
            for d in data:
                FromJson().inserting(d)
            print('The data from this file is published in Module6_paste.txt file')
            print(f'This file {path_for_remove} will be removed now\n')
            os.remove(path_for_remove)
        elif flag == '6':
            print('That is all.')
            break
        else:
            print('Try again')
