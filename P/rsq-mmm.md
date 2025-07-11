---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-07-04 12:30:00

title: "Mean, mode and median of the coefficient of determination under the null hypothesis"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "R-squared"
theorem: "Mean/mode/median under null hypothesis"

sources:

proof_id: "P508"
shortcut: "rsq-mmm"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr) with known design matrix $X = \left[ 1_n, \; X_1 \right] \in \mathbb{R}^{n \times p}$, known covariance structure $V$, unknown regression parameters $\beta$ and unknown noise variance $\sigma^2$:

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$

Then, under the [null hypothesis](/D/h0) that the true [coefficient of determination](/D/rsq) is zero, i.e. $H_0: \; R^2 = 0$, the [expected value](/D/mean), the [median](/D/med) and the [mode](/D/mode) of $R^2$ are

$$ \label{eq:rsq-mmm}
\begin{split}
     \mathrm{E}(R^2) &= \frac{p-1}{n-1} \\
\mathrm{median}(R^2) &= I^{-1}\left( \frac{1}{2}; \frac{p-1}{2}, \frac{n-p}{2} \right) \\
  \mathrm{mode}(R^2) &= \frac{p-3}{n-5}
\end{split}
$$

where $I^{-1}(p; a, b)$ is the inverse function of the [regularized incomplete beta function](/P/beta-cdf).


**Proof:** We know that [R-squared follows a beta distribution](/P/rsq-dist) under $H_0$:

$$ \label{eq:rsq-dist}
R^2 \sim \mathrm{Bet}\left( \frac{p-1}{2}, \frac{n-p}{2} \right) \; .
$$

Using [mean](/D/beta-mean), [median](/D/beta-med) and [mode](/D/beta-mode) of the [beta distribution](/D/beta)

$$ \label{eq:beta-mmm}
\begin{split}
                 X &\sim \mathrm{Bet}(\alpha, \beta) \\ \Rightarrow \quad
     \mathrm{E}(X) &= \frac{\alpha}{\alpha+\beta} \\
\mathrm{median}(X) &= I^{-1}\left( 1/2; \alpha, \beta \right) \\
  \mathrm{mode}(X) &= \frac{\alpha-1}{\alpha+\beta-2} \; ,
\end{split}
$$

we have:

$$ \label{eq:rsq-mmm-qed}
\begin{split}
     \mathrm{E}(R^2) &= \frac{(p-1)/2}{(p-1)/2+(n-p)/2} \\
                     &= \frac{p-1}{n-1} \\
\mathrm{median}(R^2) &= I^{-1}\left( 1/2; (p-1)/2, (n-p)/2 \right) \\
                     &= I^{-1}\left( \frac{1}{2}; \frac{p-1}{2}, \frac{n-p}{2} \right) \\
  \mathrm{mode}(R^2) &= \frac{(p-1)/2-1}{(p-1)/2+(n-p)/2-2} \\
                     &= \frac{p-3}{n-5} \; .
\end{split}
$$

This completes the proof.