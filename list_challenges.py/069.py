countries = ("senegal", "nigeria", "ghana", "togo", "mali")#
print(countries)
country = input("Enter a country in the tuple: ")

if country in countries:
    print(countries.index(country))