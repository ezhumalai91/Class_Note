def check_digits(input_string):
    if input_string.isdigit():
        return True
    else:
        return False


print(check_digits("12345"))  # Returns: True
print(check_digits("123a5"))  # Returns: False
