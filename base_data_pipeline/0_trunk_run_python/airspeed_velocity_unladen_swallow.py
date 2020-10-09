


birds_dict = {'european_swallow': {'flaps_per_min': 15, 'meters_per_beat': 0.22} ,
        'african_swallow': {'flaps_per_min': 12, 'meters_per_beat': 0.37}
         }

birds_tuple =(('name','flaps_per_min', 'meters_per_beat'),
              ('european_swallow', 15, 0.22),
              ('african_swallow', 12, 0.37)
              )


def calculate_bird_terminal_velocity(flaps_per_min, meters_per_beat):
    #U ≈ 3fA
    U = 3 * flaps_per_min * meters_per_beat
    return u


def calculate_velocity_from_dict(birds_dict):
    print(birds_dict)
    #add code here

def calculate_velocity_from_tuple(birds_tuple):
    print(birds_tuple)
    #add code here


if __name__ == "__main__":
    calculate_velocity_from_dict(birds_dict)

    calculate_velocity_from_tuple(birds_tuple)
