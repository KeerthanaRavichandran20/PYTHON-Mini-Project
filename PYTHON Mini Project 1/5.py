from cryptography.fernet import Fernet

'''
def load_key():
    key = fornet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def write_key():
    file = open("key.key", "rb")
    key = File.read()
    file.close()
    return key

master_pwd = input("What is the master password")
key = load_key() + master_pwd.encode()
fer = fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines(): 
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, " | Password:", str(fer.decrypt(passw.encode())) + "\n"))        
        

def add():
    name = input('Account Name: ')
    pwd = input("password: ")

    with open('password.txt','a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")

while True:
    mode = (
        "Would you like to add a new password or view existing ones (view, add)? ")
    
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue