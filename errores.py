
countries = {
"mexico": 122,
"colombia": 39,
"argentina": 49,
"paraguay": 16
}
try:
    e
except NameError:
    pass
while True:
    country = str(input("Escribe el nombre de un pais: ")) .lower()
    try:
        print ("la poblacion de {} es: {}".format (country, countries[country]))
    except KeyError:
        print (" No tenemos el dato de poblacion de {}".format(country))
