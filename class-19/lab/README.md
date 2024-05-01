# LAB-17: Cryptography

Encryption is the process of converting normal message (plaintext) into meaningless message (Ciphertext). Whereas Decryption is the process of converting meaningless message (Ciphertext) into its original form (Plaintext).

## Steps

- Please follow the below steps as an example.
 
1. Create a local git repo with root folder named `cryptography`.
2. Create a new repo on Github called `cryptography`.
3. Link your local and remote repositories
4. then set it up based on the following structure.

```cryptography
├── .venv
├── module_name
    ├── __init__.py
│   ├── name.py
├── test
    ├── __init__.py
│   ├── test_module_name.py
├── .gitignore
├── README.md
├── requirements.txt

Please make sure don't use the names as its here its just an example.
```

5- create a new branch and called it `encrypt-decrypt`.\
6. Work on a `encrypt-decrypt` branch.\
7. After completing the lab, create a PR from your `encrypt-decrypt` branch to `main` then merge your code.

## Lab Requirements

- create a function called encrypt that get two parameters first one is string to encrypt it and second one will be the key.
- create a function called decrypt that get two parameters first one is string to decrypt it and second one will be the key.
- you can use anyway you like to encrypt string but you must make sure when we use the out put of it as an input to the decrypt function will return the input of encrypt function.
for example: encrypt("abc",1) return "bcd" then the decrypt("bcd",1) will return "abc".
- You can't use any package related with decryption and encryption.

## Testing Requirements

- Create a three test for encrypt function.
- Create a three test for decrypt function.


## Submission Instructions

- Submit your pull request.
- Tell us if you faced any issue.
- Tell us the time you used to solved the lab. 
- Ensure that your functions has a well-formed docstring.
- Ensure you have a `README.md` file that explain your lab.