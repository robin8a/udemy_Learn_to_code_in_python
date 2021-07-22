def say_hello(person1, person2="No-One"):
    print("Hello " + person1 + " and " + person2 + " How are you?")

say_hello("Mary", "Cata")
say_hello("Peter")
say_hello("Simon")


def fahr2celsius(fahr):
    return (5 * (fahr-32))/9

print("Celsius: ", round ( fahr2celsius(75), 2) )
print("Kelvin: ", round ( fahr2celsius(75) + 273.5, 2) )
