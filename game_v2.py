"""Игра, где компьтер сам угадывает число"""

import numpy as np
from numpy import random

def random_predict(number:int=1) -> int:
    """Угадываем число

    Args:
        number (int, optional): Загадываем число

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1,101) #предполагаемое число
        if number == predict_number:
            break
        
    return(count)

def score_game(random_predict) ->int:
    """Функция измерения средненго кол-во попыток угадывания за 1000 попыток

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: Среднее кол-во попыток
    """
    
    count_ls = []
    np.random.seed(1) # функция постоянного рандомного числа
    random_array = np.random.randint(1, 101, size=(1000)) #задали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return(score)


if __name__== "__main__":
#run
score_game(random_predict)

#print(f"Количество попыток: {random_predict(10)}")
    
    