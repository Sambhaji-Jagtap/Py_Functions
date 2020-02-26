'''
1. Positional Parameters
2. Named Parameters
3. Default Parameters
4. Arbitrary (*args) Parameters (Variable Length)
5. Keyword (**kwargs) Parameters (Variable Length)
Correct Sequence: (Positional, *args, Named, Default, **kwargs)
'''


def func(a,*b,c, d=30, **e):
    print(a,b,c,d,e)


func(10, 20, 1, 3, 4, c=900, r=60,t=70)

