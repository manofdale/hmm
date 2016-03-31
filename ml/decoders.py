import numpy as np
import operator
import copy
from ds.graph import SinglyLinkedNode
from math import log


def viterbi(observed_seq, hmm):
    """ recover a sequence of hidden states from a sequence of observations

    :param hmm: container for initial probabilities, transition graph, emission matrix, observation, and state space
    :param observed_seq: a sequence of observations
    :return: the probability alongside with the most likely sequence of states
    """

    if hmm is None or observed_seq is None or not hmm.is_valid() or len(observed_seq) == 0:
        print(hmm is None, observed_seq is None, not hmm.is_valid(), len(observed_seq) == 0)
        return None, None

    hidden_seq = [""]*len(observed_seq)
    # a list of states except the beginning and ending states
    states = hmm.emitters
    log_0 = log(hmm.convert_zero)
    # state window on the trellis diagram, width = 1, height = # states, slide at each observation step
    state_window = [SinglyLinkedNode(s.id) for s in states]  # parent= None
    # initialize scores
    scores = [hmm.starting_ps[s.id] + s.emission_ps[observed_seq[0]] for s in states]  # updated at each obs step
    for obs in observed_seq[1:]:  # construct survivor paths for each state
        prev_states = state_window
        prev_scores = copy.deepcopy(scores)  # scores = posterior log probabilities
        state_window = [SinglyLinkedNode(s.id) for s in states]  # window for the next step, parents are None
        for i, s in enumerate(states):
            parent_score = -np.inf
            parent_i = -1
            for j, sc in enumerate(prev_scores):  # pick the best parent + transition score
                #print(prev_scores)
                # default transition_p = 0, parent = None
                transition_p, _ = s.parents.get(prev_states[j].id, [-np.inf, None])
                score = sc + transition_p
                if parent_score < score:  # if there are two parents with the same score, choose the first one
                    parent_score = score
                    parent_i = j
            if parent_i > -1:
                state_window[i].link = prev_states[parent_i]
            else:  # no parent was found
                raise Exception("Something is wrong! No surviving parent was found for state %s" % str(s.id))
            scores[i] = s.emission_ps.get(obs, log_0) + parent_score  # update scores, if emission p==0, won't survive
    # end of observations, scores are calculated for len(states) surviving paths
    # now pick the best score and backtrack the best survived path
    print(scores)
    index, max_score = max(enumerate(scores), key=operator.itemgetter(1))
    node = state_window[index]
    for i in range(len(hidden_seq) - 1, -1, -1):
        hidden_seq[i] = node.id
        node = node.link
    return max_score, hidden_seq
