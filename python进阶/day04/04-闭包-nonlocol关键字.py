def fn_outer():
    a = 100
    def fn_inner():     #内部函数，有嵌套
        nonlocal a
        a += 1
        print(f'a的值{a}')

    return fn_inner


if __name__ == '__main__':
    fn = fn_outer()     #等价于fn_inner这个函数

    fn()                #101
    fn()                #102















