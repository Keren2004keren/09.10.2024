# START
# a
print(" fun-day ".replace(" ", ""))

# b
print("hello".isalpha())

# c
print("777".isdigit())

# d
print("    ".isspace())

# e
list_to_str: list[str] = ["N","I","N","J","A"]
print("".join(list_to_str))

# f
print("*".join(list_to_str))

# g
text: str = "hELLo"
print("e" in text.lower() or text.upper())

# h
word: str = input("Enter a random word:")
comp_list: list[str] = [letter for letter in word.upper() if letter.isalpha() ]
print(comp_list)

# STOP