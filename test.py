ocinka=int(input('який бал вихотіли б перевірити?(від 0 до 100) '))
if ocinka>=90 and ocinka<=100:
    print('рівень А, відмінно')
elif ocinka>=82 and ocinka<=89:
    print('рівень B, дуже добре')
elif ocinka>=75 and ocinka<=81:
    print('рівень С, добре')
elif ocinka>=67 and ocinka<=74:
    print('рівень D, задовільно')
elif ocinka>=60 and ocinka<=66:
    print('рівень Е, достатній')
elif ocinka>=35 and ocinka<=59:
    print('рівень FX, незадовільно, на перездачу шуруй')
elif ocinka>=1 and ocinka<=34:
    print('smert')
else:
    print('ти шо ввів')