# Tower of Hanoi

## Overview
The Tower of Hanoi is a classic mathematical puzzle that demonstrates the principles of recursion and problem-solving. This application visually represents the Tower of Hanoi problem and provides a hands-on experience for understanding recursion in programming.

## Story of the Tower of Hanoi
Legend has it that the Tower of Hanoi was created by a group of monks in a temple built by the Buddha. The temple contains three pegs and 64 golden discs of varying sizes, which the monks must move from one peg to another according to specific rules:

1. Only one disc may be moved at a time.
2. Each move consists of taking the upper disc from one of the stacks and placing it on top of another stack.
3. No larger disc may be placed on top of a smaller disc.

### The Punishment and the End of the World
The monks are tasked with moving the discs from the first peg to the last peg. According to legend, once they complete their task, the world will end. The time taken to complete the task increases exponentially with each additional disc; specifically, adding a new disc doubles the number of moves required. For example, with 3 discs, it takes 7 moves, but with 4 discs, it takes 15 moves, and so on, following the formula \(2^n - 1\), where \(n\) is the number of discs.

## Technical Explanation

### Why Adding a New Disc Doubles the Time Taken
The recursive nature of the problem leads to a doubling of the time taken when a new disc is added. To move \(n\) discs from one peg to another, the following steps occur:
1. Move \(n-1\) discs to an auxiliary peg.
2. Move the largest disc to the target peg.
3. Move the \(n-1\) discs from the auxiliary peg to the target peg.

This results in \(2\) moves for every previous configuration, leading to the exponential growth in time complexity.

### Recursion and Tail Recursion
Recursion is a method of solving a problem where the solution involves solving smaller instances of the same problem. In this application, recursion is used to break down the Tower of Hanoi problem into simpler steps.

Tail recursion is a specific kind of recursion where the recursive call is the last operation in the function. This allows for optimizations that can reduce the stack frame used, making it more memory efficient.

## Application Features
- **Visual Representation**: The application uses Tkinter to create an interactive UI, showcasing the movement of discs in real-time.
- **Dynamic Controls**: Users can adjust the number of discs and the delay between moves.
- **Pause and Stop Functionality**: Users can pause or stop the simulation at any time.

### Screenshots
![Running App Screenshot](path/to/screenshot.png)  
*Caption: The Tower of Hanoi application in action, illustrating the movement of discs.*

## Usage of Tkinter
Tkinter is the standard GUI toolkit for Python and is used to create the visual interface of this application. The application features a canvas for drawing the pegs and discs, alongside control buttons for managing the simulation.

## License
