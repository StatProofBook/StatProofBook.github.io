---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-09-03 06:05:00

title: "Covariance of independent random variables"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
theorem: "Covariance under independence"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Covariance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-09-03"
    url: "https://en.wikipedia.org/wiki/Covariance#Uncorrelatedness_and_independence"

proof_id: "P158"
shortcut: "cov-ind"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be [independent](/D/ind) [random variables](/D/rvar). Then, the [covariance](/D/cov) of $X$ and $Y$ is zero:

$$ \label{eq:cov-ind}
X, Y \; \text{independent} \quad \Rightarrow \quad \mathrm{Cov}(X,Y) = 0 \; .
$$


**Proof:** The [covariance can be expressed in terms of expected values](/P/cov-mean) as

$$ \label{eq:cov-mean}
\mathrm{Cov}(X,Y) = \mathrm{E}(X\,Y) - \mathrm{E}(X) \, \mathrm{E}(Y) \; .
$$

For independent random variables, [the expected value of the product is equal to the product of the expected values](/P/mean-mult):

$$ \label{eq:mean-mult}
\mathrm{E}(X\,Y) = \mathrm{E}(X) \, \mathrm{E}(Y) \; .
$$

Taking \eqref{eq:cov-mean} and \eqref{eq:mean-mult} together, we have

$$ \label{eq:cov-ind-qed}
\begin{split}
\mathrm{Cov}(X,Y) &\overset{\eqref{eq:cov-mean}}{=} \mathrm{E}(X\,Y) - \mathrm{E}(X) \, \mathrm{E}(Y) \\
&\overset{\eqref{eq:mean-mult}}{=} \mathrm{E}(X) \, \mathrm{E}(Y) - \mathrm{E}(X) \, \mathrm{E}(Y) \\
&= 0 \; .
\end{split}
$$