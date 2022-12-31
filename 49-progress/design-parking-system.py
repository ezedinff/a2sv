import unittest

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.small > 0:
                self.small -= 1
                return True
            else:
                return False

class Test(unittest.TestCase):
    def test1(self):
        big = 1
        medium = 1
        small = 0
        parkingSystem = ParkingSystem(big, medium, small)
        self.assertEqual(parkingSystem.addCar(1), True)
        self.assertEqual(parkingSystem.addCar(2), True)
        self.assertEqual(parkingSystem.addCar(3), False)
        self.assertEqual(parkingSystem.addCar(1), False)

    def test2(self):
        big = 2
        medium = 1
        small = 0
        parkingSystem = ParkingSystem(big, medium, small)
        self.assertEqual(parkingSystem.addCar(1), True)
        self.assertEqual(parkingSystem.addCar(2), True)
        self.assertEqual(parkingSystem.addCar(3), False)
        self.assertEqual(parkingSystem.addCar(1), True)

if __name__ == '__main__':
    unittest.main()