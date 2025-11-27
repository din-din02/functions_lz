def v(x):
    k = 0
    for i in range(2, x // 2+1):
        if (x % i == 0):
            k = k+1
    if (k <= 0):
            print('Число является простым')
    else:
            print('Число не является простым')
def main():
    x=int(input('Добрый день!Введите число:  '))
    v(x)
if __name__ == "__main__":
    main()

