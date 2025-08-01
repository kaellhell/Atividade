def notas(*n,sit=False):
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media']>=7:
            r['Situação'] ='BOA'
        elif r['media'] > 5:
            r['Situação'] ='Razoavel'
        else:
            r['Situação'] ='Ruim'
    return r

resp = notas(8, 6,7,8, sit=True)
print(resp)