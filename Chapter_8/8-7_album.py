def make_album(artist_name, album_title, track_number = ''):
	album = {'name': artist_name, 'title': album_title}
	if track_number:
		album['track number'] = track_number
	return album

selection = make_album('sarah bareilles', 'waittress', track_number = '4')
print(selection)

selection = make_album('nina simone', 'sinnerman')
print(selection)

selection = make_album('woodkid', 'run boy run')
print(selection)