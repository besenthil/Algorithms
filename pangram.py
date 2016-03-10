for _ in range(int(input())):
    sentence = input()
    y = set()
    for x in sentence:
        if x.strip().isalpha():
            y.add(x.lower())
    if len(y) == 26:
        print ('pangram')
    else:
        print('not pangram')