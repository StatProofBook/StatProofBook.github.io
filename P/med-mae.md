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
topic: "Measures of central tendency
theorem: "The median minimizes the mean absolute error"

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
    title: "Jensen's Inequality"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-09-23"
    url: "https://en.wikipedia.org/wiki/Jensen%27s_inequality"
  - authors: "Wikipedia"
    year: 2024
    title: "Convex Function"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-09-23"
    url: "https://en.wikipedia.org/wiki/Convex_function"

proof_id: "P470"
shortcut: "med-mae"
username: "salbalkus"
---


**Theorem:** Let $X_1, \ldots, X_n$ be a collection of continuous [random variables](/D/rvar) drawn from the [probability density function](/D/pdf) $f(x)$ supported on $(-\infty, \infty)$ with common [median](/D/med) $m$. Then, $m$ minimizes the mean absolute error:

$$ \label{eq:med-mae}
m = \operatorname*{arg\,min}_{a \in \mathbb{R}} \mathrm{E}\left[ \lvert X_i - a \rvert \right] \; .
$$


**Proof:** We can find the optimum by performing a derivative test. First, since an absolute value function is not directly differentaible, simplify the objective function by splitting it into two separate integrals like so:

$$ \label{eq:med-mae-split}
E(\lvert X_i - a \rvert) = \int_{-\infty}^a (a - x) f(x)dx + \int_{a}^\infty (x - a) f(x)dx
$$

Now note that $\lvert\frac{\partial}{\partial a}(a - x)f(x)\rvert = \lvert\frac{\partial}{\partial a}(x - a)f(x)\rvert = f(x)$. Consequently, $\int_{-\infty}^af(x) = P(X_i < a)$ and $\int_{a}^\infty f(x) = P(X_i > a)$ both of which must be finite by the [axioms of probability](/D/prob-ax). Therefore, these integrals meet the conditions for [Leibniz's rule](https://en.wikipedia.org/wiki/Leibniz_integral_rule) to be applied.

Applying Leibniz's rule, we can differentiate the objective function as follows:

$$ \label{eq:med-mae-split}
\frac{\partial}{\partial a} \Big(\int_{-\infty}^a (a - x) f(x)dx + \int_{a}^\infty (x - a) f(x)dx\Big) = (a - x)f(x) + \int_{-\infty}^a f(x)dx - (x - a)f(x) - \int_{a}^\infty f(x)dx
$$

Canceling terms and setting this derivative to 0, it must be true that

$$\label{eq:dmed-da}
\int_{-\infty}^a f(x)dx - \int_{a}^\infty f(x)dx = 0 \implies P(X_i < a) = P(X_i > a)
$$

This yields the implication

$$\label{eq:med-mae-qed}
P(X_i < a) = P(X_i > a) \implies P(X_i < a) = 1 - P(X_i < a) \implies P(X_i < a) = 0.5
$$

As a result, $a$ satisfies the [definition of a median](/D/med) at the critical point of the objective function.

Finally, absolute value is a [convex function](https://en.wikipedia.org/wiki/Convex_function), and so is its expected value by [Jensen's inequality](https://en.wikipedia.org/wiki/Jensen%27s_inequality); this implies, since the median is the sole critical point, it must be a global minimum. Therefore, the median must minimize the mean absolute error, completing the proof.

