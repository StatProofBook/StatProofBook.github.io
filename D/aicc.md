---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-02-11 06:49:00

title: "Corrected Akaike information criterion"
chapter: "Model Selection"
section: "Classical information criteria"
topic: "Akaike information criterion"
definition: "Corrected AIC"

sources:
  - authors: "Hurvich CM, Tsai CL"
    year: 1989
    title: "Regression and time series model selection in small samples"
    in: "Biometrika"
    pages: "vol. 76, no. 2, pp. 297-307"
    url: "https://academic.oup.com/biomet/article-abstract/76/2/297/265326"
    doi: "10.1093/biomet/76.2.297"

def_id: "D171"
shortcut: "aicc"
username: "JoramSoch"
---


**Definition:** Let $m$ be a [generative model](/D/gm) with [likelihood function](/D/lf) $p(y \vert \theta, m)$ and [maximum likelihood estimates](/D/mle)

$$ \label{eq:MLE}
\hat{\theta} = \operatorname*{arg\,max}_\theta \log p(y | \theta, m) \; .
$$

Then, the [corrected Akaike information criterion](/D/aicc) ($\mathrm{AIC}_\mathrm{c}$) of this model is defined as

$$ \label{eq:AICc}
\mathrm{AIC}_\mathrm{c}(m) = \mathrm{AIC}(m) + \frac{2k^2 + 2k}{n-k-1}
$$

where $\mathrm{AIC}(m)$ is the [Akaike information criterion](/D/aic) and $k$ is the number of free parameters estimated via \eqref{eq:MLE}.