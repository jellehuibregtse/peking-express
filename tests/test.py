import peking_express
import unittest
import json
import ast


class TestSortFunction(unittest.TestCase):
    def test_isSolvable(self):
        fo = open("test_files/test1.txt", encoding="utf8")
        text = fo.read().split('\n')
        fo.close()
        result = peking_express.PekingExpress(json.loads(text[0]), int(text[1]), int(text[2]), ast.literal_eval(text[3]))
        self.assertEqual(result, [3, 2, 2, 88, 88])


if __name__ == '__main__':
    unittest.main()
