# Immutable Sequence

a: str = 'string'
print(id('string'))
print(id(a))

a = 'aaa'
print(id('aaa'))
print(id(a))

# tuple과 bytes도 Immutable하다.
