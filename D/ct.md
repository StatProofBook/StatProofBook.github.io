---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-09-18 09:51:07

title: "General contingency table"
chapter: "Statistical Models"
section: "Count data"
topic: "General contingency table"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2026
    title: "Contingency table"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2026-09-18"
    url: "https://en.wikipedia.org/wiki/Contingency_table#Example"

def_id: "D242"
shortcut: "ct"
username: "JoramSoch"
---


**Definition:** Let $A$ and $B$ be [categorical random variables](/D/cat) with their possible values denoted by [random events](/D/reve) $A_1, \ldots, A_k$ and $B_1, \ldots, B_l$, respectively. Then, (i) the set of relative frequencies of $A$'s and $B$'s outcomes' occurences or (ii) the set of absolute frequencies of all combinations of $A_1, \ldots, A_k$ and $B_1, \ldots, B_l$ in a [sample](/D/samp) is referred to as a contingency table.

[Observed data](/D/data) from a $k \times l$ contingency table are characterized as follows:

* $y_{ij}$ for $i \in \left\lbrace 1,\ldots,k \right\rbrace$ and $j \in \left\lbrace 1,\ldots,l \right\rbrace$ is the number of cases in which $A_i$ and $B_j$;

* $y_{i \bullet} = \sum_{j=1}^l y_{ij}$ is the (marginal total) number of cases in which $A_i$;

* $y_{\bullet j} = \sum_{i=1}^k y_{ij}$ is the (marginal total) number of cases in which $B_j$;

* $n = \sum_{i=1}^k \sum_{j=1}^l y_{ij}$ is the [total number of cases](/D/samp-size).

[The distribution](/D/dist) underlying a $k \times l$ contingency table is characterized as follows:

* $p_{ij}$ for $i \in \left\lbrace 1,\ldots,k \right\rbrace$ and $j \in \left\lbrace 1,\ldots,l \right\rbrace$ is the [joint probability](/D/prob-joint) that $A_i$ and $B_j$;

* $p_{i \bullet}$ is the [marginal probability](/D/prob-marg) that $A_i$;

* $p_{\bullet j}$ is the marginal probability that $B_j$;

* $1 = \sum_{i=1}^k \sum_{j=1}^l p_{ij}$ is the [probability of the sample space](/D/prob-ax).