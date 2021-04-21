---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2019-09-27 16:13:00

title: "Partition of the log model evidence into accuracy and complexity"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Log model evidence"
theorem: "Partition into accuracy and complexity"

sources:
  - authors: "Penny et al."
    year: 2007
    title: "Bayesian Comparison of Spatially Regularised General Linear Models"
    in: "Human Brain Mapping"
    pages: "vol. 28, pp. 275–293"
    url: "https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.20327"
    doi: "10.1002/hbm.20327"
  - authors: "Soch et al."
    year: 2016
    title: "How to avoid mismodelling in GLM-based fMRI data analysis: cross-validated Bayesian model selection"
    in: "NeuroImage"
    pages: "vol. 141, pp. 469–489"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811916303615"
    doi: "10.1016/j.neuroimage.2016.07.047"

proof_id: "P3"
shortcut: "lme-anc"
username: "JoramSoch"
---


**Theorem:** The [log model evidence](/D/lme) can be partitioned into accuracy and complexity

$$ \label{eq:LME}
\mathrm{LME}(m) = \mathrm{Acc}(m) - \mathrm{Com}(m)
$$

where the accuracy term is the [posterior](/D/post) [expectation](/P/mean-lotus) of the [log-likelihood function](/D/llf)

$$ \label{eq:Acc}
\mathrm{Acc}(m) = \left\langle \log p(y|\theta,m) \right\rangle_{p(\theta|y,m)}
$$

and the complexity penalty is the [Kullback-Leibler divergence](/D/kl) of [posterior](/D/post) from [prior](/D/prior)

$$ \label{eq:Com}
\mathrm{Com}(m) = \mathrm{KL} \left[ p(\theta|y,m) \, || \, p(\theta|m) \right] \; .
$$


**Proof:** We consider Bayesian inference on [data](/D/data) $y$ using [model](/D/gm) $m$ with parameters $\theta$. Then, [Bayes' theorem](/P/bayes-th) makes a statement about the [posterior distribution](/D/post), i.e. the probability of parameters, given the data and the model:

$$ \label{eq:AnC-s1}
p(\theta|y,m) = \frac{p(y|\theta,m) \, p(\theta|m)}{p(y|m)} \; .
$$

[Rearranging this for the model evidence](/P/lme-der), we have:

$$ \label{eq:AnC-s2}
p(y|m) = \frac{p(y|\theta,m) \, p(\theta|m)}{p(\theta|y,m)} \; .
$$

Logarthmizing both sides of the equation, we obtain:

$$ \label{eq:AnC-s3}
\log p(y|m) = \log p(y|\theta,m) - \log \frac{p(\theta|y,m)}{p(\theta|m)} \; .
$$

Now taking the expectation over the posterior distribution yields:

$$ \label{eq:AnC-s4}
\log p(y|m) = \int p(\theta|y,m) \log p(y|\theta,m) \, \mathrm{d}\theta - \int p(\theta|y,m) \log \frac{p(\theta|y,m)}{p(\theta|m)} \, \mathrm{d}\theta \; .
$$

By definition, the left-hand side is the log model evidence and the terms on the right-hand side correspond to the posterior expectation of the log-likelihood function and the Kullback-Leibler divergence of posterior from prior

$$ \label{eq:LME-AnC}
\mathrm{LME}(m) = \left\langle \log p(y|\theta,m) \right\rangle_{p(\theta|y,m)} - \mathrm{KL} \left[ p(\theta|y,m) \, || \, p(\theta|m) \right]
$$

which proofs the partition given by \eqref{eq:LME}.