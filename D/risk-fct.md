---
layout: definition
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-28 22:32:01

title: "Risk and Bayes risk"
chapter: "General Theorems"
section: "Estimation theory"
topic: "Basic concepts of estimation"
definition: "Risk and Bayes risk"

sources:
  - authors: "George Casella, Roger L. Berger"
    year: 2002
    title: "Loss function optimality"
    in: "Statistical Inference"
    pages: "Second edition, Section 7.3.4, pp. 349 and 352"

def_id: "D245"
shortcut: "risk-fct"
username: "kjpetrykowski"
---

**Definition:** Let $\Theta$ be the set of possible parameter values and $P\_\theta$ the distribution of the data $X$ at $\theta\in\Theta$. A decision rule $\delta$ assigns an action $\delta(X)$ to the data. Suppose its [loss](/D/loss-fct) $L(\delta(X),\theta)$ is a random variable under each $P\_\theta$. The risk of the rule at $\theta$ is

$$ \label{eq:risk}
R(\theta,\delta)=\mathrm{E}_\theta[L(\delta(X),\theta)] \; .
$$

Here $\mathrm{E}\_\theta$ averages over draws of $X$ with $\theta$ fixed. Let $\Pi$ be a [prior](/D/prior) on $\Theta$ with total probability one. Suppose the loss is also a random variable under the joint distribution of $\theta$ and $X$. The Bayes risk is the average risk over the prior:

$$ \label{eq:bayes-risk}
r(\delta)=\int_\Theta R(\theta,\delta)\,\Pi(\mathrm{d}\theta)
=\mathrm{E}[L(\delta(X),\theta)] \; .
$$

The last expectation averages over both $\theta$ and the data drawn given $\theta$. If the prior has density $\pi$, then

$$ \label{eq:bayes-risk-density}
r(\delta)=\int_\Theta R(\theta,\delta)\pi(\theta)\,\mathrm{d}\theta \; .
$$

For a discrete prior, take the sum weighted by the prior probabilities. Both risks may be infinite. For an observed sample and a fixed action, [posterior expected loss](/D/post-loss) averages over the posterior distribution of $\theta$.
