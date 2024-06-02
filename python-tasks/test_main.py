import unittest

class TestGraphFunctions(unittest.TestCase):
    def test_walkGraph(self):
        A = ExampleGNode('A')
        B = ExampleGNode('B')
        C = ExampleGNode('C')
        A.children = [B, C]
        result = walkGraph(A)
        self.assertEqual(result, [A, B, C])

    def test_paths(self):
        A = ExampleGNode('A')
        B = ExampleGNode('B')
        C = ExampleGNode('C')
        A.children = [B, C]
        result = paths(A)
        self.assertEqual(result, [[A, B], [A, C]])

if __name__ == '__main__':
    unittest.main()
