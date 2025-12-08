from collections import deque
import time
import os

# Queue for storing cars
car_queue = deque()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_car():
    car_number = input("Enter Car Number/Name: ")
    car_queue.append(car_number)
    print(f"✔ {car_number} added to the queue.\n")

def wash_car():
    if not car_queue:
        print(" No cars in the queue! Add cars first.\n")
    else:
        current_car = car_queue.popleft()
        print(f" Washing car: {current_car}")
        for i in range(1, 6):
            print(f" Washing... {i*20}% completed")
            time.sleep(0.5)
        print(f" {current_car} wash completed!\n")

def display_queue():
    if not car_queue:
        print(" Queue is currently empty.\n")
    else:
        print(" Cars in Queue:")
        for car in car_queue:
            print(f"  {car}")
        print()

def menu():
    while True:
        print("====== CAR WASHING SYSTEM (QUEUE) ======")
        print("1. Add Car to Queue")
        print("2. Wash Next Car")
        print("3. View Queue")
        print("4. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_car()
        elif choice == "2":
            wash_car()
        elif choice == "3":
            display_queue()
        elif choice == "4":
            print("Thank you! Exiting car washing system. ")
            break
        else:
            print("Invalid choice! Please try again.\n")

        input("Press Enter to continue...")
        clear_screen()

# Run main program
clear_screen()
menu()
