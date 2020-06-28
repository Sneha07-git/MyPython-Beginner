import unittest
import script2   #Import the file which is to be tested

class TestGame(unittest.TestCase):

    def test_input(self):
        result = script2.guess_game(5,5) # calling the function using the imported file name
        self.assertTrue(result)

    def test_input_wrong_number(self):
        result = script2.guess_game(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number3(self):
        result = script2.guess_game(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = script2.guess_game(5, '11') #parameter 1 = guess, Parameter 2=answer; we're taking input as anser
        self.assertFalse(result)



if __name__ == '__main__' :
    unittest.main()