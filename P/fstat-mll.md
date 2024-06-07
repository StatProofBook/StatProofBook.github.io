---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-03-28 10:34:17

title: "Relationship between F-statistic and maximum log-likelihood"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "F-statistic"
theorem: "Relationship to maximum log-likelihood"

sources:

proof_id: "P443"
shortcut: "fstat-mll"
username: "JoramSoch"
---


**Theorem:** Consider two [linear regression models](/D/mlr) with [independent](/D/ind) observations

$$ \label{eq:m0-m1}
\begin{split}
m_1: \; y &= X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \\
m_0: \; y &= X_0\beta_0 + \varepsilon_0, \; \varepsilon_{0i} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma_0^2) \; .
\end{split}
$$

Then, the [F-statistic](/D/fstat) can be expressed in terms of the [maximum log-likelihood](/D/mll) as

$$ \label{eq:F-MLL}
F = \left[ \left( \exp[\Delta\mathrm{MLL}] \right)^{2/n} - 1 \right] \cdot \frac{n-p}{p-p_0}
$$

where $n$, $p$ and $p_0$ are the dimensions of the design matrices $X = \left[ X_0, X_1 \right] \in \mathbb{R}^{n \times p}$ and $X_0 \in \mathbb{R}^{n \times p_0}$ and $\Delta\mathrm{MLL}$ is the difference in maximum log-likelihood between the two model given by \eqref{eq:m0-m1}


**Proof:** Under the conditions mentioned in the theorem, the [F-statistic is defined in terms of the residual sum of squares](/D/fstat) as

$$ \label{eq:F}
F = \frac{(\mathrm{RSS}_0-\mathrm{RSS})/(p-p_0)}{\mathrm{RSS}/(n-p)} \; .
$$

We also know that the [maximum log-likelihood can be expressed in terms of residual sum of squares](/P/mlr-mll):

$$ \label{eq:mlr-mll}
\mathrm{MLL}(m) = - \frac{n}{2} \log\left( \frac{\mathrm{RSS}}{n} \right) - \frac{n}{2} \left[ 1 + \log(2\pi) \right] \; .
$$

Based on this, we see that the difference of the maximum log-likelihoods develops into

$$ \label{eq:dMLL-m1-m0}
\begin{split}
\Delta\mathrm{MLL}
&= \mathrm{MLL}(m_1) - \mathrm{MLL}(m_0) \\
&= \left( - \frac{n}{2} \log\left( \frac{\mathrm{RSS}}{n} \right) - \frac{n}{2} \left[ 1 + \log(2\pi) \right] \right) \\
&- \left( - \frac{n}{2} \log\left( \frac{\mathrm{RSS}_0}{n} \right) - \frac{n}{2} \left[ 1 + \log(2\pi) \right] \right) \\
&= - \frac{n}{2} \log\left( \frac{\mathrm{RSS}}{n} \right) + \frac{n}{2} \log\left( \frac{\mathrm{RSS}_0}{n} \right) \; .
\end{split}
$$

Finally, we [simply perform algebraic operations on both sides](/P/rsq-mll) until we reach the F-statistic on the right side. We start by exponentiating the MLL difference:

$$ \label{eq:F-MLL-qed}
\begin{split}
\exp[\Delta\mathrm{MLL}]
&= \exp\left[ - \frac{n}{2} \log(\mathrm{RSS}/n) + \frac{n}{2} \log(\mathrm{RSS}_0/n) \right] \\
\exp[\Delta\mathrm{MLL}]
&= \left( \exp\left[ \log(\mathrm{RSS}/n) - \log(\mathrm{RSS}_0/n) \right] \right)^{-n/2} \\
\exp[\Delta\mathrm{MLL}]
&= \left( \frac{\exp[\log(\mathrm{RSS}/n)]}{\exp[\log(\mathrm{RSS}_0/n)]} \right)^{-n/2} \\
\exp[\Delta\mathrm{MLL}]
&= \left( \frac{\mathrm{RSS}/n}{\mathrm{RSS}_0/n} \right)^{-n/2} \\
\exp[\Delta\mathrm{MLL}]
&= \left( \frac{\mathrm{RSS}_0}{\mathrm{RSS}} \right)^{n/2} \\
\left( \exp[\Delta\mathrm{MLL}] \right)^{2/n}
&= \frac{\mathrm{RSS}_0}{\mathrm{RSS}} \\
\left( \exp[\Delta\mathrm{MLL}] \right)^{2/n} - 1
&= \frac{\mathrm{RSS}_0}{\mathrm{RSS}} - 1 \\
\left( \exp[\Delta\mathrm{MLL}] \right)^{2/n} - 1
&= \frac{\mathrm{RSS}_0}{\mathrm{RSS}} - \frac{\mathrm{RSS}}{\mathrm{RSS}} \\
\left[ \left( \exp[\Delta\mathrm{MLL}] \right)^{2/n} - 1 \right] \cdot \frac{n-p}{p-p_0}
&= \left[ \frac{\mathrm{RSS}_0 - \mathrm{RSS}}{\mathrm{RSS}} \right] \cdot \frac{n-p}{p-p_0} \\
\left[ \left( \exp[\Delta\mathrm{MLL}] \right)^{2/n} - 1 \right] \cdot \frac{n-p}{p-p_0}
&= \frac{(\mathrm{RSS}_0-\mathrm{RSS})/(p-p_0)}{\mathrm{RSS}/(n-p)} \\
\left[ \left( \exp[\Delta\mathrm{MLL}] \right)^{2/n} - 1 \right] \cdot \frac{n-p}{p-p_0}
&= F \; .
\end{split}
$$

This completes the proof.