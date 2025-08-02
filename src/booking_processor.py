import pandas as pd

def process_reservations(df):
    confirmed = []
    for index, row in df.iterrows():
        if not row['Passenger'] or pd.isna(row['Passenger']):
            continue

        if row['Status'] == "Confirmed":
            confirmed.append(row)
    return confirmed
