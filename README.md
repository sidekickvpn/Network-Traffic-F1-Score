# Network-Traffic-F1-Score

Returns the F1 measurement of how well an event can be detected from a stream of network activity.

Building
--------

```bash
docker build -t network-traffic-learning .
```

Running
-------

- Start the container

```bash
docker run --rm --network none -it network-traffic-learning
```

- Then, from inside the container:

```
python autotrain_filter.py <CLIENT IP ADDRESS> <TRAINING THRESHOLD (between 0.00 and 1.00)> <TREE for decision tree classifier, anything else for Naive Bayes>
```
