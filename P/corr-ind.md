---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-09-27 12:32:50

title: "Independent random variables are uncorrelated"
chapter: "General Theorems"
section: "Probability theory"
topic: "Correlation"
theorem: "Correlation under independence"

sources:
  - authors: "StatProofBook"
    year: 2022
    title: "Uncorrelated random variables are not necessarily independent."
    in: "X"
    pages: "Nov 22, 2022, 06:34 AM"
    url: "https://x.com/StatProofBook/status/1594927275514134528"

proof_id: "P472"
shortcut: "corr-ind"
username: "JoramSoch"
---


**Theorem:** [Independent](/D/ind) [random variables](/D/rvar) are uncorrelated.


**Proof:** The [correlation](/D/corr) of two random variables is defined as:

$$ \label{eq:corr}
\mathrm{Corr}(X,Y) = \frac{\mathrm{Cov}(X,Y)}{\sqrt{\mathrm{Var}(X)} \sqrt{\mathrm{Var}(Y)}} \; .
$$

The [covariance of independent random variables is zero](/P/cov-ind):

$$ \label{eq:cov-ind}
X, Y \; \text{independent} \quad \Rightarrow \quad \mathrm{Cov}(X,Y) = 0 \; .
$$

Thus, the correlation of independent random variables is also zero:

$$ \label{eq:corr-ind-qed}
X, Y \; \text{independent} \quad \Rightarrow \quad \mathrm{Corr}(X,Y) = 0 \; .
$$