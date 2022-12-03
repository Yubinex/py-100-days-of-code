travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]


def add_new_country(country_name, times_visited, city_list):
    travel_log.append(
        {"country": country_name, "visited": times_visited, "cities": city_list})


add_new_country("Russia", 2, ["Moscow", "Saint Petersberg"])
print(travel_log)
