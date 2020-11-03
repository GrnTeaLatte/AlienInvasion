def make_album(artist_name, album_title, track_number = ''):
	album = {'name': artist_name, 'title': album_title}
	if track_number:
		album['track number'] = track_number
	return album

while True:
	print("\nPlease enter your favorite album: ")
	print("(enter 'q' at any time to quit)")

	a_name = input("Artist name: ")
	if a_name == 'q':
		break
	a_title = input("Album title: ")
	if a_title == 'q':
		break
		
	selection = make_album(a_name, a_title)
	print("\nYour favorite album is: " + a_title.title() + " by " + a_name.title())


