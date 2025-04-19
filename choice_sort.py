# choice_sort.py

from datetime import datetime
import logging

class Sorter():
    # create logger with 'spam_application'
    logger = logging.getLogger('lang_helper')
    logger.setLevel(logging.INFO)
    # create file handler which logs even debug messages
    logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO)

    def log(self, *text):
        mess = str(datetime.now().strftime('%d-%m-%Y %H:%M'))
        mess += ': '
        for line in text:
            mess += ' ' + str(line)

        logging.info(mess)
        print(mess)

        return

    def sort(self, in_list):
        for i in range(len(in_list)):
            for j in range(i):
                if in_list[j] > in_list[i]:
                    buf = in_list.pop(i)
                    in_list.insert(j, buf)

        self.log('choice sort:', in_list)  # логируем запись о действии в файл

        return in_list