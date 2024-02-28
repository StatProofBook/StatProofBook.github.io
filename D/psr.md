---
layout: definition
mathjax: true

author: "Karahan Sarıtaş"
affiliation: "University of Tübingen"
e_mail: "karahan.saritas@student.uni-tuebingen.de"
date: 2024-02-28 20:50:00

title: "Proper Scoring rule"
chapter: "General Theorems"
section: "Probability theory"
topic: "Decision Theory"
definition: "Proper Scoring rule"

sources:
  - authors: "Bálint Mucsányi, Michael Kirchhof, Elisa Nguyen, Alexander Rubinstein, Seong Joon Oh"
    year: 2023
    title: "Proper/Strictly Proper Scoring Rule"
    in: "Trustworthy Machine Learning"
    url: "https://trustworthyml.io/"
    doi: " 10.48550/arXiv.2310.08215"

def_id: "D193"
shortcut: "psr"
username: "KarahanS"
---


**Definition:** A [scoring rule](/D/sr) $\mathbf{S}$ is called a _proper_ scoring rule if and only if 

$$
\max_{Q \in \mathcal{Q}} \mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] = \max_{Q \in \mathcal{Q}} \mathbb{E}_{Y \sim P}[\mathbf{S}(P, Y)]
$$
In other words, score function is a _proper_ scoring rule if it is maximized when the forecaster gives exactly the ground truth distribution $P(Y)$ as its probabilistic forecast $Q \in \mathcal{Q}$.
