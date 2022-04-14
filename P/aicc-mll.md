---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-03-11 16:53:00

title: "Corrected Akaike information criterion in terms of maximum log-likelihood"
chapter: "Model Selection"
section: "Classical information criteria"
topic: "Akaike information criterion"
theorem: "Corrected AIC and maximum log-likelihood"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Akaike information criterion"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-03-11"
    url: "https://en.wikipedia.org/wiki/Akaike_information_criterion#Modification_for_small_sample_size"

proof_id: "P315"
shortcut: "aicc-mll"
username: "JoramSoch"
---


**Theorem:** The [corrected Akaike information criterion](/D/aicc) of a [generative model](/D/gm) with [likelihood function](/D/lf) $p(y \vert \theta, m)$ is equal to

$$ \label{eq:aicc-mll}
\mathrm{AIC}_\mathrm{c}(m) = -2 \log p(y | \hat{\theta}, m) + \frac{2nk}{n-k-1}
$$

where $\log p(y \vert \hat{\theta}, m)$ is the [maximum log-likelihood](/D/mll), $k$ is the number of free parameters and $n$ is the number of observations.


**Proof:** The [Akaike information criterion](/D/aic) (AIC) is defined as

$$ \label{eq:aic}
\mathrm{AIC}(m) = -2 \log p(y | \hat{\theta}, m) + 2 \, k
$$

and the [corrected Akaike information criterion](/D/aicc) is defined as

$$ \label{eq:aicc}
\mathrm{AIC}_\mathrm{c}(m) = \mathrm{AIC}(m) + \frac{2k^2 + 2k}{n-k-1} \; .
$$

Plugging \eqref{eq:aic} into \eqref{eq:aicc}, we obtain:

$$ \label{eq:aicc-mll-qed}
\begin{split}
\mathrm{AIC}_\mathrm{c}(m) &= -2 \log p(y | \hat{\theta}, m) + 2 \, k + \frac{2k^2 + 2k}{n-k-1} \\
&= -2 \log p(y | \hat{\theta}, m) + \frac{2k(n-k-1)}{n-k-1} + \frac{2k^2 + 2k}{n-k-1} \\
&= -2 \log p(y | \hat{\theta}, m) + \frac{2nk - 2k^2 - 2k}{n-k-1} + \frac{2k^2 + 2k}{n-k-1} \\
&= -2 \log p(y | \hat{\theta}, m) + \frac{2nk}{n-k-1} \; .
\end{split}
$$