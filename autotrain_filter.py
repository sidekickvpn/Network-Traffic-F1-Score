#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pickle

from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score

from scapy.all import *
from NBurstLearning import NBurst_Detector, AutoN

#CLIENT_IP = "172.17.0.2"
#CLIENT_IP = "172.19.0.2"
CLIENT_IP = sys.argv[1]
TRAINING_F_THRESH = float(sys.argv[2])
CLF_TYPE = sys.argv[3]


OBJ_MAX_SIZE = 15000
PICKLE_FILENAME = "trained_classifier.pickle"
POSITIVE_SAMPLES = ["Positive/001.pcap", "Positive/002.pcap", "Positive/003.pcap", "Positive/004.pcap", "Positive/005.pcap", "Positive/006.pcap", "Positive/007.pcap", "Positive/008.pcap"]
NEGATIVE_SAMPLES = ["Negative/001.pcap", "Negative/002.pcap", "Negative/003.pcap", "Negative/004.pcap", "Negative/005.pcap", "Negative/006.pcap", "Negative/007.pcap", "Negative/008.pcap"]

def pcap_transform(sample_set, n):
	nburst_category = []
	for samp in sample_set:
		cap = rdpcap(samp)
		nbt = NBurst_Detector(n)
		these_samples = []
		for pkt in cap:
			if pkt.haslayer(TCP):
				if pkt[IP].dst == CLIENT_IP:
					res = nbt.add_event(len(pkt[TCP]))
					if res is not None:
						these_samples.append({"time": pkt.time, "size": res})
		#Fixup times
		if len(these_samples) > 0:
			initial_time = these_samples[0]['time']
			for i in range(len(these_samples)):
				these_samples[i]['time'] = these_samples[i]['time'] - initial_time
			
			nburst_category.append(these_samples)
	
	return nburst_category

"""
Example: sliding_window_transform([1,2,3,4,5,6,7,8], 3) ==> [[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7], [6,7,8]]
"""
def sliding_window_transform(data, winsize):
	windows = []
	for i in range(0, len(data)):
		this_win = data[i:i+winsize]
		if len(this_win) == winsize:
			windows.append(this_win)
	
	return windows

"""
Example: [[{'time': 0.11, 'size': 32}], [{'time': 0.15, 'size': 43}]] ==> [[32], [43]]
"""
def convert_winlist_sizeonly(winlist):
	converted_winlist = []
	for win in winlist:
		vect = []
		for comp in win:
			vect.append(comp['size'])
		converted_winlist.append(vect)
	
	return converted_winlist

def histogram_transform(values, low_end, high_end):
	hist = []
	for i in range(low_end, high_end):
		hist.append(values.count(i))
	return hist

def list_histogram_transform(input_list, low_end, high_end):
	out_hist = []
	for lst in input_list:
		out_hist.append(histogram_transform(lst, low_end, high_end))
	return out_hist

#Get the best value for N from the POSITIVE_SAMPLES
auto_n = AutoN()
best_n = 0
for ps in POSITIVE_SAMPLES:
	cap = rdpcap(ps)
	for pkt in cap:
		if pkt.haslayer(TCP):
			if pkt[IP].dst == CLIENT_IP:
				best_n = auto_n.add_event(len(pkt[TCP]))

#Transform the POSITIVE_SAMPLES to list of NBursts
nburst_positive = pcap_transform(POSITIVE_SAMPLES, best_n)
nburst_negative = pcap_transform(NEGATIVE_SAMPLES, best_n)

#Do some pretty printing for debugging purposes
print "Positive Samples"
print "----------------"
for smp in nburst_positive:
	print ""
	for evt in smp:
		print "{}:\t{}".format(evt['time'], evt['size'])

print ""

print "Negative Samples"
print "----------------"
for smp in nburst_negative:
	print ""
	for evt in smp:
		print "{}:\t{}".format(evt['time'], evt['size'])


#Split into training/testing sets (50% / 50%)
train_pos = nburst_positive[0:len(nburst_positive)/2]
test_pos = nburst_positive[len(nburst_positive)/2:]
train_neg = nburst_negative[0:len(nburst_negative)/2]
test_neg = nburst_negative[len(nburst_negative)/2:]

#Try different window sizes
minsize = None
for smp in nburst_negative + nburst_positive:
	if minsize is None:
		minsize = smp
	
	if len(smp) < minsize:
		minsize = len(smp)


optimal_fscore = 0.0
optimal_winsize = None
optimal_clf = None
for ws in range(1, minsize+1):
	print "Testing with a window size of {} objects.".format(ws)
	sklearn_train_pos = []
	sklearn_train_neg = []
	for smp in train_pos:
		this_win = sliding_window_transform(smp, ws)
		converted_win = list_histogram_transform(convert_winlist_sizeonly(this_win), 0, OBJ_MAX_SIZE)
		for gram in converted_win:
			sklearn_train_pos.append(gram)
		
	for smp in train_neg:
		this_win = sliding_window_transform(smp, ws)
		converted_win = list_histogram_transform(convert_winlist_sizeonly(this_win), 0, OBJ_MAX_SIZE)
		for gram in converted_win:
			sklearn_train_neg.append(gram)
	
	#print "\tPositive training: {}".format(sklearn_train_pos)
	#print "\tNegative training: {}".format(sklearn_train_neg)
	
	if CLF_TYPE == "TREE":
		clf = tree.DecisionTreeClassifier()
	else:
		clf = GaussianNB()
	
	clf.fit(sklearn_train_pos + sklearn_train_neg, [True]*len(sklearn_train_pos) + [False]*len(sklearn_train_neg))
	predicted = clf.predict(sklearn_train_pos + sklearn_train_neg)
	performance = f1_score([True]*len(sklearn_train_pos) + [False]*len(sklearn_train_neg), predicted)
	print "\tF1: {}".format(performance)
	if performance > optimal_fscore:
		optimal_fscore = performance
		optimal_winsize = ws
		optimal_clf = clf
	
	#Have we already found an acceptable classifier?
	if performance >= TRAINING_F_THRESH:
		break

if optimal_winsize is None:
	print "Could not find an optimal sliding window size."
	sys.exit(-1)


#Transform the testing data according to the optimized winsize
sklearn_test_pos = []
sklearn_test_neg = []

for smp in test_pos:
	this_win = sliding_window_transform(smp, optimal_winsize)
	converted_win = list_histogram_transform(convert_winlist_sizeonly(this_win), 0, OBJ_MAX_SIZE)
	for gram in converted_win:
		sklearn_test_pos.append(gram)
	
for smp in test_neg:
	this_win = sliding_window_transform(smp, optimal_winsize)
	converted_win = list_histogram_transform(convert_winlist_sizeonly(this_win), 0, OBJ_MAX_SIZE)
	for gram in converted_win:
		sklearn_test_neg.append(gram)

#Evaluate!
test_prediected = optimal_clf.predict(sklearn_test_pos + sklearn_test_neg)
overall_performance = f1_score([True]*len(sklearn_test_pos) + [False]*len(sklearn_test_neg), test_prediected)

#print "\tPositive testing: {}".format(sklearn_test_pos)
#print "\tNegative testing: {}".format(sklearn_test_neg)

print "The side-channel vulnerability rating for this scenario is {}.".format(overall_performance)

f_pickle = open(PICKLE_FILENAME, 'w')
f_pickle.write(pickle.dumps(optimal_clf))
f_pickle.close()

print "Saved the trained classifier for this scenario to: {}".format(PICKLE_FILENAME)
print "Use with N={}, WINSIZE={}.".format(best_n, optimal_winsize)
print "Done."
