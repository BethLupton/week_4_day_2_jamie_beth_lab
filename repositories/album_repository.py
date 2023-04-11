from db.run_sql import run_sql

from repositories import artist_repository
from models.album import Album

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    album.id = id
    return album

def select_all():  
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist_id = row['artist_id']
        artist = artist_repository.select(artist_id)
        album = Album( row['title'], row['genre'], row['artist_id'], row['id'] )
        albums.append(album)
    return albums

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist_id = result['artist_id']
        artist = artist_repository.select(artist_id)
        album = Album(result['title'], result['genre'], result['artist_id'])
    return album
    
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(album):
    sql = "UPDATE albums SET (id, title, genre, artist_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [album.id, album.title, album.genre, album.artist.id]
    run_sql(sql, values)