import datetime
import unittest

from reached_date import str_to_datetime, insert_all_dates, check_datetime_reached


class TestDate(unittest.TestCase):
    def test_str_to_datetime(self):
        date, time = str_to_datetime("01.01.2020", "10:00")
        self.assertIsInstance(date, datetime.date)
        self.assertIsInstance(time, datetime.time)

    def test_insert_all_dates(self):
        dates, times = insert_all_dates(2)
        self.assertEqual(len(dates), 2)
        self.assertEqual(len(times), 2)

    def test_check_datetime_reached(self):
        reached = check_datetime_reached(datetime.datetime.strptime("01.01.2020", '%d.%m.%Y').date(), \
                                        datetime.datetime.strptime("10:00", '%H:%M').time())
        not_reached = check_datetime_reached(datetime.datetime.strptime("01.01.2050", '%d.%m.%Y').date(), \
                                        datetime.datetime.strptime("10:00", '%H:%M').time())
        self.assertTrue(reached)
        self.assertFalse(not_reached)


if __name__ == "__main__":
    unittest.main()