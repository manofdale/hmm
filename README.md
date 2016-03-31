# Hidden Markov Model and Viterbi Decoding

Data structures for HMM  and the Vterbi algorithm in Python. 

# Prediction
Viterbi decoding algorithm predicts the most probable sequence of hidden states given observations from hmmdata
The decoding accuracy is evaluated by using the true sequence of hidden states from hmmdata.

# Simulation (Emission)
Markov Model class has a simulate method that can be used to output a sequence of emissions. Sample output:

    (0, 'St1', 'b')
    ..
    (4, 'St1', 'c')
    (5, 'St1', 'b')
    ..
    (32, 'St2', 'a')
    (33, 'St2', 'a')
    (34, 'St2', 'b')
    (35, 'St2', 'b')
    (36, 'St1', 'b')
    ...

# Results

confusion matrix:

    St1	        St2
    212         6
    7           175
true positives:

    St1	        St2
    212.        175.
true negatives:

    St1	        St2
    175.        212.
false positives:

    St1	        St2
    7.          6.
false negatives:

    St1	        St2
    6.          7.
precision:

    St1	        St2
    0.96803653  0.96685083
recall:

    St1	        St2
    0.97247706  0.96153846
fscore:

    St1	        St2
    0.97025172  0.96418733
support:

    St1	        St2
    218         182
