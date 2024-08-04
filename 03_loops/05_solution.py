str = "prafulaswale"
nonStr = ""

for i in range(len(str)):
    flag = True
    for j in range(len(str)):
        if i == j:
            continue
        if str[i] == str[j]:
            flag = False
    if flag:
       nonStr += str[i]
print(nonStr[0])

input_str = "teeteracdacd"

for char in input_str:
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break
