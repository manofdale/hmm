from ml import decoders
from ds.graph import DirectedGraph
import unittest

# TODO coverage

class DirectedGraphTest(unittest.TestCase):
    def test_graph_invalid(self):
        self.assertEqual(decoders.viterbi(None, []), None)



if __name__ == '__main__':
    unittest.main()
