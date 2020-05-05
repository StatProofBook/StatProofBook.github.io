---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-11 15:03:00

title: "Median of the exponential distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Exponential distribution"
theorem: "Median"

sources:

proof_id: "P49"
shortcut: "exp-med"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following an [exponential distribution](/D/exp):

$$ \label{eq:exp}
X \sim \mathrm{Exp}(\lambda) \; .
$$

Then, the [median](/D/med) of $X$ is

$$ \label{eq:exp-med}
\mathrm{median}(X) = \frac{\ln 2}{\lambda} \; .
$$


**Proof:** The [median](/D/med) is the value at which the [cumulative distribution function](/D/cdf) is $1/2$:

$$ \label{eq:median}
F_X(\mathrm{median}(X)) = \frac{1}{2} \; .
$$

The [cumulative distribution function of the exponential distribution](/P/exp-cdf) is

$$ \label{eq:exp-cdf}
F_X(x) = 1 - \exp[-\lambda x], \quad x \geq 0 \; .
$$

Thus, the inverse CDF is

$$ \label{eq:exp-cdf-inv}
x = -\frac{\ln(1-p)}{\lambda}
$$

and setting $p = 1/2$, we obtain:

$$ \label{eq:exp-med-qed}
\mathrm{median}(X) = -\frac{\ln(1-\frac{1}{2})}{\lambda} = \frac{\ln 2}{\lambda} \; .
$$