---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-13 20:14:00

title: "Non-negativity of the expected value"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Non-negativity"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Expected value"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-13"
    url: "https://en.wikipedia.org/wiki/Expected_value#Basic_properties"

proof_id: "P52"
shortcut: "mean-nonneg"
username: "JoramSoch"
---


**Theorem:** If a [random variable](/D/rvar) is strictly non-negative, its [expected value](/D/mean) is also non-negative, i.e.

$$ \label{eq:mean-nonneg}
\mathrm{E}(X) \geq 0, \quad \text{if} \quad X \geq 0 \; .
$$


**Proof:**

1) If $X \geq 0$ is a discrete random variable, then, because the [probability mass function](/D/pmf) is always non-negative, all the addends in

$$ \label{eq:mean-disc}
\mathrm{E}(X) = \sum_{x \in \mathcal{X}} x \cdot f_X(x)
$$

are non-negative, thus the entire sum must be non-negative.

<br>
2) If $X \geq 0$ is a continuous random variable, then, because the [probability density function](/D/pdf) is always non-negative, the integrand in

$$ \label{eq:mean-cont}
\mathrm{E}(X) = \int_{\mathcal{X}} x \cdot f_X(x) \, \mathrm{d}x
$$

is strictly non-negative, thus the term on the right-hand side is a Lebesgue integral, so that the result on the left-hand side must be non-negative.