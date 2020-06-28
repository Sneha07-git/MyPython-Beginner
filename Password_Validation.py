import re

password = input("enter your password: ")
flag = 0
while True:
    if len(password) < 8:
        flag = -1
        break
    elif not re.search('[a-z]', password):
        flag = -1
        break
    elif not re.search('[A-Z]', password):
        flag = -1
        break
    elif not re.search('[0-9]', password):
        flag = -1
        break

    elif not re.search('[_$@]', password):
        flag = -1
        break

    elif re.search('\s', password):
        flag = 0
        print('valid password')
        break
    else:
        flag = 0
        print('valid password')
        break

if flag == -1:
    print('not a valid password. Length of the password should be Maximum 8 characters Long.'
          'Password should contain upper case, lower case, numbers and special characters.')
