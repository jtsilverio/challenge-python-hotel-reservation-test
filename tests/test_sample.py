from unittest import TestCase
from context import src
from src.my_module import get_cheapest_hotel

class MyTest(TestCase):
    def test1(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test2(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test3(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))

    def test4(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 26Mar2009(thur)"))

    def test5(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 14May2022(sat)"))

    def test6(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur)"))

    def test7(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 14May2022(sat)"))
    
    def test8(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards:26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))

    def test9(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards:26Mar2009(thur),27Mar2009(fri),28Mar2009(sat)"))

    def test10(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel(" Rewards:26Mar2009(thur),27Mar2009(fri),28Mar2009(sat)"))