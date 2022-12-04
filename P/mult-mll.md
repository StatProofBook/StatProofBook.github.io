---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-02 17:22:00

title: "Maximum log-likelihood for multinomial observations"
chapter: "Statistical Models"
section: "Count data"
topic: "Multinomial observations"
theorem: "Maximum log-likelihood"

sources:

proof_id: "P386"
shortcut: "mult-mll"
username: "JoramSoch"
---


**Theorem:** Let $y = [y_1, \ldots, y_k]$ be the number of observations in $k$ categories resulting from $n$ independent trials with unknown category probabilities $p = [p_1, \ldots, p_k]$, such that $y$ follows a [multinomial distribution](/D/mult):

$$ \label{eq:Mult}
y \sim \mathrm{Mult}(n,p) \; .
$$

Then, the [maximum log-likelihood](/D/mll) for this model is

$$ \label{eq:Mult-MLL}
\mathrm{MLL} = \log \Gamma(n+1) - \sum_{j=1}^{k} \log \Gamma(y_j+1) - n \log (n) + \sum_{j=1}^{k} y_j \log (y_j) \; .
$$


**Proof:** With the [probability mass function of the multinomial distribution](/P/mult-pmf), equation \eqref{eq:Mult} implies the following [likelihood function](/D/lf):

$$ \label{eq:Mult-LF}
\begin{split}
\mathrm{p}(y|p) &= \mathrm{Mult}(y; n, p) \\
&= {n \choose {y_1, \ldots, y_k}} \prod_{j=1}^{k} {p_j}^{y_j} \; .
\end{split}
$$

Thus, the [log-likelihood function](/D/llf) is given by

$$ \label{eq:Mult-LL}
\begin{split}
\mathrm{LL}(p) &= \log \mathrm{p}(y|p) \\
&= \log {n \choose {y_1, \ldots, y_k}} + \sum_{j=1}^{k} y_j \log (p_j) \; .
\end{split}
$$

The [maximum likelihood estimates of the category probabilities](/P/mult-mle) $p$ are

$$ \label{eq:Mult-MLE}
\hat{p} = \left[ \hat{p}_1, \ldots, \hat{p}_k \right] \quad \text{with} \quad \hat{p}_j = \frac{y_j}{n} \quad \text{for all} \quad j = 1, \ldots, k \; .
$$

Plugging \eqref{eq:Mult-MLE} into \eqref{eq:Mult-LL}, we obtain the [maximum log-likelihood](/D/mll) of the multinomial observation model in \eqref{eq:Mult} as

$$ \label{eq:Mult-MLL-s1}
\begin{split}
\mathrm{MLL} &= \mathrm{LL}(\hat{p}) \\
&= \log {n \choose {y_1, \ldots, y_k}} + \sum_{j=1}^{k} y_j \log \left( \frac{y_j}{n} \right) \\
&= \log {n \choose {y_1, \ldots, y_k}} + \sum_{j=1}^{k} \left[ y_j \log (y_j) - y_j \log (n) \right] \\
&= \log {n \choose {y_1, \ldots, y_k}} + \sum_{j=1}^{k}  y_j \log (y_j) - \sum_{j=1}^{k} y_j \log (n) \\
&= \log {n \choose {y_1, \ldots, y_k}} + \sum_{j=1}^{k}  y_j \log (y_j) - n \log (n) \; .
\end{split}
$$

With the definition of the multinomial coefficient

$$ \label{eq:mult-coeff}
{n \choose {k_1, \ldots, k_m}} = \frac{n!}{k_1! \cdot \ldots \cdot k_m!}
$$

and the definition of the gamma function

$$ \label{eq:gam-fct}
\Gamma(n) = (n-1)! \; ,
$$

the MLL finally becomes

$$ \label{eq:Mult-MLL-s2}
\mathrm{MLL} = \log \Gamma(n+1) - \sum_{j=1}^{k} \log \Gamma(y_j+1) - n \log (n) + \sum_{j=1}^{k} y_j \log (y_j) \; .
$$