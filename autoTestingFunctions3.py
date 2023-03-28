import unittest
import Functions3

class TestFunctions3(unittest.TestCase):
    def test_invstring(self):
        self.assertEqual(Functions3.invstring("All along the watchtower"), "rewothctaw eht gnola llA")
        self.assertEqual(Functions3.invstring("1234567890"), "0987654321")

    def test_oddvseven(self):
        self.assertEqual(Functions3.oddvseven(45), "This number is odd.")
        self.assertEqual(Functions3.oddvseven(144), "This number is even.")
        self.assertEqual(Functions3.oddvseven(-33), "This number is odd.")

    def test_findbigboy(self):
        self.assertEqual(Functions3.findbigboy([34, 2, 18]), "The highest number is:  34")
        self.assertEqual(Functions3.findbigboy(["asd", "ff", "asj"]), "Please use only digits.")
        self.assertEqual(Functions3.findbigboy([-14, 16, 3, "number"]), "Please use only digits.")
        self.assertEqual(Functions3.findbigboy([-11, -4, -1, 0]), "The highest number is:  0")

    def test_findsmol(self):
        self.assertEqual(Functions3.findsmol([11, 2, 44, 33]), "The smallest number is:  2")
        self.assertEqual(Functions3.findsmol(["asd", -1, "ph", 14]), "Please use only digits.")
        self.assertEqual(Functions3.findsmol([-72, 1, -931, 14]),"The smallest number is:  -931")

    def test_checkdiv(self):
        self.assertEqual(Functions3.checkdiv(144, 12), "These numbers can be divided with each other.")
        self.assertEqual(Functions3.checkdiv(16, "two"), "Please use only digits.")
        self.assertEqual(Functions3.checkdiv(11, 7), "These numbers cannot be divided with each other.")
        self.assertEqual(Functions3.checkdiv(-6, 3), "These numbers can be divided with each other.")

if __name__ == '__main__':
    unittest.main()