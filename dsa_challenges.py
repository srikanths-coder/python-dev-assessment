def filter_and_sort_evens(numbers):
    # Filter the even numbers and sort them in ascending order
    even_numbers = [num for num in numbers if num % 2 == 0]
    return sorted(even_numbers)

# Example usage:
result = filter_and_sort_evens([3, 1, 4, 1, 5, 9, 2, 6])
print(result)  # Output: [2, 4, 6]

