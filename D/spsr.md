---
layout: definition
mathjax: true

author: "Karahan Sarıtaş"
affiliation: "University of Tübingen"
e_mail: "karahan.saritas@student.uni-tuebingen.de"
date: 2024-02-28 20:50:00

title: "Strictly proper scoring rule"
chapter: "General Theorems"
section: "Machine learning"
topic: "Scoring rules"
definition: "Strictly proper scoring rule"

sources:
  - authors: "Bálint Mucsányi, Michael Kirchhof, Elisa Nguyen, Alexander Rubinstein, Seong Joon Oh"
    year: 2023
    title: "Proper/Strictly Proper Scoring Rule"
    in: "Trustworthy Machine Learning"
    url: "https://trustworthyml.io/"
    doi: "10.48550/arXiv.2310.08215"

def_id: "D194"
shortcut: "spsr"
username: "KarahanS"
---


**Definition:** A [scoring rule](/D/sr) $\mathbf{S}$ is called a strictly proper scoring rule, if and only if

* $\mathbf{S}$ is a [proper scoring rule](/D/psr), and

* $\operatorname*{arg\,max}\_{Q \in \mathcal{Q}} \mathbb{E}\_{Y \sim P}[\mathbf{S}(Q, Y)] = P$ is the unique maximizer of $\mathbf{S}$ in $Q$.

In other words, a strictly proper scoring rule is maximized only when the the forecaster gives exactly the ground truth distribution $P(Y)$ as its probabilistic forecast $Q \in \mathcal{Q}$.