import pdb
from models.album import Album
from models.artist import Artist
from repositories import album_repository
from repositories import artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist('The Cure')
artist_repository.save(artist_1)

artist_2 = Artist('Mogwai')
artist_repository.save(artist_2)

artist_3 = Artist('The Twilight Sad')
artist_repository.save(artist_3)

album_1 = Album("Head on the Door", "Shoegazing", artist_1)
album_repository.save(album_1)

album_2 = Album("Disintegration", "Shoegazing", artist_1)
album_repository.save(album_2)

album_3 = Album("Mr. Beast", "Instrumental", artist_2)
album_repository.save(album_3)

album_4 = Album("Forget The Night Ahead", "Shoegazing", artist_3)
album_repository.save(album_4)

result = artist_repository.select_all()

for artist in result:
    print(artist.__dict__)

result = album_repository.select_all()

for album in result:
    print(album.__dict__)

results = album_repository.select(album_1)
print(album_1.__dict__)

results = artist_repository.select(artist_1)
print(artist_1.__dict__)

# results = artist_repository.get_albums(artist_1)
# print(artist_1.__dict__)

results = artist_repository.update(artist_3)
print(artist_3.__dict__)




