print("Хисамов Искандер Равилевич Лабораторная работа №9\n")
# 1
ALPHABET_DOWN = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET_UP = ALPHABET_DOWN.upper()
CHARACTERS = ' .,;"|/=+-*?!`~_%^&()$#№@:'


def crypt(txt, k):
    result = ''
    for letter in txt:
        if letter in CHARACTERS:
            result += CHARACTERS[CHARACTERS.index(letter)]
        else:
            if letter.islower():
                result += ALPHABET_DOWN[(ALPHABET_DOWN.index(letter) + k) % len(ALPHABET_DOWN)]
            else:
                result += ALPHABET_UP[(ALPHABET_UP.index(letter) + k) % len(ALPHABET_UP)]
    return result


def decrypt(txt, k):
    result = ''
    for letter in txt:
        if letter in CHARACTERS:
            result += CHARACTERS[CHARACTERS.index(letter)]
        else:
            if letter.islower():
                result += ALPHABET_DOWN[(ALPHABET_DOWN.index(letter) - k) % len(ALPHABET_DOWN)]
            else:
                result += ALPHABET_UP[(ALPHABET_UP.index(letter) - k) % len(ALPHABET_UP)]
    return result


text = input("Текст: ")
key = int(input("Ключ: "))
ciphertext = crypt(text, key)
print("Результат: " + ciphertext)

# 2
file = open("key.txt", "w")
file.write(str(key))
file.close()

# 3
file = open("key.txt", "r")
line = file.readline()
count = 0
while True:
    count += 1
    key = int(input("\nВведите ключ для декодирования: "))
    if str(key) == line:
        print("Успешное декодирование!")
        print("Декодированный текст: " + decrypt(ciphertext, key))
        break
    else:
        print("Неправильный ключ!")
file.close()

# 4
print("\nСделано попыток: " + str(count))
