import os
import re
import sqlite3
from HW_module_6 import News, Advertising, Guess, FromAnotherSource
from HW_module_7 import WordsCount, LettersCount
from HW_module_8 import FileInsert, FromJson
from HW_module_9 import FromXml

class DBInsert:

    def convert_to_tuple(self, list):
        return tuple(i for i in list)

    def inserting(self, lst):
        conn = sqlite3.connect('newsfeed05.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS news (news_text text, location text, date text)')
        cursor.execute('CREATE TABLE IF NOT EXISTS advertisement (advert_text text, actual_date text, days_left text)')
        cursor.execute('CREATE TABLE IF NOT EXISTS guess (guess_question text, conclusion text)')
        conn.commit()

        new_list = list(lst)

        # remove "\n" symbols
        for el in new_list:
            re.sub('\n', '', el)
        try:
            new_list.pop()
        except:
            pass
        if len(new_list) == 0:
            pass
        elif new_list[0] == 'News ----------------------------\n':
            new_list[1] = new_list[1].replace('\n', '')
            split = new_list[2].split(', ')
            new_list[2] = split[0]
            new_list.append(split[1].replace('\n', ''))
            tuple_result = self.convert_to_tuple(new_list[1:4])
            cursor.execute('SELECT * FROM news')
            result = cursor.fetchall()
            if tuple_result in result:
                print(f'We already have such record in "news" table: {tuple_result}')
            else:
                cursor.execute('INSERT INTO news VALUES (?, ?, ?)', tuple_result)
        elif new_list[0] == 'Private Ad -----------------------\n':
            new_list[1] = new_list[1].replace('\n', '')
            split = new_list[2].split(', ')
            new_list[2] = split[0]
            new_list.append(split[1].replace('\n', ''))
            tuple_result = self.convert_to_tuple(new_list[1:4])
            cursor.execute('SELECT * FROM advertisement')
            result = cursor.fetchall()
            if tuple_result in result:
                print(f'We already have such record in "advertisement" table: {tuple_result}')
            else:
                cursor.execute('INSERT INTO advertisement VALUES (?, ?, ?)', tuple_result)
        elif new_list[0] == 'Ask me about your future? ----------------\n':
            new_list[1], new_list[2] = new_list[1].replace('\n', ''), new_list[2].replace('\n', '')
            tuple_result = self.convert_to_tuple(new_list[1:4])
            cursor.execute('SELECT * FROM guess')
            result = cursor.fetchall()
            if tuple_result in result:
                print(f'We already have such record in "guess" table: {tuple_result}')
            else:
                cursor.execute('INSERT INTO guess VALUES (?, ?)', tuple_result)

        conn.commit()
        cursor.close()
        conn.close()

    def selecting_all_tables(self):

        conn = sqlite3.connect('newsfeed05.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM news;")
        result = cursor.fetchall()
        print('"News" table:', result)
        cursor.execute("SELECT * FROM advertisement;")
        result = cursor.fetchall()
        print('"Advertisement" table:', result)
        cursor.execute("SELECT * FROM guess;")
        result = cursor.fetchall()
        print('"Guess" table:', result)

        cursor.close()
        conn.close()


# ask a user what data he wants to print and then call a class and insert the data into file
if __name__ == "__main__":
    while True:
        print('Please enter your choice:', '1 - News', '2 - Private Ad', '3 - Divination',
              '4 - Add data from another file', '5 - Calculate number of words and letters',
              '6 - Add data from json file', '7 - Add data from xml file',
              '8 - Nothing', sep='\n')
        flag = input('Choose the appropriate number: ')
        if flag == '1':        # it works
            news = News(input('Please enter news text\n'),
                        input('Please enter location\n'))
            news.news_message()
            d = news.message_list()
            DBInsert().inserting(d)
        elif flag == '2':        # it works
            advng = Advertising(input('Please enter advertisement text\n'),
                                input('Please enter expire date in the format dd/mm/yy\n'))
            advng.advertising()
            d = advng.message_list()
            DBInsert().inserting(d)
        elif flag == '3':         # it works
            guessing = Guess(input('Ask me about your near future\n'))
            guessing.ask_future()
            d = guessing.message_list()
            DBInsert().inserting(d)
        elif flag == '4':      # it works
            f_contents_new, f_contents_new_fix, path_for_remove = FromAnotherSource().read_file()
            with open("Module6_paste.txt", "a", encoding='utf-8') as file:
                file.writelines(f_contents_new)
            print(f'This file {path_for_remove} will be removed now\n')
            os.remove(path_for_remove)
            for d in f_contents_new_fix:
                DBInsert().inserting(d)
        elif flag == '5':
            word_count = WordsCount("newsfeed05.txt", 'Word_count.csv')
            word_count.write_to_csv()
            letters_count = LettersCount("newsfeed05.txt", 'Letter_count.csv')
            letters_count.write_to_csv()
            print('Word_count.csv and Letter_count.csv files are updated')
            break
        elif flag == '6':        # it works
            data, path_for_remove = FromJson().publishing()
            for d in data:
                DBInsert().inserting(d)
                FromJson().inserting(d)
            print('The data from this file is published in Module6_paste.txt file')
            print(f'This file {path_for_remove} will be removed now\n')
            os.remove(path_for_remove)
        elif flag == '7':        # it works
            data, path_for_remove = FromXml().publishing()
            for d in data:
                DBInsert().inserting(d)
                FromXml().inserting(d)
            print('The data from this file is published in Module6_paste.txt file')
            print(f'This file {path_for_remove} will be removed now\n')
            os.remove(path_for_remove)
        elif flag == '8':
            print('That is all.')
            break
        else:
            print('Try again')

DBInsert().selecting_all_tables()     # for viewing results from database newsfeed05.db
