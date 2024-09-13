---
layout: proof
mathjax: true

author: "Osvaldo Martin"
affiliation: "Universidad Nacional de San Martín"
e_mail: "aloctavodia@gmail.com"
date: 2024-09-11 15:30:00

title: "Posterior predictive distribution"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
theorem: "Posterior predictive distribution"

sources:

proof_id: "P467"
shortcut: "post-pred"
username: "aloctavodia"
---

Theorem:  The [posterior predictive distribution](/D/post-pred) is the [marginal distribution](/D/dist-marg) of new data $y_{\mathrm{new}}$ given the [measured data](/D/data) $y$:


$$
p(y_{\mathrm{new}} \vert y) = \int p(y_{\mathrm{new}} \vert \theta) \, p(\theta \vert y) \, \mathrm{d}\theta \; .
$$

Proof: To find $y_{\text{new}}$ we first write the joint distribution of $y_{\text{new}}$ and $\theta$ given $y$ and marginalize over all possible values of $\theta$:

$$ \label{eq:post-pred-marg}
p(y_{\mathrm{new}} \vert y) = \int p(y_{\mathrm{new}}, \theta \vert y) \, \mathrm{d}\theta 
$$

By using the [law of conditional probability](/D/prob-cond) we can write the joint distribution as:

$$
p(y_{\text{new}}, \theta \vert y) = p(y_{\text{new}} \vert \theta, y) \, p(\theta \vert y)
$$

We notice that $y_{\text{new}}$ depends on $\theta$, but is conditionally independent of the observed data $y$ given $\theta$, then we can write:

$$
p(y_{\text{new}}, \theta \vert y) = p(y_{\text{new}} \vert \theta) \, p(\theta \vert y)
$$
   
Thus, expression \ref{eq:post-pred-marg} can be written as:

$$
p(y_{\text{new}} \vert y) = \int p(y_{\text{new}} \vert \theta) \, p(\theta \vert y) \, \mathrm{d}\theta \; .
$$

