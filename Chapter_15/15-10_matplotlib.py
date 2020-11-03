import matplotlib.pyplot as plt 

from die import Die 

while True:
# Make a random walk, and plot the points.
    die = Die()
    die.roll()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(1, die.num_sides +1))
    plt.scatter(die.x_values, die.y_values, c= point_numbers, cmap= plt.cm.Blues, edgecolor= 'none', s= 1)
    plt.scatter(die.x_values[-1], die.y_values[-1], c= 'red', edgecolors= 'none', s=100)

    # Remove the axes.
    axes = plt.axes() 
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

# Create a D4.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides +1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

print(frequencies)