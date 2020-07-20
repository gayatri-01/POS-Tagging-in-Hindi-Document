import sys
import math
from decimal import *
import codecs

tag_list = set()
tag_count = {}
word_set = set()


def parse_traindata():
    fin = "train_data/train_data.txt"
    output_file = "model/hmmmodel.txt"
    wordtag_list = []

    try:
    	# read the training data file #
        input_file = codecs.open(fin, mode = 'r', encoding="utf-8")
        lines = input_file.readlines()
        # pushing words of a line into a list #
        for line in lines:
            line = line.strip('\n')
            data = line.split(" ")
            wordtag_list.append(data)

        input_file.close()
        return wordtag_list

    except IOError:
        fo = codecs.open(output_file,mode = 'w',encoding="utf-8")
        fo.write("File not found: {}".format(fin))
        fo.close()
        sys.exit()


def transition_count(train_data):
    global tag_list
    global word_set    
    transition_dict = {}
    global tag_count
    for value in train_data:
        previous = "start"
        for data in value:
        	# we store words and their corresponding tags #
            i = data[::-1]
            word = data[:-i.find("/") - 1]
            word_set.add(word.lower())
            data = data.split("/")
            tag = data[-1]
            tag_list.add(tag)

            # store frequency of each tag #

            if tag in tag_count:
                tag_count[tag] += 1
            else:
                tag_count[tag] = 1

            # store the frequency of each combination of tags #

            if (previous + "~tag~" + tag) in transition_dict:
                transition_dict[previous + "~tag~" + tag] += 1
                previous = tag
            else:
                transition_dict[previous + "~tag~" + tag] = 1
                previous = tag

    return transition_dict


def transition_probability(train_data):
    count_dict = transition_count(train_data)
    prob_dict = {}
    for key in count_dict:
        den = 0
        val = key.split("~tag~")[0]
        # Probabilty of a tagA to be followed by tagB out of all possible tags # 
        for key_2 in count_dict:
            if key_2.split("~tag~")[0] == val:
                den += count_dict[key_2]
        prob_dict[key] = Decimal(count_dict[key])/(den)
    return prob_dict


def transition_smoothing(train_data):
    transition_prob = transition_probability(train_data)
    for tag in tag_list:
    	# if a tag does not occur as a start tag, then set its probability to be a start tag to minimum value #
        if "start" + tag not in  transition_prob:
            transition_prob[("start" + "~tag~" + tag)] = Decimal(1) / Decimal(len(word_set) + tag_count[tag])
    for tag1 in tag_list:
        for tag2 in tag_list:
        	# if a particular tag combination does not exist in the dictionary, we set its probability to minimum#
            if (tag1 +"~tag~" + tag2) not in transition_prob:
                transition_prob[(tag1+"~tag~"+tag2)] = Decimal(1)/Decimal(len(word_set) + tag_count[tag1])
    return transition_prob


def emission_count(train_data):  
    count_word = {}
    for value in train_data:
        for data in value:
            i = data[::-1]
            word = data[:-i.find("/") - 1]
            tag = data.split("/")[-1]
            # map the words in the training set to their tagged POS #
            if word.lower() + "/" + tag in count_word:
                count_word[word.lower() + "/" + tag] +=1
            else:
                count_word[word.lower() + "/" + tag] = 1
    return count_word


def emission_probability(train_data):
    global tag_count
    word_count = emission_count(train_data)
    emission_prob_dict = {}
    # calculate probability of a word to be a certain Tag out of all the possible tags that it can be #
    for key in word_count:
        emission_prob_dict[key] = Decimal(word_count[key])/tag_count[key.split("/")[-1]]
    return emission_prob_dict



train_data = parse_traindata()
transition_model = transition_smoothing(train_data)
emission_model = emission_probability(train_data)

fout = codecs.open("model/hmmmodel.txt", mode ='w', encoding="utf-8")
for key, value in transition_model.items():
    fout.write('%s:%s\n' % (key, value))

fout.write(u'Emission Model\n')
for key, value in emission_model.items():
    fout.write('%s:%s\n' % (key, value))


