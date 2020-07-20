# `POS Tagging in Hindi Document`
Identification of Parts Of Speech  From Hindi Document

[![made-with-python](https://img.shields.io/badge/Made%20With-Python-red?style=for-the-badge&logo=Python)](https://www.python.org/)

## Dataset
We have obtained the source dataset containing Hindi Sentences with tagged POS from Hindi (Original) sections of the universal dependencies corpus. 
The source corpora, documentation, and credits can be found at http://universaldependencies.org

-------------------------------------------------

## Steps in POS Tagging
- Obtain a tagged data set for Training
- Using Hidden Markov Model to identify Transmission and Emission Probabilities
- Apply Viterbi Algorithm on Testing Data Set
- Output the tagging sequence with the highest probability

-------------------------------------------------

## How it works
### Hidden Markov Model

- **Hidden Markov Model** can be defined using a finite set of states. (Here states can be noun(N), verb(V), adjective(A), adverb(AD) etc )
- A sequence of observations. (terminals i.e the words in our sentence)
- **Transition probability** defined as the probability of a state “s” appearing right after observing “u” and “v” in the sequence of observations.
- **Emission probability** defined as the probability of making an observation x given that the state was s.

### Viterbi Algorithm
Instead of this brute force approach, we will see that we can find the highest probable tag sequence efficiently using a dynamic programming algorithm known as the Viterbi Algorithm.

![Viterbi Algorithm](https://github.com/gayatri-01/POS-Tagging-in-Hindi-Marathi-Document/blob/master/images/image1.jpeg)

### Model

![HMM model](https://github.com/gayatri-01/POS-Tagging-in-Hindi-Marathi-Document/blob/master/images/model.jpeg)

### Output

![Output](https://github.com/gayatri-01/POS-Tagging-in-Hindi-Marathi-Document/blob/master/images/output.jpeg)


### Youtube Video Link : https://www.youtube.com/watch?v=YvmV7AwOv4o
