import numpy as np
import operator
import copy


def viterbi(observed_seq, hmm):
    """ recover a sequence of hidden states from a sequence of observations

    :param hmm: container for initial probabilities, transition graph, emission matrix, observation, and state space
    :param observed_seq: a sequence of observations
    :return: the probability alongside with the most likely sequence of states
    """
    if hmm is None or observed_seq is None or not hmm.is_valid() or len(observed_seq) == 0:
        return None

    class TrellisNode:  # to keep only the survivor paths in the trellis diagram
        def __init__(self, state_id, node_parent):
            self.state_id = state_id
            self.parent = node_parent  # keep a reference to parent

    hidden_seq = np.zeros(len(observed_seq))
    # a list of states except the beginning and ending states
    states = hmm.emitters
    # state window on the trellis diagram, width = 1, height = # states, slide at each observation step
    state_window = [TrellisNode(s.id, None) for s in states]  # parent: None
    # initialize scores
    scores = [hmm.starting_p[s.id] + s.emission_p[observed_seq[0]] for s in states]  # updated at each observation step
    for obs in observed_seq[1:]:  # construct survivor paths for each state
        prev_states = state_window
        prev_scores = copy.deepcopy(scores)  # scores = posterior log probabilities
        state_window = [TrellisNode(s.id, None) for s in states]  # window for the next step
        for i, s in enumerate(states):
            parent_score = 0
            for j, sc in enumerate(prev_scores):  # pick the best parent + transition score
                # default transition_p = 0, parent = None
                transition_p, parent = s.parents.get(prev_states[j].id, (0, None))
                score = sc + transition_p
                if parent_score < score:  # if there are two parents with the same score, choose the first one
                    parent_score = score
                    state_window[i].parent = prev_states[j]
            scores[i] += s.emission_p[obs] + parent_score  # update scores
    # end of observations, scores are calculated for len(states) surviving paths
    # now pick the best score and backtrack the best survived path
    index, max_score = max(enumerate(scores), key=operator.itemgetter(1))
    node = state_window[index]
    for i in range(len(hidden_seq) - 1, -1, -1):
        hidden_seq[i] = node.id
        node = node.parent

    return score, hidden_seq
