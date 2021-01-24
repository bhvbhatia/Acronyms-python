# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
user_input = input("Enter a Phrase: ")
text = user_input.split()
acronyms = " "
for i in text:
    acronyms = acronyms + i[0].upper()

print("The Acronyms of the phrase is:",acronyms+".")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
