choice=int(input("enter 1 to encrypt/n2 to decrypt:"))
message=input("enter your message:")
shift=int(input("enter number of places to shift:"))

def encrypt(word):
    expression=''
    for i in range (len(word)):
         if word[i]==' ':
            ch=' '
         else:
             ch=chr((ord(word[i]))+shift)
         expression=expression+ch
    return expression

def decrypt(word):
    expression=''
    for i in range (len(word)):
        if word[i]==' ':
            ch=' '
        else:
            ch=chr((ord(word[i]))-shift)
        expression=expression+ch
    return expression

if choice==1:
    new=encrypt(message)
    print(f"your new message is:{new}")
elif choice==2:
    new=decrypt(message)
    print(f"your new message is:{new}")
else:
    print("wrong choice")


