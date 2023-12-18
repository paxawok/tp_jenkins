import unittest
import datetime
from app import DictionaryList
from unittest.mock import patch
import io
import json

class TestDictionaryList(unittest.TestCase):

    def setUp(self):
        self.counter = DictionaryList()

    def test_empty(self):
        self.assertTrue(self.counter.empty())
        self.counter.add(99, '2001-09-01')
        self.assertFalse(self.counter.empty())
        
    def test_add(self):
        self.counter.clear_values()
        self.counter.add(234, 'dqrtokoks')
        self.counter.add('222', '2004-10-10') #додається лише це значення
        self.counter.add('йцукен', '65пч848')
            
        self.counter.print_all()

    def test_remove(self):
        self.counter.clear_values()

        num = 55
        date = "2023-10-08"
        self.counter.add(num, date)
        self.assertEqual(len(self.counter.items), 1)

        removed = self.counter.remove(num)
        self.assertTrue(removed)

        self.assertEqual(len(self.counter.items), 0)

        removed = self.counter.remove(num)
        self.assertFalse(removed)

    def test_oldest_verification_date(self):
        self.counter.clear_values()

        num1 = 1
        num2 = 2
        num3 = 3
        date1 = '2023-10-08'
        date2 = '1990-10-09'
        date3 = '2023-10-07'
        
        self.counter.add(num1, date1)
        self.counter.add(num2, date2)
        self.counter.add(num3, date3)

        expected_oldest_date = datetime.datetime(1990, 10, 9)
        oldest_date = self.counter.oldest_verification_date()
        self.assertEqual(oldest_date, expected_oldest_date)

    def test_find_by_number(self):
        self.counter.clear_values()

        num1 = 1
        num2 = 2
        num3 = 3
        date1 = '2023-10-08'
        date2 = '2023-10-09'
        date3 = '2023-10-07'

        self.counter.add(num1, date1)
        self.counter.add(num2, date2)
        self.counter.add(num3, date3)

        found_date = self.counter.find_by_number(num2)
        expected_date = datetime.datetime(2023, 10, 9)
        self.assertEqual(found_date, expected_date)
    
    def test_print_all(self):
        self.counter.clear_values()

        num1 = 1
        num2 = 2
        date1 = '2023-10-08'
        date2 = '2023-10-09'
        
        self.counter.add(num1, date1)
        self.counter.add(num2, date2)

        captured_output = io.StringIO()
        with patch('sys.stdout', new=captured_output):
            self.counter.print_all()

        printed_output = captured_output.getvalue()

        captured_output.close()
        expected_output = 'Номер квартири: 1, Дата повірки: 2023-10-08\n' \
                          'Номер квартири: 2, Дата повірки: 2023-10-09\n'

        self.assertEqual(printed_output, expected_output)

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-report')
    unittest.main(testRunner=runner)
    unittest.main