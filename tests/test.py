import ast
import json
import unittest

from peking_express import PekingExpress


def load_peking_from_file(file):
    return PekingExpress(json.loads(file[0]), int(file[1]), int(file[2]), ast.literal_eval(file[3]))


class TestSortFunction(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.file1 = [
            '{"locations": {"number": 4, "critical": [3]}, "connections": {"source": [1, 1, 1, 2, 3], "target": [2, '
            '3, 88, 3, 88], "price": [1, 3, 7, 1, 1]}}', '3', '21', '[[2, 3], [3], [88], [88]]']

        self.file1_alternative = [
            '{"locations": {"number":4, "critical":[3]}, "connections": {"source": [1, 1, 1, 2, 3],"target": [2, 3, '
            '88, 3, 88],"price": [1, 3, 7, 1, 1]}}', '1', '5', '[[2,3],[3],[88],[88]]']

        self.file2 = [
            '{"locations": {"number": 10, "critical": [7, 6, 3]}, "connections": {"source": [2, 7, 3, 1, 9, 4, 6, 8, '
            '5, 4], "target": [7, 3, 1, 9, 4, 6, 8, 5, 88, 5], "price": [3, 1, 5, 6, 2, 8, 3, 7, 2, 5]}}',
            '2', '39',
            '[[4, 9, 8, 88], [6, 1, 9], [4, 1, 3, 8, 9], [4, 5, 1, 9, 3], [3, 6, 1, 88, 5], [5, 4, 7, 3, 88], [4, 2, '
            '5, 7], [9, 2, 8, 3], [4, 1, 6, 5], [4, 5, 9, 88, 6]]']

        self.file3 = [
            '{"locations": {"number": 10, "critical": [8, 9, 4, 2]}, "connections": {"source": [8, 5, 1, 4, 9, 6, '
            '2, 3, 7, 6, 2, 4, 3, 8, 6, 5, 9, 6, 2, 1, 5, 9, 1, 1, 4, 4, 8, 8, 8, 4], "target": [5, 1, 4, 9, 6, '
            '2, 3, 7, 88, 7, 88, 88, 88, 9, 88, 88, 3, 3, 7, 9, 4, 2, 6, 7, 2, 6, 2, 4, 88, 3], "price": [6, 4, '
            '1, 3, 2, 8, 2, 7, 8, 7, 2, 2, 3, 2, 1, 1, 4, 5, 4, 7, 3, 9, 6, 3, 3, 5, 1, 1, 8, 8]}}',
            '8', '105', '[[1, 88, 9], [3, 5], [9, 6], [8, 6, 3], [88, 3, 2], [7, 8, 4], [5, 3], [88, 1, 9], [7, '
                        '3], [2, 1, 3]]']

        self.file4 = [
            '{"locations": {"number": 40, "critical": [20, 38, 39, 19, 11, 26, 1, 2, 15, 8]}, "connections": {'
            '"source": [8, 30, 16, 24, 10, 22, 19, 36, 13, 5, 11, 18, 26, 25, 4, 7, 6, 20, 32, 37, 1, 12, 27, 35, 3, '
            '34, 9, 38, 28, 39, 2, 29, 23, 14, 33, 31, 21, 17, 15, 38, 37, 24, 22, 28, 14, 18, 30, 24, 20, 34, 9, 37, '
            '11, 1, 35, 14, 9, 16, 20, 33], "target": [30, 16, 24, 10, 22, 19, 36, 13, 5, 11, 18, 26, 25, 4, 7, 6, '
            '20, 32, 37, 1, 12, 27, 35, 3, 34, 9, 38, 28, 39, 2, 29, 23, 14, 33, 31, 21, 17, 15, 88, 23, 23, 38, 2, '
            '31, 15, 35, 13, 34, 38, 39, 21, 88, 32, 34, 9, 21, 88, 11, 3, 21], "price": [4, 1, 6, 5, 3, 3, 7, 7, 5, '
            '2, 3, 4, 8, 2, 3, 4, 1, 4, 7, 9, 8, 1, 6, 2, 8, 9, 7, 6, 8, 6, 8, 4, 5, 5, 4, 2, 6, 5, 9, 9, 2, 9, 3, 9, '
            '4, 2, 5, 1, 2, 3, 9, 9, 7, 7, 9, 2, 2, 2, 5, 7]}}',
            '8', '110',
            '[[7, 30, 31, 25, 8], [28, 33, 4, 26, 6], [18, 25, 38, 20, 31, 14], [11, 20, 32, 6, 15], [32, 7, 20, 11, '
            '3], [16, 20, 3, 34, 11, 6, 38], [9, 38, 35, 18, 3, 30, 11], [13, 11, 23, 24, 3, 21, 35], [16, 20, 30, '
            '10, 32], [3, 8, 16, 32, 6, 22, 38], [9, 20, 2, 24, 37, 35, 28], [23, 6, 9, 32, 88], [35, 37, 20, 14, 11, '
            '21], [31, 6, 5, 3, 16], [35, 11, 20, 24, 13, 33, 28], [32, 21, 6, 14, 34, 3, 10], [3, 1, 31, 11, 9, 35], '
            '[28, 18, 38, 12, 37, 33], [24, 9, 38, 32, 26], [28, 10, 21, 20, 24, 37, 11], [32, 6, 34, 5, 9, 23, 24], '
            '[16, 9, 3, 37, 11], [24, 16, 5, 30, 38], [10, 8, 38, 9, 34], [22, 34, 88, 39, 28, 21, 3], [15, 31, 17, '
            '33, 28, 3], [15, 21, 39, 38, 20], [24, 23, 28, 32, 88, 2], [16, 38, 14, 37, 20], [20, 3, 32, 1, 28, 9, '
            '6]]']

    def test_can_initialize_graph_test_file1(self):
        peking1 = load_peking_from_file(self.file1)
        graph = peking1.pekingMap

        vertices = list(graph.get_vertices())
        critical_vertex = graph.get_vertex(3).critical

        self.assertIsNotNone(graph, "Graph gets initialized.")
        self.assertEqual(vertices, [1, 2, 3, 88], "Graph should contain vertices [1, 2, 3, 88].")
        self.assertTrue(critical_vertex, "Vertex with index 3 should be a critical vertex.")

    def test_path_length_test_file1(self):
        peking1 = load_peking_from_file(self.file1)

        length = peking1.get_path_length()

        self.assertEqual(2, length, "The length of the path should be 2.")

    def test_path_test_file1_alternative(self):
        peking1 = load_peking_from_file(self.file1_alternative)
        graph = peking1.pekingMap

        vertices = list(graph.get_vertices())
        critical_vertex = graph.get_vertex(3).critical
        length = peking1.get_path_length()

        self.assertIsNotNone(graph, "Graph gets initialized.")
        self.assertEqual(vertices, [1, 2, 3, 88], "Graph should contain vertices [1, 2, 3, 88].")
        self.assertTrue(critical_vertex, "Vertex with index 3 should be a critical vertex.")
        self.assertEqual(1, peking1.get_path()[0], "Peking start location should be 1.")
        self.assertEqual(5, peking1.budget, "Peking budget should be 5.")
        self.assertEqual(5, length, "The length of the path should be 5.")

    def test_can_initialize_graph_test_file2(self):
        peking2 = load_peking_from_file(self.file2)
        graph = peking2.pekingMap

        vertices = list(graph.get_vertices())
        critical_vertices = graph.get_critical_vertices()
        critical_vertices_indices = [vertex.index for vertex in critical_vertices]

        self.assertIsNotNone(graph, "Graph gets initialized.")
        self.assertEqual(set(vertices), {1, 2, 3, 4, 5, 6, 7, 8, 9, 88},
                         "Graph should contain vertices [1, 2, 3, 4, 5, 6, 7, 8, 9, 88].")
        self.assertEqual(set(critical_vertices_indices), {3, 6, 7}, "Graph should contain critical vertices [7, 6, 3]")

    def test_can_initialize_graph_test_file3(self):
        peking3 = load_peking_from_file(self.file3)
        graph = peking3.pekingMap

        vertices = list(graph.get_vertices())
        critical_vertices = graph.get_critical_vertices()
        critical_vertices_indices = [vertex.index for vertex in critical_vertices]

        self.assertIsNotNone(graph, "Graph gets initialized.")
        self.assertEqual(set(vertices), {1, 2, 3, 4, 5, 6, 7, 8, 9, 88},
                         "Graph should contain vertices [1, 2, 3, 4, 5, 6, 7, 8, 9, 88].")
        self.assertEqual(set(critical_vertices_indices), {8, 9, 4, 2}, "Graph should contain critical vertices [8, 9, "
                                                                       "4, 2]")

    def test_can_initialize_graph_test_file4(self):
        peking3 = load_peking_from_file(self.file4)
        graph = peking3.pekingMap

        vertices = list(graph.get_vertices())
        critical_vertices = graph.get_critical_vertices()
        critical_vertices_indices = [vertex.index for vertex in critical_vertices]

        self.assertIsNotNone(graph, "Graph gets initialized.")
        self.assertEqual(set(vertices),
                         {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                          27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 88},
                         "Graph should contain vertices [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, "
                         "18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, "
                         "88].")
        self.assertEqual(set(critical_vertices_indices), {20, 38, 39, 19, 11, 26, 1, 2, 15, 8}, "Graph should contain "
                                                                                                "critical vertices ["
                                                                                                "20, 38, 39, 19, 11, "
                                                                                                "26, 1, 2, 15, 8]")


if __name__ == '__main__':
    unittest.main()
