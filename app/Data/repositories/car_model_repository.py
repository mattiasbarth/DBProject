from Data.models.models import CarModel


def find_car_model_by_id(id):
    return CarModel.find(**{f'_id': id})  # TODO sökfunktionen funkar ej
