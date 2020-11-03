def make_shirt(size, text):
	print("\nYour shirt is size " + size + " and will say '" + text.title() + "' on the front.")

# Positional Argument
make_shirt('S', 'cats rock')

#Keyward Argument
make_shirt(size = 'Small', text = 'cats rock')