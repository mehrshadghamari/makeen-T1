a=input('write dr or rd    r= radian  d=dgree  ')
if a=='dr':
    b=float(input(' enter degree'))
    p=3.14
    c=b*p/180
    print(f'in radian = {c}')
if a=='rd':
    b=float(input(' enter radian'))
    p=3.14
    c=b*180/p
    print(f'in degree = {c}')