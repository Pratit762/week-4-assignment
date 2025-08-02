import pandas as pd
from faker import Faker
import random

fake = Faker()
airports = ['JFK', 'LAX', 'ORD', 'DFW', 'ATL']

def generate_reservations(n=200):
    data = []
    for _ in range(n):
        data.append({
            "PNR": fake.uuid4()[:8],
            "Passenger": fake.name(),
            "Origin": random.choice(airports),
            "Destination": random.choice(airports),
            "Fare": round(random.uniform(100, 1000), 2),
            "Status": random.choice(["Confirmed", "Pending", "Cancelled"])
        })
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_reservations()
    df.to_csv("data/reservations.csv", index=False)
