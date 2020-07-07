---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-07-07 06:10:00

title: "Variance of the sum of two random variables"
chapter: "General Theorems"
section: "Probability theory"
topic: "Variance"
theorem: "Variance of a sum"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-07-07"
    url: "https://en.wikipedia.org/wiki/Variance#Basic_properties"

proof_id: "P128"
shortcut: "var-sum"
username: "JoramSoch"
---


**Theorem:** The [variance](/D/var) of the sum of two [random variables](/D/rvar) equals the sum of the variances of those random variables, plus two times their [covariance](/D/cov):

$$ \label{eq:var-sum}
\mathrm{Var}(X+Y) = \mathrm{Var}(X) + \mathrm{Var}(Y) + 2 \, \mathrm{Cov}(X,Y) \; .
$$


**Proof:** The [variance](/D/var) is defined in terms of the [expected value](/D/mean) as

$$ \label{eq:var}
\mathrm{Var}(X) = \mathrm{E}\left[ (X-\mathrm{E}(X))^2 \right] \; .
$$

Using this and the [linearity of the expected value](/P/mean-lin), we can derive \eqref{eq:var-sum} as follows:

$$ \label{eq:var-sum-qed}
\begin{split}
\mathrm{Var}(X+Y) &\overset{\eqref{eq:var}}{=} \mathrm{E}\left[ ((X+Y)-\mathrm{E}(X+Y))^2 \right] \\
&= \mathrm{E}\left[ ([X-\mathrm{E}(X)] + [Y-\mathrm{E}(Y)])^2 \right] \\
&= \mathrm{E}\left[ (X-\mathrm{E}(X))^2 + (Y-\mathrm{E}(Y))^2 + 2 \, (X-\mathrm{E}(X)) (Y-\mathrm{E}(Y)) \right] \\
&= \mathrm{E}\left[ (X-\mathrm{E}(X))^2 \right] + \mathrm{E}\left[ (Y-\mathrm{E}(Y))^2 \right] + \mathrm{E}\left[ 2 \, (X-\mathrm{E}(X)) (Y-\mathrm{E}(Y)) \right] \\
&\overset{\eqref{eq:var}}{=} \mathrm{Var}(X) + \mathrm{Var}(Y) + 2 \, \mathrm{Cov}(X,Y) \; . \\
\end{split}
$$