p=input('what is your shape?  mosalas or moraba or mostatil? ')
if p=='mosalas':
    a=int(input('zele mosalas'))
    area=3*a
    S=((3**0.5)/4)*(a**2)
    print(f'S={S}')
    print(f'2p={area}')
if p=='moraba':
    a=int(input('zele moraba'))
    area=4*a
    S=a**2
    print(f'area = {area}')
    print(f'S = {S}')
if p=='mostatil':
    a=int(input('tol'))
    b=int(input('arz'))
    area=2*(a+b)
    S=a*b
    print(f'S= {S}')
    print(f'area= {area}')

