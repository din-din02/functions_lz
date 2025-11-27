def b(r):
    S=3.14*r*r
    l = 2*3.14*r
    print('Площадь круга:',S, '\nДлина окружности:', l)
    return S,l
def main():
    r=int(input('Добрый день!Введите радиус круга в сантиметрах:  '))
    b(r)
if __name__ == "__main__":
    main()