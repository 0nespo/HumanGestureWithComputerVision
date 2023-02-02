def remove_subsequent_duplicates(input_string):
    result = ""
    last_char = ""
    for char in input_string:
        if char != last_char:
            result += char
            last_char = char
    return result

input_string = "hello world"
output = remove_subsequent_duplicates(input_string)
print("Input string:", input_string)
print("Output string after removing subsequent duplicates:", output)
 