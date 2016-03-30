from ml import decoders
from ds.pgm import HiddenMarkov
import unittest

class ViterbiTest(unittest.TestCase):
    def test_viterbi_invalid(self):
        self.assertEqual(decoders.viterbi(None,[]),None)
        self.assertEqual(decoders.viterbi(HiddenMarkov(),[]),None)
        self.assertEqual(decoders.viterbi(HiddenMarkov(),None),None)
        self.assertEqual(decoders.viterbi(HiddenMarkov(),None),None)  # TODO give a valid HMM
        self.assertEqual(decoders.viterbi(HiddenMarkov(),[]),[])  # TODO give a valid HMM

if __name__ == '__main__':
    unittest.main()
