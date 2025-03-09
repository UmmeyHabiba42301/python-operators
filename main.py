#Airthmetic operators(+,-,*,/,%,//,**)

a = 5
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#Assignment operators(=,+=,-=,*=,/=,//=,%=,**=)

x = 3
x += 3
print(x)

x -= 2
print(x)

x *= 2
print(x)

x /= 2
print(x)

x //= 3
print(x)

x %= 1
print(x)

x **= 3
print(x)

#Comparison operators(==,!=,>,<,<=,>=)

a = 10
b = 5

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)

#logical operators(and,or,not)

x = True
y = False

print(x and y)
print(x or y)
print(not x)

#Identity operators(is,is not)
p = [1,2,3]
q = p
r = [1,2,3]

print(p is q)
print(p is r)
print(p is not r)

#Membership operators(in, not in)

my_list = [1,2,3,4,5]
print(2 in my_list)
print(10 in my_list)
print(10 not in my_list)

#Bitwise operstors(&,|,^,~,<<,>>)

s = 5
t = 3

print(s & t)
print(s|t)
print(s^t)
print(~s)
print(s << 1)
print(s >> 1)