---
layout: proof
mathjax: true

author: "Salvador Balkus"
affiliation: "Harvard T.H. Chan School of Public Health"
e_mail: "sbalkus@g.harvard.edu"
date: 2024-09-13 23:30:00

title: "The expected value minimizes the mean squared error"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Expected value minimizes squared error"

sources:
  - authors: "Wikipedia"
    year: 2024
    title: "Derivative test"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-09-13"
    url: "https://en.wikipedia.org/wiki/Derivative_test"

proof_id: "P469"
shortcut: "mean-mse"
username: "salbalkus"
---


**Theorem:** Let $X_1, \ldots, X_n$ be a collection of [random variables](/D/rvar) with common [mean](/D/mean) $\mathrm{E}(X_i) = \mu$, $i = 1,\ldots,n$. Then, $\mu$ minimizes the mean squared error:

$$ \label{eq:mean-mse}
\mu = \operatorname*{arg\,min}_{a \in \mathbb{R}} \mathrm{E}\left[ (X_i - a)^2 \right] \; .
$$


**Proof:** Using the [linearity of expectation](/P/mean-lin), we can simplify the objective function:

$$ \label{eq:mse}
\mathrm{E}\left[ (X_i - a)^2 \right] = \mathrm{E}\left[ X_i^2 - 2aX_i + a^2 \right] = a^2 - 2a\mu + \mathrm{E}(X_i^2) \; .
$$

Setting the first derivative

$$ \label{eq:dmse-da}
\frac{d}{da} \left[ a^2 - 2a\mu + \mathrm{E}(X_i^2) \right] = 2a - 2\mu
$$

to zero to perform a derivative test, we obtain:

$$ \label{eq:mean-mse-qed}
2a - 2\mu = 0 \quad \Leftrightarrow \quad a = \mu \; .
$$

The second derivative is equal to 2, which is greater than 0. Since $a = \mu$ is the sole critical point, we can conclude that this value is the unique global minimum. This completes the proof that the expected value minimizes the mean squared error.