def count_dog_occurrences(input_string):
    words = input_string.split()
    
    count = 0
    
    for word in words:
        if word.lower() == "dog":
            count += 1
    
    return count

# Example usage:
test_string = "I have a dog, and my neighbor has a dog too. Dogs are great!"
result = count_dog_occurrences(test_string)
print(f"The word 'dog' appears {result} times in the string.")
