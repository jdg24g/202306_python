#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) 
# la operacion da 5

#2
def number_of_military_branches():
    return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# la operacion da NameError: name 'number_of_days_in_a_week_silicon_or_triangle_sides' is not defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# la operacion da 5

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# la operacion da 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# la operacion da 5 , None

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# la operacion da TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# la operacion da "25"

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# la operacion da 100, 10
#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# la operacion da 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# la operacion da 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# la operacion da 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# la operacion da 8

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# la operacion da 500,500, 300, 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# la operacion da 500, 500, 300, 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# la operacion da 500, 500, 300, 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# la operacion da 1, 3, 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# la operacion da 1, 3, 5 , 10