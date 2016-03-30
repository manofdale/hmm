import bisect
import numpy as np
class MarkovState(object):
    def __init__(self, state_id, parents=None, children=None, direction=0):
        self.id = state_id
        if direction >= 0:  # only store children -> e.g. for simulation
            self.children = children
        if direction <= 0:  # only store parents -> e.g. for viterbi
            self.parents = parents


class HiddenMarkov(object):
    def __init__(self, direction=0, initial_prob=None, transition_prob=None, emission_prop=None, end_state='E',
                 start_state='B', log_prob=True):
        pass

    def is_valid(self):
        return (self.emitters is not None and len(self.emitters) > 0 and self.starting_p is not None and len(
            self.starting_p) > 0
    def random_pick(self, p_ranges):
        p_sum=p_ranges[0]
        for i in range(1,len(p_ranges)):
            p_sum+=p_ranges[i]
            p_ranges[i]=p_sum
        return bisect.bisect(p_ranges,np.random.uniform())  # probabilistically select an index

    def simulate(self, limit):
        states=self.emitters
        p_ranges=[self.starting_p[s.id] for s in states]
        ix=self.random_pick(p_ranges)
        node=states[ix]
        emitted_seq=[]
        for i in range(limit):
            if node is None:
                return emitted_seq
            # p_ranges=[p for p,c in node.children.values()]


# parents.get(i) returns (weight, parent) -> parents = {parent_id:(weight,parent_Node)}

# if direction == 0: save both parents and children, if direction == 1: save only children, if -1 save only parents
# initial probabilities, transition matrix, emission matrix, observation and state space,
"""states = ('Healthy', 'Fever')
end_state = 'E'

observations = ('normal', 'cold', 'dizzy')

initial_p = {'Healthy': 0.6, 'Fever': 0.4}

transition_probability = {
   'Healthy' : {'Healthy': 0.69, 'Fever': 0.3, 'E': 0.01},
   'Fever' : {'Healthy': 0.4, 'Fever': 0.59, 'E': 0.01},
   }

emission_probability = {
   'Healthy' : {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
   'Fever' : {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
   }"""
