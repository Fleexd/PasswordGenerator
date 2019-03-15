import random #Module that makes the random password possible
sitename = input("Enter site name: ") #User input for the name of the site
username = input("Chosen username: ") #User input for the desired username
pwd = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ" #All characters that may be used in the generated password
passlen = 8 #Length of the password
p =  "".join(random.sample(pwd,passlen )) #Creating password



createfile = open("log.log","a+") #Creates a bit stealthier textfile to store all the different credentials for each site.
createfile.write("Site name: "+sitename+"\nPassword generated: "+p+"\n") #Writes the credentials and site name in an organized way.
createfile.close() #Closes the file


