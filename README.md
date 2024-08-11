# Sorting Algorithm Visualiser

- This project is a visualisation tool for sorting algorithms, created using `pygame`.
- This program allows you to observe how different sorting algorithms work by visualising the step-by-step process of sorting a list of numbers.

## Usage

<p align="center">
  <img src="https://github.com/dominic-portfolio/Algorithm-Visualizer/blob/master/usage.gif?raw=true" alt="program in use" />
</p>


## Features

- **Sorting Algorithms Visualised:**
  - Bubble Sort
  - Insertion Sort
  - Selection Sort
  - Heap Sort
- **Control Sorting:**
  - Start, pause, and resume the sorting process.
  - Switch between ascending and descending order.
  - Control sorting speed by editing the `clock.tick()` value.
- **Performance Information:**
  - Displays the time and space complexity for each sorting algorithm.
- **User Controls:**
  - `Q` : Exit's the program
  - `R` : Reset the list with new random values
  - `SPACE` : Start/Resume/Stop the sorting process
  - `A` : Sort in ascending order
  - `D` : Sort in descending order
  - `I` : Switch to Insertion Sort
  - `B` : Switch to Bubble Sort
  - `S` : Switch to Selection Sort
  - `H` : Switch to Heap Sort

## Installation

To run this project, ensure you have Python installed. Then, install the necessary dependencies:

```bash
pip install pygame
python Algorithm-Visualiser.py