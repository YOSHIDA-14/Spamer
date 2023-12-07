import random
import pyautogui
import time

greetings = ["Hi", "Hello", "Hey", "Heyyy", "hoi", "HOI"]

def send_random_greetings(count):
    for _ in range(count):
        selected_greeting = random.choice(greetings)
        pyautogui.typewrite(selected_greeting)
        pyautogui.press("enter")
        time.sleep(0)

if __name__ == "__main__":
    try:
        greeting_count = int(input("Enter the number "))
        if greeting_count <= 0:
            raise ValueError("Count must be a positive integer.")
        send_random_greetings(greeting_count)

    except ValueError as e:
        print(f"Error: {e}")

