def hotel_cost(nights):
    hotel_cost = 140
    return hotel_cost * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    if city == "Tampa":
        return 220
    if city == "Pittsburgh":
        return 222
    if city == "Los Angeles":
        return 475

def rental_car_cost(days):
    car_hire = 40 * days
    if days >= 7:
        car_hire -= 50
    elif days >= 3:
        car_hire -= 20
    return car_hire

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
