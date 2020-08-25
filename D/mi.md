---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-19 18:35:00

title: "Mutual information"
chapter: "General Theorems"
section: "Information theory"
topic: "Discrete mutual information"
definition: "Definition"

sources:
  - authors: "Cover TM, Thomas JA"
    year: 1991
    title: "Relative Entropy and Mutual Information"
    in: "Elements of Information Theory"
    pages: "ch. 2.3/8.5, p. 20/251"
    url: "https://www.wiley.com/en-us/Elements+of+Information+Theory%2C+2nd+Edition-p-9780471241959"

def_id: "D19"
shortcut: "mi"
username: "JoramSoch"
---


**Definition:**

1) The mutual information of two discrete [random variables](/D/rvar) $X$ and $Y$ is defined as

$$ \label{eq:mi-disc}
\mathrm{I}(X,Y) = - \sum_{x \in \mathcal{X}} \sum_{x \in \mathcal{Y}} p(x,y) \cdot \log \frac{p(x,y)}{p(x) \cdot p(y)}
$$

where $p(x)$ and $p(y)$ are the [probability mass functions](/D/pmf) of $X$ and $Y$ and $p(x,y)$ is the [joint probability](/D/prob-joint) mass function of $X$ and $Y$.

2) The mutual information of two continuous [random variables](/D/rvar) $X$ and $Y$ is defined as

$$ \label{eq:mi-cont}
\mathrm{I}(X,Y) = - \int_{\mathcal{X}} \int_{\mathcal{Y}} p(x,y) \cdot \log \frac{p(x,y)}{p(x) \cdot p(y)} \, \mathrm{d}y \, \mathrm{d}x
$$

where $p(x)$ and $p(y)$ are the [probability density functions](/D/pmf) of $X$ and $Y$ and $p(x,y)$ is the [joint probability](/D/prob-joint) density function of $X$ and $Y$.