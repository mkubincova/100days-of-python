from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]

        message = (f"Low price alert! Only €{flight.price} to fly "
                   f"from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, "
                   f"from {flight.out_date} to {flight.return_date}")
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        # print(message)
        notification_manager.send_sms(message=message)
        notification_manager.send_emails(message=message, emails=emails)



