def i(f,c):
    for _ in f:
        with open('chunks/' + _, 'r') as k:
            c.append(k.read())
    return c