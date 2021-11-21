class Car:
    def __init__(self, data):
        self.car = data

    def get_car_by_id(self, id):
        """

        :param id int:
        :return: Dict
        """
        car = self.car.get(id)
        return car
