from peking_express import PekingExpress
import unittest
import json
import ast


def read_file(path: str) -> list[str]:
    with open(path, 'r', encoding='utf8') as file:
        return file.read().split('\n')


class TestSortFunction(unittest.TestCase):
    def test_can_load_file(self):
        file = read_file('test_files/test1.txt')
        self.assertIsNotNone(PekingExpress(json.loads(file[0]), int(file[1]), int(file[2]), ast.literal_eval(file[3])))


if __name__ == '__main__':
    unittest.main()
