---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-07 05:38:00

title: "Scaling of the variance upon multiplication with a constant"
chapter: "General Theorems"
section: "Probability theory"
topic: "Variance"
theorem: "Scaling upon multiplication"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-07-07"
    url: "https://en.wikipedia.org/wiki/Variance#Basic_properties"

proof_id: "P127"
shortcut: "var-scal"
username: "JoramSoch"
---


**Theorem:** The [variance](/D/var) scales upon multiplication with a [constant](/D/const):

$$ \label{eq:var-scal}
\mathrm{Var}(aX) = a^2 \, \mathrm{Var}(X)
$$


**Proof:** The [variance](/D/var) is defined in terms of the [expected value](/D/mean) as

$$ \label{eq:var}
\mathrm{Var}(X) = \mathrm{E}\left[ (X-\mathrm{E}(X))^2 \right] \; .
$$

Using this and the [linearity of the expected value](/P/mean-lin), we can derive \eqref{eq:var-scal} as follows:

$$ \label{eq:var-scal-qed}
\begin{split}
\mathrm{Var}(aX) &\overset{\eqref{eq:var}}{=} \mathrm{E}\left[ ((aX)-\mathrm{E}(aX))^2 \right] \\
&= \mathrm{E}\left[ (aX - a\mathrm{E}(X))^2 \right] \\
&= \mathrm{E}\left[ (a [X - \mathrm{E}(X)])^2 \right] \\
&= \mathrm{E}\left[ a^2 (X - \mathrm{E}(X))^2 \right] \\
&= a^2 \, \mathrm{E}\left[ (X - \mathrm{E}(X))^2 \right] \\
&\overset{\eqref{eq:var}}{=} a^2 \, \mathrm{Var}(X) \; . \\
\end{split}
$$