# HiddenPasswords

HiddenPasswords is a Python script that allows you to securely accept passwords from users and hide them with a desired character on the terminal. This can be particularly useful for maintaining password confidentiality during user input.

## Getting Started

Follow these steps to use the HiddenPasswords script in your project:

1. Download or clone this repository and extract it into your project folder.

2. Import the `GetPassWord` function from the `Pass_Getter` module in your Python script.

```python
from Pass_Getter import GetPassWord
```

## Example Usage

Here's an example of how to use the `GetPassWord` function to securely accept a password from a user:

```python
username = input("Enter your username: ")
password = GetPassWord(prompt="Enter password: ", hidden="*")

if username == "Git" and password == "Hub":
    print("Authorization Successful")
else:
    print("Error: Incorrect username or password")
```

In this example, the `GetPassWord` function is used to get a password from the user while displaying asterisks (*) on the screen for each character entered. If the entered username and password match the predefined values ("Git" and "Hub" in this case), the script prints "Authorization Successful"; otherwise, it prints "Error."

## Function Parameters

The `GetPassWord` function takes two optional parameters:

- `prompt` (default: "Enter your password:"): You can specify a custom prompt to be displayed to the user when entering the password.

- `hidden` (default: "*"): You can choose a custom character to display on the screen instead of the password characters for added security.

## Compatibility

This script is designed for use on Windows operating systems due to its use of the `msvcrt` library, which is specific to Windows. It provides a basic method for securely accepting passwords from users on Windows platforms.

## Contributors

- [Your Name]
- [Your Email]

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
