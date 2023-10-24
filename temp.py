text_list = ['1', '+', '(', '2', '+', '3', ")", "+", "4"]
new_list = []

for j in text_list[3:len(text_list)]:
    if j == ")":
        break
    else:
        new_list.append(j)

print(new_list)