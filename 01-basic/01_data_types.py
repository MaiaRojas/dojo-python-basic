# 1) Boolean values

from hashlib import new


is_hungry = True
has_freckles = False

print(is_hungry)
print(has_freckles)

# 2) Numbers Values

age = 35 # Integer number
weight = 160.57 # float number

print(age)
print(weight)

# 3) String Values
name = "John Doe"
print(name)

# 4) List
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas)
print(ninjas[1])
print(ninjas[-3])
ninjas.append("Charlie")
print(ninjas)
print(ninjas.pop(2))
print(ninjas)


# 5) Diccionarios
new_person = { 'name':  'john', 'age': 28, 'weight': 160.20, 'has_glasses': False }
print(new_person)
print(new_person['name'])
print(new_person['age'])
new_person['skills'] = ['readind', 'swimming', 'karate']
print(new_person)
print(new_person['skills'])
new_person['number_of_friends'] = 20;
print(new_person)
new_person['address'] = {
  'street': 'my_street_s',
  'number': 123456,
  'state': 'xyz'
}


print(new_person)

# 6) Common Functions

# 6.1) type
print(type(is_hungry)) #bool
print(type(name)) #str
print(type(age)) # int
print(type(new_person)) # dic

#6.2) len()
print(len(name)) # 8 ('John Doe')
print(len(ninjas)) # 3
print(len(new_person)) # 7
print(len(ninjas[1])) # 5 ('KB')
print(len(new_person['address'])) # 3
print(len(new_person['skills'])) # 3
print(len(str(new_person['address']['number']))) # 6 (123456)
print(len(new_person['skills'][0])) # 7 ('reading')
print(len('Coding Dojo')) # 11







