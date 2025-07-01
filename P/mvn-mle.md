---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-06-20 17:22:00

title: "Maximum likelihood estimation for multivariate normally distributed data"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Multivariate Gaussian"
definition: "Maximum likelihood estimation (p > 2)"

sources:
  - authors: "Alt"
    year: 2014
    title: "MLE of multivariate (bivariate) normal distribution"
    in: "StackExchange Mathematics"
    pages: "retrieved on 2025-07-01"
    url: "https://math.stackexchange.com/a/688030"
  - authors: "Petersen, Kaare Brandt; Pedersen, Michael Syskind"
    year: 2012
    title: "Derivatives"
    in: "The Matrix Cookbook"
    pages: "Section 2, eqs. (100), (117), (57), (124)"
    url: "https://www2.imm.dtu.dk/pubdb/pubs/3274-full.html"
  - authors: "Wikipedia"
    year: 2025
    title: "Multivariate normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-07-01"
    url: "https://en.wikipedia.org/wiki/Multivariate_normal_distribution#Parameter_estimation"

proof_id: "P504"
shortcut: "mvn-mle"
username: "JoramSoch"
---


**Theorem:** Let there be a [multivariate normally distributed data set](/D/mvn-data) $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$:

$$ \label{eq:mvn-data}
y_i = \left[ \begin{matrix} y_{i1} \\ \vdots \\ y_{ip} \end{matrix} \right] \sim \mathcal{N}\left( \mu, \Sigma \right), \quad i = 1, \ldots, n \; .
$$

Then, the [maximum likelihood estimates](/D/mle) of $\mu$ and $\Sigma$ are given by

$$ \label{eq:mvn-mle}
\begin{split}
\hat{\mu}    &= \frac{1}{n} \sum_{i=1}^n y_i \\
\hat{\Sigma} &= \frac{1}{n} \sum_{i=1}^n (y_i - \hat{\mu}) (y_i - \hat{\mu})^\mathrm{T} \; .
\end{split}
$$


**Proof:** With the [probability density function of the multivariate normal distribution](/P/mvn-pdf), the likelihood function for a [single data point](/D/data) is

$$ \label{eq:mvn-lf-yi}
\begin{split}
   p(y_i|\mu,\Sigma)
&= \mathcal{N}(y_i; \mu, \sigma^2) \\
&= \frac{1}{\sqrt{(2 \pi)^p |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (y_i-\mu)^\mathrm{T} \Sigma^{-1} (y_i-\mu) \right]
\end{split}
$$

and all data points are [independent](/D/ind), the total likelihood function [is equal to the product](/P/prob-ind) of the individual likelihood functions:

$$ \label{eq:mvn-lf-y}
\begin{split}
   p(y|\mu,\Sigma)
&= \prod_{i=1}^n p(y_i|\mu,\Sigma) \\
&= \frac{1}{\sqrt{(2 \pi)^{np} |\Sigma|^n}} \cdot \exp \left[ -\frac{1}{2} \sum_{i=1}^n (y_i-\mu)^\mathrm{T} \Sigma^{-1} (y_i-\mu) \right] \; .
\end{split}
$$

Thus, the [log-likelihood function](/D/llf) is

$$ \label{eq:mvn-LL}
\begin{split}
   \mathrm{LL}(\mu,\Sigma)
&= \log p(y|\mu,\Sigma) \\
&= - \frac{np}{2} \log(2\pi) - \frac{n}{2} \log|\Sigma| - \frac{1}{2} \sum_{i=1}^n (y_i-\mu)^\mathrm{T} \Sigma^{-1} (y_i-\mu) \\
&= - \frac{np}{2} \log(2\pi) - \frac{n}{2} \log|\Sigma| - \frac{1}{2} \sum_{i=1}^n \left( y_i^\mathrm{T} \Sigma^{-1} y_i - 2 \mu^\mathrm{T} \Sigma^{-1} y_i + \mu^\mathrm{T} \Sigma^{-1} \mu \right) \; .
\end{split}
$$

The derivative of the log-likelihood function \eqref{eq:mvn-LL} with respect to $\mu$ is

$$ \label{eq:dLL-dmu}
\begin{split}
   \frac{\mathrm{d}\mathrm{LL}(\mu,\Sigma)}{\mathrm{d}\mu}
&= \frac{\mathrm{d}}{\mathrm{d}\mu} \left[ - \frac{1}{2} \sum_{i=1}^n \left( y_i^\mathrm{T} \Sigma^{-1} y_i - 2 \mu^\mathrm{T} \Sigma^{-1} y_i + \mu^\mathrm{T} \Sigma^{-1} \mu \right) \right] \\
&= -\frac{1}{2} \sum_{i=1}^n \left( - 2 \Sigma^{-1} y_i + 2 \Sigma^{-1} \mu \right) \\
&= \sum_{i=1}^n \left( \Sigma^{-1} y_i  - \Sigma^{-1} \mu \right)
\end{split}
$$

and setting this derivative to zero gives the MLE for $\mu$:

$$ \label{eq:mu-mle}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\mu},\Sigma)}{\mathrm{d}\mu} &= 0_p \\
0_p &= \sum_{i=1}^n \left( \Sigma^{-1} y_i - \Sigma^{-1} \hat{\mu} \right) \\
0_p &= \Sigma^{-1} \sum_{i=1}^n \left( y_i - \hat{\mu} \right) \\
0_p &= \sum_{i=1}^n y_i - n \cdot \hat{\mu} \\
\hat{\mu} &= \frac{1}{n} \sum_{i=1}^n y_i \; .
\end{split}
$$

