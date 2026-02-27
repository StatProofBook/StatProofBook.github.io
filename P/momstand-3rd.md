---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-02-27 11:52:31

title: "The third standardized moment equals the skewness"
chapter: "General Theorems"
section: "Probability theory"
topic: "Further moments"
theorem: "Third standardized moment is skewness"

sources:

proof_id: "P528"
shortcut: "momstand-3rd"
username: "JoramSoch"
---


**Theorem:** The third [standardized moment](/D/mom-stand) equals the [skewness](/D/skew), i.e.

$$ \label{eq:momstand-3rd}
\mu_3^{*} = \mathrm{Skew}(X) \; .
$$


**Proof:** The third [standardized moment](/D/mom-stand) of a [random variable](/D/rvar) $X$ with [expected value](/D/mean) $\mu$ and [standard deviation](/D/std) $\sigma$ is defined as

$$ \label{eq:momstand-3rd-def}
\mu_3^{*} = \frac{\mathrm{E}[(X-\mu)^3]}{\sigma^3}
$$

which is equivalent to the [definition of the skewness](/D/skew):

$$ \label{eq:momstand-3rd-qed}
\mu_3^{*} = \mathrm{Skew}(X) \; .
$$