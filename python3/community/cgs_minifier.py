n = int(input())
content = ""
for i in range(n):
    content += input()

variable_id = 'a'
variables = {}
result = ""
variable = ""
value = ""
for l in content:

    if variable == "" and l == "$":
        variable += l
    elif variable != "":
        variable += l
        if l == "$":
            result += variable
            if variable not in variables.keys():
                variables[variable] = "$"+variable_id+"$"
                variable_id = chr(ord(variable_id) + 1)
            variable = ""
    elif value == "" and l == "'":
        value += l
    elif value != "":
        value += l
        if l == "'":
            result += value
            value = ""
    elif l != " ":
        result += l
        
for k, v in variables.items():
    result = result.replace(k, v)

print(result)
