def get_hotel_info():
    """Get Hotel info

    Returns:
        dict: Hotel rating and price rates for regular and reward clients
    """
    hotel_info = {
        "Lakewood": {
            "rating": 3,
            "regular": {"week": 110, "weekend": 90},
            "rewards": {"week": 80, "weekend": 80},
        },
        "Bridgewood": {
            "rating": 4,
            "regular": {"week": 160, "weekend": 60},
            "rewards": {"week": 110, "weekend": 50},
        },
        "Ridgewood": {
            "rating": 5,
            "regular": {"week": 220, "weekend": 150},
            "rewards": {"week": 100, "weekend": 40},
        },
    }
    
    return hotel_info


def get_quotes(days_of_week, hotel_info, client_type):
    """Function to get quotes for a given number of days depending on the client type

    Args:
        days_of_week (list): Days of the week formatted as mon, tue, wed, thur, sat, sun.
        hotel_info (dict): A dict containing the hotel rates and rating
        client_type (str): A string with the client type: "regular" or "rewards"

    Returns:
        dict: Quotes for all hotels
    """
    # calculate total quotes
    quotes = {}
    for hotel in hotel_info:
        quotes[hotel] = 0
        for day in days_of_week:
            if day in ["sat", "sun"]:
                quotes[hotel] += hotel_info[hotel][client_type]["weekend"]
            else:
                quotes[hotel] += hotel_info[hotel][client_type]["week"]

    return quotes


def get_cheapest_hotel(input):  # DO NOT change the function's name
    """Process hotel info and determine the cheapest highest rating hotel

    Args:
        input (str): String wiht info on the client type and number of days in the following format: "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"

    Returns:
        str: Cheapest hotel name
    """
    # separate date and client type from input
    input = input.split(sep=":")

    client_type = input[0].lower()
    if client_type == "reward":
        client_type = "rewards"

    dates = input[1].split(sep=",")
    days_of_week = [date[11:-1] for date in dates]  # get only weekday names

    # calculate quotes
    hotel_info = get_hotel_info()
    quotes = get_quotes(days_of_week, hotel_info, client_type)

    # get hotel names with the lowest quotes
    min_quote = min(quotes.values())
    cheapest_hotel = [hotel for hotel in quotes.keys() if quotes[hotel] == min_quote]

    # get hotel name with highest rating in case of draw
    if len(cheapest_hotel) > 1:
        hotel_ratings = [hotel_info[hotel]["rating"] for hotel in cheapest_hotel]
        cheapest_hotel = cheapest_hotel[hotel_ratings.index(max(hotel_ratings))]
    else:
        cheapest_hotel = cheapest_hotel[0]

    return cheapest_hotel
