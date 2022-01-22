from abc import ABC, abstractmethod


class Director:
    """ Controls the construction process.

    Director class has a Builder class associated with him.Director then
    delegates building of the smaller parts to the builder and
    assembles them together And create a Car object.
    """
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()

        body = self.__builder.get_body()
        car.set_body(body)

        wheel = self.__builder.get_wheel()
        car.set_wheel(wheel)

        engine = self.__builder.get_engine()
        car.set_engine(engine)

        return car


class Car:
    """
    Base Car class to create a car object
    """

    def __init__(self):
        self.__wheel = None
        self.__body = None
        self.__engine = None

    def set_wheel(self, wheel):
        self.__wheel = wheel

    def set_body(self, body):
        self.__body = body

    def set_engine(self, engine):
        self.__engine = engine

    def car_detail(self):
        print(f'body shape: {self.__body.shape}')
        print(f'wheel size: {self.__wheel.size}')
        print(f'engine power: {self.__engine.power}')


class Builder(ABC):
    """
    Builder is a abstract Class to specify the Builders components
    """

    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_wheel(self):
        pass

    @abstractmethod
    def get_body(self):
        pass


class BmwBuilder(Builder):

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_body(self):
        body = Body()
        body.shape = 'sedan'
        return body

    def get_engine(self):
        engine = Engine()
        engine.power = 2000
        return engine


class BenzBuilder(Builder):

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 18
        return wheel

    def get_body(self):
        body = Body()
        body.shape = 'coupe'
        return body

    def get_engine(self):
        engine = Engine()
        engine.power = 3000
        return engine


class Wheel:
    size = None


class Body:
    shape = None


class Engine:
    power = None


bmw_builder = BmwBuilder()
director = Director()
director.set_builder(bmw_builder)
car1 = director.get_car()
car1.car_detail()