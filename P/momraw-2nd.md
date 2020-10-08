---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-08 05:05:00

title: "Relationship between second raw moment, variance and mean"
chapter: "General Theorems"
section: "Probability theory"
topic: "Further moments"
theorem: "Second raw moment and variance"

sources:

proof_id: "P172"
shortcut: "momraw-2nd"
username: "JoramSoch"
---


**Theorem:** The second [raw moment](/D/mom-raw) can be expressed as

$$ \label{eq:momraw-2nd}
\mu_2' = \mathrm{Var}(X) + \mathrm{E}(X)^2
$$

where $\mathrm{Var}(X)$ is the [variance](/D/var) of $X$ and $\mathrm{E}(X)$ is the [expected value](/D/mean) of $X$.


**Proof:** The second [raw moment](/D/mom-raw) of a [random variable](/D/rvar) $X$ is defined as

$$ \label{eq:momraw-2nd-def}
\mu_2' = \mathrm{E}\left[ (X-0)^2 \right] \; .
$$

Using the [partition of variance into expected values](/P/var-mean)

$$ \label{eq:var-mean}
\mathrm{Var}(X) = \mathrm{E}(X^2) - \mathrm{E}(X)^2 \; ,
$$

the second raw moment can be rearranged into:

$$ \label{eq:momraw-2nd-qed}
\mu_2' \overset{\eqref{eq:momraw-2nd-def}}{=} \mathrm{E}(X^2) \overset{\eqref{eq:var-mean}}{=} \mathrm{Var}(X) + \mathrm{E}(X)^2 \; .
$$