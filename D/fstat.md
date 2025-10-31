---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2024-03-15 11:31:22

title: "F-statistic"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "F-statistic"
definition: "Definition"

sources:
  - authors: "Wikipedia"
    year: 2024
    title: "F-test"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-03-15"
    url: "https://en.wikipedia.org/wiki/F-test#Regression_problems"

def_id: "D196"
shortcut: "fstat"
username: "JoramSoch"
---


**Definition:** Consider two [linear regression models](/D/mlr) with [independent](/D/ind) observations

$$ \label{eq:m0-m1}
\begin{split}
m_1: \; y &= X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \\
m_0: \; y &= X_0\beta_0 + \varepsilon_0, \; \varepsilon_{0i} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma_0^2)
\end{split}
$$

operating on identical measured data $y$, but with different design matrices $X \in \mathbb{R}^{n \times p}$ and $X_0 \in \mathbb{R}^{n \times p_0}$ and thus different regression coefficients $\beta \in \mathbb{R}^{p \times 1}$ and $\beta_0 \in \mathbb{R}^{p_0 \times 1}$. Furthermore, let the design matrix of the null model be fully contained in the design matrix of the full model:

$$ \label{eq:X-X0-X1}
X = \left[ \begin{array}{cc} X_0 & X_1 \end{array} \right] \; .
$$

Then, the F-statistic for model comparison is defined as the ratio of the difference in [residual sum of squares](/D/rss) between the two models, divided by the difference in [number of parameters](/D/mlr), to the [residual sum of squares](/D/rss) of the full model, divided by the number of [degrees of freedom](/D/dof):

$$ \label{eq:F}
F = \frac{(\mathrm{RSS}_0-\mathrm{RSS})/(p-p_0)}{\mathrm{RSS}/(n-p)} \; .
$$