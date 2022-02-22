# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.


duration = int(input('Введите продолжительность времени(сек.): '))

days = duration // 86400
duration -= days * 86400

hours = duration // 3600
duration -= hours * 3600

minutes = duration // 60
duration -= minutes * 60

seconds = duration

if days:
    print(f'{days} дней, {hours} часов, {minutes} минут и {seconds} секунд')
elif hours:
    print(f'{hours} часов, {minutes} минут и {seconds} секунд')
elif minutes:
    print(f'{minutes} минут и {seconds} секунд')
else:
    print(f'{seconds} секунд')
