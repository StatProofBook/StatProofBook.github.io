---
layout: definition
mathjax: true

author: "Karahan Sarıtaş"
affiliation: "University of Tübingen"
e_mail: "karahan.saritas@student.uni-tuebingen.de"
date: 2024-02-28 20:50:00

title: "Log probability scoring rule"
chapter: "General Theorems"
section: "Probability theory"
topic: "Decision Theory"
definition: "Log probability scoring rule"

sources:
  - authors: "Bálint Mucsányi, Michael Kirchhof, Elisa Nguyen, Alexander Rubinstein, Seong Joon Oh"
    year: 2023
    title: "Proper/Strictly Proper Scoring Rule"
    in: "Trustworthy Machine Learning"
    url: "https://trustworthyml.io/"
    doi: "10.48550/arXiv.2310.08215"

def_id: "D195"
shortcut: "lpsr"
username: "KarahanS"
---


**Definition:** A log (probability) [scoring rule](/D/sr) $S(q, y)$ is as a scoring rule that measures the quality of a probabilistic forecast in decision theory. Formally, it can be defined in discrete or continuous form as follows:

1) Log scoring rule for binary classification:

$$ % \label{eq:binary-lpsr-cases}
S(q, y) = \left\{
\begin{array}{rl}
\log q \; , & \text{if} \; y = 1 \\
\log(1-q) \; , & \text{if} \; y = 0
\end{array}
\right.
$$

which can be expressed as

$$ \label{eq:binary-lpsr}
S(q, y) = y \log q + (1-y) \log (1-q)
$$

Note that the expressions given above have slightly different domains. For the first equation, the domain is $D_1 = ([0,1) \times \{0\}) \cup ((0, 1] \times \{1\})$, while for the second equation, the domain is $D_2 = (0,1) \times \left\{ 0,1 \right\}$.

2) Log scoring rule for multiclass classification:

$$ \label{eq:multiclass-lpsr}
S(q, y) = \sum_k y_k \log q_k(x) = \log q_{y^*}(x)
$$

where $y^*$ is the true class and $q$ is the predicted probability distribution over the classes. We have $y_k = 1$, if the true class is $k$ and $y_k = 0$ otherwise.

3) Log scoring rule for regression (continuous case):

$$ \label{eq:regression-lpsr}
S(q, y) = \log q(y)
$$

where $q$ is the predicted probability distribution over the continuous space and $y$ is the true value.