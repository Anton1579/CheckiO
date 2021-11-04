def checkio(words_set):
    a = [i  for i in words_set]
    b = []

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if len(a[i]) < len(a[j]):
                if a[i] == a[j][-len(a[i]):]:
                    b.append(True)
                b.append(False)
            else:
                if a[j] == a[i][-len(a[j]):]:
                    b.append(True)
                b.append(False)

    return any(b)

