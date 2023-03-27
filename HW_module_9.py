import os
import xml.etree.ElementTree as et
from HW_module_6 import News, Advertising, Guess, FromAnotherSource
from HW_module_7 import WordsCount, LettersCount
from HW_module_8 import FileInsert, FromJson

class FromXml(FileInsert):

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
                        xml_file = et.parse(file_name)
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
                        xml_file = et.parse(file_name)
                        print('Okay, such file exists')
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
        return xml_file, path_for_remove

    def publishing(self):
        xml_file, path_for_remove = self.read_file()
        root = xml_file.getroot()
        insert_into_file = []
        for i in root.iter('block'):
            data = []
            if i.get('type') == 'News':
                try:
                    data.append('News ----------------------------' + "\n")
                    data.append(i.find('text').text + "\n")
                    data.append(i.find('location').text + ', ' + i.find('date').text + "\n")
                    data.append('---------------------------------' + "\n\n")
                    insert_into_file.append(data)
                except TypeError:
                    print("Empty text in tag for news was found")
                    insert_into_file = 'Empty'
                    break
            elif i.get('type') == 'Private Ad':
                try:
                    data.append('Private Ad -----------------------' + "\n")
                    data.append(i.find('text').text + "\n")
                    data.append(i.find('date').text + "\n")
                    data.append('----------------------------------' + "\n\n")
                    insert_into_file.append(data)
                except TypeError:
                    print("Empty text in tag for ad was found")
                    insert_into_file = 'Empty'
                    break
            elif i.get('type') == 'Ask me about your future?':
                try:
                    data.append('Ask me about your future? ----------------' + "\n")
                    data.append(i.find('question').text + "\n")
                    data.append(i.find('conclusion').text + "\n")
                    data.append('----------------------------------' + "\n\n")
                    insert_into_file.append(data)
                except TypeError:
                    print("Empty text in tag for divination was found")
                    insert_into_file = 'Empty'
                    break
            else:
                print('Some unknown type of records was found')
                insert_into_file = 'Empty'
                break

        return insert_into_file, path_for_remove

# ask a user what data he wants to print and then call a class and insert the data into file
if __name__ == "__main__":
    while True:
        print('Please enter your choice:', '1 - News', '2 - Private Ad', '3 - Divination',
              '4 - Add data from another file', '5 - Calculate number of words and letters',
              '6 - Add data from json file', '7 - Add data from xml file', '8 - Nothing', sep='\n')
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
            word_count = WordsCount("newsfeed05.txt", 'Word_count.csv')
            word_count.write_to_csv()
            letters_count = LettersCount("newsfeed05.txt", 'Letter_count.csv')
            letters_count.write_to_csv()
            print('Word_count.csv and Letter_count.csv files are updated')
            break
        elif flag == '6':
            data, path_for_remove = FromJson().publishing()
            for d in data:
                FromJson().inserting(d)
            print('The data from this file is published in Module6_paste.txt file')
            print(f'This file {path_for_remove} will be removed now\n')
            os.remove(path_for_remove)
        elif flag == '7':
            data, path_for_remove = FromXml().publishing()
            for d in data:
                FromXml().inserting(d)
            print('The data from this file is published in Module6_paste.txt file')
            print(f'This file {path_for_remove} will be removed now\n')
            os.remove(path_for_remove)
        elif flag == '8':
            print('That is all.')
            break
        else:
            print('Try again')
