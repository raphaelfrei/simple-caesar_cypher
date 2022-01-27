mode = ''
result = ''
 
mode = input("Choose:\n1 - Crypt\n2 - Uncrypt\n")
 

text = input("Insert a text: \n")
 
for i in range (0, len(text)):
    if(mode == '1'):
        result = result + chr(ord(text[i]) + 2)
    elif(mode == '2'):
        result = result + chr(ord(text[i]) - 2)
    print(result)
    result = ''
