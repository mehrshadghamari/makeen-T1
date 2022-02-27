print('please enter 3 number')
a=float(input())
b=float(input())
c=float(input())

if a<b and a<c:
    print(f'min= {a}')
elif b<a and b<c:
      print(f'min= {b}')
else:
       print(f'min= {c}')
