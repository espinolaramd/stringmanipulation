#Diego Espinola
#02.05.20
#String manipulation

word= input("Hello user, please enter 2-3 words with commas between each word and you will creat a string.\n >")
print("Your words are", word)
first_letter = word[0]
last_letter = word [-1]
uppercase= word.upper()
lowercase= word.lower()
title_case=word.title()
x = word.split(",")
y = word.endswith('d')


print(f"This string coontain {len(word)} letters minus the commas.")
print(f"The first letter of the string is {first_letter}")
print(f"The last letter of the string is {last_letter}")
print(uppercase)
print(lowercase)
print(word.isalpha())
print(x)
print(y)
