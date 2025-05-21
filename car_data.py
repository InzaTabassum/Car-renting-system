class CarData:
    def __init__(self):
        self.car_list = [
            {
                "ID": "1014",
                "Name": "Tesla Model S",
                "Price": "€100/day",
                "Availability": "Available",
                "Booking": None
            },
            {
                "ID": "996",
                "Name": "BMW X5",
                "Price": "€80/day",
                "Availability": "Available",
                "Booking": None
            },
            {
                "ID": "2087",
                "Name": "Toyota Corolla",
                "Price": "€50/day",
                "Availability": "Available",
                "Booking": None
            }
        ]

    def get_cars(self):
        return self.car_list

    def update_cars(self, new_list):
        self.car_list.clear()
        self.car_list.extend(new_list)

    def set_booking(self, car_id, start_date, end_date):
        for car in self.car_list:
            if car["ID"] == car_id:
                car["Booking"] = {
                    "Start": start_date,
                    "End": end_date
                }
