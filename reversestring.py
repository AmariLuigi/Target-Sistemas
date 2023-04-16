string = 'Essa frase sera reversa'

nova_string = ""
for i in range(len(string)-1, -1, -1):
    nova_string += string[i]

print(nova_string)