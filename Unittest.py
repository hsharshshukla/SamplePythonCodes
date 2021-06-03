import unittest
from WebScrap import fullname


class NameTestCase(unittest.TestCase):

    def test_fullname(self):
        full_name = fullname('Janis', 'Joplin')
        self.assertEqual(full_name, 'Janis Joplin')  # check result against expected result


if __name__ == '__main__':
    unittest.main()


