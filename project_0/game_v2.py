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
    while number != predict_number:
        count += 1
        if number > predict_number:
            low_border = predict_number 
            predict_number = round(low_border + upper_border)//2                
        elif number < predict_number: 
            upper_border = predict_number            
            predict_number = round(low_border + upper_border)//2
        else: break          
    return count

def score_game(random_predict) ->int:
    """Функция измерения среднего кол-во попыток угадывания за 1000 попыток

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: cреднее кол-во попыток
    """
    
    count_ls = [] #список для хренения количества попыток
    np.random.seed(1) # функция постоянного рандомного числа
    random_array = np.random.randint(1, 101, size=(100)) #задали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__== "__main__":
#run
    score_game(random_predict)