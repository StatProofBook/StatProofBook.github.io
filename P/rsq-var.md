---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-07-04 13:12:00

title: "Variance of the coefficient of determination under the null hypothesis"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "R-squared"
theorem: "Variance under null hypothesis"

sources:

proof_id: "P509"
shortcut: "rsq-var"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr) with known design matrix $X = \left[ 1_n, \; X_1 \right] \in \mathbb{R}^{n \times p}$, known covariance structure $V$, unknown regression parameters $\beta$ and unknown noise variance $\sigma^2$:

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$

Then, under the [null hypothesis](/D/h0) that the true [coefficient of determination](/D/rsq) is zero, i.e. $H_0: \; R^2 = 0$, the [variance](/D/var) of the coefficient of determination is

$$ \label{eq:rsq-var}
\mathrm{Var}(R^2) = 2 \cdot \frac{(p-1) \cdot (n-p)}{(n+1) \cdot (n-1)^2} \; .
$$


**Proof:** We know that [R-squared follows a beta distribution](/P/rsq-dist) under $H_0$:

$$ \label{eq:rsq-dist}
R^2 \sim \mathrm{Bet}\left( \frac{p-1}{2}, \frac{n-p}{2} \right) \; .
$$

Using the [variance of the beta distribution](/P/beta-var)

$$ \label{eq:beta-var}
X \sim \mathrm{Bet}(\alpha, \beta) \\
\quad \Rightarrow \quad
\mathrm{Var}(X) = \frac{\alpha \beta}{(\alpha+\beta+1) \cdot (\alpha+\beta)^2} \; ,
$$

we have:

$$ \label{eq:rsq-var-qed}
\begin{split}
\mathrm{Var}(R^2) &= \frac{\frac{p-1}{2} \cdot \frac{n-p}{2}}{\left( \frac{p-1}{2} + \frac{n-p}{2} + 1 \right) \cdot \left( \frac{p-1}{2} + \frac{n-p}{2} \right)^2} \\
                  &= \frac{\frac{(p-1) \cdot (n-p)}{4}}{\frac{1}{2} \cdot (n+1) \cdot \frac{(n-1)^2}{4}} \\
                  &= 2 \cdot \frac{(p-1) \cdot (n-p)}{(n+1) \cdot (n-1)^2} \; .
\end{split}
$$

This completes the proof.