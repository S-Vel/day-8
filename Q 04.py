
# program to take string as input and
# change the first occurence with user input


inp = input("enter string here:\n")
rpl = input("enter the character that has to be change with first word:\n")
new_str = inp.replace(inp[0], rpl ,1)
print(new_str)