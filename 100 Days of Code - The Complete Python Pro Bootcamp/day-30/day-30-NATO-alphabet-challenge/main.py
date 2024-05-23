import pandas as pd

# TODO 1. Create a dictionary in this format:
"""
METHOD 1
phonetic_df = pd.read_csv("nato_phonetic_alphabet.csv", index_col=0)
phonetic_df_transposed = phonetic_df.transpose()
phonetic_dict = phonetic_df_transposed.to_dict('list')

dict_final = {letter: phonetic[0] for (letter, phonetic) in phonetic_dict.items()}

phonetic_df_transposed = phonetic_df.transpose()
phonetic_dict = phonetic_df_transposed.to_dict('list')

dict_final = {letter: phonetic[0] for (letter, phonetic) in phonetic_dict.items()}

print(dict_final)

"""

# Expected method in the exercise

df = pd.read_csv("nato_phonetic_alphabet.csv")
dict_final = {row.letter: row.code for (index, row) in df.iterrows()}
print(dict_final)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Input your word! \n")
phonetic_list = [dict_final[letter.upper()] for letter in word]

print(phonetic_list)
