#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
number = np.random.randint(1,100)    # загадали число от 1 до 100
print ("Загадано число от 1 до 100")


def change(a):  #Задаем функцию, изменяющую размер шага. Размер шага не должен быть меньше одного, чтобы избежать зацикливания.
    if a!=1:
        a=a//2
    return(a)


def game_core_v1(number): #Задаем функцию,которая будет фиксировать число попыток угадать число
    thinknumber=50 # задаем число, с которым будем сравнивать число, которое загадал компьютер. Выбрала 50, потому что это ровно середина
    step=25 # устанавливаем размер шага- число, на которое мы будем менять thinknumber в зависимости от результата сравнения.
    i=0     # устанавливаем счетчик итераций
    while number!=thinknumber :
        i+=1
        if number>thinknumber:
            thinknumber+=step
            step=change(step)
        elif number<thinknumber:
            thinknumber-=step
            step=change(step)
    return(i)


def score_game(game_core):
    #Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,100, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number)) 
    score = np.mean(count_ls)
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v1)

