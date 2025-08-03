---
layout: definition
mathjax: true

author: "Alexander D. Bolton"
affiliation: "The Book of Statistical Proofs"
e_mail: "StatProofBook@gmail.com"
date: 2025-07-15 00:00:00

title: "Minimum required sample size"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Hypothesis testing"
definition: "Minimum required sample size"

sources:
  - authors: "Sylvain Chabé-Ferret"
    year: 2025
    title: "Power Analysis"
    in: "Statistical Tools for Causal Inference"
    pages: "retrieved on 2025-07-05"
    url: "https://chabefer.github.io/STCI/Power.html"

def_id: "D225"
shortcut: "mrss"
username: "alexanderdbolton"
---


**Definition:** Consider a [hypothesis test](/D/test) concerning parameter $\theta$. We have $H_0: \theta \in \Theta_0$ versus $H_1: \theta \in \Theta_1$, where $\{\Theta_0, \Theta_1\}$ is a partition of $\Theta$. Let the probability of rejecting the null hypothesis for the test with $n$ observations be $\kappa_n(\theta)$.

Given a pre-specified [significance level](/D/alpha) $\alpha \in [0,1]$ and a desired [power](/D/power) $1 - \beta \in [0,1]$, the test must satisfy two conditions:

1. significance constraint: The probability of a type I error must not exceed $\alpha$:
$$ \label{eq:type1error}
\sup_{\theta \in \Theta_0} \kappa_n(\theta) \le \alpha \; .
$$
2. power constraint: The power of the test must be at least $1 - \beta$ for all parameters corresponding to a [minimum detectable effect](/D/mde), $\delta$. This is represented by a specified subset of the alternative hypothesis space, $\Theta_{1,\delta} \subset \Theta_1$:
$$ \label{eq:power}
\inf_{\theta \in \Theta_{1,\delta}} \kappa_n(\theta) \ge 1 - \beta \; .
$$

The minimum required sample size, $n_{m}$, is the smallest integer $n$ so that the hypothesis test simultaneously satisfies both the significance and power constraint.