#!/usr/bin/python3
"""
Module for handling Place-related API endpoints
"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity

@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def search_places():
    """
    Search for places based on provided criteria
    """
    try:
        search_data = request.get_json()
        if search_data is None:
            return jsonify({"error": "Not a JSON"}), 400
    except Exception as e:
        return jsonify({"error": "Not a JSON"}), 400

    states = search_data.get('states', [])
    cities = search_data.get('cities', [])
    amenities = search_data.get('amenities', [])

    if not states and not cities and not amenities:
        places = storage.all(Place).values()
        return jsonify([place.to_dict() for place in places])

    place_set = set()

    if states:
        for state_id in states:
            state = storage.get(State, state_id)
            if state:
                for city in state.cities:
                    for place in city.places:
                        place_set.add(place)

    if cities:
        for city_id in cities:
            city = storage.get(City, city_id)
            if city:
                for place in city.places:
                    place_set.add(place)

    if amenities:
        amenity_objs = [storage.get(Amenity, amenity_id) for amenity_id in amenities]
        place_set = {place for place in place_set if all(amenity in place.amenities for amenity in amenity_objs)}

    return jsonify([place.to_dict() for place in place_set])


