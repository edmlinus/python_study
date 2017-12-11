def gen(n):
    print("generator starts")
    i=0
    while i<n :
        yield i
        print("yield 이후 %d" %i)
        i += 1
    print("generator ends")
for i in gen(3):
    print("the value now is %d " %i)

print( "A" + "B")


a = { "A":1 ,"B":2, "C":3 }

b = { "A":0 ,"B":3, "D":3 }

c = list(a.items()) + list(b.items())

print(c)
