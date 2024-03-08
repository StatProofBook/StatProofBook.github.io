---
layout: definition
mathjax: true

author: "Karahan Sarıtaş"
affiliation: "University of Tübingen"
e_mail: "karahan.saritas@student.uni-tuebingen.de"
date: 2024-02-28 20:50:00

title: "Proper scoring rule"
chapter: "General Theorems"
section: "Machine learning"
topic: "Scoring rules"
definition: "Proper scoring rule"

sources:
  - authors: "Bálint Mucsányi, Michael Kirchhof, Elisa Nguyen, Alexander Rubinstein, Seong Joon Oh"
    year: 2023
    title: "Proper/Strictly Proper Scoring Rule"
    in: "Trustworthy Machine Learning"
    url: "https://trustworthyml.io/"
    doi: "10.48550/arXiv.2310.08215"

def_id: "D193"
shortcut: "psr"
username: "KarahanS"
---


**Definition:** A [scoring rule](/D/sr) $\mathbf{S}$ is called a proper scoring rule, if and only if 

$$ \label{eq:psr}
\max_{Q \in \mathcal{Q}} \mathbb{E}_{Y \sim P}[\mathbf{S}(Q, Y)] =  \mathbb{E}_{Y \sim P}[\mathbf{S}(P, Y)] \; .
$$

In other words, score function $\mathbf{S}$ is a proper scoring rule, if it is maximized when the forecaster gives exactly the ground truth distribution $P(Y)$ as its probabilistic forecast $Q \in \mathcal{Q}$.