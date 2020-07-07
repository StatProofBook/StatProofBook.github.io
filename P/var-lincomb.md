---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-07 06:21:00

title: "Variance of the linear combination of two random variables"
chapter: "General Theorems"
section: "Probability theory"
topic: "Variance"
theorem: "Variance of linear combination"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-07-07"
    url: "https://en.wikipedia.org/wiki/Variance#Basic_properties"

proof_id: "P129"
shortcut: "var-lincomb"
username: "JoramSoch"
---


**Theorem:** The [variance](/D/var) of the linear combination of two [random variables](/D/rvar) is a function of the variances as well as the [covariance](/D/cov) of those random variables:

$$ \label{eq:var-lincomb}
\mathrm{Var}(aX+bY) = a^2 \, \mathrm{Var}(X) + b^2 \, \mathrm{Var}(Y) + 2ab \, \mathrm{Cov}(X,Y) \; .
$$


**Proof:** The [variance](/D/var) is defined in terms of the [expected value](/D/mean) as

$$ \label{eq:var}
\mathrm{Var}(X) = \mathrm{E}\left[ (X-\mathrm{E}(X))^2 \right] \; .
$$

Using this and the [linearity of the expected value](/P/mean-lin), we can derive \eqref{eq:var-lincomb} as follows:

$$ \label{eq:var-lincomb-qed}
\begin{split}
\mathrm{Var}(aX+bY) &\overset{\eqref{eq:var}}{=} \mathrm{E}\left[ ((aX+bY)-\mathrm{E}(aX+bY))^2 \right] \\
&= \mathrm{E}\left[ (a [X-\mathrm{E}(X)] + b [Y-\mathrm{E}(Y)])^2 \right] \\
&= \mathrm{E}\left[ a^2 \, (X-\mathrm{E}(X))^2 + b^2 \, (Y-\mathrm{E}(Y))^2 + 2ab \, (X-\mathrm{E}(X)) (Y-\mathrm{E}(Y)) \right] \\
&= \mathrm{E}\left[ a^2 \, (X-\mathrm{E}(X))^2 \right] + \mathrm{E}\left[ b^2 \, (Y-\mathrm{E}(Y))^2 \right] + \mathrm{E}\left[ 2ab \, (X-\mathrm{E}(X)) (Y-\mathrm{E}(Y)) \right] \\
&\overset{\eqref{eq:var}}{=} a^2 \, \mathrm{Var}(X) + b^2 \, \mathrm{Var}(Y) + 2ab \, \mathrm{Cov}(X,Y) \; . \\
\end{split}
$$