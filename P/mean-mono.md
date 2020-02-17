---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-17 21:00:00

title: "Monotonicity of the expected value"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Monotonicity"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Expected value"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-02-17"
    url: "https://en.wikipedia.org/wiki/Expected_value#Basic_properties"

proof_id: "P54"
shortcut: "mean-mono"
username: "JoramSoch"
---


**Theorem:** The [expected value](/D/mean) is monotonic, i.e.

$$ \label{eq:mean-mono}
\mathrm{E}(X) \leq \mathrm{E}(Y), \quad \text{if} \quad X \leq Y \; .
$$


**Proof:** Let $Z = Y - X$. Due to the [linearity of the expected value](/P/mean-lin), we have

$$ \label{eq:mean-XYZ}
\mathrm{E}(Z) = \mathrm{E}(Y-X) = \mathrm{E}(Y) - \mathrm{E}(X) \; .
$$

With the [non-negativity property of the expected value](/P/mean-nonneg), it also holds that

$$ \label{eq:mean-Z}
Z \geq 0 \quad \Rightarrow \quad \mathrm{E}(Z) \geq 0 \; .
$$

Together with \eqref{eq:mean-XYZ}, this yields

$$ \label{eq:mean-mono-qed}
\mathrm{E}(Y) - \mathrm{E}(X) \geq 0 \; .
$$