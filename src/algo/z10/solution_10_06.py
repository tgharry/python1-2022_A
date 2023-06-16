import random
import string
"""""
Zadania na dziś... napiszemy parę encoder(s: str) -> str i decoder(s: str) -> str, 
które będą kodowały i rozkodowywały napis.
🇦 Encoder ma działać następująco -- dla każego kolejnego znaku napisu s, 
oznaczmy go c zamieniamy go na ciąg c + {losowe znaki różne od c} + c; 
i wszystkie tego typu napisy łączymy
czyli, przykładowo, jeśli s='kad, to
k → kxak
a → abba
d → dfffrassd
"""""
dictionary = {}
word = ""
def id_generator(size=3, chars = string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def encodering():
    a = list(string.printable)
    for _ in a:
        dictionary[_] = id_generator()
def encoder(s: str) -> str:
    encodering()
    word=""
    for item in s:
        word += dictionary[item]
    print(word)
    return word
def decoder(s: str) -> str:
    word = encoder(s)
    dictionary_swap = {value: key for key, value in dictionary.items()}
    result = ""
    chunks=[word[i:i + 3] for i in range(0, len(word), 3)]
    for item in chunks:
        result+=dictionary_swap[item]
    returner = f'{word} == {result}'
    print(returner)
    return result