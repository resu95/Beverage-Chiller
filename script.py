import math
import constants

def time_to_cool(bev_temp_is, cooling_temp, target_temp, tau_beer=1.7): # Actual Function which calculates the time to cool
    if target_temp <= cooling_temp:
        raise ValueError("Your drink is chilled enough")
    if bev_temp_is <= target_temp:
        return 0.0
    return tau_beer * math.log((bev_temp_is - cooling_temp) / (target_temp - cooling_temp))

def get_cooling(): # Gets the cooling Method and returs it.
    print("What Beverage are you cooling?")
    beverage = input("Enter type of bev e.g. Beer ")
    bev_size = input("Enter size of bev e.g. 0.5 ")
    bev_temp_is = constants.environment_temperature
    cooling_met = input("Whats your cooling Method?")
    if cooling_met == "fridge":
        cooling_temp = constants.temperature_fridge
    elif cooling_met == "freezer":
        cooling_temp = constants.temperature_freezer
    elif cooling_met == "icewater":
        cooling_temp = constants.temperature_icewater
    return beverage, cooling_temp, bev_temp_is


def cooling(): 
    beverage, cooling_temp, bev_temp_is = get_cooling()
    return f"It takes {time_to_cool(bev_temp_is, cooling_temp, constants.drinking_temperature_beer)}h to cool your {beverage}!"
print(cooling())