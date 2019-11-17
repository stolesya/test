mark=int(input('який бал ви хотіли б перевірити?(від 0 до 100) '))
if mark>=90 and mark<=100:
    print('рівень А, відмінно')
elif mark>=82 and mark<=89:
    print('рівень B, дуже добре')
elif mark>=75 and mark<=81:
    print('рівень С, добре')
elif mark>=67 and mark<=74:
    print('рівень D, задовільно')
elif mark>=60 and mark<=66:
    print('рівень Е, достатній')
elif mark>=35 and mark<=59:
    print('рівень FX, незадовільно, на перездачу шуруй')
elif mark>=1 and mark<=34:
    print('smert')
else:
    print('ти шо ввів')