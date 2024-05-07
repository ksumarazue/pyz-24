import threading
import time
#
# def print_numbers(numbers):
#     for i in numbers:
#         print(i)
#         time.sleep(1)  # Opóźnieniedla symulacji czasochłonnej operacji
#
# def perform_main_thread_tasks():
#     print("Wątek główny wykonuje inne zadania.")
#     for _ in range(55):
#         print('.', end="")
#         time.sleep(0.1)  # Opóźnieniedla symulacji trwającej operacji
#     print()
#     print('Koniec głównego zadania')
#
# def main():
#     # Utworzenie wątku
#     numbers = []
#     for i in range(10, 0, -1):
#         numbers.append(i)
#     thread = threading.Thread(target=print_numbers, args=(numbers,))
#     # Uruchomienie wątku
#     thread.start()
#
#     # Wykonanie zadania przez główny wątek
#     perform_main_thread_tasks()
#
#     # Oczekiwanie na zakończenie wątku
#     thread.join()
#     print("Wątek pomocniczy zakończył pracę.")
#
# if __name__ == "__main__":
#     main()


# SuperFastPython.com
# example of using a thread timer object
from time import sleep
from threading import Timer


# target task function
def task(message):
    # report the custom message
    for i in message:
        print(i)

table = [4, 3, 2, 1]
# create a thread timer object
timer = Timer(3, task, args=(table,))
# start the timer object
timer.start()
# block for a moment
sleep(1)
# cancel the thread
print('Canceling the timer...')
timer.cancel()