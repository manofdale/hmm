from math import log
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    for i in states:
        V[0][i] = log(start_p[i]) + log(emit_p[i][obs[0]])
    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for y in states:
            prob = max(V[t - 1][y0] + log(trans_p[y0][y]) + log(emit_p[y][obs[t]]) for y0 in states)
            V[t][y] = prob
    for i in dptable(V):
        print i
    opt = []
    for j in V:
        for x, y in j.items():
            if j[x] == max(j.values()):
                opt.append(x)
    # The highest probability
    h = max(V[-1].values())
    # print h
    print 'The steps of states are ' + ' '.join(opt) + ' with highest probability of %s' % h

def dptable(V):
    # Print a table of steps from dictionary
    yield " ".join(("%10d" % i) for i in range(len(V)))
    for y in V[0]:
        yield "%.7s: " % y + " ".join("%.7s" % ("%f" % v[y]) for v in V)

states = ('St1', 'St2')
observations = ('a', 'b', 'c')
start_p = {'St1': 0.526, 'St2': 0.474}
trans_p = {
   'St1' : {'St1': 0.969, 'St2': 0.029},
   'St2' : {'St1': 0.063, 'St2': 0.935}
}
emit_p = {
  'St1' : {'a': 0.005, 'b': 0.775, 'c': 0.220},
   'St2' : {'a': 0.604, 'b': 0.277, 'c': 0.119}
}
observed_sequence = []
with open("../data/hmmdata.txt", "r") as f:
    header = next(f)
    assert (header.strip().split() == ["step", "state", "observation"])
    for line in f:
        splitted = line.strip().split()
        if len(splitted) > 2:
            # hidden_sequence.append(splitted[1])
            observed_sequence.append(splitted[2])
viterbi(observed_sequence, states, start_p, trans_p, emit_p)