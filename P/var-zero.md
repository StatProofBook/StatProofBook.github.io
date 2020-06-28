---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-06-27 07:05:00

title: "Variance zero implies constant"
chapter: "General Theorems"
section: "Probability theory"
topic: "Variance"
theorem: "Variance equals zero"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-06-27"
    url: "https://en.wikipedia.org/wiki/Variance#Basic_properties"

proof_id: "P125"
shortcut: "var-zero"
username: "JoramSoch"
---


**Theorem:** If the [variance](/D/var) of $X$ is zero, then $X$ is a [constant](/D/const):

$$ \label{eq:var-zero}
\mathrm{Var}(X) = 0 \quad \Rightarrow \quad X = \text{const.}
$$


**Proof:** The [variance](/D/var) is defined as

$$ \label{eq:var}
\mathrm{Var}(X) = \mathrm{E}\left[ (X-\mathrm{E}(X))^2 \right] \; .
$$

Because $(X-\mathrm{E}(X))^2$ is [strictly non-negative](/P/mean-nonneg), the only way for the variance to become zero is, if the squared deviation is always zero:

$$ \label{eq:sqr-dev-zero}
(X-\mathrm{E}(X))^2 = 0 \; .
$$

Thus, in turn, requires that $X$ is equal to its [expected value](/D/mean)

$$ \label{eq:X-eq-E-X}
X = \mathrm{E}(X)
$$

which can only be the case, if $X$ [always has the same value](/D/const):

$$ \label{eq:X-const}
X = \text{const.}
$$
