import csv
import re
from HW_module_6 import News, Advertising, Guess, FromAnotherSource
import os

#in the result create output csv-file that shows word-counter (all words are preprocessed in lowercase)of any input file
class WordsCount:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def write_to_csv(self):
        with open(self.input_file, 'r') as read_txt:
            data_to_read = read_txt.read()
            row = data_to_read.lower()
            list_with_numbers = re.findall(r'\w+', row)
            output_list = [x for x in list_with_numbers if not any(i.isdigit() for i in x)]
            read_txt.close()

        count_dict = {}
        for i in output_list:
            count_dict[i] = output_list.count(i)
            read_txt.close()

        with open(self.output_file, 'w', encoding='UTF8', newline='') as csvfile:
            for key, value in count_dict.items():
                writer = csv.writer(csvfile, delimiter='-')
                writer.writerow([key, output_list.count(key)])
            csvfile.close()


#in the result create csv-file that shows the count of letters, count_all, count_uppercase,
# percentage (add header, spacecharacters are not included)
class LettersCount:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def write_to_csv(self):
        with open(self.input_file, 'r') as read_txt:
            data_to_read = read_txt.read()
            row = data_to_read.lower()
            list_with_numbers = re.findall(r'\w+', row)
            list_with_numbers_init = re.findall(r'\w+', data_to_read)
            output_list = [x for x in list_with_numbers if not any(i.isdigit() for i in x)]
            output_list_init = [x for x in list_with_numbers_init if not any(i.isdigit() for i in x)]
            string_united = ''.join(output_list)
            string_united_init = ''.join(output_list_init)
            string_united = list(string_united)
            string_united_init = list(string_united_init)
            string_united_init = list(''.join([x for x in string_united_init if x.isupper()]))

            count_dict = {}
            for i in string_united:
                count_dict[i] = string_united.count(i)
            count_dict_upper = {}
            for x in string_united_init:
                count_dict_upper[x] = string_united_init.count(x)
            read_txt.close()

        with open(self.output_file, 'w', encoding='UTF8', newline='') as csvfile:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']     # determine headers according to task
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()                                                   # write headers in file
            count_letters = len(string_united)
            for key, value in count_dict.items():
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow([key, string_united.count(key), '', round(string_united.count(key)/count_letters*100, 2)])
            for key, value in count_dict_upper.items():
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow([key, '', string_united_init.count(key), round(string_united_init.count(key)/count_letters*100, 2)])
            csvfile.close()


# ask a user what data he wants to print and then call a class and insert the data into file using inserting method
if __name__ == "__main__":
    while True:
        print('Please enter your choice:', '1 - News', '2 - Private Ad', '3 - Divination',
              '4 - Add data from another file', '5 - Calculate number of words and letters', '6 - Nothing', sep='\n')
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
            f_contents, path_for_remove = FromAnotherSource().read_file()
            with open("newsfeed05.txt", "a", encoding='utf-8') as file:
                file.writelines(f_contents)
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
            print('That is all.')
            break
        else:
            print('Try again')
