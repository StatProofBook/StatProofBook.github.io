---
layout: proof
mathjax: true

author: "Jesse Onland"
affiliation: ""
e_mail: ""
date: 2026-09-28 23:42:00

title: "Maximum likelihood estimation of number of trials from binomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Binomial observations"
theorem: "Maximum likelihood estimation (n)"

sources:
  - authors: "fawadria"
    year: 2020
    title: "Maximum likelihood estimate of N (trials) in Binomial"
    in: "Mathematics Stack Exchange"
    pages: "retrieved on 2026-09-24"
    url: https://math.stackexchange.com/a/3739034

proof_id: "P556"
shortcut: "bin-mlen"
username: "jdonland"
---


**Theorem:** Let $y$ be the number of successes resulting from an unknown number $n$ of independent trials with known success probability $p$, such that $y$ follows a [binomial distribution](/D/bin):

$$ \label{eq:Bin}
y \sim \mathrm{Bin}(n,p) \; .
$$

Suppose $0 < p < 1$. Then, the [maximum likelihood estimator](/D/mle) of $n$ is

$$ \label{eq:Bin-MLE-Trials}
\hat{n} = \begin{cases}
  \lfloor \frac{y}{p} \rfloor \; ,             & \text{if } p \nmid y \\
  \frac{y}{p} \text{ and } \frac{y}{p}-1, \; , & \text{otherwise} \; .
\end{cases}
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

Note that ${n \choose y} = \frac{n!}{y!(n-y)!} = \frac{\Gamma(n+1)}{\Gamma(y+1)\Gamma(n+1-y)}$ and that $\frac{\mathrm{d}}{\mathrm{d}n} \log \Gamma(n) = \psi(n)$ by definition. Now, since $\Gamma(n + 1) = n \Gamma(n)$, we have $\psi(n+1) = \psi(n) + \frac{1}{n}$, so $\psi(n+1)$ differs from the $n$-th harmonic number $H_n = \sum_{k=1}^{n} \frac{1}{k}$ only by a constant.

Thus, the derivative of the log-likelihood function \eqref{eq:Bin-LL} with respect to $n$ is

$$ \label{eq:dLL-dn}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(n)}{\mathrm{d}n} &= \psi(n+1) - \psi(n+1-y) + \log (1-p) \\
&= H_n - H_{n-y} + \log (1-p) \; .
\end{split}
$$

The log-likelihood derivative \eqref{eq:dLL-dn} can be bounded below by $\log\left( \frac{n+1}{n+1-y} \right) + \log(1 - p)$ and above by $\log\left( \frac{n}{n-y} \right) + \log(1 - p)$ using the Hermite-Hadamard inequality.

Since these bounding functions are continuous and monotone for $n > y$, setting them to zero and solving gives bounds for the maximum likelihood estimate of $n$:

$$ \label{eq:n-MLE}
\begin{split}
\log\left( \frac{\hat{n}_\mathrm{lower}+1}{\hat{n}_\mathrm{lower}+1-y} \right) + \log (1 - p) &= 0 \\
\frac{(1 - p)\hat{n}_\mathrm{lower}+1}{\hat{n}_\mathrm{lower}+1-y} &= 1 \\
(1 - p)\hat{n}_\mathrm{lower}+1 &= \hat{n}_\mathrm{lower}+1-y \\
\hat{n}_\mathrm{lower} &= \frac{y}{p} - 1 \; .
\end{split}
$$

Likewise, $\hat{n}_\mathrm{upper} = \frac{y}{p}$.

Thus, we have $\frac{y}{p} - 1 \leq \hat{n} \leq \frac{y}{p}$. If $p \nmid y$, then $\lfloor \frac{y}{p} \rfloor$ is the only integer in this interval. Otherwise, both bounds are integers yielding equal values for the likelihood function.