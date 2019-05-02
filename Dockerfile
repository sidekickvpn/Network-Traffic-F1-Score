FROM ubuntu:16.04

RUN apt-get update
RUN apt-get -y install \
	python \
	python-scapy \
	python-sklearn

ADD Negative /Negative
ADD Positive /Positive
ADD autotrain_filter.py /
ADD NBurstLearning.py /

CMD bash
