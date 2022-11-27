---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-23 18:17:00

title: "Maximum likelihood estimation for binomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Binomial observations"
theorem: "Maximum likelihood estimation"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Binomial distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-11-23"
    url: "https://en.wikipedia.org/wiki/Binomial_distribution#Statistical_inference"

proof_id: "P381"
shortcut: "bin-mle"
username: "JoramSoch"
---


**Theorem:** Let $y$ be the number of successes resulting from $n$ independent trials with unknown success probability $p$, such that $y$ follows a [binomial distribution](/D/bin):

$$ \label{eq:Bin}
y \sim \mathrm{Bin}(n,p) \; .
$$

Then, the [maximum likelihood estimator](/D/mle) of $p$ is

$$ \label{eq:Bin-MLE}
\hat{p} = \frac{y}{n} \; .
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

The derivative of the log-likelihood function \eqref{eq:Bin-LL} with respect to $p$ is

$$ \label{eq:dLL-dp}
\frac{\mathrm{d}\mathrm{LL}(p)}{\mathrm{d}p} = \frac{y}{p} - \frac{n-y}{1-p}
$$

and setting this derivative to zero gives the MLE for $p$:

$$ \label{eq:p-MLE}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(p)}{\mathrm{d}\hat{p}} &= 0 \\
0 &= \frac{y}{\hat{p}} - \frac{n-y}{1-\hat{p}} \\
\frac{n-y}{1-\hat{p}} &= \frac{y}{\hat{p}} \\
(n-y) \, \hat{p} &= y \, (1-\hat{p}) \\
n \, \hat{p} - y \, \hat{p} &= y - y \, \hat{p} \\
n \, \hat{p} &= y \\
\hat{p} &= \frac{y}{n} \; .
\end{split}
$$