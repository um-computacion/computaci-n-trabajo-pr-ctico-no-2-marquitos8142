def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

user_input = input("Ingresa un texto para verificar si es un palindromo: ")
if is_palindrome(user_input):
    print("El texto es un palindromo.")
else:
    print("El texto no es un palindromo.")