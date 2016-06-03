pyg = 'ay'
original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
truncated_word = word[1:]
new_word = truncated_word + first + pyg
print "#", truncated_word
print "#", first
print "#", original
# GOAL: "hello" > "ellohay"

if len(original) > 0 and original.isalpha():
    print new_word
