import collections

INITIAL_WORDS = [
    "арбуз", "банан", "весна", "город", "дверь", "енот", "жизнь", "завод",
    "игрок", "карта", "книга", "лампа", "метро", "налог", "океан", "пирог",
    "радио", "слово", "трава", "улица", "факел", "хомяк", "цапля", "чашка",
    "школа", "экран", "юрист", "ягода", "ручка", "мышка", "поезд", "рукав", "принц"
]

def calculate_letter_frequencies(words):
    frequencies = collections.Counter()
    for word in words:
        for letter in set(word):
            frequencies[letter] += 1
    return frequencies


def score_word(word, frequencies):
    return sum(frequencies[letter] for letter in set(word))


def filter_words(words, guess, exact, wrong_place):
    filtered = []
    for word in words:
        current_exact = sum(1 for w, g in zip(word, guess) if w == g)
        word_counts = collections.Counter(word)
        guess_counts = collections.Counter(guess)
        total_matches = sum((word_counts & guess_counts).values())
        current_wrong_place = total_matches - current_exact

        if current_exact == exact and current_wrong_place == wrong_place:
            filtered.append(word)
    return filtered


def main():
    print("Игра где Компьютер угадывает ваше 5-буквенное слово.")
    possible_words = [w.lower() for w in INITIAL_WORDS if len(w) == 5]

    secret_word = input("Введите загаданное слово (программа его 'забудет'): ").strip().lower()
    while len(secret_word) != 5:
        secret_word = input("Слово должно быть строго из 5 букв! Попробуйте еще раз: ").strip().lower()

    attempts = 0
    while True:
        if not possible_words:
            print("Ошибка! Похоже, вы где-то ошиблись в подсчетах, или слова нет в словаре.")
            break

        frequencies = calculate_letter_frequencies(possible_words)
        guess = max(possible_words, key=lambda w: score_word(w, frequencies))
        attempts += 1
        print(f"\nПопытка №{attempts}: Компьютер говорит слово '{guess.upper()}'")

        if guess == secret_word:
            print(f"Компьютер угадал слово '{secret_word.upper()}' за {attempts} попыток!")
            break

        try:
            exact = int(input("Сколько букв угадано НА СВОИХ местах? "))
            wrong_place = int(input("Сколько букв угадано НЕ НА СВОИХ местах? "))
        except ValueError:
            print("Пожалуйста, вводите только числа.")
            attempts -= 1
            continue

        if exact == 5:
            print(f"Отлично! Слово '{guess.upper()}' угадано!")
            break

        possible_words = [w for w in possible_words if w != guess]
        possible_words = filter_words(possible_words, guess, exact, wrong_place)


if __name__ == "__main__":
    main()
  
def filter_words(words, guess, exact, wrong_place):  
    filtered = []  
    for word in words:  
        current_exact = sum(1 for w, g in zip(word, guess) if w == g)  
        word_counts = collections.Counter(word)  
        guess_counts = collections.Counter(guess)  
        total_matches = sum((word_counts & guess_counts).values())  
        current_wrong_place = total_matches - current_exact  
        if current_exact == exact and current_wrong_place == wrong_place:  
            filtered.append(word)  
    return filtered 

def main():
    print("Игра где Компьютер угадывает ваше 5-буквенное слово.")
    possible_words = [w.lower() for w in INITIAL_WORDS if len(w) == 5]
    secret_word = input("Введите загаданное слово: ").strip().lower()
    while len(secret_word) != 5:
        secret_word = input("Слово должно быть из 5 букв!: ").strip().lower()
    attempts = 0
    while True:
        if not possible_words: break
        frequencies = calculate_letter_frequencies(possible_words)
        guess = max(possible_words, key=lambda w: score_word(w, frequencies))
        attempts += 1
        print(f"Попытка {attempts}: {guess.upper()}")
        if guess == secret_word: break
        try:
            exact = int(input("На своих местах? "))
            wrong_place = int(input("Не на своих местах? "))
        except ValueError:
            attempts -= 1; continue
        possible_words = [w for w in possible_words if w != guess]
        possible_words = filter_words(possible_words, guess, exact, wrong_place)

if __name__ == "__main__":
    main()
