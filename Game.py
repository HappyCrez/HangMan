import Main_loop
import random

words = ["Собака","Автомобиль","Автобус","Телефон","Магнит","Магазин",
             "Работа","Свинья","Трактор","Студент","Стена","Глаз","Казашка"]
    
while True:
    restart_game_message = "Начать игру? д\н : "
    answer = input(restart_game_message)

    if (answer == "н"):
        break
                
    index = random.randint(0, len(words) - 1)
    Main_loop.main_loop(words[index])
