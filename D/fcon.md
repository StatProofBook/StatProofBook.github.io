---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-16 12:42:00

title: "F-contrast for contrast-based inference in multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
definition: "F-contrast"

sources:
  - authors: "Stephan, Klaas Enno"
    year: 2010
    title: "Classical (frequentist) inference"
    in: "Methods and models for fMRI data analysis in neuroeconomics"
    pages: "Lecture 4, Slides 23/25"
    url: "http://www.socialbehavior.uzh.ch/teaching/methodsspring10.html"

def_id: "D186"
shortcut: "fcon"
username: "JoramSoch"
---


**Definition:** Consider a [linear regression model](/D/mlr) with $n \times p$ design matrix $X$ and $p \times 1$ regression coefficients $\beta$:

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$

Then, an F-contrast is specified by a $p \times q$ matrix $C$, yielding a $q \times 1$ vector $\gamma = C^\mathrm{T} \beta$, and it entails the [null hypothesis](/D/h0) that each value in this vector is zero:

$$ \label{eq:mlr-f-h0}
H_0: \; \gamma_1 = 0 \wedge \ldots \wedge \gamma_q = 0 \; .
$$

Consequently, the [alternative hypothesis](/D/h1) of the [statistical test](/D/test) would be that at least one entry of this vector is non-zero:

$$ \label{eq:mlr-f-h1}
H_1: \; \gamma_1 \neq 0 \vee \ldots \vee \gamma_q \neq 0 \; .
$$

Here, $C$ is called the "contrast matrix" and $C^\mathrm{T} \beta$ are called the "contrast values". With estimated regression coefficients, $C^\mathrm{T} \hat{\beta}$ are called the "estimated contrast values".