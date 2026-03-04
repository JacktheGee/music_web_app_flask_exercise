from lib.album_repository import AlbumRepository

def test_get_all_artists(web_client):
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Childish Gambino, Bring Me The Horizon, Mac Miller, Blink-182, Zeds Dead"

def test_get_single_artist(web_client):
    response = web_client.get("/artists/1")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Childish Gambino"

def test_get_single_album(web_client):
    response = web_client.get("/albums/2")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Because the Internet"

def test_add_album(web_client):
    response = web_client.post("/albums", data={'album_name': 'Atavista', 
                                    'release_year': 2024,  
                                    'artist_id': 1})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Added album: Atavista"

def test_get_all_albums(web_client):
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Camp, Because the Internet, Sempiternal, Swimming, K.I.D.S, Enema of the State, Return to the Spectrum of Intergalactic Happiness, Atavista"
