with open('F1.txt', 'w') as f1:
    while True:
        line = input("Введите строку (пустая строка - окончание ввода): ")
        if not line:
            break
        f1.write(line + '\n')

with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    for line in f1:
        words = line.split()
        if len(words) > 2:
            f2.write(line)