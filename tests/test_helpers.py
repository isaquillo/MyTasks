import unittest
import helpers


class TestHelpers(unittest.TestCase):
    def test_validate_text_length(self):
        text1 = ""
        text2 = "a"
        text3 = "abc"
        text4 = "abcdefghijklmnopqrstuvwxyzkjklsdjklsfdjklsdfjskldfjsdfojikpjsdk"
        self.assertEqual(helpers.validate_text_length(text1, 1, 30), False)
        self.assertEqual(helpers.validate_text_length(text2, 1, 30), True)
        self.assertEqual(helpers.validate_text_length(text3, 0, 30), True)
        self.assertEqual(helpers.validate_text_length(text4, 0, 30), False)

    def test_validate_int(self):
        self.assertEqual(helpers.validate_int(1), True)
        self.assertEqual(helpers.validate_int("1"), True)
        self.assertEqual(helpers.validate_int(1.0), False)
        self.assertEqual(helpers.validate_int("abc"), False)
        self.assertEqual(helpers.validate_int(True), False)
        self.assertEqual(helpers.validate_int(False), False)
        self.assertEqual(helpers.validate_int(1, 0, 1), True)
        self.assertEqual(helpers.validate_int(4, 1, 1), False)
        self.assertEqual(helpers.validate_int(4, 1, None), True)
        self.assertEqual(helpers.validate_int(4, None, 1), False)

    def test_validate_date_format(self):
        self.assertEqual(helpers.validate_date_format("01-01-1978"), True)
        self.assertEqual(helpers.validate_date_format("01/01/1978"), False)
        self.assertEqual(helpers.validate_date_format("45-13-1978"), False)
        self.assertEqual(helpers.validate_date_format("1978-01-12"), False)
        self.assertEqual(helpers.validate_date_format("11-06-2023"), True)

    def test_validate_correct_range_date(self):
        self.assertEqual(
            helpers.validate_correct_range_date("01-01-1978", "01-12-1978"), True
        )
        self.assertEqual(
            helpers.validate_correct_range_date("01/01/1978", "01/01/1977"), False
        )
        self.assertEqual(
            helpers.validate_correct_range_date("45-13-1978", "01-12-1978"), False
        )
        self.assertEqual(
            helpers.validate_correct_range_date("1978-01-12", "01-12-1978"), False
        )
        self.assertEqual(
            helpers.validate_correct_range_date("11-06-2023", "01-12-2022"), False
        )


if __name__ == "__main__":
    unittest.main()
