#!/usr/bin/python3
"""
Handles all default RESTful API actions for Place objects
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity


@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def places_search():
    """
    Retrieves all Place objects depending on the JSON in the body
    """
    if not request.is_json:
        abort(400, "Not a JSON")
    search_data = request.get_json()
    if not search_data:
        return jsonify([place.to_dict() for place in storage.all(Place).values()])

    states = search_data.get('states', [])
    cities = search_data.get('cities', [])
    amenities = search_data.get('amenities', [])

    place_set = set()

    # Add places based on states
    if states:
        for state_id in states:
            state = storage.get(State, state_id)
            if state:
                for city in state.cities:
                    for place in city.places:
                        place_set.add(place)

    # Add places based on cities
    if cities:
        for city_id in cities:
            city = storage.get(City, city_id)
            if city:
                for place in city.places:
                    place_set.add(place)

    # If no states or cities are provided, return all places
    if not states and not cities:
        place_set = set(storage.all(Place).values())

    # Filter places by amenities
    if amenities:
        amenities_set = set(amenities)
        filtered_places = []
        for place in place_set:
            place_amenities = set([amenity.id for amenity in place.amenities])
            if amenities_set.issubset(place_amenities):
                filtered_places.append(place)
        place_set = filtered_places

    return jsonify([place.to_dict() for place in place_set])


