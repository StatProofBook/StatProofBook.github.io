---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-07 05:23:00

title: "Invariance of the variance under addition of a constant"
chapter: "General Theorems"
section: "Probability theory"
topic: "Variance"
theorem: "Invariance under addition"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-07-07"
    url: "https://en.wikipedia.org/wiki/Variance#Basic_properties"

proof_id: "P126"
shortcut: "var-inv"
username: "JoramSoch"
---


**Theorem:** The [variance](/D/var) is invariant under addition of a [constant](/D/const):

$$ \label{eq:var-inv}
\mathrm{Var}(X+a) = \mathrm{Var}(X)
$$


**Proof:** The [variance](/D/var) is defined in terms of the [expected value](/D/mean) as

$$ \label{eq:var}
\mathrm{Var}(X) = \mathrm{E}\left[ (X-\mathrm{E}(X))^2 \right] \; .
$$

Using this and the [linearity of the expected value](/P/mean-lin), we can derive \eqref{eq:var-inv} as follows:

$$ \label{eq:var-inv-qed}
\begin{split}
\mathrm{Var}(X+a) &\overset{\eqref{eq:var}}{=} \mathrm{E}\left[ ((X+a)-\mathrm{E}(X+a))^2 \right] \\
&= \mathrm{E}\left[ (X + a - \mathrm{E}(X) - a)^2 \right] \\
&= \mathrm{E}\left[ (X-\mathrm{E}(X))^2 \right] \\
&\overset{\eqref{eq:var}}{=} \mathrm{Var}(X) \; . \\
\end{split}
$$