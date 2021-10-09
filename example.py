from Pass_Getter import GetPassWord

username = input("Enter UserName: ")
password = GetPassWord(prompt="Enter password: ", hidden="*")

if username=="git" and password=="hub":
    print("Auth Sucessful")
else:
    print("Incorrect username or password")
