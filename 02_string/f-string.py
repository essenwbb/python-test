import time

birth = 1994

age = time.localtime().tm_year - birth

print(f'I born in {birth}, and I\'m {age} years old.')
