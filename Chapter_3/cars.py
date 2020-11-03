#These methods to sort list permanently 

#sort method = variable.sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#reverse sort = var.sort(reverse = True)
cars.sort(reverse = True)
print(cars)

#These methods to temporarily change lists

print("Here is the original list:")
print(cars)

#Sorted
print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#reverse method = var.reverse()
print(cars)
cars.reverse()
print(cars)

print(len(cars))