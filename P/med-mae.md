---
layout: proof
mathjax: true

author: "Salvador Balkus"
affiliation: "Harvard T.H. Chan School of Public Health"
e_mail: "sbalkus@g.harvard.edu"
date: 2024-09-23 23:30:00

title: "The median minimizes the mean absolute error"
chapter: "General Theorems"
section: "Probability theory"
topic: "Measures of central tendency"
theorem: "Median minimizes mean absolute error"

sources:
  - authors: "Wikipedia"
    year: 2024
    title: "Derivative test"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-09-23"
    url: "https://en.wikipedia.org/wiki/Derivative_test"
  - authors: "Wikipedia"
    year: 2024
    title: "Leibniz integral rule"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-09-23"
    url: "https://en.wikipedia.org/wiki/Leibniz_integral_rule"
  - authors: "Wikipedia"
    year: 2024
    title: "Jensen's inequality"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-09-23"
    url: "https://en.wikipedia.org/wiki/Jensen%27s_inequality"
  - authors: "Wikipedia"
    year: 2024
    title: "Convex function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-09-23"
    url: "https://en.wikipedia.org/wiki/Convex_function"

proof_id: "P471"
shortcut: "med-mae"
username: "salbalkus"
---


**Theorem:** Let $X_1, \ldots, X_n$ be a collection of [continuous](/D/rvar-disc) [random variables](/D/rvar) drawn from a [probability distribution](/D/dist) with the [probability density function](/D/pdf) $f(x)$ supported on $(-\infty, \infty)$ with common [median](/D/med) $m$. Then, $m$ minimizes the mean absolute error:

$$ \label{eq:med-mae}
m = \operatorname*{arg\,min}_{a \in \mathbb{R}} \mathrm{E}\left[ \lvert X_i - a \rvert \right] \; .
$$


**Proof:** We can find the optimum by performing a derivative test. First, since an absolute value function is not differentaible at 0, we simplify the objective function by splitting it into two separate integrals:

$$ \label{eq:med-mae-s1}
E(\lvert X_i - a \rvert) = \int_{-\infty}^a (a - x) f(x) \, \mathrm{d}x + \int_{a}^\infty (x - a) f(x) \, \mathrm{d}x \; .
$$

Now note that $\lvert\frac{\partial}{\partial a}(a - x)f(x)\rvert = \lvert\frac{\partial}{\partial a}(x - a)f(x)\rvert = f(x)$. Consequently, $\int_{-\infty}^af(x) = P(X_i < a)$ and $\int_{a}^\infty f(x) = P(X_i > a)$, both of which must be finite by the [axioms of probability](/D/prob-ax). Therefore, these integrals meet the conditions for application of Leibniz's integral rule.

Applying Leibniz's rule, we can differentiate the objective function as follows:

$$ \label{eq:med-mae-s2}
\frac{\partial}{\partial a} \left( \int_{-\infty}^a (a - x) f(x) \, \mathrm{d}x + \int_{a}^\infty (x - a) f(x) \, \mathrm{d}x \right) = (a - x) f(x) + \int_{-\infty}^a f(x) \, \mathrm{d}x - (x - a) f(x) - \int_{a}^\infty f(x) \, \mathrm{d}x \; .
$$

Canceling terms and setting this derivative to 0, it must be true that

$$\label{eq:dmed-da}
\int_{-\infty}^a f(x) \, \mathrm{d}x - \int_{a}^\infty f(x) \, \mathrm{d}x = 0
\quad \Rightarrow \quad
P(X_i < a) = P(X_i > a) \; .
$$

This yields the implication

$$\label{eq:med-mae-qed}
P(X_i < a) = P(X_i > a)
\quad \Rightarrow \quad 
P(X_i < a) = 1 - P(X_i < a)
\quad \Rightarrow \quad
P(X_i < a) = 0.5
$$

As a result, $a$ satisfies the [definition of a median](/D/med) at the critical point of the objective function.

Finally, the absolute value is a convex function, and so is its expected value by Jensen's inequality. This implies, since the median is the sole critical point, it must be a global minimum. Therefore, the median must minimize the mean absolute error, completing the proof.