---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-09-11 09:58:43

title: "Binary contingency table"
chapter: "Statistical Models"
section: "Count data"
topic: "Binary contingency table"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2026
    title: "Contingency table"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2026-09-11"
    url: "https://en.wikipedia.org/wiki/Contingency_table#Example"

def_id: "D239"
shortcut: "ct2x2"
username: "JoramSoch"
---


**Definition:** Let $A$ and $B$ be [random events](/D/reve) and let $\overline{A}$ and $\overline{B}$ denote their [complements](/D/reve). Then, (i) the set of relative frequencies of $A$'s and $B$'s occurence or (ii) the set of absolute frequencies of the combinations of $A$/$\overline{A}$ and $B$/$\overline{B}$ in a [sample](/D/samp) is referred to as a $2 \times 2$ contingency table.

[Observed data](/D/data) from a $2 \times 2$ contingency table are characterized as follows:

* $y_1 = y_{11}$ is the number of cases in which $A$ and $B$;

* $y_2 = y_{10}$ is the number of cases in which $A$ and $\overline{B}$;

* $y_3 = y_{01}$ is the number of cases in which $\overline{A}$ and $B$;

* $y_4 = y_{00}$ is the number of cases in which $\overline{A}$ and $\overline{B}$;

* $y_{1 \bullet} = y_{11} + y_{10}$ is the (marginal total) number of cases in which $A$;

* $y_{0 \bullet} = y_{01} + y_{00}$ is the (marginal total) number of cases in which $\overline{A}$;

* $y_{\bullet 1} = y_{11} + y_{01}$ is the (marginal total) number of cases in which $B$;

* $y_{\bullet 0} = y_{10} + y_{00}$ is the (marginal total) number of cases in which $\overline{B}$;

* $n = y_{11} + y_{10} + y_{01} + y_{00}$ is the [total number of cases](/D/samp-size).

[The distribution](/D/dist) underlying a $2 \times 2$ contingency table is characterized as follows:

* $p_1 = p_{11}$ is the [joint probability](/D/prob-joint) that $A$ and $B$;

* $p_2 = p_{10}$ is the probability that $A$ and $\overline{B}$;

* $p_3 = p_{01}$ is the probability that $\overline{A}$ and $B$;

* $p_4 = p_{00}$ is the probability that $\overline{A}$ and $\overline{B}$;

* $p_{1 \bullet} = p_{11} + p_{10}$ is the [marginal probability](/D/prob-marg) that $A$;

* $p_{0 \bullet} = p_{01} + p_{00}$ is the marginal probability that $\overline{A}$;

* $p_{\bullet 1} = p_{11} + p_{01}$ is the marginal probability that $B$;

* $p_{\bullet 0} = p_{10} + p_{00}$ is the marginal probability that $\overline{B}$;

* $1 = p_{11} + p_{10} + p_{01} + p_{00}$ is the [probability of the sample space](/D/prob-ax).