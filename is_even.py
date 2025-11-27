def k(x):
    if x%2==0:
        print('Число четное')
    else:
        print('Число нечетное')
def main():
    x=int(input('Добрый день!Введите число:  '))
    k(x)
if __name__ == "__main__":
    main()