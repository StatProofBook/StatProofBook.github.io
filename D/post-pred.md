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


**Definition:** Consider a [full probability model](/D/fpm) with [likelihood function](/D/lf) $p(y \vert \theta)$ and [posterior distribution](/D/post) $p(\theta \vert y)$ based on [measured data](/D/data) $y$. Then, the [marginal distribution](/D/dist-marg) of new data, predicted based on the posterior distribution, is called the posterior predictive distribution:

$$ \label{eq:post-pred}
p(y_{\mathrm{new}} \vert y) = \int p(y_{\mathrm{new}} \vert \theta) \, p(\theta \vert y) \, \mathrm{d}\theta \; .
$$