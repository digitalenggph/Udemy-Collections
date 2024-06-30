import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
dict_final = {row.letter: row.code for (index, row) in df.iterrows()}
print(dict_final)

# my solution
word = input("Input your word! \n")


def search_dict(character):
    try:
        return dict_final[character.upper()]
    except KeyError:
        return "_"


phonetic_list = [search_dict(letter) for letter in word]
print(phonetic_list)


# instructor's solution

def generate_phonetic():
    word_ = input("Enter a word: ").upper()
    try:
        output_list = [dict_final[letter] for letter in word_]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
