import pytest
import uuid
from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com a base de dados")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_respository = TripsRepository(conn)

    trips_infos ={
        "id": trip_id,
        "destination": "London",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Julieta",
        "owner_email": "julieta@email.com"

    }

    trips_respository.create_trip(trips_infos)

@pytest.mark.skip(reason="interacao com a base de dados")
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_respository = TripsRepository(conn)

    trip = trips_respository.find_trip_by_id(trip_id)
    print(trip)

@pytest.mark.skip(reason="interacao com a base de dados")
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trips_respository = TripsRepository(conn)

    trip = trips_respository.update_trip_status(trip_id)