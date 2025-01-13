import re

def val_car_num(car_id):
    pattern = r'^[АВЕКМНОРСТХУ]{1}\d{3}[АВЕКМНОРСТХУ]{2}\d{2,3}$'
    
    if re.match(pattern, car_id):
        number = car_id[:-2]
        region = car_id[-2:]
        return f"Номер {number} валиден. Регион: {region}."
    else:
        return "Номер не валиден."

print(val_car_num(input()))
