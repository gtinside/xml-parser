import unittest
from xml_parser import XMLParser

class XMLParserTestCase(unittest.TestCase):
    def test_parse(self):
        # Create an instance of XMLParser
        parser = XMLParser('assets/tasks3.xml')

        # Call the parse method
        items = parser.parse()

        # Assert that the returned items list is not empty
        self.assertTrue(items)

        # Assert that each item in the list has the expected attributes
        for item in items:
            self.assertIsNotNone(item.id)
            self.assertIsNotNone(item.name)
            self.assertIsNotNone(item.description)
            self.assertIsNotNone(item.details)


if __name__ == '__main__':
    unittest.main()