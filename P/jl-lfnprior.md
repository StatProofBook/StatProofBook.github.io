---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-05 04:21:00

title: "Joint likelihood is the product of likelihood function and prior density"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
theorem: "Joint likelihood is product of likelihood and prior"

sources:

proof_id: "P89"
shortcut: "jl-lfnprior"
username: "JoramSoch"
---


**Theorem:** Let there be a [generative model](/D/gm) $m$ describing measured data $y$ using model parameters $\theta$ and a [prior distribution](/D/prior) on $\theta$. Then, the [joint likelihood](/D/jl) is equal to the product of [likelihood function](/D/lf) and [prior density](/D/prior):

$$ \label{eq:jl}
p(y,\theta|m) = p(y|\theta,m) \, p(\theta|m) \; .
$$


**Proof:** The [joint likelihood](/D/jl) is defined as the [joint probability](/D/prob-joint) [density function](/D/pdf) of data $y$ and parameters $\theta$:

$$ \label{eq:jl-def}
p(y,\theta|m) \; .
$$

Applying the [law of conditional probability](/D/prob-cond), we have:

$$ \label{eq:jl-qed}
\begin{split}
p(y|\theta,m) &= \frac{p(y,\theta|m)}{p(\theta|m)} \\
&\Leftrightarrow \\
p(y,\theta|m) &= p(y|\theta,m) \, p(\theta|m) \; .
\end{split}
$$