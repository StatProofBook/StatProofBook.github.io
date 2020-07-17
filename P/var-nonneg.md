---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-06-06 07:29:00

title: "Non-negativity of the variance"
chapter: "General Theorems"
section: "Probability theory"
topic: "Variance"
theorem: "Non-negativity"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-06-06"
    url: "https://en.wikipedia.org/wiki/Variance#Basic_properties"

proof_id: "P123"
shortcut: "var-nonneg"
username: "JoramSoch"
---


**Theorem:** The [variance](/D/var) is always non-negative, i.e.

$$ \label{eq:var-nonneg}
\mathrm{Var}(X) \geq 0 \; .
$$


**Proof:** The [variance](/D/var) of a [random variable](/D/rvar) is defined as

$$ \label{eq:var}
\mathrm{Var}(X) = \mathrm{E}\left[ (X-\mathrm{E}(X))^2 \right] \; .
$$

<br>
1) If $X$ is a discrete [random variable](/D/rvar), then, because squares and probabilities are stricly non-negative, all the addends in

$$ \label{eq:var-disc}
\mathrm{Var}(X) = \sum_{x \in \mathcal{X}} (x-\mathrm{E}(X))^2 \cdot f_X(x)
$$

are also non-negative, thus the entire sum must be non-negative.

<br>
2) If $X$ is a continuous [random variable](/D/rvar), then, because squares and probability densities are strictly non-negative, the integrand in

$$ \label{eq:var-cont}
\mathrm{Var}(X) = \int_{\mathcal{X}} (x-\mathrm{E}(X))^2 \cdot f_X(x) \, \mathrm{d}x
$$

is always non-negative, thus the term on the right-hand side is a Lebesgue integral, so that the result on the left-hand side must be non-negative.