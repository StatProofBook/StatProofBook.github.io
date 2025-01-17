---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-01-10 12:27:58

title: "Chebyshev's inequality"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Chebyshev's inequality"

sources:
  - authors: "Wikipedia"
    year: 2025
    title: "Chebyshev's inequality"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-01-10"
    url: "https://en.wikipedia.org/wiki/Chebyshev%27s_inequality#Proof"

proof_id: "P482"
shortcut: "cheb-ineq"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) with finite [expected value](/D/mean) $\mu$ and finite [variance](/D/var) $\sigma^2$. Then, for any positive real number $k > 0$, the following inequality holds:

$$ \label{eq:cheb-ineq}
\mathrm{Pr}\left( |X-\mu| \geq k \sigma \right) \leq \frac{1}{k^2} \; .
$$


**Proof:** [Markov's inequality](/P/mark-ineq) states that, for any positive real number $a > 0$, the [probability](/D/prob) that $Y$ is larger than or equal to $a$ is smaller than or equal to the [expected value](/D/mean) of $Y$, divided by $a$:

$$ \label{eq:mark-ineq}
\mathrm{Pr}(Y \geq a) \leq \frac{\mathrm{E}(Y)}{a} \; .
$$

The [variance of a random variable](/D/var) is defined as:

$$ \label{eq:var}
\sigma^2 = \mathrm{Var}(X) = \mathrm{E}\left[ (X-\mu)^2 \right]
\quad \text{where} \quad
\mu = \mathrm{E}(X) \; .
$$

Let $Y = (X-\mu)^2$ and $a = (k \sigma)^2$. Using Markov's inequality, we then have:

$$ \label{eq:cheb-ineq-qed}
\begin{split}
   \mathrm{Pr}\left( |X-\mu| \geq k \sigma \right)
&= \mathrm{Pr}\left( (X-\mu)^2 \geq (k \sigma)^2 \right) \\
&\overset{\eqref{eq:mark-ineq}}{\leq} \frac{\mathrm{E}\left[ (X-\mu)^2 \right]}{(k \sigma)^2} \\
&\overset{\eqref{eq:var}}{=} \frac{\sigma^2}{k^2 \sigma^2} \\
&= \frac{1}{k^2} \; .
\end{split}
$$