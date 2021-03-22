import ast
import json
import sys
import unittest

sys.path.append('../')

from peking_express import PekingExpress

def read_file(path: str) -> list[str]:
    with open(path, 'r', encoding='utf8') as file:
        return file.read().split('\n')


class TestSortFunction(unittest.TestCase):
    def test_can_load_file(self):
        file = [
            '{"locations": {"number": 4, "critical": [3]}, "connections": {"source": [1, 1, 1, 2, 3], "target": [2, 3, 88, 3, 88], "price": [1, 3, 7, 1, 1]}}',
            '1', '5', '[[2, 3], [3], [88], [88]]']
        self.assertIsNotNone(PekingExpress(json.loads(file[0]), int(file[1]), int(file[2]), ast.literal_eval(file[3])))

    def test_file1(self):
        file = read_file('./test_files/test1.txt')
        self.assertIsNotNone(PekingExpress(json.loads(file[0]), int(file[1]), int(file[2]), ast.literal_eval(file[3])))

    def test_file2(self):
        file = read_file('./test_files/test2.txt')
        self.assertIsNotNone(PekingExpress(json.loads(file[0]), int(file[1]), int(file[2]), ast.literal_eval(file[3])))

    def test_file3(self):
        file = read_file('./test_files/test3.txt')
        self.assertIsNotNone(PekingExpress(json.loads(file[0]), int(file[1]), int(file[2]), ast.literal_eval(file[3])))

    def test_file4(self):
        file = read_file('./test_files/test4.txt')
        self.assertIsNotNone(PekingExpress(json.loads(file[0]), int(file[1]), int(file[2]), ast.literal_eval(file[3])))


if __name__ == '__main__':
    unittest.main()
