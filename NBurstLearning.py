#!/usr/bin/env python
# -*- coding: utf-8 -*-

class NBurst_Detector:
	def __init__(self, n_len):
		self.n = n_len
		self.running_counter = 0
	
	def add_event(self, evt):
		if evt == self.n:
			self.running_counter += self.n
		else:
			if self.running_counter == 0:
				return None
			else:
				ret = self.running_counter + evt
				self.running_counter = 0
				return ret
		return None

class AutoN:
	def __init__(self, ex_list=[]):
		self.freqs = [0]*1500
		self.exclusion_list = ex_list
	
	def add_event(self, evt):
		if evt in range(0, 1500):
			if evt not in self.exclusion_list:
				self.freqs[evt] = self.freqs[evt] + 1
		
		#Return the index of the maximum
		return self.freqs.index(max(self.freqs))

"""
def test_nburst_detector():
	nbt = NBurst_Detector(1370)
	input_data = [43, 54, 17, 1370, 1370, 121, 324, 1370, 1370, 1370, 12]
	expected_output = [2861, 4122]
	real_output = []
	for indata in input_data:
		filt_out = nbt.add_event(indata)
		if filt_out:
			real_output.append(filt_out)
	
	print "Expected: {}".format(expected_output)
	print "Got: {}".format(real_output)


def test_auto_nburst_detector():
	input_data = [43, 54, 17, 1370, 1370, 121, 324, 1370, 1370, 1370, 12]
	auto_n = AutoN()
	discovered_n = 0
	for indata in input_data:
		discovered_n = auto_n.add_event(indata)
	
	nbt = NBurst_Detector(discovered_n)
	expected_output = [2861, 4122]
	real_output = []
	for indata in input_data:
		filt_out = nbt.add_event(indata)
		if filt_out:
			real_output.append(filt_out)
	
	print "Expected: {}".format(expected_output)
	print "Got: {}".format(real_output)

print "Testing..."
print "----------"

test_nburst_detector()

print ""

test_auto_nburst_detector()
"""
