
# Quicksort Algorithm: Deterministic vs Randomized

## Overview
This repository contains Python implementations of the **Quicksort algorithm** in two versions:
1. **Deterministic Quicksort** – where the pivot is selected using a fixed strategy (the middle element).
2. **Randomized Quicksort** – where the pivot is selected randomly from the subarray being sorted.

Both algorithms are tested for performance on different types of input arrays: random, sorted, and reverse-sorted. The goal is to compare the efficiency of the deterministic and randomized versions of Quicksort and analyze the effect of randomization on avoiding worst-case scenarios.

## Project Structure
- `quicksort.py`: Contains the implementation of both deterministic and randomized Quicksort algorithms.
- `performance_analysis.py`: Contains the code to measure and compare the execution times of the two algorithms on various types of input arrays.
- `README.md`: This file. Provides an overview of the project, instructions for setup, and usage.

## Requirements
To run this project, you need to have **Python 3.x** installed on your machine.

## How to Run
1. Clone this repository to your local machine using:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd <project-directory>
   ```
3. Run the Quicksort algorithms using:
   ```
   python quicksort.py
   ```

4. To run the performance analysis script:
   ```
   python performance_analysis.py
   ```

This will execute both the deterministic and randomized versions of Quicksort on different input arrays (random, sorted, and reverse-sorted) and output their execution times for comparison.

## Contributing
Feel free to submit issues or pull requests for improvements and bug fixes. Contributions are welcome!

## License
This project is licensed under the MIT License.
