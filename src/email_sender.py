def send_confirmation(row):
    try:
        print(f"Email sent to {row['Passenger']} for PNR: {row['PNR']}")
    except Exception as e:
        print("Error sending email:", str(e))
