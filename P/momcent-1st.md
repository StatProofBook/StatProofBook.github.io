---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-09-09 07:51:00

title: "First central moment is zero"
chapter: "General Theorems"
section: "Probability theory"
topic: "Further moments"
theorem: "First central moment is zero"

sources:
  - authors: "ProofWiki"
    year: 2020
    title: "First Central Moment is Zero"
    in: "ProofWiki"
    pages: "retrieved on 2020-09-09"
    url: "https://proofwiki.org/wiki/First_Central_Moment_is_Zero"

proof_id: "P167"
shortcut: "momcent-1st"
username: "JoramSoch"
---


**Theorem:** The first [central moment](/D/mom-cent) is zero, i.e.

$$ \label{eq:momcent-1st}
\mu_1 = 0 \; .
$$


**Proof:** The first [central moment](/D/mom-cent) of a [random variable](/D/rvar) $X$ with [mean](/D/mean) $\mu$ is defined as

$$ \label{eq:momcent-1st-def}
\mu_1 = \mathrm{E}\left[ (X-\mu)^1 \right] \; .
$$

Due to the [linearity of the expected value](/P/mean-lin) and by plugging in $\mu = \mathrm{E}(X)$, we have

$$ \label{eq:momcent-1st-qed}
\begin{split}
\mu_1 &= \mathrm{E}\left[ X-\mu \right] \\
&= \mathrm{E}(X) - \mu \\
&= \mathrm{E}(X) - \mathrm{E}(X) \\
&= 0 \; .
\end{split}
$$