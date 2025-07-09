# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json

def load_words_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    words = []
    for letter in data:
        words.extend(data[letter])
    return words


def filter_words(words, excluded_letters, included_letters):
    excluded_letters = [letter.lower() for letter in excluded_letters]
    included_letters = [letter.lower() for letter in included_letters]

    filtered_words = []
    for word in words:
        word_lower = word.lower()

        if any(letter in word_lower for letter in excluded_letters):
            continue

        if all(letter in word_lower for letter in included_letters):
            filtered_words.append(word)
    return filtered_words


def main():
    file_path = 'five_letter_words_filtered.json'
    words = load_words_from_json(file_path)

    excluded_input = input("Введите буквы, которых нет в слове (через пробел или запятую): ")
    included_input = input("Введите буквы, которые могут быть в слове (через пробел или запятую): ")

    excluded_letters = [letter.strip().lower() for letter in excluded_input.replace(',', ' ').split() if letter.strip()]
    included_letters = [letter.strip().lower() for letter in included_input.replace(',', ' ').split() if letter.strip()]

    filtered_words = filter_words(words, excluded_letters, included_letters)

    print("\nРезультаты поиска:")
    print(f"Исключены буквы: {', '.join(excluded_letters) if excluded_letters else 'нет'}")
    print(f"Обязательные буквы: {', '.join(included_letters) if included_letters else 'нет'}")
    print(f"\nНайдено слов: {len(filtered_words)}")

    if filtered_words:
        print("\nПодходящие слова:")
        for i in range(0, len(filtered_words), 5):
            print("  ".join(filtered_words[i:i + 5]))
    else:
        print("\nПо вашему запросу ничего не найдено.")


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
