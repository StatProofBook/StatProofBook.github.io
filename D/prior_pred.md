---
layout: definition
mathjax: true

author: "Osvaldo Martin"
affiliation: "Universidad Nacional de San Martín"
e_mail: "aloctavodia@gmail.com"
date: 2024-08-19 14:57:00

title: "Prior predictive distribution"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
definition: "Prior predictive distribution"

sources:

def_id: "D202"
shortcut: "prior-pred"
username: "aloctavodia"
---

**Definition:** If the prior distribution is $p(\theta)$ and the likelihood function is $p(y | \theta)$ then the distribution that predicts new data $y_{\text{new}}$ when no data $y$ has already been measured is: 

$$ \label{eq:prior-pred}
p(y_{\text{new}}) = \int p(y_{\text{new}}|\theta) \, p(\theta) \, d\theta \; ,
$$

This is the **prior predictive distribution** 