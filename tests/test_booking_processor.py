import pandas as pd
from src.booking_processor import process_reservations

def test_process_reservations():
    data = {
        "PNR": ["1234", "5678"],
        "Passenger": ["Alice", ""],
        "Origin": ["JFK", "LAX"],
        "Destination": ["LAX", "ORD"],
        "Fare": [500.0, 600.0],
        "Status": ["Confirmed", "Confirmed"]
    }
    df = pd.DataFrame(data)
    result = process_reservations(df)
    assert len(result) == 1
