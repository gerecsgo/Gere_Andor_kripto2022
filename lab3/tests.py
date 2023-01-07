import crypto
import string    
import random  
import numpy as np

# S hosszúságú random stringek generálása minden karakterrel.
def generate_inputs(n):
    strings = []
    for i in range(n):
        S = random.randint(1, 100)
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation, k = S)) 
        strings.append(str(ran))
    return strings

def test_solitaire(n):
    input = generate_inputs(n)
    solitaire_kulcs = np.random.permutation([28, 15, 20, 30, 7, 9, 12, 49, 40, 6, 19, 48, 33, 34, 31, 27, 18, 38, 10, 46, 1, 14, 23, 39, 53, 29, 37, 54, 3, 22, 21, 51, 8, 45, 16, 44, 11, 17, 5, 26, 42, 2, 36, 24, 52, 47, 35, 25, 4, 50, 32, 43, 13, 41])
    errors = 0
    print('Running Solitaire test...')
    for i in input:
        encoded = crypto.encode_solitaire(i, solitaire_kulcs.tolist())
        decoded = crypto.decode_solitaire(encoded, solitaire_kulcs.tolist())
        if(decoded != i):
            errors += 1
    print('Test completed.')
    print('Tested items: '+str(n))
    print('Succeded items:'+str(n-errors))
    print('Errors: '+str(errors))

def test_merkel(n):
    input = generate_inputs(n)
    private_key = crypto.generate_private_key()
    public_key = crypto.create_public_key(private_key)
    errors = 0
    print('Running Merkel test...')
    for i in input:
        encoded = crypto.encrypt_mh(i, public_key)
        decoded = crypto.decrypt_mh(encoded, private_key)
        if(decoded != i):
            errors += 1
    print('Test completed.')
    print('Tested items: '+str(n))
    print('Succeded items:'+str(n-errors))
    print('Errors: '+str(errors))

test_solitaire(1000)
test_merkel(1000)

