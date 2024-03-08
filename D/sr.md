---
layout: definition
mathjax: true

author: "Karahan Sarıtaş"
affiliation: "University of Tübingen"
e_mail: "karahan.saritas@student.uni-tuebingen.de"
date: 2024-02-28 20:50:00

title: "Scoring rule"
chapter: "General Theorems"
section: "Machine learning"
topic: "Scoring rules"
definition: "Scoring rule"

sources:
  - authors: "Bálint Mucsányi, Michael Kirchhof, Elisa Nguyen, Alexander Rubinstein, Seong Joon Oh"
    year: 2023
    title: "Proper/Strictly Proper Scoring Rule"
    in: "Trustworthy Machine Learning"
    url: "https://trustworthyml.io/"
    doi: "10.48550/arXiv.2310.08215"
  - authors: "Wikipedia"
    year: 2024
    title: "Scoring rule"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-02-28"
    url: "https://en.wikipedia.org/wiki/Scoring_rule"    

def_id: "D192"
shortcut: "sr"
username: "KarahanS"
---


**Definition:** A scoring rule is any extended real-valued function $\mathbf{S}: \mathcal{Q} \times \Omega \rightarrow \mathbb {R}$ where $\mathcal{Q}$ is a family of probability distributions over the space $\Omega$, such that $\mathbf{S}(Q, \cdot) $ is $\mathcal{Q}$-quasi-integrable for all $Q \in \mathcal{Q}$. Output of the function $\mathbf{S}(Q, y)$ represents the loss or penalty when the forecast $Q \in \mathcal{Q}$ is issued and the observation $y \in \Omega$ is realized.