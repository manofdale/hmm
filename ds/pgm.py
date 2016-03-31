from graph import Node, DirectedGraph
from ml.util import random_pick, try_to_log
from ds.cfg_reader import load_config
import logging


class EmitterNode(Node):
    def __init__(self, state_id, parents=None, children=None, **kwargs):
        super(EmitterNode, self).__init__(state_id, parents, children, **kwargs)
        self.emission_ps = {}  # will be a dictionary [obs] = emission_prob


class HiddenMarkov(object):
    def __init__(self, config_path, transitions=None, emissions=None, start_id='B', end_id='E',
                 convert_zero=0.000000000001):
        """
        :param config_path: to initialize the model path, sample format is available in ../data/hmm.cfg
        :param transitions: a list of triplets (from_id, to_id, probability), where from_id and to_id are state labels
        :param emissions: a list of triplets (emitter_id, emission_id, probability), where emitter_id is a state label
        :param start_id: label for the initial state, (can not emit obs), used for getting the starting probabilities
        :param end_id: label for the final state (can not emit obs), only required for the simulations
        :param convert_zero: a small number to handle missing or zero entries in the emission and transition data,
             if convert_zero is 0 and there is a missing or zero entry in the probabilities, an exception will be raised
        """
        self.graph = DirectedGraph(node_t=EmitterNode)
        self.emitters = []
        self.convert_zero = convert_zero
        self.start_id = start_id
        self.end_id = end_id
        if isinstance(config_path, basestring):
            transitions, emissions = load_config(path=config_path)  # load from data
        else:
            assert (transitions is not None and emissions is not None)
        self.set_transitions(transitions)  # (re)init emitters here
        self.starting_ps = {child.id: w for [w, child] in self.graph.nodes[self.start_id].children.values()}
        self.set_emissions(emissions)
        self.update_emitters()

    def set_transitions(self, transitions):
        for from_id, to_id, p in transitions:
            log_p, converted = try_to_log(p, convert_zero=self.convert_zero)  # use log probabilities
            if converted:
                self.graph.add_vertex(from_id, to_id, log_p)
            else:
                raise Exception("transition log probability conversion failed for %s" % str(p))

    def update_emitters(self):
        self.emitters = [state for state_id, state in self.graph.nodes.items() if
                         len(state.emission_ps.items()) != 0]  # list of emitter nodes

    def set_emissions(self, emissions):
        for node_id, obs_id, p in emissions:
            log_p, converted = try_to_log(p, convert_zero=self.convert_zero)  # use log probabilities
            if converted:
                if node_id in self.graph.nodes:
                    self.graph.nodes[node_id].emission_ps[obs_id] = log_p
            else:
                raise Exception("emission log probability conversion failed for %s" % str(p))

    def is_valid(self):
        valid = (self.emitters is not None and len(self.emitters) > 0 and self.starting_ps is not None and len(
            self.starting_ps) > 0)
        print(self.emitters is not None, len(self.emitters) > 0, self.starting_ps is not None, len(
            self.starting_ps) > 0)
        # valid = valid and other_checks()  # Can do more checks here
        return valid

    def might_not_stop(self, stop_p=0.0000001):
        needy_nodes = set()
        end_id = self.end_id  # end node
        for state in self.emitters:
            if end_id not in state.children or state.children[end_id][0] < stop_p:  # need another node to end
                needy_nodes.add(state)
        for state in needy_nodes:
            all_needy = True
            for p, child in state.children.items():  # if all kids are needy, then possible infinite loop
                if child not in needy_nodes:
                    all_needy = False
                    break
            if all_needy:
                return True
        return False

    def simulate(self, limit):
        print("to be implemented")
        return
        if not self.is_valid():
            logging.error("The model configuration is not valid, can not simulate..")
        if self.might_not_stop():
            inp = raw_input("This simulation might get into an infinite loop, continue anyway? (y/n)")
            if inp.lower() != 'y':
                print("Smart choice!")
                return
            else:
                print("Alright, let's burn some cpu!")

        states = self.emitters
        p_ranges = [self.starting_ps[s.id] for s in states]
        ix = random_pick(p_ranges)
        node = states[ix]
        emitted_seq = []
        for i in range(limit):
            if node is None:
                return emitted_seq
                # p_ranges=[p for p,c in node.children.values()]
                # TODO finish this later
