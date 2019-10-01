#Продолжаем играть на бирже:

#После выполнения задачи ohlc_setup.py, в которой вы скорее всего, явно укажите название входного файла,
#необхоимо сделать ее более гибкой.
#Для этого воспользуемся либой https://docs.python.org/2/library/optparse.html 'optparse'  или
# https://docs.python.org/2/library/argparse.html 'argparse' и научим принимать нашу программу
#путь до файла со сделками из command line. 


#Запуск вашей программы должен выглядеть как : 
# python ohlc_script.py --file=%path_to_%trades.csv или 
# python ohlc_script.py [--file %path_to_%trades.csv ]

#Дополнительно ваша программа должна иметь флажок --help: с коротким описанием доступных CLI-команд
#Добавьте флаг --full_info отображающий короткое описание всех используемых функций
