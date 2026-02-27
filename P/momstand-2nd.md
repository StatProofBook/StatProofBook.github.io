---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-02-27 11:46:01

title: "The second standardized moment equals one"
chapter: "General Theorems"
section: "Probability theory"
topic: "Further moments"
theorem: "Second standardized moment is one"

sources:

proof_id: "P527"
shortcut: "momstand-2nd"
username: "JoramSoch"
---


**Theorem:** The second [standardized moment](/D/mom-stand) is zero, i.e.

$$ \label{eq:momstand-2nd}
\mu_2^{*} = 1 \; .
$$


**Proof:** The second [standardized moment](/D/mom-stand) of a [random variable](/D/rvar) $X$ with [expected value](/D/mean) $\mu$ and [standard deviation](/D/std) $\sigma$ is defined as

$$ \label{eq:momstand-2nd-def}
\mu_2^{*} = \frac{\mathrm{E}[(X-\mu)^2]}{\sigma^2} \; .
$$

By plugging in $\mu = \mathrm{E}(X)$ and with the definitions of [variance](/D/var) and [standard deviation](/D/std), we have

$$ \label{eq:momstand-2nd-qed}
\begin{split}
   \mu_2^{*}
&= \frac{\mathrm{E}\left[ (X-\mathrm{E}(X))^2 \right]}{\sigma^2} \\
&= \frac{\mathrm{Var}(X)}{\left( \sqrt{\mathrm{Var}(X)} \right)^2} \\
&= \frac{\mathrm{Var}(X)}{\mathrm{Var}(X)} \\
&= 1 \; .
\end{split}
$$