import time
import random

# Import the time module to measure the execution time of the sorting algorithms.
# Import the random module to implement randomized pivot selection in Quicksort.

def deterministic_quicksort(arr):
    # Define the deterministic Quicksort function.
    # It takes 'arr' as input, which is the array that needs to be sorted.
    
    if len(arr) <= 1:
        # Base case: If the array has 0 or 1 element, it's already sorted.
        return arr
    else:
        # Choose the middle element as the pivot for deterministic Quicksort.
        pivot = arr[len(arr) // 2]
        
        # Create a 'left' subarray with elements smaller than the pivot.
        left = [x for x in arr if x < pivot]
        
        # Create a 'middle' subarray with elements equal to the pivot.
        middle = [x for x in arr if x == pivot]
        
        # Create a 'right' subarray with elements greater than the pivot.
        right = [x for x in arr if x > pivot]
        
        # Recursively call Quicksort on the left and right subarrays, and concatenate the results.
        return deterministic_quicksort(left) + middle + deterministic_quicksort(right)

def randomized_quicksort(arr):
    # Define the randomized Quicksort function.
    # It takes 'arr' as input, which is the array that needs to be sorted.
    
    if len(arr) <= 1:
        # Base case: If the array has 0 or 1 element, it's already sorted.
        return arr
    else:
        # Choose a random element from the array as the pivot using the 'random.randint' function.
        pivot = arr[random.randint(0, len(arr) - 1)]
        
        # Create a 'left' subarray with elements smaller than the pivot.
        left = [x for x in arr if x < pivot]
        
        # Create a 'middle' subarray with elements equal to the pivot.
        middle = [x for x in arr if x == pivot]
        
        # Create a 'right' subarray with elements greater than the pivot.
        right = [x for x in arr if x > pivot]
        
        # Recursively call Quicksort on the left and right subarrays, and concatenate the results.
        return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Function to measure the running time of a sorting function (either deterministic or randomized Quicksort).
def measure_time(func, arr):
    start = time.time()  # Record the start time.
    func(arr)  # Call the sorting function.
    return time.time() - start  # Calculate and return the time difference (execution time).

# Create a random array of 1000 elements, with integers ranging from 0 to 10,000.
random_array = [random.randint(0, 10000) for _ in range(1000)]

# Create a sorted version of the random array for testing the worst-case scenario for deterministic Quicksort.
sorted_array = sorted(random_array)

# Create a reverse-sorted version of the random array for further testing.
reverse_sorted_array = sorted(random_array, reverse=True)

# Run the deterministic Quicksort on the random array and measure the time taken.
print("Deterministic Quicksort (Random array):", measure_time(deterministic_quicksort, random_array.copy()))

# Run the randomized Quicksort on the random array and measure the time taken.
print("Randomized Quicksort (Random array):", measure_time(randomized_quicksort, random_array.copy()))

# Run the deterministic Quicksort on the sorted array and measure the time taken.
# This is typically a worst-case scenario for deterministic Quicksort.
print("Deterministic Quicksort (Sorted array):", measure_time(deterministic_quicksort, sorted_array.copy()))

# Run the randomized Quicksort on the sorted array and measure the time taken.
# Randomized Quicksort should perform better than deterministic Quicksort in this case.
print("Randomized Quicksort (Sorted array):", measure_time(randomized_quicksort, sorted_array.copy()))

# Run the deterministic Quicksort on the reverse-sorted array and measure the time taken.
# This is another worst-case scenario for deterministic Quicksort.
print("Deterministic Quicksort (Reverse sorted array):", measure_time(deterministic_quicksort, reverse_sorted_array.copy()))

# Run the randomized Quicksort on the reverse-sorted array and measure the time taken.
# Randomized Quicksort should handle this case more efficiently.
print("Randomized Quicksort (Reverse sorted array):", measure_time(randomized_quicksort, reverse_sorted_array.copy()))
