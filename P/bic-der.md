---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-26 23:36:00

title: "Derivation of the Bayesian information criterion"
chapter: "Model Selection"
section: "Classical information criteria"
topic: "Bayesian information criterion"
theorem: "Derivation"

sources:
  - authors: "Claeskens G, Hjort NL"
    year: 2008
    title: "The Bayesian information criterion"
    in: "Model Selection and Model Averaging"
    pages: "ch. 3.2, pp. 78-81"
    url: "https://www.cambridge.org/core/books/model-selection-and-model-averaging/E6F1EC77279D1223423BB64FC3A12C37"
    doi: "10.1017/CBO9780511790485"

proof_id: "P32"
shortcut: "bic-der"
username: "JoramSoch"
---


**Theorem:** Let $p(y \vert \theta, m)$ be the [likelihood function](/D/lf) of a [generative model](/D/gm) $m \in \mathcal{M}$ with model parameters $\theta \in \Theta$ describing measured data $y \in \mathbb{R}^n$. Let $p(\theta \vert m)$ be a [prior distribution](/D/prior) on the model parameters. Assume that likelihood function and prior density are twice differentiable.

Then, as the number of data points goes to infinity, an approximation to the log-[marginal likelihood](/D/ml) $\log p(y \vert m)$, up to constant terms not depending on the model, is given by the [Bayesian information criterion](/D/bic) (BIC) as

$$ \label{eq:BIC}
-2 \log p(y|m) \approx \mathrm{BIC}(m) = -2 \log p(y|\hat{\theta}, m) + p \log n
$$

where $\hat{\theta}$ is the [maximum likelihood estimator](/D/mle) (MLE) of $\theta$, $n$ is the number of data points and $p$ is the number of model parameters.


**Proof:** Let $\mathrm{LL}(\theta)$ be the [log-likelihood function](/D/llf)

$$ \label{eq:LL}
\mathrm{LL}(\theta) = \log p(y|\theta,m)
$$

and define the functions $g$ and $h$ as follows:

$$ \label{eq:gh}
\begin{split}
g(\theta) &= p(\theta|m) \\
h(\theta) &= \frac{1}{n} \, \mathrm{LL}(\theta) \; .
\end{split}
$$

Then, the [marginal likelihood](/D/ml) can be written as follows:

$$ \label{eq:ML}
\begin{split}
p(y|m) &= \int_{\Theta} p(y|\theta,m) \, p(\theta|m) \, \mathrm{d}\theta \\
&= \int_{\Theta} \exp\left[n \, h(\theta)\right] \, g(\theta) \, \mathrm{d}\theta \; .
\end{split}
$$

This is an integral suitable for Laplace approximation which states that

$$ \label{eq:LA}
\int_{\Theta} \exp\left[n \, h(\theta)\right] \, g(\theta) \, \mathrm{d}\theta = \left( \sqrt{\frac{2 \pi}{n}} \right)^p \exp\left[n \, h(\theta_0)\right] \left( g(\theta_0) \left| J(\theta_0) \right|^{-1/2} + O(1/n) \right)
$$

where $\theta_0$ is the value that maximizes $h(\theta)$ and $J(\theta_0)$ is the Hessian matrix evaluated at $\theta_0$. In our case, we have $h(\theta) = 1/n \, \mathrm{LL}(\theta)$ such that $\theta_0$ is the maximum likelihood estimator $\hat{\theta}$:

$$ \label{eq:MLE}
\hat{\theta} = \operatorname*{arg\,max}_\theta \mathrm{LL}(\theta) \; .
$$

With this, \eqref{eq:LA} can be applied to \eqref{eq:ML} using \eqref{eq:gh} to give:

$$ \label{eq:ML-approx}
p(y|m) \approx \left( \sqrt{\frac{2 \pi}{n}} \right)^p p(y|\hat{\theta},m) \, p(\hat{\theta}|m) \, \left| J(\hat{\theta}) \right|^{-1/2} \; .
$$

Logarithmizing and multiplying with $-2$, we have:

$$ \label{eq:LME-approx}
-2 \log p(y|m) \approx -2 \, \mathrm{LL}(\hat{\theta}) + p \log n - p \log(2 \pi) - 2 \log p(\hat{\theta}|m) + \log \left| J(\hat{\theta}) \right| \; .
$$

As $n \to \infty$, the last three terms are $O_p(1)$ and can therefore be ignored when comparing between models $\mathcal{M} = \left\lbrace m_1, \ldots, m_M \right\rbrace$ and using $p(y \vert m_j)$ to compute [posterior model probabilies](/D/pmp) $p(m_j \vert y)$. With that, the BIC is given as

$$ \label{eq:BIC-qed}
\mathrm{BIC}(m) = -2 \log p(y|\hat{\theta}, m) + p \log n \; .
$$