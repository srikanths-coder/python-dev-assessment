def count_character_frequency(text):
    # Convert the text to lowercase to make the count case-insensitive
    text = text.lower()
    
    # Create an empty dictionary to store the character frequencies
    frequency_dict = {}
    
    # Loop through each character in the string
    for char in text:
        # If the character is already in the dictionary, increment its count
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            # If the character is not in the dictionary, add it with a count of 1
            frequency_dict[char] = 1
    
    return frequency_dict

# Example usage:
result = count_character_frequency("Hello World")
print(result)

