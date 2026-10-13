# Drinking Temperature for Beverages
drinking_temperature_beer = 7

# Constant temperatures for cooling methods
temperature_freezer = -18
temperature_icewater = 0
temperature_fridge = 6
# Standard roomtemperature
environment_temperature = 22
# TAU Hours
TAU_HOURS = {
    # container:        (fridge, freezer, icewater)
    "wine_0.7_glass":   (2.1,  1.2,  0.20),
    "beer_0.3_glass":   (1.65, 0.97, 0.17),
    "beer_0.5_glass":   (1.9,  1.08, 0.19),
    "can_0.33":       (1.7,  1.0,  0.12),
    "can_0.5":        (1.9,  1.1,  0.13),
    "pet_0.5":         (2.2,  1.3,  0.20),
    "pet_1.5":         (3.1,  1.8,  0.27),
}