#  =========================== Exercise  1=====================================================
def distance_from_zero(val_numbers):
    if type(val_numbers) == int or type(val_numbers) == float:
        return abs(val_numbers)
    else:
        return "Nope"


# ================================ Task - Compulsory  ====================================================
def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city == "Cape Town":
        return 2500
    elif  city == "Durban":
        return 2300
    elif  city == "JNB":
        return 2300
    elif city == "Cape Town":
        return 1800


def rental_car_cost(days):
    total = 40 * days
    if days >= 7:
       total -= 50
    elif days >= 3 and days < 7:
         total -= 30
         return total


def new_sum(*numbers):
    return sum(numbers)


def trip_cost(days,city,spending_money):
     return new_sum(rental_car_cost(days),hotel_cost(days), plane_ride_cost(city), spending_money)
