import json
person = '{ "name":"pratik", "email":"pratik@gmail.com","age":22}'
i = json.loads(person)
print(i["name"] + " " + i["email"] + " ", i["age"])