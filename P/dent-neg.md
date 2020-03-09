---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-02 20:32:00

title: "Differential entropy can be negative"
chapter: "General Theorems"
section: "Information theory"
topic: "Differential entropy"
theorem: "Negativity"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Differential entropy"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-02"
    url: "https://en.wikipedia.org/wiki/Differential_entropy#Definition"

proof_id: "P68"
shortcut: "dent-neg"
username: "JoramSoch"
---


**Theorem:** [Unlike its discrete analogue](/P/ent-nonneg), the [differential entropy](/D/dent) can become negative.


**Proof:** Let $X$ be a [random variable](/D/rvar) following a [continuous uniform distribution](/D/cuni) with minimum $0$ and maximum $1/2$:

$$ \label{eq:X}
X \sim \mathcal{U}(0, 1/2) \; .
$$

Then, its [probability density function](/P/cuni-pdf) is:

$$ \label{eq:X-pdf}
f_X(x) = 2 \quad \text{for} \quad 0 \leq x \leq \frac{1}{2} \; .
$$

Thus, the [differential entropy](/D/dent) follows as

$$ \label{eq:X-dent}
\begin{split}
\mathrm{h}(X) &= - \int_{\mathcal{X}} f_X(x) \log_b f_X(x) \, \mathrm{d}x \\
&= - \int_{0}^{\frac{1}{2}} 2 \, \log_b(2) \, \mathrm{d}x \\
&= -\log_b(2) \int_{0}^{\frac{1}{2}} 2 \, \mathrm{d}x \\
&= -\log_b(2) \left[ 2x \right]_{0}^{\frac{1}{2}} \\
&= -\log_b(2)
\end{split}
$$

which is negative for any base $b > 1$.