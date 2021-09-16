listin = input().split()
strin = ''.join(listin)


def per(s):

    perlist = []

    if len(s) == 1:
        perlist = [s]
    else:
        for i,let in enumerate(s):
            for perm in per(s[:i]+s[i+1:]):
                perlist += [let+perm]
    return perlist

res = per(strin)
print (res)