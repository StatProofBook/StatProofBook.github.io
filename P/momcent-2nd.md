---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-08 05:13:00

title: "Second central moment is variance"
chapter: "General Theorems"
section: "Probability theory"
topic: "Further moments"
theorem: "Second central moment is variance"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Moment (mathematics)"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-10-08"
    url: "https://en.wikipedia.org/wiki/Moment_(mathematics)#Significance_of_the_moments"

proof_id: "P173"
shortcut: "momcent-2nd"
username: "JoramSoch"
---


**Theorem:** The second [central moment](/D/mom-cent) equals the [variance](/D/var), i.e.

$$ \label{eq:momcent-2nd}
\mu_2 = \mathrm{Var}(X) \; .
$$


**Proof:** The second [central moment](/D/mom-cent) of a [random variable](/D/rvar) $X$ with [mean](/D/mean) $\mu$ is defined as

$$ \label{eq:momcent-2nd-def}
\mu_2 = \mathrm{E}\left[ (X-\mu)^2 \right]
$$

which is equivalent to the [definition of the variance](/D/var):

$$ \label{eq:momraw-1st-qed}
\mu_2 = \mathrm{E}\left[ (X - \mathrm{E}(X))^2 \right] = \mathrm{Var}(X) \; .
$$