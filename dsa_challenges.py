# Function 1: filter_and_sort_evens
def filter_and_sort_evens(numbers):
    # Filter the even numbers and sort them in ascending order
    even_numbers = [num for num in numbers if num % 2 == 0]
    return sorted(even_numbers)

# Function 2: count_character_frequency
def count_character_frequency(text):
    # Convert text to lowercase to ensure case-insensitivity
    text = text.lower()
    
    # Create a dictionary to store frequencies of characters
    frequency_dict = {}
    
    for char in text:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
            
    return frequency_dict


# Test calls for Function 1
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_evens = filter_and_sort_evens(numbers)
print("Sorted Evens:", sorted_evens)
# Expected Output: [2, 4, 6]

# Test calls for Function 2
text = "Hello World"
char_freq = count_character_frequency(text)
print("Character Frequency:", char_freq)
# Expected Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
