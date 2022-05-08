def get_rates():
    rates = {
        "Lakewood": {
            "rating": 3,
            "regular": {
                "week": 110,
                "weekend": 90
            },
            "rewards": {
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
            "rewards": {
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
            "rewards": {
                "week": 100,
                "weekend": 40
            }
        }
    }
    return rates

def get_quotes(days_of_week, rates, client_type):
    # calculate total quotes
    quotes = {}
    for hotel in rates:
        quotes[hotel] = 0
        for day in days_of_week:
            if day in ["sat","sun"]:
                quotes[hotel] += rates[hotel][client_type]["weekend"]
            else:
                quotes[hotel] += rates[hotel][client_type]["week"]
    
    return quotes

def get_cheapest_hotel(input):   #DO NOT change the function's name
    # separate date and client type from input
    input = input.split(sep=":")
    
    client_type = input[0].lower()
    if client_type == "reward":
        client_type = "rewards"
    
    dates = input[1].split(sep = ",")
    days_of_week = [date[11:-1] for date in dates] # get only weekday names

    # calculate quotes
    rates = get_rates()
    quotes = get_quotes(days_of_week, rates, client_type)

    # get hotel names with min quotes
    min_quote = min(quotes.values())
    cheapest_hotel = [hotel for hotel in quotes.keys() if quotes[hotel] == min_quote]

    # get hotel with highest rating in case of draw
    if len(cheapest_hotel) > 1:
        hotel_ratings = [rates[hotel]["rating"] for hotel in cheapest_hotel]
        cheapest_hotel = cheapest_hotel[hotel_ratings.index(max(hotel_ratings))]
    else:
        cheapest_hotel = cheapest_hotel[0]

    return cheapest_hotel