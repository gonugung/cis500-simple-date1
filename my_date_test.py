import unittest
import my_date


class MyDateTest(unittest.TestCase):

    def year_divided_by_4(self):
        self.assertTrue(my_date.is_leap_year(2028))
        self.assertTrue(my_date.is_leap_year(1604))
        self.assertTrue(my_date.is_leap_year(1960))

    def year_divided_by_100_and_400(self):
        self.assertTrue(my_date.is_leap_year(2400))
        self.assertTrue(my_date.is_leap_year(2000))
        self.assertTrue(my_date.is_leap_year(1600))

    def year_divided_by_100_but_not_400(self):
        self.assertFalse(my_date.is_leap_year(1800))
        self.assertFalse(my_date.is_leap_year(1700))

    def year_not_divided_by_4(self):
        self.assertFalse(my_date.is_leap_year(2003))
        self.assertFalse(my_date.is_leap_year(2019))

    def _2023_jan_11(self):
        self.assertEqual(my_date.ordinal_date(2023, 1, 1), 11)

    def _2023_feb_14(self):
        self.assertEqual(my_date.ordinal_date(2023, 2, 15), 45)

    def _2024_feb_28(self):
        self.assertEqual(my_date.ordinal_date(2024, 2, 29), 59)

    def _2023_dec_31(self):
        self.assertEqual(my_date.ordinal_date(2023, 12, 31), 366)

    def _2022_same_dates(self):
        self.assertEqual(my_date.days_elapsed(2022, 3, 24, 2022, 3, 24), 0)

    def _2024_consecutive_dates(self):
        self.assertEqual(my_date.days_elapsed(2024, 7, 24, 2024, 7, 25), 1)

    def _2024_same_year_dates(self):
        self.assertEqual(my_date.days_elapsed(2024, 6, 13, 2024, 12, 13), 183)

    def _2024_different_years(self):
        self.assertEqual(my_date.days_elapsed(2024, 9, 22, 2025, 9, 22), 365)

    def _2020_leapyear_dates(self):
        self.assertEqual(my_date.days_elapsed(2020, 12, 29, 2024, 12, 31), 1463)

    def _2025_Tuesday(self):
        self.assertEqual(my_date.day_of_week(2025, 9, 25), "Tuesday")

    def _2022_Friday(self):
        self.assertEqual(my_date.day_of_week(2022, 7, 8), "Friday")

    def _2020_Thursday(self):
        self.assertEqual(my_date.day_of_week(2020, 12, 3), "Thursday")

    def _2020_Monday(self):
        self.assertEqual(my_date.day_of_week(2020, 2, 17), "Monday")

    def _2019_Wednesday(self):
        self.assertEqual(my_date.day_of_week(2019, 12, 11), "Wednesday")

    def _2022_Sunday(self):
        self.assertEqual(my_date.to_str(2022, 11, 20), "Sunday, 20 November 2022")

    def _2011_Sunday(self):
        self.assertEqual(my_date.to_str(2011, 1, 9), "Sunday, 09 January 2011")


if __name__ == '__main__':
    unittest.main()
