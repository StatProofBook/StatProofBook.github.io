---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2019-11-27 14:26:00

title: "Partition of the mean squared error into bias and variance"
chapter: "General Theorems"
section: "Estimation theory"
topic: "Point estimates"
theorem: "Partition of the mean squared error into bias and variance"

sources:
  - authors: "Wikipedia"
    year: 2019
    title: "Mean squared error"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2019-11-27"
    url: "https://en.wikipedia.org/wiki/Mean_squared_error#Proof_of_variance_and_bias_relationship"

proof_id: "P5"
shortcut: "mse-bnv"
username: "JoramSoch"
---


**Theorem:** The [mean squared error](/D/mse) can be partitioned into variance and squared bias

$$ \label{eq:MSE}
\mathrm{MSE}(\hat{\theta}) = \mathrm{Var}(\hat{\theta}) + \mathrm{Bias}(\hat{\theta},\theta)^2
$$

where the [variance](/D/var) is given by

$$ \label{eq:Var}
\mathrm{Var}(\hat{\theta}) = \mathbb{E}_{\hat{\theta}}\left[ \left( \hat{\theta} - \mathbb{E}_{\hat{\theta}}(\hat{\theta}) \right)^2 \right]
$$

and the [bias](/D/bias) is given by

$$ \label{eq:Bias}
\mathrm{Bias}(\hat{\theta},\theta) = \left( \mathbb{E}_{\hat{\theta}}(\hat{\theta}) - \theta \right) \; .
$$


**Proof:** The mean squared error (MSE) [is defined as](/D/mse) the [expected value](/D/mean) of the squared deviation of the estimated value $\hat{\theta}$ from the true value $\theta$ of a parameter, over all values $\hat{\theta}$:

$$ \label{eq:MSE-def}
\mathrm{MSE}(\hat{\theta}) = \mathbb{E}_{\hat{\theta}}\left[ \left( \hat{\theta} - \theta \right)^2 \right] \; .
$$

This formula can be evaluated in the following way:

$$ \label{eq:MSE-ref1}
\begin{split}
\mathrm{MSE}(\hat{\theta}) &= \mathbb{E}_{\hat{\theta}}\left[ \left( \hat{\theta} - \theta \right)^2 \right] \\
&= \mathbb{E}_{\hat{\theta}}\left[ \left( \hat{\theta} - \mathbb{E}_{\hat{\theta}}(\hat{\theta}) + \mathbb{E}_{\hat{\theta}}(\hat{\theta}) - \theta \right)^2 \right] \\
&= \mathbb{E}_{\hat{\theta}}\left[ \left( \hat{\theta} - \mathbb{E}_{\hat{\theta}}(\hat{\theta}) \right)^2 + 2 \left( \hat{\theta} - \mathbb{E}_{\hat{\theta}}(\hat{\theta}) \right) \left( \mathbb{E}_{\hat{\theta}}(\hat{\theta}) - \theta \right) + \left( \mathbb{E}_{\hat{\theta}}(\hat{\theta}) - \theta \right)^2 \right] \\
&= \mathbb{E}_{\hat{\theta}}\left[ \left( \hat{\theta} - \mathbb{E}_{\hat{\theta}}(\hat{\theta}) \right)^2 \right] + \mathbb{E}_{\hat{\theta}}\left[ 2 \left( \hat{\theta} - \mathbb{E}_{\hat{\theta}}(\hat{\theta}) \right) \left( \mathbb{E}_{\hat{\theta}}(\hat{\theta}) - \theta \right) \right] + \mathbb{E}_{\hat{\theta}}\left[ \left( \mathbb{E}_{\hat{\theta}}(\hat{\theta}) - \theta \right)^2 \right] \; . \\
\end{split}
$$

Because $\mathbb{E}_{\hat{\theta}}(\hat{\theta}) - \theta$ is constant as a function of $\hat{\theta}$, we have:

$$ \label{eq:MSE-ref2}
\begin{split}
\mathrm{MSE}(\hat{\theta}) &= \mathbb{E}_{\hat{\theta}}\left[ \left( \hat{\theta} - \mathbb{E}_{\hat{\theta}}(\hat{\theta}) \right)^2 \right] + 2  \left( \mathbb{E}_{\hat{\theta}}(\hat{\theta}) - \theta \right) \mathbb{E}_{\hat{\theta}}\left[ \hat{\theta} - \mathbb{E}_{\hat{\theta}}(\hat{\theta}) \right] + \left( \mathbb{E}_{\hat{\theta}}(\hat{\theta}) - \theta \right)^2 \\
&= \mathbb{E}_{\hat{\theta}}\left[ \left( \hat{\theta} - \mathbb{E}_{\hat{\theta}}(\hat{\theta}) \right)^2 \right] + 2  \left( \mathbb{E}_{\hat{\theta}}(\hat{\theta}) - \theta \right) \left( \mathbb{E}_{\hat{\theta}}(\hat{\theta}) - \mathbb{E}_{\hat{\theta}}(\hat{\theta}) \right) + \left( \mathbb{E}_{\hat{\theta}}(\hat{\theta}) - \theta \right)^2 \\
&= \mathbb{E}_{\hat{\theta}}\left[ \left( \hat{\theta} - \mathbb{E}_{\hat{\theta}}(\hat{\theta}) \right)^2 \right] + \left( \mathbb{E}_{\hat{\theta}}(\hat{\theta}) - \theta \right)^2 \; . \\
\end{split}
$$

This proofs the partition given by \eqref{eq:MSE}.