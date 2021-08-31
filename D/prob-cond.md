---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-10 20:06:00

title: "Law of conditional probability"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability"
definition: "Conditional probability"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Conditional probability"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-10"
    url: "https://en.wikipedia.org/wiki/Conditional_probability#Definition"
  - authors: "Jason Browlee"
    year: 2019
    title: "A Gentle Introduction to Joint, Marginal, and Conditional Probability"
    in: "Machine Learning Mastery"
    pages: "retrieved on 2021-08-01"
    url: "https://machinelearningmastery.com/joint-marginal-and-conditional-probability-for-machine-learning/"

def_id: "D51"
shortcut: "prob-cond"
username: "JoramSoch"
---


**Definition:** (law of conditional probability, also called "product rule") Let $A$ and $B$ be two arbitrary statements about [random variables](/D/rvar), such as statements about the presence or absence of an event or about the value of a scalar, vector or matrix. Furthermore, assume a [joint probability](/D/prob-joint) distribution $p(A,B)$. Then, $p(A \vert B)$ is called the conditional probability that $A$ is true, given that $B$ is true, and is given by

$$ \label{eq:prob-cond}
p(A|B) = \frac{p(A,B)}{p(B)}
$$

where $p(B)$ is the [marginal probability](/D/prob-marg) of $B$.