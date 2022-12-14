# exercise-01 Vowel or Consonant

letter = input("Please enter a letter from the alphabet (a-z or A-Z):")
if letter in "a e i o u":
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is a consonant")


# exercise-02 Length of Phrase

phrase = ''
while phrase != 'quit':
    phrase = input('Please enter a word or phrase: ')
    print(f'What you entered is {len(phrase)} characters long.')

exercise-03 Calculate Dog Years

hy = int(input("Input a dog's age in human years: "))
if hy < 3:
    dy = hy * 10
else:
    dy = 20 + (hy - 2) * 7
print(f"The dog's age in dog year is {dy}")

# exercise-04 What kind of Triangle?

print('Enter the lengths of three sides of a triangle:')
a = input('a: ')
b = input('b: ')
c = input('c: ')

if a == b == c:
    print(f'A triangle with sides of {a}, {b} & {c} is an equalateral triangle')
elif a != b and a != c and b != c:
    print(f'A triangle with sides of {a}, {b} & {c} is a scalene triangle')
else:
    print(f'A triangle with sides of {a}, {b} & {c} is an isosceles triangle')

# exercise-05 Fibonacci sequence for first 50 terms

term = 1
a = 0
b = 1
while term < 51:
    if term < 2:
        print(f'term: {term} / number: {term}')
    else:
        num = a + b
        print(f'term: {term} / number: {num}')
        a = b
        b = num
    term += 1

# exercise-06 What's the  Season?

month = input('enter the month of the season (Jan - Dec)')
day = int(input('Enter the day of the month: '))
if month in ('Jan', 'Feb', 'Mar'):
    season = 'Winter'
elif month in ('Apr', 'Mar', 'May'):
    season = 'Spring'
elif month in ('Jun', 'Jul', 'Aug'):
    season = 'Summer'
else:
    season = 'Fall'
if month == 'Mar' and day < 21:
    season = 'Winter'
elif month == 'Jun' and day < 21:
    season = 'Spring'
elif month == 'Sep' and day < 21:
    season = 'Summer'
elif month == 'Dec' and day < 21:
    season = 'Fall'
print(f'{month} {day} is in {season}')