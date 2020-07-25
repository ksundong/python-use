print('A1', 'B2')

print('A1', 'B2', sep=', ')

print('aa', end=' ')

print('bb')

a = ['A', 'B']
print(' '.join(a))

idx = 1
fruit = "Apple"

# String에 값 넣기
print('{0}: {1}'.format(idx + 1, fruit))

# 인덱스를 생략 가능하다.
print('{}: {}'.format(idx + 1, fruit))

# f-string은 3.6+에서만 지원
print(f'{idx + 1}: {fruit}')
