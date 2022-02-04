---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-02-04 07:27:00

title: "Maximum log-likelihood for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Maximum log-likelihood"

sources:
  - authors: "Claeskens G, Hjort NL"
    year: 2008
    title: "Akaike's information criterion"
    in: "Model Selection and Model Averaging"
    pages: "ex. 2.2, p. 66"
    url: "https://www.cambridge.org/core/books/model-selection-and-model-averaging/E6F1EC77279D1223423BB64FC3A12C37"
    doi: "10.1017/CBO9780511790485"

proof_id: "P305"
shortcut: "mlr-mll"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr) $m$ with [correlation structure](/D/corrmat) $V$

$$ \label{eq:mlr}
m: \; y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; .
$$

Then, the [maximum log-likelihood](/D/mll) for this model is

$$ \label{eq:mlr-mll-v1}
\mathrm{MLL}(m) = - \frac{n}{2} \log\left( \frac{\mathrm{RSS}}{n} \right) - \frac{n}{2} \left[ 1 + \log(2\pi) \right]
$$

under [uncorrelated observations](/D/mlr), i.e. if $V = I_n$, and

$$ \label{eq:mlr-mll-v2}
\mathrm{MLL}(m) = - \frac{n}{2} \log\left( \frac{\mathrm{wRSS}}{n} \right) - \frac{n}{2} \left[ 1 + \log(2\pi) \right] - \frac{1}{2} \log|V| \; ,
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
\mathrm{LL}(\beta,\sigma^2) = &\log p(y|\beta,\sigma^2) \\
= &- \frac{n}{2} \log(2\pi) - \frac{n}{2} \log (\sigma^2) - \frac{1}{2} \log |V| - \frac{1}{2 \sigma^2} (y - X\beta)^\mathrm{T} V^{-1} (y - X\beta) \; .
\end{split}
$$

The [maximum likelihood estimate for the noise variance](/P/mlr-mle) is

$$ \label{eq:mlr-mle-s2}
\hat{\sigma}^2 = \frac{1}{n} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta})
$$

which can also be expressed in terms of the (weighted) [residual sum of squares](/D/rss) as

$$ \label{eq:s2-rss}
\frac{1}{n} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) = \frac{1}{n} (Wy-WX\hat{\beta})^\mathrm{T} (Wy-WX\hat{\beta}) = \frac{1}{n} \sum_{i=1}^{n} (W\hat{\varepsilon})_i^2 = \frac{\mathrm{wRSS}}{n}
$$

where $W = V^{-1/2}$. Plugging \eqref{eq:mlr-mle-s2} into \eqref{eq:mlr-llf}, we obtain the [maximum log-likelihood](/D/mll) as

$$ \label{eq:mlr-mll-v2-qed}
\begin{split}
\mathrm{MLL}(m) &= \mathrm{LL}(\hat{\beta},\hat{\sigma}^2) \\
&= - \frac{n}{2} \log(2\pi) - \frac{n}{2} \log (\hat{\sigma}^2) - \frac{1}{2} \log |V| - \frac{1}{2 \hat{\sigma}^2} (y - X\hat{\beta})^\mathrm{T} V^{-1} (y - X\hat{\beta}) \\
&= - \frac{n}{2} \log(2\pi) - \frac{n}{2} \log\left( \frac{\mathrm{wRSS}}{n} \right) - \frac{1}{2} \log |V| - \frac{1}{2} \cdot \frac{n}{\mathrm{wRSS}} \cdot \mathrm{wRSS} \\
&= - \frac{n}{2} \log\left( \frac{\mathrm{wRSS}}{n} \right) - \frac{n}{2} \left[ 1 + \log(2\pi) \right] - \frac{1}{2} \log|V|
\end{split}
$$

which proves the result in \eqref{eq:mlr-mll-v2}. Assuming $V = I_n$, we have

$$ \label{eq:mlr-mle-s2-iid}
\hat{\sigma}^2 = \frac{1}{n} (y-X\hat{\beta})^\mathrm{T} (y-X\hat{\beta}) = \frac{1}{n} \sum_{i=1}^{n} \hat{\varepsilon}_i^2 = \frac{\mathrm{RSS}}{n}
$$

and

$$ \label{eq:mlr-logdet-V-iid}
\frac{1}{2} \log|V| = \frac{1}{2} \log|I_n| = \frac{1}{2} \log 1 = 0 \; ,
$$

such that

$$ \label{eq:mlr-mll-v1-qed}
\mathrm{MLL}(m) = - \frac{n}{2} \log\left( \frac{\mathrm{RSS}}{n} \right) - \frac{n}{2} \left[ 1 + \log(2\pi) \right]
$$

which proves the result in \eqref{eq:mlr-mll-v1}. This completes the proof.