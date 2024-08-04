str = input("Enter a String:")
revStr = ""
for i in range(len(str)):
    revStr = str[i] + revStr

print(revStr)
