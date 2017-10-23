"""
The following program uses the dictionary provided by Princeton's Database.

The following program is just a fun toy program used during my internship at CloudCraze.

A colleague had hangman on the white board with a new word every week
and so I "cheated" and made this simple program to solve it =)

"""


import string
from collections import Counter


cword = input('Enter the word with question marks as the unknown letters (example: ?ppl? for apple): ')
incletters = input('Enter the letters you guessed incorrectly separated with commas (example: s,t,e): ')

print('The word is: ', cword)
print('The incorrect letters are: ', incletters)

curr_word = list(cword)
inc_letters = list(incletters)
cword_length = len(curr_word)
dict_file_names = list(string.ascii_uppercase)
invalid_word = False
potential_words = list()

princeton_list = ['adj', 'adv', 'noun', 'verb']

# Go through each file (A-Z)
count = 0
for i in range(0, 30):
    if i <= 25:
        dictionary = open(dict_file_names[i]+'.csv', 'r')
    else:
        dictionary = open('conv.data.' + princeton_list[count])
        count += 1
    # Go through every word in every file
    for line in dictionary:
        # If word being evaluated is same length as our word
        word = str.split(line, ' ')
        curr_eval_word = list(word[0])
        if curr_eval_word[0] == '\"':
            curr_eval_word.pop(0)
        if len(curr_eval_word) == cword_length:
            # Check to see if word has matching letters
            for j in range(0, cword_length):

                # If position of word is not unknown and there is a mismatch between what we know about
                # the current word vs the evaluated word, then we know it cannot be our word
                if curr_word[j] != '?' and curr_word[j] != curr_eval_word[j].lower():
                    invalid_word = True
                    break
                # If the evaluated word has a letter that is in our bank of incorrect letters,
                # it cannot be our word
                elif curr_eval_word[j].lower() in inc_letters:
                    invalid_word = True
                    break

            # If we have evaluated all the letters of our current evaluated word and invalid_word is still False
            # then we know it is a valid word, add to list
            if not invalid_word:
                # Make sure we don't append the same word to the list
                if curr_eval_word not in potential_words:
                    potential_words.append(curr_eval_word)
            # Reset invalid_word
            invalid_word = False

count = 1
print('Potential Words: ')
cnt = Counter()
for word in potential_words:
    currword = ''
    for letter in word:
        currword += letter.lower()
        if letter.lower() not in curr_word:
            cnt[letter.lower()] += 1
    print(count, '.', currword)
    count += 1

print('\nTop 3 most common letters seen with what we know: ')

for element in cnt.most_common(3):
    print(element)
