# 집합(Set) 자료형 (순서 X, 중복 X)

#선언
a = set()
b = set([1,2,3,4])
c = set([1,4,5,5])
d = set([1,2,'pen', 'seoul', 'air'])

print('a : ', type(a), a)
print('b : ', type(b), b)
print('c : ', type(c), c)
print('d : ', type(d), d)

# 튜플로 변환
t = tuple(b)
print('t : ', type(t), t)
print('t : ', t[0], t[1:3])

# 리스트 변환
l = list(c)
print('l : ', type(l), l)
print('l : ', l[0], l[1:3])

# 집합 자료형 활용
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print('s1 & s2 : ', s1 & s2)
print('s1.intersection(s2) : ', s1.intersection(s2))
print('s1 | s2 : ', s1 | s2)
print('s1.union(s2) : ', s1.union(s2))
print('s1 - s2 : ',s1 - s2)
print('s1.difference(s2) : ',s1.difference(s2))

# 추가 & 제거
s1 = set([1,2,3,4])
s1.add(5)
print('s1 : ', s1)

s1.remove(2)
print('s1 : ', s1)