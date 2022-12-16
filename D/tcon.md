---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-16 12:35:00

title: "t-contrast for contrast-based inference in multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
definition: "t-contrast"

sources:
  - authors: "Stephan, Klaas Enno"
    year: 2010
    title: "Classical (frequentist) inference"
    in: "Methods and models for fMRI data analysis in neuroeconomics"
    pages: "Lecture 4, Slides 7/9"
    url: "http://www.socialbehavior.uzh.ch/teaching/methodsspring10.html"

def_id: "D185"
shortcut: "tcon"
username: "JoramSoch"
---


**Definition:** Consider a [linear regression model](/D/mlr) with $n \times p$ design matrix $X$ and $p \times 1$ regression coefficients $\beta$:

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$

Then, a t-contrast is specified by a $p \times 1$ vector $c$ and it entails the [null hypothesis](/D/h0) that the product of this vector and the regression coefficients is zero:

$$ \label{eq:mlr-t-h0}
H_0: \; c^\mathrm{T} \beta = 0 \; .
$$

Consequently, the [alternative hypothesis](/D/h1) of a [two-tailed t-test](/D/hyp-tail) is

$$ \label{eq:mlr-t-h1}
H_1: \; c^\mathrm{T} \beta \neq 0
$$

and the [alternative hypothesis](/D/h1) of a [one-sided t-test](/D/hyp-tail) would be

$$ \label{eq:mlr-t-h1lr}
H_1: \; c^\mathrm{T} \beta < 0 \quad \text{or} \quad H_1: \; c^\mathrm{T} \beta > 0 \; .
$$

Here, $c$ is called the "contrast vector" and $c^\mathrm{T} \beta$ is called the "contrast value". With estimated regression coefficients, $c^\mathrm{T} \hat{\beta}$ is called the "estimated contrast value".