---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-06-20 11:44:00

title: "Bivariate normally distributed data"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Multivariate Gaussian"
definition: "Bivariate normally distributed data"

sources:

def_id: "D222"
shortcut: "bvn-data"
username: "JoramSoch"
---


**Definition:** Bivariate normally distributed data are defined as a set of two-dimensional vectors $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$, independent and identically distributed according to a [bivariate normal distribution](/D/bvn) with mean vector $\mu$ and covariance matrix $\Sigma$

$$ \label{eq:bvn}
y_i \sim \mathcal{N}(\mu, \Sigma), \quad i = 1, \ldots, n
$$

where $\mu$ and $\Sigma$ [can be parametrized](/P/bvn-snorm) [in terms of](/P/bvn-pdfcorr) means $\mu_1$, $\mu_2$, variances $\sigma_1^2$, $\sigma_2^2$ and correlation $\rho$:

$$ \label{eq:bvn-mu-Sigma}
\mu    = \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right] \quad \text{and} \quad
\Sigma = \left[ \begin{matrix} \sigma_1^2 & \rho \sigma_1 \sigma_2 \\
							   \rho \sigma_1 \sigma_2 & \sigma_2^2 \end{matrix} \right] \; .
$$