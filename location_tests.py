import unittest
from location import *

class TestLab1(unittest.TestCase):

    #Tests if location, SLO, is string represented correctly
    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    # Tests if location, Paris, is string represented correctly
    def test_repr2(self):
        loc = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc),"Location('Paris', 48.9, 2.4)")

    # Tests if location, Seattle, is string represented correctly
    def test_repr3(self):
        loc = Location("Seattle", 47.6, -122.3)
        self.assertEqual(repr(loc),"Location('Seattle', 47.6, -122.3)")

    # Tests if location, Melbourne, is string represented correctly
    def test_repr4(self):
        loc = Location("Melbourne", -37.8, 144.9)
        self.assertEqual(repr(loc),"Location('Melbourne', -37.8, 144.9)")

    # Tests if location, Chiang Mai, is string represented correctly
    def test_repr5(self):
        loc = Location("Chiang Mai", 18.8, 98.9)
        self.assertEqual(repr(loc),"Location('Chiang Mai', 18.8, 98.9)")

    # Tests if SLO is equivalent to SLO
    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1, loc2)

    #Tests to check that SLO is not equivalent to Paris
    def test_eq2(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertNotEqual(loc1, loc2)

    #Tests to check that Seattle equals Seattle
    def test_eq3(self):
        loc1 = Location("Seattle", 47.6, -122.3)
        loc2 = Location("Seattle", 47.6, -122.3)
        self.assertEqual(loc1, loc2)

    #Checks that Melbourne is not equivalent to Chiang Mai
    def test_eq4(self):
        loc1 = Location("Melbourne", -37.8, 144.9)
        loc2 = Location("Chiang Mai", 18.8, 98.9)
        self.assertNotEqual(loc1, loc2)


if __name__ == "__main__":
        unittest.main()
