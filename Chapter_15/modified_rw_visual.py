import matplotlib.pyplot as plt 

from modified_random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
# Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap= plt.cm.Blues, edgecolor= 'none', s= 1)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c= 'red', edgecolors= 'none', s=100)

    # Remove the axes.
    axes = plt.axes() 
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break