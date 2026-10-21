# function example 

def type_of_album(album, year_released):

    print(album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"


x = type_of_album("The BodyGaurd", 1980)
print(x)