---
layout: definition
mathjax: true

author: "Karahan Sarıtaş"
affiliation: "University of Tübingen"
e_mail: "karahan.saritas@student.uni-tuebingen.de"
date: 2024-03-23 20:50:00

title: "Brier scoring rule"
chapter: "General Theorems"
section: "Machine learning"
topic: "Scoring rules"
definition: "Brier scoring rule"

sources:
  - authors: "Bálint Mucsányi, Michael Kirchhof, Elisa Nguyen, Alexander Rubinstein, Seong Joon Oh"
    year: 2023
    title: "Proper/Strictly Proper Scoring Rule"
    in: "Trustworthy Machine Learning"
    url: "https://trustworthyml.io/"
    doi: "10.48550/arXiv.2310.08215"

def_id: "D197"
shortcut: "bsr"
username: "KarahanS"
---


**Definition:** A Brier [scoring rule](/D/sr) $S(q, y)$ is as a scoring rule that measures the quality of a probabilistic forecast in decision theory. Formally, it can be defined for binary or multiclass classification as follows:

1) Brier scoring rule for binary classification:

$$ \label{eq:binary-bsr}
S(q, y) = -(q - y)^2
$$

$q$ represents the predicted probability of the positive class ($Y = 1$) and $y$ is the true class label. Since we want the output of the scoring rule to be maximized when the predicted probability is close to the true class label, we use the negative of the squared difference between the predicted probability and the true class label.

2) Brier scoring rule for multiclass classification:

$$ \label{eq:multiclass-bsr}
S(q, y) = -\sum_k (q_k - y_k)^2 = -(q_{y^*} - 1)^2 -\sum_{k \neq y^*} q_k^2
$$

where $q_k$ is the predicted probability of class $k$ and $y^*$ is the true class label. Similar to the log probability scoring rule, we have $y_k = 1$, if the true class is $k$ and $y_k = 0$ otherwise.

3) Regression (continuous case):

Although there is no direct version of Brier score for regression, we can use the squared error loss as a scoring rule for regression problems as well.