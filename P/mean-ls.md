---
layout: proof
mathjax: true

author: "Salvador Balkus"
affiliation: "Harvard T.H. Chan School of Public Health"
e_mail: "sbalkus@g.harvard.edu"
date: 2024-09-13 23:30:00

title: "Expected value minimizes expected squared error"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Expected value minimizes expected squared error"

sources:

proof_id: "P0"
shortcut: "mean-ls"
username: "salbalkus"
---


**Theorem:** Let $X_1, X_2, \ldots, X_n$ be a collection of [random variables](/D/rvar) with common [mean](/D/mean) $E(X_i) = \mu$. Then, $\mu$ minimizes the mean squared error; that is,

$$
  \text{argmin}_{a \in \mathbb{R}} E\Big((X_i - a)^2\Big) = \mu
$$

**Proof:** Using the [linearity of expectation](/P/mean-lin) we can simplify the objective function like so:

$$
E\Big((X_i - a)^2\Big) = E\Big(X_i^2 - 2aX_i + a^2\Big) = a^2 - 2a\mu + E(X_i^2)
$$

Setting $\frac{d}{da}a^2 - 2a\mu + E(X_i^2) = 0$ to perform a [derivative test](https://en.wikipedia.org/wiki/Derivative_test), we can compute the derivative to obtain

$$
2a - 2\mu = 0 \implies a = \mu
$$

The second derivative is equal to 2, which is greater than 0; since this is the sole critical point, we can conclude by the second derivative test that this value is the unique global minimum. This completes the proof that $\text{argmin}_{a \in \mathbb{R}} E\Big((X_i - a)^2\Big) = \mu$.
