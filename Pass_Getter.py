import sys
import msvcrt

def GetPassWord(prompt = "Enter your password: ", hidden="*"):
    password = []
    print(prompt, end="")
    while 1:
        c = msvcrt.getwch()
        ascii = ord(c)
        if ascii==13:#enter
            print("")
            pwd = ""
            for leters in password:
                pwd += leters
            return pwd
        elif ascii==27:#esc
            return None
        elif ascii==8 and len(password)!=0:#backspace
            sys.stdout.write("\b")
            sys.stdout.write(" ")
            sys.stdout.write("\b")
            sys.stdout.flush()
            password = password[0:(len(password)-1)]
        elif ascii==224:
            arrow = msvcrt.getwch()
        else:
            password.append(c)
            sys.stdout.write(hidden)
            sys.stdout.flush()


username = input("Enter your username: ")
pasword = getpassword(prompt="Enter password: ", hidden="*")

if username=="Git" and pasword=="Hub":
    print("Authorisation Sucessful")
else:
    print("Error")