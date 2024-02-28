---
layout: definition
mathjax: true

author: "Karahan Sarıtaş"
affiliation: "University of Tübingen"
e_mail: "karahan.saritas@student.uni-tuebingen.de"
date: 2024-02-28 20:50:00

title: "Log Scoring rule"
chapter: "General Theorems"
section: "Probability theory"
topic: "Decision Theory"
definition: "Log Probability Scoring rule"

sources:
  - authors: "Bálint Mucsányi, Michael Kirchhof, Elisa Nguyen, Alexander Rubinstein, Seong Joon Oh"
    year: 2023
    title: "Proper/Strictly Proper Scoring Rule"
    in: "Trustworthy Machine Learning"
    url: "https://trustworthyml.io/"
    doi: " 10.48550/arXiv.2310.08215"

def_id: "D195"
shortcut: "spsr"
username: "KarahanS"
---


**Definition:** Log (probability) [scoring rule](/D/sr) can be defined as a scoring rule that measures the quality of a probabilistic forecast in decision theory. Formally, it can be defined in discrete or continuous form as follows:

* **Log Scoring Rule for Binary Classification**:

$$ % \label{eq:binary-lsr-case}
S(q, y) = \begin{cases} \log q \;\;\;\;\;\;\;\;\;\;\;\;\text{if}\; y = 1 \\ \log(1-q) \;\;\;\; \text{if} \; y = 0 \end{cases} $$

which can be expressed as,

$$ \label{eq:binary-lsr}
S(q, y) = y \log q + (1-y) \log (1-q)$$

However, it is important to notice that the expressions given above have slightly different domains. For the first equation, the domain is $D_1 = ([0,1) \times \{0\}) \cup ((0, 1] \times \{1\}) $, while for the second equation, the domain is $D_2 = (0,1) \times \{0,1\} $.
* **Log Scoring Rule for Multiclass Classification**:

$$ \label{eq:multiclass-lsr}
S(q, y) = \sum_k y_k \log q_k(x) = \log q_{y^*}(x) $$
where $y^*$ is the true class and $q$ is the predicted probability distribution over the classes. $y_k = 1$ if the true class is $k$ and $0$ otherwise.

* **Log Scoring Rule for Regression (Continuous Case)**:
$$ \label{eq:regression-lsr}
S(q, y) = \log q(y) $$

where $q$ is the predicted probability distribution over the continuous space and $y$ is the true value.
$$
