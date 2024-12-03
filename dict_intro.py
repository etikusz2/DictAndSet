vehicles = {
    'dream' : 'Honda 250T',
    'er5' : 'Kawasaki ER5',
    'can-am' : 'Bombardier Van-Am 250',
    'virago' : 'Yamaha XV250',
    'tenere' : 'Yamaha XT650',
    'jimmy' : 'Suzuki Jimmy 1.5',
    'fiesta' : 'Ford Fiesta Ghia 1.4',
    'roadster' : 'Triumph Street Triple'
}

vehicles["starfighter"] = "LockheedF-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# Update the Virago
vehicles["virago"] = "Yamaha XV535"
# for key in vehicles:
#     print(key, vehicles[key], sep=", ")
for key, value in vehicles.items():
    print(key, value, sep=", ")
