import random
u = input("Enter site name: ")
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print("Site name: "+u+"\nPassword: "+p +"\n")


createfile = open("PasswordManager.txt","a+")
createfile.write("Site name: "+u+"\nPassword generated: "+p+"\n")
createfile.close()


