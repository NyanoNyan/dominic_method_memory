
import random
import keyboard
import time
import pandas as pd

# item_list = ['00','01','02','03','04', '05', '06', '07', '08','09', '10',
#             '11','12','13','14','15','16','17','18','19','20', 
#             '21', '22','23','24','25','26','27','28','29','30',
#             '31','32','33','34','35','36','37','38','39','40',
#             '41','42','43']

dataMain = pd.read_csv('data_test_updated.csv')
dataTest = dataMain.iloc[1:,4]
personTest = dataMain.iloc[1:,3]
# print(dataTest.head())
lower = int(input("Please enter the starting number: "))
ending = int(input("Please enter the ending number + 1: "))
item_range = list(range(lower,ending))
isRand = False

def putZeros(value):

    if value < 10:
        return f'0{value}'
    else:
        return str(value)

item_list = list(map(lambda x: putZeros(x), item_range))
# print(item_list)

def modeSelect(mode, count):
    global isRand
    if mode == 'r':
        isRand = True
        return random.choice(item_list)
    
    elif mode == 'n':

            count += 1
            return item_list[count-1]
# Implement score tally
def scoreTally(game_score, count, answer):
    if (answer=="y"):
        return ((game_score + 1) / count)

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")


t = Timer()


def runProgram():

    game_score = 0
    count = 0
    item_count = int(item_list[0]) + 1
    isEnd = False
    # print('Please press enter to begin.')
    choiceVar = input('Please select which version you want to use, r for random and n for normal: ')
    print("## Press enter to start the session ##")
    while isEnd == False:

        
        if keyboard.is_pressed('enter'):

                if count > len(item_list):
                    isEnd = True

                print(f'         {modeSelect(choiceVar, count)}')
                time.sleep(2)
                if (not isRand):
                    print(f'Person: {personTest[count+item_count]}')
                    print(f'Action: {dataTest[count+item_count]}')
                    print('--------------------')
                count += 1


                continue
        if keyboard.is_pressed('q'):
            print('The program will now end')
            isEnd = True
        

runProgram()



# while True:

#     try: 
#         if keyboard.press('enter, space'):
#             print(random.choice(item_list))
#             keyboard.wait(hotkey='enter')

#     except:
#         if keyboard.is_pressed('q'):
#             break

