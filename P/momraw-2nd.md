---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-08 05:05:00

title: "The second raw moment equals squared mean plus squared standard deviation"
chapter: "General Theorems"
section: "Probability theory"
topic: "Further moments"
theorem: "Second raw moment as sum of squares"

sources:

proof_id: "P172"
shortcut: "momraw-2nd"
username: "JoramSoch"
---


**Theorem:** The second [raw moment](/D/mom-raw) can be expressed as the sum of squared [expected value](/D/mean) and squared [standard deviation](/D/std), i.e.

$$ \label{eq:momraw-2nd}
\mu_2' = \mathrm{E}(X)^2 + \sigma(X)^2 \; .
$$


**Proof:** The second [raw moment](/D/mom-raw) of a [random variable](/D/rvar) $X$ is defined as

$$ \label{eq:momraw-2nd-def}
\mu_2' = \mathrm{E}\left[ (X-0)^2 \right] \; .
$$

Using the [partition of variance into expected values](/P/var-mean)

$$ \label{eq:var-mean}
\mathrm{Var}(X) = \mathrm{E}(X^2) - \mathrm{E}(X)^2
$$

and the [relationship between standard deviation and variance](/D/std)

$$ \label{eq:std-var}
\sigma(X) = \sqrt{\mathrm{Var}(X)} \; ,
$$

the second raw moment can be rearranged into:

$$ \label{eq:momraw-2nd-qed}
\begin{split}
\mu_2'
&\overset{\eqref{eq:momraw-2nd-def}}{=} \mathrm{E}(X^2) \\
&\overset{\eqref{eq:var-mean}}{=} \mathrm{Var}(X) +  \\
&= \mathrm{E}(X)^2 + \sigma(X)^2 \; .
\end{split}
$$