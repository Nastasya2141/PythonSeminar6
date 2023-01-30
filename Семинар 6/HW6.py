import random   
def zadacha1():
    # Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
    # N может быть любой длины.
    

    n=int(input("Введите число N:"))
    temp=str(N)
    n1=temp+temp
    n2=temp+temp+temp
    print(f'{n}+{n1}+{n2}=',n+int(n1)+int(n2))

def zadacha2():
    # Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
    # Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
    numbers = list(random.randint(1, 10) for _ in range(15))
    numbers_str = ''.join(str(el) for el in numbers)
    print(numbers_str)
    user_number = (input("Введите трёхзначное натуральное число: "))
    if user_number in numbers_str:
        print('Да')
    else:
        print('Нет')


def zadacha3():
    # Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.
    def check_numbers(x, y):
        min_number = min(x, y)
        divider = 1
        for el in range(2, min_number+1):
            if x % el == 0 and y % el == 0:
                divider = el
                break
        return divider == 1

    for y in range(1, 12):
        for x in range(1, y):
            if check_numbers(x, y):
             print (f' {x}/ {y}')

# zadacha1()
# zadacha2()
# zadacha3()
