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
    low_border = 0 #нижняя граница предполагаемого числа
    upper_border = 100 #верхняя граница предполагаемого числа
    predict_number = np.random.randint(1,101) #предполагаемое число
    while True:
        count += 1
        if number != predict_number:
            if number > predict_number:
                low_border = predict_number                 
            elif number < predict_number: 
                upper_border = predict_number            
            predict_number = (low_border + upper_border)//2
        else: break          
    return (count)

def score_game(random_predict) ->int:
    """Функция измерения средненго кол-во попыток угадывания за 1000 попыток

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: Среднее кол-во попыток
    """
    
    count_ls = [] #список для хренения количества попыток
    np.random.seed(1) # функция постоянного рандомного числа
    random_array = np.random.randint(1, 101, size=(1000)) #задали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__== "__main__":
#run
    score_game(random_predict)

print(f"Количество попыток: {random_predict(10)}")   
