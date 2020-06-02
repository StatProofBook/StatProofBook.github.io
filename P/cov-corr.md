---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-06-02 21:00:00

title: "Relationship between covariance and correlation"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
theorem: "Relationship to correlation"

sources:

proof_id: "P119"
shortcut: "cov-corr"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be [random variables](/D/rvar). Then, the [covariance](/D/cov) of $X$ and $Y$ is equal to the product of their [correlation](/D/corr) and the [standard deviations](/D/std) of $X$ and $Y$:

$$ \label{eq:cov-corr}
\mathrm{Cov}(X,Y) = \sigma_X \, \mathrm{Corr}(X,Y) \, \sigma_Y \; .
$$


**Proof:** The [correlation](/D/corr) of $X$ and $Y$ is defined as

$$ \label{eq:corr}
\mathrm{Corr}(X,Y) = \frac{\mathrm{Cov}(X,Y)}{\sigma_X \sigma_Y} \; .
$$

which can be rearranged for the [covariance](/D/cov) to give

$$ \label{eq:cov-corr-qed}
\mathrm{Cov}(X,Y) = \sigma_X \, \mathrm{Corr}(X,Y) \, \sigma_Y
$$