The derivative of the log-likelihood function \eqref{eq:mvn-LL} at $\hat{\mu}$ with respect to $\Sigma$ is

$$ \label{eq:dLL-dS}
\begin{split}
   \frac{\mathrm{d}\mathrm{LL}(\hat{\mu},\Sigma)}{\mathrm{d}\Sigma}
&= -\frac{n}{2} \frac{\mathrm{d}}{\mathrm{d}\Sigma} \left[ \log|\Sigma| \right] -\frac{1}{2} \frac{\mathrm{d}}{\mathrm{d}\Sigma} \left[ \sum_{i=1}^n (y_i-\mu)^\mathrm{T} \Sigma^{-1} (y_i-\mu) \right] \\
&= -\frac{n}{2} \left( \Sigma^{-1} \right)^\mathrm{T} -\frac{1}{2} \sum_{i=1}^n \frac{\mathrm{d}}{\mathrm{d}\Sigma} \left[ \mathrm{tr} \left( (y_i-\mu)^\mathrm{T} \Sigma^{-1} (y_i-\mu) \right) \right] \\
&= -\frac{n}{2} \Sigma^{-1} -\frac{1}{2} \sum_{i=1}^n \frac{\mathrm{d}}{\mathrm{d}\Sigma} \left[ \mathrm{tr} \left( \Sigma^{-1} (y_i-\mu) (y_i-\mu)^\mathrm{T} \right) \right] \\
&= -\frac{n}{2} \Sigma^{-1} -\frac{1}{2} \sum_{i=1}^n \left[ -\left( \Sigma^{-1} (y_i-\mu) (y_i-\mu)^\mathrm{T} \Sigma^{-1} \right)^\mathrm{T} \right] \\
&= -\frac{n}{2} \Sigma^{-1} +\frac{1}{2} \sum_{i=1}^n \left[ \Sigma^{-1} (y_i-\mu) (y_i-\mu)^\mathrm{T} \Sigma^{-1} \right]
\end{split}
$$

and setting this derivative to zero gives the MLE for $\Sigma$:

$$ \label{eq:S-mle}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\mu},\hat{\Sigma})}{\mathrm{d}\Sigma} &= 0_{pp} \\
0_{pp} &= -\frac{n}{2} \hat{\Sigma}^{-1} +\frac{1}{2} \sum_{i=1}^n \left[ \hat{\Sigma}^{-1} (y_i-\mu) (y_i-\mu)^\mathrm{T} \hat{\Sigma}^{-1} \right] \\
\hat{\Sigma}^{-1} &= \frac{1}{n} \Sigma^{-1} \left( \sum_{i=1}^n (y_i-\mu) (y_i-\mu)^\mathrm{T} \right) \Sigma^{-1} \\
\hat{\Sigma} \hat{\Sigma}^{-1} \hat{\Sigma} &= \frac{1}{n} \hat{\Sigma} \Sigma^{-1} \left( \sum_{i=1}^n (y_i-\mu) (y_i-\mu)^\mathrm{T} \right) \Sigma^{-1} \hat{\Sigma} \\
I_p \hat{\Sigma} &= \frac{1}{n} I_p \left( \sum_{i=1}^n (y_i-\mu) (y_i-\mu)^\mathrm{T} \right) I_p \\
\hat{\Sigma} &= \frac{1}{n} \sum_{i=1}^n (y_i-\mu) (y_i-\mu)^\mathrm{T} \\
\end{split}
$$

Together, \eqref{eq:mu-mle} and \eqref{eq:S-mle} constitute the [maximum likelihood estimates](/D/mle) for [multivariate normally distributed data](/D/mvn-data).