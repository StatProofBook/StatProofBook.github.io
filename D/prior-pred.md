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


**Definition:** Consider a [full probability model](/D/fpm) with [likelihood function](/D/lf) $p(y \vert \theta)$ and [prior distribution](/D/prior) $p(\theta)$. Then, the [marginal distribution](/D/dist-marg) of any [data point](/D/data) $y_{\mathrm{new}}$, accounting for the prior distribution, is called the prior predictive distribution:

$$ \label{eq:prior-pred}
p(y_{\mathrm{new}}) = \int p(y_{\mathrm{new}} \vert \theta) \, p(\theta) \, \mathrm{d}\theta \; .
$$