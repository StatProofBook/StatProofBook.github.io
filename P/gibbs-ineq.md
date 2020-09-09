---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-09-09 02:18:00

title: "Gibbs' inequality"
chapter: "General Theorems"
section: "Information theory"
topic: "Shannon entropy"
theorem: "Gibbs' inequality"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Gibbs' inequality"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-09-09"
    url: "https://en.wikipedia.org/wiki/Gibbs%27_inequality#Proof"

proof_id: "P164"
shortcut: "gibbs-ineq"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a discrete [random variable](/D/rvar) and consider two [probability distributions](/D/dist) with [probability mass functions](/D/pmf) $p(x)$ and $q(x)$. Then, Gibbs' inequality states that the [entropy](/D/ent) of $X$ according to $P$ is smaller than or equal to the [cross-entropy](/D/ent-cross) of $P$ and $Q$:

$$ \label{eq:Gibbs-ineq}
- \sum_{x \in \mathcal{X}} p(x) \, \log_b p(x) \leq - \sum_{x \in \mathcal{X}} p(x) \, \log_b q(x) \; .
$$


**Proof:** Without loss of generality, we will use the natural logarithm, because a change in the base of the logarithm only implies multiplication by a constant:

$$ \label{eq:log-ln}
\log_b a = \frac{\ln a}{\ln b} \; .
$$

Let $I$ be the of all $x$ for which $p(x)$ is non-zero. Then, proving \eqref{eq:Gibbs-ineq} requires to show that

$$ \label{eq:Gibbs-ineq-s1}
\sum_{x \in I} p(x) \, \ln \frac{p(x)}{q(x)} \geq 0 \; .
$$

Because $\ln x \leq x - 1$, i.e. $-\ln x \geq 1 - x$, for all $x > 0$, with equality only if $x = 1$, we can say about the left-hand side that

$$ \label{eq:Gibbs-ineq-s2}
\begin{split}
\sum_{x \in I} p(x) \, \ln \frac{p(x)}{q(x)} &\geq \sum_{x \in I} p(x) \left( 1 - \frac{p(x)}{q(x)} \right) \\
&= \sum_{x \in I} p(x) - \sum_{x \in I} q(x) \; .
\end{split}
$$

Finally, since $p(x)$ and $q(x)$ are [probability mass functions](/D/pmf), we have

$$ \label{eq:p-q-pmf}
\begin{split}
0 \leq p(x) \leq 1, \quad \sum_{x \in I} p(x) &= 1 \quad \text{and} \\
0 \leq q(x) \leq 1, \quad \sum_{x \in I} q(x) &\leq 1 \; ,
\end{split}
$$

such that it follows from \eqref{eq:Gibbs-ineq-s2} that

$$ \label{eq:Gibbs-ineq-s3}
\begin{split}
\sum_{x \in I} p(x) \, \ln \frac{p(x)}{q(x)} &\geq \sum_{x \in I} p(x) - \sum_{x \in I} q(x) \\
&= 1 - \sum_{x \in I} q(x) \geq 0 \; .
\end{split}
$$