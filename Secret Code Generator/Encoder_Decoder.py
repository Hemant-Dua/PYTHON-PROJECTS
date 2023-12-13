import string
import random

def encode_func1(n):
    #reversal of string
    ans=n[::-1]
    print(ans)

def encode_func2(n):
    # using random.choices()
    # generating random strings
    random_letters1 = ''.join(random.choices(string.ascii_lowercase+string.digits,k=3))
    random_letters2 = ''.join(random.choices(string.ascii_lowercase+string.digits,k=3))
    # rearranging string [2 random letters + string without first letter + first letter of string + 2 random letters]
    ans=str(random_letters1)+n[1:]+n[0]+str(random_letters2)
    print(ans)

def decode_func1(n):
    #reversal of string
    ans=n[::-1]
    print(ans)

def decode_func2(n):
    # removal of random letters
    rem=n[3:(len(n)-3)]
    # putting last words in front after removal
    ans=rem[len(rem)-1]+rem[0:len(rem)-1]
    # printing answer
    print(ans)

# taking input whether to encode or decode
en_de=input("Do you want to Encode(E) or Decode(D) :")
# taking input from user
msg=input("Enter your message :")

y=msg.lower()
list=[]                             # empty list
list=y.split()                      # each word of message breaks into words

for words in list:                  
    
    # actions for encoding
    if en_de.lower()=="e":

        if len(words)<4:
            encode_func1(words)
        
        else:
            encode_func2(words)

    # actions for decoding
    elif en_de.lower()=="d":

        if len(words)<4:
            decode_func1(words)
    
        else:
            decode_func2(words)
    
    else:
        print("INVALID INPUT!!! Try Again")