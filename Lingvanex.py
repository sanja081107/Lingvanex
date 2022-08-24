
with open('words.txt', 'r') as f, \
        open('english.txt', 'w') as eng, \
        open('russian.txt', 'w') as rus:
    b = ' '
    while b is not None:
        b = f.readline()
        if b == '':
            break
        b = b.split('\t')

        # Добавляем слова в english.txt
        eng.write(b[0] + '\n')

        # Добавляем слова в russian.txt
        rus.write(b[1][:-1] + '\n')
        print(b)
