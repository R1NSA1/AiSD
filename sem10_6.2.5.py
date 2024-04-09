def statistika(otkuda, kuda):
    with open(otkuda, 'r', encoding='utf-8') as f:
        s = f.read().lower()
        for a in '.,?!;:"-()«»—':
            s = s.replace(a, '')

        d = {}
        s = s.split(' ')
        for word in s:
            if word not in d.keys() and word != '\n' and word != '':
                d[word] = s.count(word)

        d = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

    with open(kuda, 'w', encoding='utf-8') as f:
        for k, v in d.items():
            f.write(f'Количество слов {k}: {v}\n')


statistika('revisor.txt', 'results.txt')
