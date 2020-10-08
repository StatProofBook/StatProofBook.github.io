---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-08 04:19:00

title: "First raw moment is mean"
chapter: "General Theorems"
section: "Probability theory"
topic: "Further moments"
theorem: "First raw moment is mean"

sources:

proof_id: "P171"
shortcut: "momraw-1st"
username: "JoramSoch"
---


**Theorem:** The first [raw moment](/D/mom-raw) equals the [mean](/D/mean), i.e.

$$ \label{eq:momraw-1st}
\mu_1' = \mu \; .
$$


**Proof:** The first [raw moment](/D/mom-raw) of a [random variable](/D/rvar) $X$ is defined as

$$ \label{eq:momraw-1st-def}
\mu_1' = \mathrm{E}\left[ (X-0)^1 \right]
$$

which is equal to the [expected value](/D/mean) of $X$:

$$ \label{eq:momraw-1st-qed}
\mu_1' = \mathrm{E}\left[ X \right] = \mu \; .
$$