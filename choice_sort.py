# choice_sort.py

from datetime import datetime
import logging

class Sorter():
	# инициализируем логгер
	logger = logging.getLogger('lang_helper')
	logger.setLevel(logging.INFO)
	logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO)

	def log(self, *text):				# метод логирования
		mess = str(datetime.now().strftime('%d-%m-%Y %H:%M'))	# выписывает время вызова
		mess += ': '
		for line in text:
			mess += ' ' + str(line)

		logging.info(mess)	# логирует в файл
		print(mess)			# выписывает в консоль

		return


	def sort(self, in_list):	# сортировка методом выбора
		for i in range(len(in_list)):
			for j in range(i):
				if in_list[j] > in_list[i]:
					buf = in_list.pop(i)
					in_list.insert(j, buf)

		self.log('choice sort:', in_list)  # логирует запись о действии в файл

		return in_list