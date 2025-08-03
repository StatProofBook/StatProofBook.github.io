---
layout: definition
mathjax: true

author: "Alexander D. Bolton"
affiliation: "The Book of Statistical Proofs"
e_mail: "StatProofBook@gmail.com"
date: 2025-07-15 00:00:00

title: "Minimum detectable effect"
chapter: "General Theorems"
section: "Frequentist statistics"
topic: "Hypothesis testing"
definition: "Minimum detectable effect"

sources:
  - authors: "Sylvain Chabé-Ferret"
    year: 2025
    title: "Power Analysis"
    in: "Statistical Tools for Causal Inference"
    pages: "retrieved on 2025-07-05"
    url: "https://chabefer.github.io/STCI/Power.html"

def_id: "D224"
shortcut: "mde"
username: "alexanderdbolton"
---


**Definition:** Consider a [hypothesis test](/D/test) concerning parameter $\theta$. We have $H_0: \theta \in \Theta_0$ versus $H_1: \theta \in \Theta_1$, where $\{\Theta_0, \Theta_1\}$ is a partition of $\Theta$. Let the probability of rejecting the null hypothesis for the test with $n$ observations be $\kappa_n(\theta)$. The number of samples $n$ is fixed.

The effect size for a parameter $\theta \in \Theta_1$ is the distance of $\theta$ from the null parameter space $\Theta_0, d(\theta, \Theta_0)$. It can be defined as

$$ \label{eq:distancefromTheta0}
d(\theta, \Theta_0) = \inf_{\theta_0 \in \Theta_0} ||\theta - \theta_0|| \; .
$$

Let the test have a given [significance level](/D/alpha) $\alpha$ and desired [power](/D/power) $1 - \beta$. The minimum detectable effect, $\delta$, is the smallest $\delta$ so that the hypothesis test simultaneously has [size](/D/size) less than or equal to $\alpha$ and power at least $1 - \beta$:

$$ \label{eq:mdeconditions}
\left(\sup_{\theta \in \Theta_0} \kappa_n(\theta) \leq \alpha\right) \wedge \left(\inf_{\theta: \, d(\theta, \Theta_0) \leq \delta} \kappa_n(\theta) \geq 1 - \beta\right) \; .
$$