import unittest
from treasure_island.treasure import choose_first_path, choose_second_path, choose_door

class TestTreasureIsland(unittest.TestCase):

    def test_first_path(self):
        self.assertEqual(choose_first_path("left"), "lake")
        self.assertEqual(choose_first_path(" right "), "hole")

    def test_second_path(self):
        self.assertEqual(choose_second_path("wait"), "house")
        self.assertEqual(choose_second_path(" swim "), "trout")

    def test_choose_door(self):
        self.assertEqual(choose_door("red"), "fire")
        self.assertEqual(choose_door("blue"), "beasts")
        self.assertEqual(choose_door("yellow"), "treasure")
        self.assertEqual(choose_door("green"), "invalid")

if __name__ == "__main__":
    unittest.main()
