import copy

a = 'string'

if a is None:
    pass
else:
    print("뭔가 있네?")

a = [1, 2, 3]
print(a == a)
print(a == list(a))
print(a is a)
print(a is list(a))

# copy를 넣어줘야 동작함
print(a == copy.deepcopy(a))
print(a is copy.deepcopy(a))
