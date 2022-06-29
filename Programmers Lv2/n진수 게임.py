def solution(n, t, m, p):
    num = 0
    seq = 1
    result = ""
    while True:
        if n == 2:
            a = list(format(num, 'b'))
            for i in range(len(a)):
                if len(result) == t:
                    break
                if m == p:
                    if p + m * ((seq//m)-1) == seq:
                        result = result + a[i]
                else:
                    if p + m * (seq//m) == seq:
                        result = result + a[i]
                seq += 1
        elif n == 8:
            b = list(format(num, 'o'))
            for i in range(len(b)):
                if len(result) == t:
                    break
                if m == p:
                    if p + m * ((seq//m)-1) == seq:
                        result = result + b[i]
                else:
                    if p + m * (seq//m) == seq:
                        result = result + b[i]
                seq += 1
        elif n == 16:
            c = list(format(num, 'x'))
            for i in range(len(c)):
                if len(result) == t:
                    break
                if m == p:
                    if p + m * ((seq//m)-1) == seq:
                        result = result + c[i]
                else:
                    if p + m * (seq//m) == seq:
                        result = result + c[i]
                seq += 1
        num += 1
        if len(result) == t:
            break
    return result.upper()