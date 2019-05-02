FROM ubuntu:16.04

RUN apt-get update
RUN apt-get -y install \
	curl \
	tcpdump

RUN mkdir /Positive
RUN mkdir /Negative

ADD generate_data.sh /
RUN chmod +x /generate_data.sh

CMD bash
