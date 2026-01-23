---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-07-04 13:33:00

title: "Prior predictive distribution is a marginal distribution of the joint likelihood"
chapter: "General Theorems"
section: "Bayesian statistics"
topic: "Probabilistic modeling"
theorem: "Prior predictive distribution is marginal of joint likelihood"

sources:

proof_id: "P510"
shortcut: "priorpred-jl"
username: "JoramSoch"
---


**Theorem:** The [prior predictive distribution](/D/prior-pred) is the [marginal distribution](/D/dist-marg) of the [joint likelihood](/D/ml) of the [new data](/D/data) $y_{\mathrm{new}}$, unconditional on the measured data $y$:

$$ \label{eq:priorpred-jl}
p(y_{\mathrm{new}}) = \int p(y_{\mathrm{new}}, \theta) \, \mathrm{d}\theta
$$


**Proof:** The [prior predictive distribution](/D/prior-pred) is defined as the [marginal distribution](/D/dist-marg) of new data $y_{\mathrm{new}}$, predicted based on the [prior distribution](/D/prior) before seeing the measured data $y$:

$$ \label{eq:prior-pred}
p(y_{\mathrm{new}}) = \int p(y_{\mathrm{new}} \vert \theta) \, p(\theta) \, \mathrm{d}\theta \; .
$$

By using the [law of conditional probability](/D/prob-cond), we can write the integrand as

$$ \label{eq:jl-prior}
p(y_{\text{new}} \vert \theta) \, p(\theta) = p(y_{\text{new}}, \theta)
$$

which is the [joint likelihood](/D/jl). Thus, expression \eqref{eq:prior-pred} can be written as:

$$ \label{eq:priorpred-jl-qed}
p(y_{\mathrm{new}}) = \int p(y_{\text{new}}, \theta) \, \mathrm{d}\theta \; .
$$