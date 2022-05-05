from datetime import datetime

def get_prices():
    prices = {
        "Lakewood": {
            "rating": 3,
            "regular": {
                "week": 110,
                "weekend": 90
            },
            "reward": {
                "week": 80,
                "weekend": 80
            }
        },
        "Bridgewood": {
            "rating": 4,
            "regular": {
                "week": 160,
                "weekend": 60
            },
            "reward": {
                "week": 110,
                "weekend": 50
            }
        },
        "Ridgewood": {
            "rating": 5,
            "regular": {
                "week": 220,
                "weekend": 150
            },
            "reward": {
                "week": 100,
                "weekend": 40
            }
        }
    }
    return prices

def get_cheapest_hotel(input):   #DO NOT change the function's name
    prices = get_prices()

    # separate date and client type from input
    input = input.split(sep=":")
    client = input[0].upper()
    dates = input[1].split(sep = ",")

    # Just to be sure. Instructions did not match the provided tests.
    if client == "REWARD":
        client = "REWARDS"

    cheapest_hotel = "cheapest_hotel_name"
    return cheapest_hotel

input = "Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"