# s = input("Enter the string: \n")
#
# for i in range(0, len(s)-2):
#     print(s[i : i + 3])

# Program to print all the chatracters of a string except the first and last character.

# s = input('Enter the string: \n')
# print(s[1:len(s)-1:])

# Program to print the characters of a string in the reverse order except the first and last character.

# s = input('Enter the string: \n')
# print(s[len(s)-2:0:-1])


# Program to check whether the given string is palindrome or not.

# s = input('Enter the string: \n')
#
# if s == s[::-1]:
#     print(s, ' string is palindrome')
# else:
#     print(s, ' string is not palindrome')


# c  = 'a'
# print(ord(c))
# print(chr(ord(c)-32))

# s = input('Enter the string: \n')
# s_upper = ''
#
# for i in s:
#     if ord(i) >= 97 and ord(i) <= 122:
#         s_upper += chr(ord(i) - 32)
#     else:
#         s_upper += i
#
# print(s)
# print(s_upper)

# s = input('Enter the string: \n')
# s_upper = s.upper()
# print(s_upper)

# s = 'python'
# t = 'PYTHON'
#
# if s.lower() == t.lower():
#     print('String values are equal.')
# else:
#     print('String values are not equal.')


# s = input('Enter the string: \n')
#
# for i in range(0, len(s) - 2):
#     print(s[i: i + 3])

# t = input('Enter the string: \n')
# print(t[len(t)-2 : 0:-1])

# s = input('Enter the string:\n ')
#
# if s == s[::-1]:
#     print(s, 'string is a palindrime.')
# else:
#     print(s, 'string is not a palindrime.')


# c = 'A'
# print(chr(ord(c) + 32))
#
# c = 'b'
# print(chr(ord(c) - 32))
#
# s = 'python'
# t = ''
#
# for i in s:
#     if ord(i) >= 97 and ord(i) <= 122:
#         t += chr(ord(i) - 32)
#     else:
#         t += i
#
# print(t)


# s = 'python'
# t = ''
#
# for i in s:
#     if ord(i) >= 97 and ord(i) <= 122:
#         t += chr(ord(i) - 32)
#     else:
#         t += i
#
# print(s)
# print(t)


# s_upper = s.upper()
#
# print(s)
# print(s_upper)
#
# string = 'INDIA'
# string_lower = string.lower()
#
# print(string)
# print(string_lower)

# lst = ['Python', 'Java', 'Django', 'Spring']
# s = ''
#
# for i in lst:
#     s += i
#
# s = ''.join(lst)
#
# print(s)

url = ['https://www.youtube.com/', 'https://www.google.com/', 'https://chrome.google.com/webstore/category/extensions'
                                                              '?hl=en']

for i in url:
    if i[0:5:] == 'https':
        print(i)








