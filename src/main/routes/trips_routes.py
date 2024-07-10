from flask import jsonify, Blueprint

trips_reoutes_bp = Blueprint('trip_routes', __name__)

@trips_reoutes_bp.route('/trips', methods =['POST'])
def create_trip():
    return jsonify({'ola': 'mundo'}), 200