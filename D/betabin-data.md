---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-20 08:20:00

title: "Beta-binomial data"
chapter: "Statistical Models"
section: "Frequency data"
topic: "Beta-binomial data"
definition: "Definition"

sources:

def_id: "D178"
shortcut: "betabin-data"
username: "JoramSoch"
---


**Definition:** Beta-binomial data are defined as a set of counts $y = \left\lbrace y_1, \ldots, y_N \right\rbrace$ with $y_i \in \mathbb{N}, \; i = 1,\ldots,N$, [independent and identically distributed](/D/iid) according to a [beta-binomial distribution](/D/betabin) with number of trials $n$ as well as shapes $\alpha$ and $\beta$:

$$ \label{eq:betabin-data}
y_i \sim \mathrm{BetBin}(n,\alpha,\beta), \quad i = 1, \ldots, N \; .
$$