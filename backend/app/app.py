from flask import Flask, jsonify
app = Flask(__name__)

artists_list = [
    {
        "id": 1,
        "artist_name": "Dave",
        "genre": "Rap"
    },
    {
        'id': 2,
        'artist_name': 'Vivaldi',
        'genre': 'Classical'
    },
    {
        'id': 3,
        'artist_name': 'Cole',
        'genre': 'Rap'
    },
    {
        'id': 4,
        'artist_name': 'Miguel',
        'genre': 'R&B'
    },
]

venues_list = [
    {
        "id": 1,
        "venue_name": "The Golden Tulip",
        "address": "Venue1"
    },
    {
        'id': 2,
        'venue_name': 'Aztec Arcum',
        'address': 'Venue2'
    },
    {
        'id': 3,
        'venue_name': 'Ball Way',
        'address': 'Venue3'
    },
    {
        'id': 4,
        'venue_name': 'Top Town',
        'address': 'Venue4'
    },
]


# Artists

@app.route('/api/artists', methods=['GET'])
def get_artists():
    return jsonify({'artists': artists_list})


@app.route('/api/artists', methods=['POST'])
def create_artist():
    return 'create artist'


@app.route('/api/artists/<int:artist_id>', methods=['GET'])
def show_artist(artist_id):
    return jsonify({'artist': artists_list[artist_id]})


@app.route('/api/artists/<int:artist_id>/edit', methods=['PUT'])
def edit_artist(artist_id):
    return 'artist' + artist_id


@app.route('/api/artists/<int:artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    return 'delete artist' + artist_id


# Venues

@app.route('/api/venues', methods=['GET'])
def get_venues():
    return jsonify({'venues': venues_list})


@app.route('/api/venues', methods=['POST'])
def create_venue():
    return 'create venue'


@app.route('/api/venues/<int:venue_id>', methods=['GET'])
def show_venue(venue_id):
    return jsonify({'venue': venues_list[venue_id]})


@app.route('/api/venues/<int:venue_id>', methods=['PUT'])
def edit_venue(venue_id):
    return 'edit venue' + venue_id


@app.route('/api/venues/<int:venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
    return 'delete venue' + venue_id


# Shows

@app.route('/api/shows', methods=['GET'])
def get_shows():
    return 'shows'


@app.route('/api/shows', methods=['POST'])
def create_show():
    return 'create show'


@app.route('/api/shows/<int:show_id>', methods=['GET'])
def show_show(show_id):
    return 'show' + show_id

# @app.route('/api/shows/<int:show_id>', methods=['EDIT'])
# def edit_show(show_id):
#     return 'edit show' + show_id


@app.route('/api/shows/<int:show_id>', methods=['DELETE'])
def delete_show(show_id):
    return 'delete show' + show_id


# Requests

@app.route('/api/requests', methods=['GET'])
def get_requests():
    return 'requests'


@app.route('/api/requests', methods=['POST'])
def create_request():
    return 'create request'


@app.route('/api/requests/<int:request_id>', methods=['DELETE'])
def delete_request(request_id):
    return 'delete request' + request_id
