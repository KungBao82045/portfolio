import unittest
import rot13_decryption as rot


class Test_methods(unittest.TestCase):
    def rot_test(self):
        expect = "Hello, World!"
        actual = rot.rot_input
        self.assertEqual(expect, actual)


if __name__ == "__main__":
    unittest.main()