---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-03-11 16:25:00

title: "Log model evidence in terms of prior and posterior distribution"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Log model evidence"
theorem: "Expression using prior and posterior"

sources:

proof_id: "P314"
shortcut: "lme-pnp"
username: "JoramSoch"
---


**Theorem:** Let $p(y \vert \theta,m)$ be a [likelihood function](/D/lf) of a [generative model](/D/gm) $m$ for making inferences on model parameters $\theta$ given measured data $y$. Moreover, let $p(\theta \vert m)$ be a [prior distribution](/D/prior) on model parameters $\theta$. Then, the [log model evidence](/D/lme) (LME), also called marginal log-likelihood,

$$ \label{eq:LME-term}
\mathrm{LME}(m) = \log p(y|m) \; ,
$$

can be expressed in terms of [prior](/D/prior) and [posterior](/D/post) as

$$ \label{eq:LME-bayes}
\mathrm{LME}(m) = \log p(y|\theta,m) + \log p(\theta|m) - \log p(\theta|y,m) \; .
$$


**Proof:** For a [full probability model](/D/fpm), [Bayes' theorem](/P/bayes-th) makes a statement about the [posterior distribution](/D/post):

$$ \label{eq:BT}
p(\theta|y,m) = \frac{p(y|\theta,m) \, p(\theta|m)}{p(y|m)} \; .
$$

Rearranging for $p(y \vert m)$ and logarithmizing, we have:

$$ \label{eq:LME-bayes-qed}
\begin{split}
\mathrm{LME}(m) = \log p(y|m) & = \log \frac{p(y|\theta,m) \, p(\theta|m)}{p(\theta|y,m)} \\
&= \log p(y|\theta,m) + \log p(\theta|m) - \log p(\theta|y,m) \; .
\end{split}
$$