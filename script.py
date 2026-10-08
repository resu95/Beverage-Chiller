import math
import constants

def time_to_cool(bev_temp_is, cooling_temp, target_temp, tau_beer=1.7):
    if target_temp <= cooling_temp:
        raise ValueError("Your drink is chilled enough")
    if bev_temp_is <= target_temp:
        return 0.0
    return tau_beer * math.log((bev_temp_is - cooling_temp) / (target_temp - cooling_temp))

def cooling():
    bev_temp_is = int(input("Whats the temperature of your Beverage?"))
    cooling_temp = int(input("Whats your cooling temperature?"))
    return time_to_cool(bev_temp_is, cooling_temp, constants.drinking_temperature_beer)
print(cooling())