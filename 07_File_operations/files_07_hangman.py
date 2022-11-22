# Hangman. Make a file containing list of words in categories, e.g. animals, fruits, etc.
# Ask user to choose category before play. Next read list of words from chosen file, chose random one.
# The play should be as much intuitive as possible.
from random import choice


def main():
    print(f'This is a funny game "HANGMAN" \n')
    print(f'User have to guess hidden word chosen from list.\n')
    select_category()
    main_body(*words_generator())


def select_category():
    """This funktion ask user for a category of words to play and return it"""
    print(f'You can choose from a different categories like: ')
    print(f'1 - animals')
    print(f'2 - fruits')
    print(f'3 - vegetables')
    print(f'4 - vehicles')
    print(f'5 - furniture')
    user_options = '1', '2', '3', '4', '5'
    user_choice = '0'
    while user_choice not in user_options:
        user_choice = input(f'What is Your choice -> ')
    with open('words.txt', 'r') as file:
        category = ''
        for i, line in enumerate(file):
            if i == int(user_choice) - 1:
                category += line.strip()
    words = category.split(' ')
    words = words[2:]

    print(words)
    print(type(words))
    print(len(words))


def words_generator():
    """Function returns secret and hidden words"""
    words_list = ['panaceum', 'bokobrody', 'bananowy', 'magnetyczny', 'poprawkowy', 'przywileje', 'Sewastopol',
                  'pokemony', 'naturalizacja', 'mistyfikacja', 'polowanie', 'maskarada', 'książka', 'posiadłość']
    secret_word = choice(words_list)
    hidden_word = '_' * len(secret_word)
    temp_word = secret_word

    return secret_word, hidden_word, temp_word


def main_body(secret_word, hidden_word, temp_word):
    """Function find letter given by user in a secret word and return info."""
    trial_counter = 0
    while trial_counter < 10:
        user_input = input(f'Type a letter You want to check or whole word if You know it -> ')
        if user_input == secret_word:
            print(f'Congratulation!!!\nYou have guess the hidden word!')
            print(f'It really was  " {secret_word} " ')
            break
        elif user_input in secret_word:
            while user_input in temp_word:
                replace_index = temp_word.find(user_input)
                hidden_word = hidden_word[:replace_index] + user_input + hidden_word[replace_index + 1:]
                temp_word = temp_word[:replace_index] + 'X' + temp_word[replace_index + 1:]
            print(f'HIT')
            if hidden_word == secret_word:
                print(f'Congratulation!!!\nYou have guess the hidden word!')
                print(f'The secret word was  " {secret_word} " ')
                break
            print(f'Hidden word is now -> {hidden_word}')

        else:
            trial_counter += 1
            print(f'MISS...\nTry again')
    if trial_counter == 10:
        print(f'You were hanged!!!\n\nSorry....\n\nBetter luck next time.')


if __name__ == "__main__":
    main()
