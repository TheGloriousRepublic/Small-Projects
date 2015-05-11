def extract(t):
    r = {}
    t.split('\n')
    for x in t:
        v=x.split('=')[1]
        if '|' in v:
            v=v.split('|')
        r[x.split('=')[0]]=v
    return r
