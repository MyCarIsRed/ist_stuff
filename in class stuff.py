cars = ["Ford", "Volvo", 'BMW', "Holden"]
print(cars)
x = cars[1]
print(x)
cars[1] = "Alfa"
print(cars)

cars.append("Volvo")
newcar = input('What do you want to name your new car? ')
if newcar in cars:
    print('That name is already taken!')
    newcar = input('So what original name do you want your car to be called? ')
else:
    print('Nice name')
    cars.append(newcar)
print('Here are all the car names that exist:')
for car in cars:
    print(car)