from ds.pgm import HiddenMarkov
from ml import decoders, metrics


if __name__ == '__main__':
    state_space=["St1","St2"]
    hidden_sequence = []
    emitted_sequence = []
    with open("data/hmmdata", "rb") as f:
        header = next(f)
        assert (header.strip().split() == ["step", "state", "observation"])
        for line in f:
            splitted = line.strip().split()
            if len(splitted) > 2:
                hidden_sequence.append(splitted[1])
                emitted_sequence.append(splitted[2])
    # hmm = HiddenMarkov("data/hmm_params")  # load the model from file
    # hidden_pred = decoders.viterbi(hmm, emitted_sequence)  # get the most likely hidden sequence
    statistics = metrics.evaluate_prediction(hidden_sequence, hidden_sequence)
    cm, (tp,tn,fp, fn), precision, recall, fscore, support = statistics
    statistics=["confusion matrix", "tp", "tn", "fp", "fn", "precision", "recall", "fscore", "support"]
    print("for %s:"%" ".join(state_space))
    for i,j in zip(statistics, [cm, tp,tn,fp, fn, precision, recall, fscore, support]):
        print("%s:\n %s"%(i,str(j)))

