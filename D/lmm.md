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


**Definition:** For $i = 1, \ldots, m$ and $n = \sum_{i=1}^m n_i$, let $\mathbf y_i$ be an $n_i$-dimensional vector, let $\mathbf X_i$ be an $n_i \times p$ matrix and let $\mathbf Z_i$ be an $n_i \times q$ matrix. Assume that $\mathbf X_i$ is observed and fixed and that $\mathbf Z_i$ contains a subset of the columns of $\mathbf X_i$. Further, let $\boldsymbol \beta$ be a latent $p$-dimensional vector, and let $\boldsymbol \alpha_i \sim \mathcal{N}(\mathbf 0_q, \mathbf S)$ for $i = 1, \ldots, m$ be a latent $q$-dimensional vector.

A linear mixed model of $\mathbf y_i$ is given by a linear combination of the $X_i$ and the $Z_i$

$$ \label{eq:lmm-model}
\mathbf y_i = \mathbf X_i \boldsymbol \beta + \mathbf Z_i \boldsymbol \alpha_i + \boldsymbol \varepsilon_i
$$

where $\boldsymbol \varepsilon_i \sim \mathcal{N}(\mathbf 0_{n_i}, \sigma^2 \mathbf V_i)$ and $\boldsymbol \alpha_1, \ldots, \boldsymbol \alpha_m$ as well as $\boldsymbol \varepsilon_1, \ldots, \boldsymbol \varepsilon_m$ are [statistically independent](/D/ind). When $\mathbf V_i = \mathbf I_{n_i}$, the observations of group $i$ are [conditionally independent](/D/ind-cond) given $\boldsymbol \alpha_i$.

Linear mixed models are an extension of [multiple linear regression](/D/mlr) for grouped data. They split the latent parameters into two types: [Fixed effects](/D/ffx) are shared across all groups; [random effects](/D/rfx) are additional local deviations per group; they are called random, because they are modeled as draws from a [multivariate normal distribution](/D/mvn).

* $m$ is the number of groups;

* $n_i$ is the number of observations for group $i$;

* $n$ is [total number of observations](/D/samp-size);

* $q$ is the number of random effects;

* $\mathbf X_i$ is called the "fixed-effects [design matrix](/D/mlr)";

* $\mathbf Z_i$ is called the "random-effects [design matrix](/D/mlr)";

* $\boldsymbol \beta$ are the "fixed effects";

* $\boldsymbol \alpha_i$ are the "random effects" of group $i$;

* $\mathbf S$ is the "random-effects [covariance matrix](/D/covmat)".

The linear mixed model can also be written in blocked form as

$$ \label{eq:lmm-model-blocked}
\mathbf y = \mathbf X \boldsymbol\beta + \mathbf Z \boldsymbol\alpha + \boldsymbol\varepsilon, \quad
\boldsymbol\alpha \sim \mathcal{N}(\mathbf 0_{mq}, \mathbf I_m \otimes \mathbf S), \quad
\boldsymbol\varepsilon \sim \mathcal{N}(\mathbf 0_n, \sigma^2 \mathbf V)
$$

where $\otimes$ is the Kronecker product, $\mathbf y$, $\mathbf X$, $\boldsymbol\alpha$ and $\boldsymbol\varepsilon$ are stacked vectors and $\mathbf Z$ and $\mathbf V$ are block-diagonal matrices, e.g.

$$ \label{eq:lmm-blocked}
\mathbf y = \left[ \begin{matrix} \mathbf y_1 \\ \vdots \\ \mathbf y_m \end{matrix} \right], \quad
\mathbf Z = \left[ \begin{matrix} \mathbf Z_1 & & \mathbf 0 \\ & \ddots & \\ \mathbf 0 & & \mathbf Z_m \end{matrix} \right] \; .
$$

The mathematical form above assumes a single grouping factor, but extensions for nested grouping factors (e.g. students in classes in schools) and crossed grouping factors (e.g. participants and test items) are possible.