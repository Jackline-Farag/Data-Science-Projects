

# Function for calculating the flight price for each country
def plane_cost(city_flight):
    if city_flight == "germany":
        return (600)  # returns the flight price
    elif city_flight == "united kingdom":
        return (800)
    elif city_flight == "spain":
        return (300)
    elif city_flight == "italy":
        return (500)


# Function for calculating the hotel cost for each country
def hotel_cost(num_nights):
    return num_nights * hotel_costs[city_flight]


# Function for calculating the rental of a car for each country
def car_rental(rental_days):
    return rental_days * car_costs[city_flight]


# Function for calculating the total cost of the holiday for each country
def holiday_cost(city_flight, hotel_stay, car_days):
    return plane_cost(city_flight) + hotel_cost(hotel_stay) + car_rental(car_days)



# Function for menu, for the user to choose froom
def options():
    print("\nWelcome to our agency! The following are our holiday destinations:\n")
    print("Germany")
    print("United Kingdom")
    print("Spain")
    print("Italy")
    print("Exit")

options()
valid_choices = ["germany", "united kingdom", "spain", "italy"]
hotel_costs = {
    "germany": 65,
    "united kingdom": 85,
    "spain": 45,
    "italy": 35
}
car_costs = {
    "germany": 15,
    "united kingdom": 10,
    "spain": 25,
    "italy": 30
}

while True:
    city_flight = input("Please enter your option: ").lower()  # ask the user to enter their option

    # for every country the functions are called to provide the flight, car rental, hotel and the total cost
    # of each country depending on the user's input.

    if city_flight in valid_choices:
        num_nights = int(input("Please enter the number of nights you will stay in a hotel: "))
        rental_days = int(input("Please enter the number of days you will rent a car: "))
        print("\nThe cost of the flight is: $", plane_cost(city_flight))
        print("The cost of staying for", num_nights, "days in a hotel is $", hotel_cost(num_nights))
        print("The cost of renting a car for", rental_days, "days is $", car_rental(rental_days))
        print("The Total cost of the trip is: $", holiday_cost(city_flight, num_nights, rental_days))
        options()

    # The user is asked if they would like to exit the menu
    elif city_flight == "exit":
        answer = input("Are you sure you want to exit (y/n)?  ").lower()
        if answer == 'n':
            options()
        else:
            print("Thank you for choosing our website")
            break

            # if the user does not enter an option from the menu, the following message is printed
    else:
        print("Option not recognized")