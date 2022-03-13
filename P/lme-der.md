---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-06 21:27:00

title: "Derivation of the log model evidence"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Log model evidence"
theorem: "Derivation"

sources:

proof_id: "P13"
shortcut: "lme-der"
username: "JoramSoch"
---


**Theorem:** Let $p(y \vert \theta,m)$ be a [likelihood function](/D/lf) of a [generative model](/D/gm) $m$ for making inferences on model parameters $\theta$ given measured data $y$. Moreover, let $p(\theta \vert m)$ be a [prior distribution](/D/prior) on model parameters $\theta$. Then, the [log model evidence](/D/lme) (LME), also called marginal log-likelihood,

$$ \label{eq:LME-term}
\mathrm{LME}(m) = \log p(y|m) \; ,
$$

can be expressed in terms of [likelihood](/D/lf) and [prior](/D/prior) as

$$ \label{eq:LME-marg}
\mathrm{LME}(m) = \log \int p(y|\theta,m) \, p(\theta|m) \, \mathrm{d}\theta \; .
$$


**Proof:** This a consequence of the [law of marginal probability](/D/prob-marg) for continuous variables

$$ \label{eq:prob-marg}
p(y|m) = \int p(y,\theta|m) \, \mathrm{d}\theta
$$

and the [law of conditional probability](/D/prob-cond) according to which

$$ \label{eq:prob-cond}
p(y,\theta|m) = p(y|\theta,m) \, p(\theta|m) \; .
$$

Combining \eqref{eq:prob-marg} with \eqref{eq:prob-cond} and logarithmizing, we have:

$$ \label{eq:LME-marg-qed}
\mathrm{LME}(m) = \log p(y|m) = \log \int p(y|\theta,m) \, p(\theta|m) \, \mathrm{d}\theta \; .
$$