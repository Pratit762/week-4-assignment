from src.booking_processor import process_reservations
from src.email_sender import send_confirmation
import pandas as pd

def main():
    df = pd.read_csv("data/reservations.csv")
    confirmed = process_reservations(df)

    for passenger in confirmed:
        send_confirmation(passenger)

if __name__ == "__main__":
    main()
