def ast_fun():

    a = [x for x in range(10)]
    for i in range(len(a)):
        x = 5
        x = 5//3
        x = x + 5
        x += 5
        x = not x
        a[i] = a[i] << 2 # left shift
        print(a[i])
        a[i] = a[i] | 5 # or
        print(a[i])
        mask = 16
        mask = ~16 # not
        a[i] = a[i] & 16 # and
        print(a[i])
        a[i] = a[i] >> 1 # right shift
        print(a[i])
        a[i] = a[i] ^ 3 # XOR
        print(a[i])
        print("")

ast_fun()
