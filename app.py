import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    artists = repository.all()

    return ", ".join([artist.artist_name for artist in artists])

@app.route('/artists/<artist_id>', methods=['GET'])
def get_single_artist(artist_id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    artist = repository.find(artist_id)

    return artist.artist_name

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    albums = repository.all()

    return ", ".join([album.album_name for album in albums])

@app.route('/albums/<album_id>', methods=['GET'])
def get_single_album(album_id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    album = repository.find(album_id)

    return album.album_name

@app.route('/albums', methods=['POST'])
def add_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    album_name = request.form['album_name']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    new_album = Album(None, album_name, release_year, artist_id)

    repository.create(new_album)

    return "Album added"

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
