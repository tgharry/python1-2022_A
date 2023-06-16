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

def encode(string: str) -> str:
    global result
    result = {}
    coded = ''
    for item in string:
        case = {f'{item}' : f'{id_generator()}'}
        result.update(case)
        coded.join()
def id_generator(size=3, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

print(encode('abc'))