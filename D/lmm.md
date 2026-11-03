---
layout: definition
mathjax: true

author: "Alex Kipnis"
affiliation: "Helmholtz Munich"
e_mail: "adkipnis@mailbox.org"
date: 2026-10-21 16:07:52

title: "Linear mixed model"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Linear mixed model"
definition: "Definition"

sources:
  - authors: "Laird, Nan M.; Ware, James H."
    year: 1982
    title: "Random-Effects Models for Longitudinal Data"
    in: "Biometrics"
    pages: "vol. 38, iss. 4, pp. 963-974"
    doi: "10.2307/2529876"
  - authors: "Fahrmeir, Ludwig; Kneib, Thomas; Lang, Stefan; Marx, Brian"
    year: 2013
    title: "Mixed Models"
    in: "Regression: Models, Methods and Applications"
    doi: "10.1007/978-3-642-34333-9"

def_id: "D243"
shortcut: "lmm"
username: "adkipnis"
---


**Definition:** For $i = 1, \ldots, m$ and $n = \sum_{i=1}^m n_i$, let $\mathbf y_i$ be an $n_i \times 1$ vector, let $\mathbf X_i$ be an $n_i \times p$ matrix and let $\mathbf Z_i$ be an $n_i \times q$ matrix. Assume $\mathbf X_i$ is observed and fixed and $\mathbf Z_i$ contains a subset of the columns of $\mathbf X_i$.

Further, let $\boldsymbol \beta$ be a latent $p \times 1$ vector, and let $\boldsymbol \alpha_i \sim \mathcal N_q(\mathbf 0, \mathbf S)$ be a latent $q \times 1$ vector.

A linear mixed model of $\mathbf y_i$ is a linear combination of the observed data and latent parameters,

$$ \label{eq:lmm-model}
\mathbf y_i = \mathbf X_i \boldsymbol\beta + \mathbf Z_i \boldsymbol\alpha_i + \boldsymbol \varepsilon_i \; ,
$$

where $\boldsymbol \varepsilon_i \sim \mathcal N_{n_i}(\mathbf 0, \sigma^2 \mathbf V_i)$ and $\boldsymbol \alpha_1, \ldots, \boldsymbol \alpha_m, \boldsymbol \varepsilon_1, \ldots, \boldsymbol \varepsilon_m$ are [statistically independent](/D/ind).
When $\mathbf V_i = \mathbf I_{n_i}$, the observations of group $i$ are [conditionally independent](/D/ind-cond) given $\boldsymbol\alpha_i$.

Linear mixed models are an extension of [multiple linear regression](/D/mlr) for grouped data.
They split the latent parameters into two types: *Fixed* effects are shared across all groups.
*Random* effects are additional local deviations per group; they are called random because they are modeled as draws from a [multivariate normal distribution](/D/mvn).
To avoid redundancy, only terms that are new in comparison to the terms in multiple linear regression are explained:

* $m$ is the number of groups;

* $n_i$ is the number of observations for group $i$;

* $q$ is the number of random effects;

* $\mathbf Z_i$ is called the "random-effects design matrix";

* $\boldsymbol \beta$ are the "fixed effects";

* $\boldsymbol \alpha_i$ are group $i$'s "random effects";

* $\mathbf S$ is the "random-effects [covariance matrix](/D/covmat)".


The model can also be written in blocked form as

$$ \label{eq:lmm-model-blocked}
\mathbf y = \mathbf X \boldsymbol\beta + \mathbf Z \boldsymbol\alpha + \boldsymbol\varepsilon \; , \quad \boldsymbol\alpha \sim \mathcal N_{mq}(\mathbf 0, \mathbf I_m \otimes \mathbf S) \; , \quad \boldsymbol\varepsilon \sim \mathcal N_n(\mathbf 0, \sigma^2 \mathbf V) \; ,
$$

where $\otimes$ is the Kronecker product,
$\mathbf y$, $\mathbf X$, $\boldsymbol\alpha$ and $\boldsymbol\varepsilon$ are stacked,
and $\mathbf Z$ and $\mathbf V$ are block diagonal, e.g.

$$ \label{eq:lmm-blocked}
\mathbf y = \left[ \begin{matrix} \mathbf y_1 \\ \vdots \\ \mathbf y_m \end{matrix} \right] \; , \quad
\mathbf Z = \left[ \begin{matrix} \mathbf Z_1 & & \mathbf 0 \\ & \ddots & \\ \mathbf 0 & & \mathbf Z_m \end{matrix} \right] \; .
$$

The form above assumes a single grouping factor, but there are extensions for nested (e.g. students in classes in schools) and crossed (e.g. participants and test items) grouping factors.
