---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-10 20:01:00

title: "Law of marginal probability"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability"
definition: "Marginal probability"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Marginal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-10"
    url: "https://en.wikipedia.org/wiki/Marginal_distribution#Definition"
  - authors: "Jason Browlee"
    year: 2019
    title: "A Gentle Introduction to Joint, Marginal, and Conditional Probability"
    in: "Machine Learning Mastery"
    pages: "retrieved on 2021-08-01"
    url: "https://machinelearningmastery.com/joint-marginal-and-conditional-probability-for-machine-learning/"

def_id: "D50"
shortcut: "prob-marg"
username: "JoramSoch"
---


**Definition:** (law of marginal probability, also called "sum rule") Let $A$ and $X$ be two arbitrary statements about [random variables](/D/rvar), such as statements about the presence or absence of an event or about the value of a scalar, vector or matrix. Furthermore, assume a [joint probability](/D/prob-joint) distribution $p(A,X)$. Then, $p(A)$ is called the marginal probability of $A$ and,

1) if $X$ is a [discrete](/D/rvar-disc) [random variable](/D/rvar) with domain $\mathcal{X}$, is given by

$$ \label{eq:prob-marg-disc}
p(A) = \sum_{x \in \mathcal{X}} p(A,x) \; ;
$$

2) if $X$ is a [continuous](/D/rvar-disc) [random variable](/D/rvar) with domain $\mathcal{X}$, is given by

$$ \label{eq:prob-marg-cont}
p(A) = \int_{\mathcal{X}} p(A,x) \, \mathrm{d}x \; .
$$