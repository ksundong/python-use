import collections

# Dictiionary는 Key Value로 이루어진 구조
a = {'a': 123, 'B': 333, 'b': 'abcd'}

print(len(a))
print(a['a'])
a['c'] = 'Ccc'
print('B' in a)
print('D' in a)
print(a)

# 3.6- 에서는 Dictionary가 순서보장을 하지 않으므로 아래의 것을 사용했다. 순서보장이 필요하면 아래의 것을 사용할 것
b = collections.OrderedDict()

# 기본값을 지정해 키 오류를 방지
c = collections.defaultdict(int)
print(c)
print(c['a'])
print(c)

c = collections.defaultdict(set)
print(c)
print(c['a'])
print(c)


# 요소의 값을 키로 하고 개수를 값 형태로 만들어 카운팅을 한다. 기본적으로 많은 개수가 앞으로 나오는 듯 하다.
d = collections.Counter('11234335545234')

print(d)
print(d.most_common())  # 가장 많은 수 순으로 정렬된 list 제공
print(d.most_common(1))  # 가장 개수가 많은 k개 제공
print(type(d.most_common(1)))  # list형태로 제공함을 알 수 있다.

# 빈 Dictionary 선언
a = dict()
print(type(a))
a = {}
print(type(a))

# 존재하지 않는 키를 조회할 경우 Key Error 가 발생한다.
try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키')

try:
    del a['key4']
except KeyError:
    print('존재하지 않는 키')

if 'key4' in a:
    print('존재하는 키')
else:
    print('존재하지 않는 키')

a = {'key1': 'a', 'key2': 1, 'key3': 'value3'}

# 반복문으로 조회하기
for k in a:
    print(k)  # key가 조회된다.

for k, v in a.items():
    print(k, v)  # key value가 조회된다.
