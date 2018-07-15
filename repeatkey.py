from pynput.keyboard import Key, Controller
import time

key = input("enter a letter: ")
n = int(input("enter the amount of times to repeat: "))
interval = int(input("enter the interval: "))

keyboard = Controller()

time.sleep(3) #3 second delay to select active window
for i in range(n):
    keyboard.press(key)
    keyboard.press(Key.enter)
    time.sleep(interval)
