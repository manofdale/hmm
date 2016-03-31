import re
import io


def preprocess(line):
    return re.sub(r"[->:,;\'\(\)]", " ", line).split()


def load_config(path="data/hmm.cfg"):
    with io.open(path, "r", encoding="utf-8-sig") as config:
        transitions = []
        emissions = []
        for line in config:
            words = preprocess(line.strip().encode('ascii', 'ignore'))
            if len(words) == 0 or len(words[0]) == 0 or words[0][0] == '#':
                continue
            if len(words) == 3:  # transition data
                transitions.append(words)
            elif len(words) == 1:  # emission label
                emission_label = words[0]
            elif len(words) == 2:  # emission data
                emission = [emission_label] + words
                emissions.append(emission)
        return transitions, emissions
