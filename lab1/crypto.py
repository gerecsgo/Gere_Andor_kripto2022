#!/usr/bin/env python3 -tt
"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: <YOUR NAME>
SUNet: <SUNet ID>

Replace this with a description of the program.
"""
from base64 import decode
from math import ceil
import utils

# Caesar Cipher

def encrypt_caesar(plaintext):
    text = plaintext.upper()
    n = 3
    encoded = ''
    for i in range(len(text)):
        if(ord(text[i]) >= 65 and ord(text[i]) <= 90):
          encoded += chr((ord(text[i]) + n - 65) % 26 + 65)
        else:
          encoded += text[i] 
    print(encoded)
    return encoded

def decrypt_caesar(ciphertext):
    text = ciphertext.upper()
    n = 3
    decoded = ''
    for i in range(len(text)):
        if(ord(text[i]) >= 65 and ord(text[i]) <= 90):
          decoded += chr((ord(text[i]) - n - 65) % 26 + 65)
        else:
          decoded += text[i]  
    print(decoded)
    return decoded

# Vigenere Cipher

def encrypt_vigenere(plaintext, keyword):
    text = plaintext.upper()
    key = keyword.upper()
    encoded = ''
    cursor = 0
    for i in range(len(text)):
        if(ord(text[i]) >= 65 and ord(text[i]) <= 90):
          encoded += chr((ord(text[i]) + ord(key[cursor%len(key)]) - 65*2) % 26 + 65)
          cursor += 1
        else:
          encoded += text[i] 
    print(encoded)
    return encoded



def decrypt_vigenere(ciphertext, keyword):
    text = ciphertext.upper()
    key = keyword.upper()
    decoded = ''
    cursor = 0
    for i in range(len(text)):
        if(ord(text[i]) >= 65 and ord(text[i]) <= 90):
          decoded += chr((ord(text[i]) - ord(key[cursor%len(key)]) - 65*2) % 26 + 65)
          cursor += 1
        else:
          decoded += text[i] 
    print(decoded)
    return decoded


# Merkle-Hellman Knapsack Cryptosystem

def generate_private_key(n=8):
    """Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem.

    Following the instructions in the handout, construct the private key components
    of the MH Cryptosystem. This consistutes 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        (Note: you can check if a sequence is superincreasing with `utils.is_superincreasing(seq)`)
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q` (you can use utils.coprime)

    You'll need to use the random module for this function, which has been imported already

    Somehow, you'll have to return all of these values out of this function! Can we do that in Python?!

    @param n bitsize of message to send (default 8)
    @type n int

    @return 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    raise NotImplementedError  # Your implementation here

def create_public_key(private_key):
    """Create a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r × w_i mod q

    Hint: this can be written in one line using a list comprehension

    @param private_key The private key
    @type private_key 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    @return n-tuple public key
    """
    raise NotImplementedError  # Your implementation here


def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.

    1. Separate the message into chunks the size of the public key (in our case, fixed at 8)
    2. For each byte, determine the 8 bits (the `a_i`s) using `utils.byte_to_bits`
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk in the message

    Hint: think about using `zip` at some point

    @param message The message to be encrypted
    @type message bytes
    @param public_key The public key of the desired recipient
    @type public_key n-tuple of ints

    @return list of ints representing encrypted bytes
    """
    raise NotImplementedError  # Your implementation here

def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key

    1. Extract w, q, and r from the private key
    2. Compute s, the modular inverse of r mod q, using the
        Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w to recover the original byte
    5. Reconsitite the encrypted bytes to get the original message back

    @param message Encrypted message chunks
    @type message list of ints
    @param private_key The private key of the recipient
    @type private_key 3-tuple of w, q, and r

    @return bytearray or str of decrypted characters
    """
    raise NotImplementedError  # Your implementation here

def main():
    str = encrypt_vigenere('WEAREDISCOVERED', 'LEMON')
    decrypt_vigenere(str, 'LEMON')

if __name__ == "__main__": main()
    