# Car Washing Simulation System – Python (Queue)

## Overview
The Car Washing Simulation System is a Python project that models a real-world car wash service using the Queue (FIFO) data structure. Cars are added to a waiting line and washed in the same order they arrive. This project demonstrates queue operations in a practical and interactive way with menu-driven options and file storage to maintain car data.

## Features
• Add cars to the queue  
• Wash cars in FIFO order  
• View cars currently waiting  
• Persistent storage using cars.txt  
• Realistic progress animation during washing  
• Clear and interactive display menu

## Concept Used
Queue (FIFO – First In First Out)
Enqueue – Add car to queue
Dequeue – Remove car after wash

## Technology Stack
• Python  
• Collections (deque)  
• File Handling  
• Time & OS modules

## How to Run
python car_wash.py

## Folder Structure
CarWashingSimulation/
│── car_wash.py
│── cars.txt
└── README.md

## Sample Output
====== CAR WASHING SYSTEM ======
1. Add Car
2. Wash Next Car
3. View Queue
4. Exit
Enter choice: 1
Enter Car Number: TN10AB1234
✔ Car added to queue

## Future Enhancements
• Billing system + receipt  
• Multiple wash types (Normal, Deluxe, Foam)  
• GUI using Tkinter  
• Average waiting time calculation

## Conclusion
This project helps students understand queue operations in a real-world scenario while practicing Python concepts like functions, loops, and file handling. It demonstrates the importance of FIFO order through an interactive simulation.
