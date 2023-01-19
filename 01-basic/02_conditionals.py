# 1) Conditionals without a method definition
num = 12

if num > 2:
  print(f"{num} is greater than 2")
elif num < 2:
  print(f"{num} is less than 2")
else:
  print(f"{num} is less than 2")

print("-"*50)

# 2) Conditionals With a method defeinition

def comparison(num):
  if num > 2:
    print(f"{num} is greater than 2")
  elif num < 2:
    print(f"{num} is less than 2")
  else:
    print(f"{num} is less than 2")


comparison(12)
comparison(1)
comparison(2)