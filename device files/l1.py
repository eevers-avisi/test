import os
import l2,l3
def l():
    c = []
    f = l3.s(os.listdir('chunks'))
    c = l2.i(f, c)
    return ''.join(c)
