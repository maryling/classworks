##  * - любое кол-во раз; + - любое кол-во раз больше 0; . - любой символ
##  ? - предыдущий символ есть или нет (...|...)
##  * и + - жадные квантификаторы
##  [...] - один из перечисленных символов [а-яА-Яё] - любая буква русского алфавита

import re
s = input('Введите слово ')
regex = r'\bвыражени(и|й|ем?|ю|я(х|м|ми)?)\b'
while s:
    m = re.search(regex, s)
    if m != None:
        print('Вы ввели форму слова "выражение"')
    s = input('Введите другое слово ')

