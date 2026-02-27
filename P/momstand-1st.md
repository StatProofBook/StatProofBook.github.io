---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-02-27 11:43:40

title: "The first standardized moment equals zero"
chapter: "General Theorems"
section: "Probability theory"
topic: "Further moments"
theorem: "First standardized moment is zero"

sources:

proof_id: "P526"
shortcut: "momstand-1st"
username: "JoramSoch"
---


**Theorem:** The first [standardized moment](/D/mom-stand) is zero, i.e.

$$ \label{eq:momstand-1st}
\mu_1^{*} = 0 \; .
$$


**Proof:** The first [standardized moment](/D/mom-stand) of a [random variable](/D/rvar) $X$ with [expected value](/D/mean) $\mu$ and [standard deviation](/D/std) $\sigma$ is defined as

$$ \label{eq:momstand-1st-def}
\mu_1^{*} = \frac{\mathrm{E}[(X-\mu)^1]}{\sigma^1} \; .
$$

Due to the [linearity of the expected value](/P/mean-lin) and by plugging in $\mu = \mathrm{E}(X)$, we have

$$ \label{eq:momstand-1st-qed}
\begin{split}
   \mu_1^{*}
&= \frac{\mathrm{E}[X-\mu]}{\sigma} \\
&= \frac{\mathrm{E}(X) - \mu}{\sigma} \\
&= \frac{\mathrm{E}(X) - \mathrm{E}(X)}{\sigma} \\
&= 0 \; .
\end{split}
$$