from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese car maker"},
        {"name": "Mercedes", "description": "German car maker"},
        {"name": "Audi", "description": "German car maker"},
        {"name": "Kia", "description": "Korean car maker"},
        {"name": "Toyota", "description": "Japanese car maker"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(name=data['name'], description=data['description'])
        )

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer_id": 2},
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer_id": 3},
        {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer_id": 4},
        {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer_id": 5},
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer_id": 6},
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer_id": 7},
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer_id": 8},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3], "dealer_id": 9},
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances[3], "dealer_id": 10},
        {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": car_make_instances[3], "dealer_id": 11},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "dealer_id": 12},
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "dealer_id": 13},
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances[4], "dealer_id": 14},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            dealer_id=data['dealer_id'],
        )
