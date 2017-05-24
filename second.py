### DEMONIC SUMMON ALGORITHM ###

an_letters = 'aefhilmnorsxAEFHILMNORSX'
word = input('I will summon a demon for you! Enter a name: ')
times = int(input('How many soul you have? (1-10): '))

for char in word:
    if char in an_letters:
        print('Give me an',char,'!',char)
    else:
        print('Give me a ',char,'!',char)
print('What does that spell?')
for i in range(times):
    print(word,'!!!')
