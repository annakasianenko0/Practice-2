inp = " "
i = 1
input_list = []
print("Enter words. Finish with empty value:")
while inp != '':
    inp = input("Word #" + str(i) + ": ")
    if inp == '' and len(input_list) < 1:
        print("Please enter at least one word!")
        inp = " "
    elif inp != '':
        i += 1
        input_list.append(inp)

if(len(input_list) == 1):
    print(input_list[0])
elif(len(input_list) == 2):
    print(input_list[0], 'and', input_list[1])
else:
    for i in range(0, len(input_list) - 1):
        print(input_list[i], end=', ')
    print('and', input_list[len(input_list) - 1])
    

