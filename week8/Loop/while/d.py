n = int(input())
x = 1
if n != 1:
 while x < n:
  x = x * 2
if n & x:
 print('YES')
else:
 print('NO')