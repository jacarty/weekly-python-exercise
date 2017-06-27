def holidays():

    travel = {}

    while True:
        location = raw_input("Please enter the city, country that you visited: ").strip()

        if not location:
            break

        try:
            city, country = location.split(",")

            if len(country.strip()) <= 2:
                country = country.strip().upper()
            else:
                country = country.strip().title()

            if country not in travel:
                travel[country] = []

            if city not in travel[country]:
                travel[country].append(city.strip().title())

        except ValueError:
            print "Please check input format and try again - it should be city, country"

    for country, cities in sorted(travel.items()):
        print country+":"
        for each_city in sorted(cities):
            print "\t", each_city

if __name__ == '__main__':
    holidays()
