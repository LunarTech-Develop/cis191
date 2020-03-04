#Lab 8
#Boolean Operators
def ifValidVoter(age):
    #if age is greater or the same as 18
    if age >= 18 and age <= 135:
        return True
    else:
        return False
def ifLeapYear(year):
    #if this year is a leap year
    if year % 4 == 0:
        return True
    else:
        return False

def main():
    #ask user for name and age and year
    name = input('Whats your name, new feller? ' )
    age = int(input('What is your age feller? '))
    year = int(input('What year is it feller? '))
    #call ifValidVoter
    if ifValidVoter(age):
        print('%s, at %d years old you are a valid voter' % (name, age))
    else:
        print('%s, at %d years old you are not a valid voter' % (name, age))
    #call ifLeapYear
    if ifLeapYear(year):
        print("The year %d is a Leap Year" % (year))
    else:
        print("The year %d is not a Leap Year" % (year))

main()
