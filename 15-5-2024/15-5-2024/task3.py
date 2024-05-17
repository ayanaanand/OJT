def count_whitespace(string):
    count = 0
    for char in string:
        if char.isspace():
            count += 1
    return count

# Example usage:
text = "h ow yo u doin"
whitespace_count = count_whitespace(text)
print("Whitespace count:", whitespace_count)