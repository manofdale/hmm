

def viterbi(hmm,observed):
    """ recover a sequence of hidden states from a sequence of observations

    :param hmm: container for initial probabilities, transition matrix, emission matrix, observation and state space,
    :param observed: a sequence of observations
    :return: the most likely sequence of states
    """

    """
    obs, states, start_p, trans_p, emit_p
    The observation space  O=\{o_1,o_2,\dots,o_N\},
the state space  S=\{s_1,s_2,\dots,s_K\} ,
a sequence of observations  Y=\{y_1,y_2,\ldots, y_T\}  such that  y_t==i  if the observation at time  t  is  o_i ,
transition matrix  A  of size  K\cdot K  such that  A_{ij}  stores the transition probability of transiting from state  s_i  to state  s_j ,
emission matrix  B  of size  K\cdot N  such that  B_{ij}  stores the probability of observing  o_j  from state  s_i ,
an array of initial probabilities  \pi  of size  K  such that  \pi_i  stores the probability that  x_1 ==  s_i
    :param hmm:
    :param seq:
    :return:
    """
