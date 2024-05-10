---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-03-01 08:42:00

title: "Deviance for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Deviance function"

sources:

proof_id: "P312"
shortcut: "mlr-dev"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr) $m$ with [correlation structure](/D/corrmat) $V$

$$ \label{eq:mlr}
m: \; y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$

Then, the [deviance](/D/dev) for this model is

$$ \label{eq:mlr-dev-v1}
D(\beta,\sigma^2) = \mathrm{RSS}/\sigma^2 + n \cdot \left[ \log(\sigma^2) + \log(2\pi) \right]
$$

under [uncorrelated observations](/D/mlr), i.e. if $V = I_n$, and

$$ \label{eq:mlr-dev-v2}
D(\beta,\sigma^2) = \mathrm{wRSS}/\sigma^2 + n \cdot \left[ \log(\sigma^2) + \log(2\pi) \right] + \log|V| \; ,
$$

in the general case, i.e. if $V \neq I_n$, where $\mathrm{RSS}$ is the [residual sum of squares](/D/rss) and $\mathrm{wRSS}$ is the [weighted residual sum of squares](/P/mlr-wls2).


**Proof:** The [likelihood function](/D/lf) for multiple linear regression [is given by](/P/mlr-mle)

$$ \label{eq:mlr-lf}
\begin{split}
p(y|\beta,\sigma^2) &= \mathcal{N}(y; X\beta, \sigma^2 V) \\
&= \sqrt{\frac{1}{(2\pi)^n |\sigma^2 V|}} \cdot \exp\left[ -\frac{1}{2} (y - X\beta)^\mathrm{T} (\sigma^2 V)^{-1} (y - X\beta) \right] \; ,
\end{split}
$$

such that, with $\lvert \sigma^2 V \rvert = (\sigma^2)^n \lvert V \rvert$, the [log-likelihood function](/D/llf) for this model [becomes](/P/mlr-mle)

$$ \label{eq:mlr-llf}
\begin{split}
\mathrm{LL}(\beta,\sigma^2) &= \log p(y|\beta,\sigma^2) \\
&= - \frac{n}{2} \log(2\pi) - \frac{n}{2} \log (\sigma^2) - \frac{1}{2} \log |V| - \frac{1}{2 \sigma^2} (y - X\beta)^\mathrm{T} V^{-1} (y - X\beta) \; .
\end{split}
$$


The last term can be expressed in terms of the (weighted) [residual sum of squares](/D/rss) as

$$ \label{eq:mll-rss}
\begin{split}
- \frac{1}{2 \sigma^2} (y - X\beta)^\mathrm{T} V^{-1} (y - X\beta) &= - \frac{1}{2 \sigma^2} (Wy-WX\beta)^\mathrm{T} (Wy-WX\beta) \\
&= - \frac{1}{2 \sigma^2} \left( \frac{1}{n} \sum_{i=1}^{n} (W\varepsilon)_i^2 \right) = - \frac{\mathrm{wRSS}}{2 \sigma^2}
\end{split}
$$

where $W = V^{-1/2}$. Plugging \eqref{eq:mll-rss} into \eqref{eq:mlr-llf} and multiplying with $-2$, we obtain the [deviance](/D/dev) as

$$ \label{eq:mlr-dev-v2-qed}
\begin{split}
D(\beta,\sigma^2) &= -2 \, \mathrm{LL}(\beta,\sigma^2) \\
&= -2 \left( - \frac{\mathrm{wRSS}}{2 \sigma^2} - \frac{n}{2} \log (\sigma^2) - \frac{n}{2} \log(2\pi) - \frac{1}{2} \log |V| \right) \\
&= \mathrm{wRSS}/\sigma^2 + n \cdot \left[ \log(\sigma^2) + \log(2\pi) \right] + \log|V|
\end{split}
$$

which proves the result in \eqref{eq:mlr-dev-v2}. Assuming $V = I_n$, we have

$$ \label{eq:mll-rss-iid}
\begin{split}
- \frac{1}{2 \sigma^2} (y - X\beta)^\mathrm{T} V^{-1} (y - X\beta) &= - \frac{1}{2 \sigma^2} (y - X\beta)^\mathrm{T} (y - X\beta) \\
&= - \frac{1}{2 \sigma^2} \left( \frac{1}{n} \sum_{i=1}^{n} \varepsilon_i^2 \right) = - \frac{\mathrm{RSS}}{2 \sigma^2}
\end{split}
$$

and

$$ \label{eq:mlr-logdet-V-iid}
\frac{1}{2} \log|V| = \frac{1}{2} \log|I_n| = \frac{1}{2} \log 1 = 0 \; ,
$$

such that

$$ \label{eq:mlr-mll-v1-qed}
D(\beta,\sigma^2) = \mathrm{RSS}/\sigma^2 + n \cdot \left[ \log(\sigma^2) + \log(2\pi) \right]
$$

which proves the result in \eqref{eq:mlr-dev-v1}. This completes the proof.