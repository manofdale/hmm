import numpy as np
from scipy.sparse import lil, csr


def viterbi(observed_seq, hmm):
    """ recover a sequence of hidden states from a sequence of observations

    :param hmm: container for initial probabilities, transition matrix, emission matrix, observation, and state space
    :param observed_seq: a sequence of observations
    :return: the most likely sequence of states
    """
    if hmm is None or observed_seq is None or not hmm.is_valid():
        return None
    if len(observed_seq) == 0:
        return []

    class TrellisNode:  # to keep only the survivor paths in the trellis diagram
        def __init__(self, state_id, parent):
            self.state_id = state_id
            self.parent = parent  # keep a reference to parent

    hidden_seq = []
    states = hmm.states[2:]  # all states except the states B & E
    emissions = hmm.emission_log_probs
    transitions = hmm.transition_log_probs
    nb_state = len(states)
    state_window = [TrellisNode(i, None) for i in range(nb_state)]
    posteriors = [hmm.starting_log_probs[i] + emissions[i][observed_seq[0]] for i in range(nb_state)]  # current scores

    for obs in observed_seq[1:]:
        prev_states = state_window  # allow the garbage collector to free the dead paths
        state_window = [TrellisNode(i, None) for i in range(nb_state)]

        for i,state in enumerate(transitions):
            best_parent=0
            for p in state.parents:
                # if [p.id]
                pass

    return hidden_seq
