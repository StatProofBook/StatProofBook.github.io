---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-11-24 14:19:00

title: "Maximum log-likelihood for binomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Binomial observations"
theorem: "Maximum log-likelihood"

sources:

proof_id: "P382"
shortcut: "bin-mll"
username: "JoramSoch"
---


**Theorem:** Let $y$ be the number of successes resulting from $n$ independent trials with unknown success probability $p$, such that $y$ follows a [binomial distribution](/D/bin):

$$ \label{eq:Bin}
y \sim \mathrm{Bin}(n,p) \; .
$$

Then, the [maximum log-likelihood](/D/mll) for this model is

$$ \label{eq:Bin-MLL}
\begin{split}
\mathrm{MLL} &= \log \Gamma(n+1) - \log \Gamma(y+1) - \log \Gamma(n-y+1) \\
&- n \log (n) + y \log (y) + (n-y) \log (n-y) \; .
\end{split}
$$


**Proof:** The [log-likelihood function for binomial data](/P/bin-mle) is given by

$$ \label{eq:Bin-LL}
\mathrm{LL}(p) = \log {n \choose y} + y \log p + (n-y) \log (1-p)
$$

and the [maximum likelihood estimate of the success probability](/P/bin-mle) $p$ is

$$ \label{eq:Bin-MLE}
\hat{p} = \frac{y}{n} \; .
$$

Plugging \eqref{eq:Bin-MLE} into \eqref{eq:Bin-LL}, we obtain the [maximum log-likelihood](/D/mll) of the binomial observation model in \eqref{eq:Bin} as

$$ \label{eq:Bin-MLL-s1}
\begin{split}
\mathrm{MLL} &= \mathrm{LL}(\hat{p}) \\
&= \log {n \choose y} + y \log \left( \frac{y}{n} \right) + (n-y) \log \left( 1 - \frac{y}{n} \right) \\
&= \log {n \choose y} + y \log \left( \frac{y}{n} \right) + (n-y) \log \left( \frac{n-y}{n} \right) \\
&= \log {n \choose y} + y \log (y) + (n-y) \log (n-y) - n \log (n) \; .
\end{split}
$$

With the definition of the binomial coefficient

$$ \label{eq:bin-coeff}
{n \choose k} = \frac{n!}{k! \, (n-k)!}
$$

and the definition of the gamma function

$$ \label{eq:gam-fct}
\Gamma(n) = (n-1)! \; ,
$$

the MLL finally becomes

$$ \label{eq:Bin-MLL-s2}
\begin{split}
\mathrm{MLL} &= \log \Gamma(n+1) - \log \Gamma(y+1) - \log \Gamma(n-y+1) \\
&- n \log (n) + y \log (y) + (n-y) \log (n-y) \; .
\end{split}
$$