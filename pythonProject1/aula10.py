from datetime import date, time

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%A %B %y'))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)


if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()