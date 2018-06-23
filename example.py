from declarativa.declarative_var import declarative_var

number = declarative_var(list, [1])

print(number.get())
print(number.getPrevState())

number.set([2])

print(number.get())
print(number.getPrevState())
