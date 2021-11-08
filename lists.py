list1 = [100, 200, 300, 400, 500]

print(list1)

list1.append(600)

print(list1)

a = ['a', 100, False]

print(a[2])

#      LIST METHODS

a = [1, 2, 3]
b = [4, 5, 6]

c = a + b

print(c)

s = 'a b c d e f'

z = s.split() # or s.split(' ')

print(z)

if 'a' in z:
    print('A is in z')
else:
    print("A is not in z")

if 'g' not in z:
    print('G is not in z')
else:
    print("G is in z")

for i in z:
   print(i)

q = [4,23,6,41,9,6,453,3]
q.sort()
print(q)
q.reverse()
print(q)
print(q.count(6)) # it appears twice
print(len(q))
print(min(q))
print(max(q))