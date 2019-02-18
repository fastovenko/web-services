import re

# https://habr.com/ru/post/349860/
# https://regex101.com/
# https://www.hackerrank.com/domains/regex
# https://docs.python.org/3/library/re.html
# Книга: Фридл Дж. Регулярные выражения 3-е издание
# "Если у Вас есть проблема и Вы решили использовать регулярные выражения - у Вас уже две проблемы."

# \d = цифра 0-9 = [0-9]
# \D = все, что угодно, кроме цифр = [^\d] = [^0-9]
# \w = [a-zA-Z_0-9] + unicode (re.ASCII, если без юникода)
# \W = [^\w]
# \s = пробел(табуляция, перенос строки: [\f\n\r\t\v])
# \S = [^\s]
# \b = граница между \w и \W (пустая строка, граница слова - занимает ноль символов)
# \B = позиция внутри слова
# ^ = начало строки
# $ = конец строки

# . = любой символ, кроме \n
# + = >0 = {1, бесконечность}
# * = >=0 = {0, бесконечность}
# ? = 0 or 1 раз = {0,1}
# *? = не жадничать
# () = сгруппировать и запомнить
# (?: ) = сгруппировать и НЕ запомнить
# re.IGNORECASE = игнорировать при поиске
# re.DOTALL = точка обозначает ЛЮБОЙ символ, включая \n
# [abcd1234] = [a-d1-4] = один из символов множества
# {1,2} = 1 или 2 раза
# {,2} = {0,2}
# {2,} = {2,бесконечность}

# abc = abc
# a\db = a0b, a1b,..., a9b, ba1bc; НО: a11b, adb
# a\Db = azb, aab, a_b, a b; НО a1b, a11b, ab,aaab
# a.b = a0b, aab, a b; НО ab, a11b, abc
# a\d?b = ab, a5b; НО a55b, acb, a\d?b
# a.*b = ab, a123XYZb, a-b=b
# a.*?b = ab, a123XYZb, a-b

# reg = re.compile(r'\w+')
# re.findall(r'[А-Я]\w*на', text)
# re.sub(r'а', '?', text)
# re.sub(r'(\w)\1', lambda r: r.group(0).upper(), text) - все двойные буквы меняет на большие
# re.sub(r'\b(\w*(\w)\2\w*)\b', r'[\1]', text) - выделить все слово, где есть двойные буквы
#  \1, \2 - номер группы. Группы присваиваются, начиная с первой открывающейся скобке - 1, 2 и т.д.
# 'Как защитить [металл] от [процесса] [коррозии]?'

# re.search(match, text)

# Найти все действительные числа, например: -100; 21.4; +5.3; -1.5; 0
res = re.findall(r"[-+]?\d+(?:\.\d+)?", test_str)

# Проверить, что строка это серийный номер вида 00XXX-XXXXX-XXXXX-XXXXX, где X - шестнадцатиричная цифра
if re.match(r"^00[\da-f]{3}(?:-[\da-f]{5}){3}$", serial_str, re.IGNORECASE):

# Проверить, что строка является корректным IPv4 адресом
if re.match(r"^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(\.|$)){4}(?<!\.)$", ip_str):

# Проверить, что логин содержит от 8 до 16 латинских букв, цифр и _
if re.match(r"^\w{8,16}$", login):

# Проверить, что пароль состоит не менее чем из 8 символов без пробелов. Пароль должен содержать хотя бы одну: строчную букву, заглавную, цифру
if re.match(r"^(?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9])\S{8,}$", password):

# Переформатировать код, убрав лишние пробелы между def, именем функции и (
# Например: def    myFunc   (x, y):  => def myFunc(x, y):
re.sub(r'def\s+(\w+)\s*\(', r'def \1(', code)

# Заменить все "camel_case" на "сamelCase"
# Например: my_function_name, peer__2__peer  =>  myFunctionName, peer2Peer
re.sub('_+([a-zA-Z\d])', lambda x: x.group(1).upper(), code.lower())
