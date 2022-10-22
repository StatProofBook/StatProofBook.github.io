---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-20 10:11:00

title: "Derivation of the model evidence"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Model evidence"
theorem: "Derivation"

sources:

proof_id: "P367"
shortcut: "me-der"
username: "JoramSoch"
---


**Theorem:** Let $p(y \vert \theta,m)$ be a [likelihood function](/D/lf) of a [generative model](/D/gm) $m$ for making inferences on model parameters $\theta$ given measured data $y$. Moreover, let $p(\theta \vert m)$ be a [prior distribution](/D/prior) on model parameters $\theta$ in the parameter space $\Theta$. Then, the [model evidence](/D/me) (ME) can be expressed in terms of [likelihood](/D/lf) and [prior](/D/prior) as

$$ \label{eq:ME-marg}
\mathrm{ME}(m) = \int_{\Theta} p(y|\theta,m) \, p(\theta|m) \, \mathrm{d}\theta \; .
$$


**Proof:** This a consequence of the [law of marginal probability](/D/prob-marg) for [continuous variables](/D/rvar-disc)

$$ \label{eq:prob-marg}
p(y|m) = \int_{\Theta} p(y,\theta|m) \, \mathrm{d}\theta
$$

and the [law of conditional probability](/D/prob-cond) according to which

$$ \label{eq:prob-cond}
p(y,\theta|m) = p(y|\theta,m) \, p(\theta|m) \; .
$$

Plugging \eqref{eq:prob-cond} into \eqref{eq:prob-marg}, we obtain:

$$ \label{eq:ME-marg-qed}
\mathrm{ME}(m) = p(y|m) = \int_{\Theta} p(y|\theta,m) \, p(\theta|m) \, \mathrm{d}\theta \; .
$$