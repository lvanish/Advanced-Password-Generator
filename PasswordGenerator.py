import random

from string import punctuation, ascii_letters, digits

symbols = punctuation + ascii_letters + digits  # collection of characters

secured_random = random.SystemRandom()
password = "".join(secured_random.choice(symbols) for i in range(10))

print(password)