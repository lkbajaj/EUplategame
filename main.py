from plate import LicensePlate, Sweden, Ukraine, Romania, Estonia

counter = 1
while True:
    if counter == 1:
        plate = Sweden()
    elif counter == 2:
        plate = Ukraine()
    elif counter == 3:
        plate = Romania()
    elif counter == 4:
        plate = Estonia()
    
    # print(plate)
    # plate.image_plate()
    print(plate.dict_sw())

    counter += 1
    if counter > 4:
        counter = 1

    input('Printing plate. Press enter to continue')
