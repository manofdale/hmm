from ds.pgm import HiddenMarkov
from ml import decoders, util
from math import exp
import sys
import os

if __name__ == '__main__':
    key = 1
    D = {}
    state_space = ["St1", "St2"]
    hidden_sequence = []
    observed_sequence = []
    with open("data/hmmdata.txt", "r") as f:
        header = next(f)
        assert (header.strip().split() == ["step", "state", "observation"])
        for line in f:
            splitted = line.strip().split()
            if len(splitted) > 2:
                hidden_sequence.append(splitted[1])
                observed_sequence.append(splitted[2])
    hmm = HiddenMarkov("data/hmm.cfg")  # load the model from file
    probability, hidden_pred = decoders.viterbi(observed_sequence, hmm)  # get the most likely hidden sequence
    print("viterbi algorithm has found the following hidden sequence with the probability p = %f" % exp(probability))
    print(hidden_pred)
    statistics = util.evaluate_prediction(hidden_sequence, hidden_pred)
    cm, (tp, tn, fp, fn), precision, recall, fscore, support = statistics
    statistics = ["confusion matrix", "tp", "tn", "fp", "fn", "precision", "recall", "fscore", "support"]
    print("for %s:" % " ".join(state_space))
    for i, j in zip(statistics, [cm, tp, tn, fp, fn, precision, recall, fscore, support]):
        print("%s:\n  %s\n %s" % (i, "\t".join(state_space), str(j).replace("[", "").replace("]", "")))
