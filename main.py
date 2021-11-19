#XadievDev
#37-lesson.Classlarni tekshirish

#-------------------------------------------------#

import unittest
from classlar import Car

class CarTest(unittest.TestCase):
    def test_car(self):
        avto1 = Car('toyota','camry',2021)
        self.assertIsNotNone(avto1.make)
        self.assertIsNotNone(avto1.model)
        self.assertIsNotNone(avto1.year)
        self.assertIsNone(avto1.price)
        self.assertEqual(0,avto1.get_km())
        avto2 = Car("toyota","camry",2020,price=75000)
        self.assertEqual(75000,avto2.price)
unittest.main()