import unittest
from python_advanced.module_03_ci_culture_beginning.homework.hw_2_4_hello_world_with_day import app




class TestMaxNumberApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    def test_can_get_correct_max_number_in_series_of_two(self):
        day_to_word_map = {
            0: "понедельника",
            1: "вторника",
            2: "среды",
            3: "четверга",
            4: "пятницы",
            5: "субботы",
            6: "воскресенья",
        }
        weekday=3
        daytoday=day_to_word_map[weekday]

        username = 'username'
        response = self.app.get(self.base_url + username)

        response_text = response.data.decode()
        print(response_text)
        self.assertTrue(username in response_text)
        self.assertTrue(daytoday in response_text)

if __name__ == '__main__':
    unittest.main()