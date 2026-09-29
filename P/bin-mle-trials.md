---
layout: proof
mathjax: true

author: "Jesse Onland"
date: 2026-09-28 23:42:00 EDT

title: "Maximum likelihood estimation for binomial trials"
chapter: "Statistical Models"
section: "Count data"
topic: "Binomial observations"
theorem: "Maximum likelihood estimation"

sources:
  - author: "fawadria"
    year: 2020
    in: "Mathematics Stack Exchange"
    pages: "retrieved on 2026-09-24"
    url: https://math.stackexchange.com/a/3739034

proof_id: "????"
shortcut: "bin-mle-trials"
username: "jdonland"
---


**Theorem:** Let $y$ be the number of successes resulting from an unknown number $n$ of independent trials with known success probability $p$, such that $y$ follows a [binomial distribution](/D/bin):

$$ \label{eq:Bin}
y \sim \mathrm{Bin}(n,p) \; .
$$

Suppose $0 < p < 1$. Then, the [maximum likelihood estimator](/D/mle) of $n$ is

$$ \label{eq:Bin-MLE-Trials}
\hat{n} = \begin{cases}
  \lfloor \frac{y}{p} \rfloor, & \text{if } p \nmid y \\
  \frac{y}{p} \text{ and } \frac{y}{p}-1  & \text{otherwise}
\end{cases} \;
$$

**Proof:** With the [probability mass function of the binomial distribution](/P/bin-pmf), equation \eqref{eq:Bin} implies the following [likelihood function](/D/lf):

$$ \label{eq:Bin-LF}
\begin{split}
\mathrm{p}(y|p) &= \mathrm{Bin}(y; n, p) \\
&= {n \choose y} \, p^y \, (1-p)^{n-y} \; .
\end{split}
$$

Thus, the [log-likelihood function](/D/llf) is given by

$$ \label{eq:Bin-LL}
\begin{split}
\mathrm{LL}(p) &= \log \mathrm{p}(y|p) \\
&= \log {n \choose y} + y \log p + (n-y) \log (1-p) \; .
\end{split}
$$

The derivative of the log-likelihood function \eqref{eq:Bin-LL} with respect to $n$ is

$$ \label{eq:dLL-dn}
\frac{\mathrm{d}\mathrm{LL}(p)}{\mathrm{d}n} = H_n - H_{n-y} + \log (1-p)
$$

where $H_n$ is the nth harmonic number.

\eqref{eq:dLL-dn} can be bounded below by $\log (\frac{n+1}{n+1-y}) + \log (1 - p)$ and above by $\log (\frac{n}{n-y}) + \log (1 - p)$ using the Hermite-Hadamard inequality.

Since these bounding functions are continuous and monotone for $n > y$, setting them to zero and solving gives bounds for the MLE for $n$:

$$ \label{eq:n-MLE}
\begin{split}
log (\frac{\hat{n}_{lower}+1}{\hat{n}_{lower}+1-y}) + \log (1 - p) &= 0 \\
\frac{(1 - p)\hat{n}_{lower}+1}{\hat{n}_{lower}+1-y} &= 1 \\
(1 - p)\hat{n}_{lower}+1 &= \hat{n}_{lower}+1-y \\
\hat{n}_{lower} &= \frac{y}{p} - 1
\end{split}
$$

and likewise $\hat{n}_{upper} = frac{y}{p}$.

Thus $\frac{y}{p} - 1 \leq \hat{n} \leq \frac{y}{p}$. If $p \nmid y$, then $\lfloor \frac{y}{p} \rfloor$ is the only integer in this interval. Otherwise, both bounds are integers yielding equal likelihoods.
