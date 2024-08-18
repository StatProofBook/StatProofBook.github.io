---
layout: definition
mathjax: true

author: "Osvaldo Martin"
affiliation: "Universidad Nacional de San Martín"
e_mail: "aloctavodia@gmail.com"
date: 2024-08-18 07:50:00

title: "Posterior predictive distribution"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
definition: "Posterior predictive distribution"

sources:

def_id: "D201"
shortcut: "post-pred"
username: "aloctavodia"
---

**Definition:** Consider measured data $y$, if the posterior distribution is $p(\theta | y)$ and the likelihood function is $p(y | \theta)$ then the distribution that predicts new data $y_{\text{new}}$ is: 

$$ \label{eq:post-pred}
p(y_{\text{new}}|y) = \int p(y_{\text{new}}|\theta) \, p(\theta|y) \, d\theta \; ,
$$

This is the **posterior predictive distribution** 