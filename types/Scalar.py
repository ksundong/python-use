# int
print("""=========================
int 타입
=========================""")
print(int(0b10))

print(int())

print(int('13'))

print(int(13.6))

print(int(True))

print(int("1000", 2))

# float
print("""=========================
float 타입
=========================""")
print(3.125)

print(3e+8)

print(3e8)

print(1.672e+2)

print(16.16e-10)

print(float(7))

print(float("1.618"))

print(float(False))

print(float("nan"))

print(float("inf"))

print(float("-inf"))

print(3.0 + 1)

# None
print("""=========================
None 타입
=========================""")
print(None)

a = None
print(a is None)

print(type(None))

# bool
print("""=========================
bool 타입
=========================""")
print(bool(0))  # 0만 False

print(bool(1))

print(bool(2))

print(bool(-1))

print(bool(0.0))  # 0.0만 False

print(bool(0.201))

print(bool(-1.5))

print(bool(""))  # empty string만 False

print(bool("abcde"))

print(bool([]))  # 빈 Collection은 False

print(bool({}))  # 빈 Collection은 False

print(bool(set()))  # 빈 Collection은 False

print(bool([0]))

print(bool({"a": 0}))

print(bool({1}))
