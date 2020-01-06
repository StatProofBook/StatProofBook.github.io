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

dependencies:
  - theorem: "law of marginal probability, also called 'sum rule of probability'"
  - theorem: "Bayes' theorem"

sources:

proof_id: "P13"
shortcut: "lme-der"
username: "JoramSoch"
---


**Theorem:** Let $p(y \mid \theta,m)$ be a likelihood function of a generative model $m$ for making inferences on model parameters $\theta$ given measured data $y$. Moreover, let $p(\theta \mid m)$ be a prior distribution on model parameters $\theta$. Then, the log model evidence (LME), also called marginal log-likelihood,

$$ \label{eq:LME-term}
\mathrm{LME}(m) = \log p(y|m) \; ,
$$

can be expressed

1) as

$$ \label{eq:LME-marg}
\mathrm{LME}(m) = \log \int p(y|\theta,m) \, p(\theta|m) \, \mathrm{d}\theta
$$

2) or

$$ \label{eq:LME-bayes}
\mathrm{LME}(m) = \log p(y|\theta,m) + \log p(\theta|m) - \log p(\theta|y,m) \; .
$$


**Proof:**

1) The first expression is a simple consequence of the law of marginal probability for continuous variables according to which

$$ \label{eq:ME}
p(y|m) = \int p(y|\theta,m) \, p(\theta|m) \, \mathrm{d}\theta
$$

which, when logarithmized, gives

$$ \label{eq:LME-marg-qed}
\mathrm{LME}(m) = \log p(y|m) = \log \int p(y|\theta,m) \, p(\theta|m) \, \mathrm{d}\theta \; .
$$

2) The second expression can be derived from Bayes' theorem which makes a statement about the posterior distribution:

$$ \label{eq:BT}
p(\theta|y,m) = \frac{p(y|\theta,m) \, p(\theta|m)}{p(y|m)} \; .
$$

Rearranging for $p(y \mid m)$ and logarithmizing, we have:

$$ \label{eq:LME-bayes-qed}
\begin{split}
\mathrm{LME}(m) = \log p(y|m) & = \log \frac{p(y|\theta,m) \, p(\theta|m)}{p(\theta|y,m)} \\
&= \log p(y|\theta,m) + \log p(\theta|m) - \log p(\theta|y,m) \; .
\end{split}
$$
