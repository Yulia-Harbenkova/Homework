str = 'Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека.\nА у нас управдом — друг человека!'
str2 = 'Python yes'
str3 = 'Я Денис'
sub_str = str3.split()
sub_str.reverse()
str3 = ' '.join(sub_str)

print('Шаг1 - количество символов', '-', len(str))
print('Шаг2 - развернутая строка', '-', str2[::-1])
print('Шаг3 - каждое слово с большой буквы', '-', str.title())
print('Шаг4 - текст прописными буквами', '-', str.casefold())
print('Шаг5 - число вхождений "нд"', '=', str.count("нд"), 'число вхождений "ам"', '=', str.count("ам"), 'число вхождений "о"', '=', str.count("о"),)
print('Шаг6 - собственное упражнение, вывести с 10 по 97 символы', '=',  str[10:98])
print('Шаг6 - собственное упражнение, заменить "а" на "о"', '=',  str.replace('а', 'о'))
print('Шаг7 - развернутое предложение', '=', str3)
print('Шаг8 - исходняа строка', '=', str)