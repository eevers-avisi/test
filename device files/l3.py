def s(f):
    f.sort(key=lambda _: int(_.split('_')[1]))
    return f