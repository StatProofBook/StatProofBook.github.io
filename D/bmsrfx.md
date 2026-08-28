---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-06-24 11:43:00

title: "Random-effects Bayesian model selection"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Random-effects Bayesian model selection"
definition: "Definition"

sources:
  - authors: "Stephan KE, Penny WD, Daunizeau J, Moran RJ, Friston KJ"
    year: 2009
    title: "Bayesian model selection for group studies"
    in: "NeuroImage"
    pages: "vol. 46, pp. 1004–1017, eqs. 3-5"
    url: "https://www.sciencedirect.com/science/article/abs/pii/S1053811909002638"
    doi: "10.1016/j.neuroimage.2009.03.025"
  - authors: "Penny WD, Stephan KE, Daunizeau J, Rosa MJ, Friston KJ, Schofield TM, Leff AP"
    year: 2010
    title: "Comparing Families of Dynamic Causal Models"
    in: "PLoS Computational Biology"
    pages: "vol. 6, iss. 3, art. e1000709, eqs. 11-12"
    url: "https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000709"
    doi: "10.1371/journal.pcbi.1000709"
  - authors: "Soch J, Allefeld C"
    year: 2018
    title: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    in: "Journal of Neuroscience Methods"
    pages: "vol. 306, pp. 19-31, eq. 24"
    url: "https://www.sciencedirect.com/science/article/pii/S0165027018301468"
    doi: "10.1016/j.jneumeth.2018.05.017"

def_id: "D235"
shortcut: "bmsrfx"
username: "JoramSoch"
---


**Definition:** Let $\mathcal{M}$ be a set of $K$ [statistical models](/D/fpm) describing a group of $N$ [independent](/D/ind) [data sets](/D/data) $y = \left\lbrace y_1, \ldots, y_N \right\rbrace$ with [model evidences](/D/ml) $p(y_i \vert m)$ for $i = 1,\ldots,N$ and $m \in \mathcal{M}$.

Assume that $m_i \in \left\lbrace 0, 1 \right\rbrace^K$ is a [discrete](/D/disc) [random vector](/D/rvec) specifying the generating model of $y_i$ and let $m_i = e_j$ denote the situation that the $j$-th model generated the $i$-th data set. Then, the model evidences $p(y_i \vert m)$ constitute a [probability distribution](/D/dist) specifying the how likely it is to observe a specific data set given a specific model:

$$ \label{eq:p-y-m}
p(y_i|m_i = e_j)
\quad \mathrm{for} \quad
i = 1,\ldots,N
\quad \mathrm{and} \quad
j = 1,\ldots,K \; .
$$

Moreover, let the generating model for each data set come from a [categorical distribution](/D/cat) with unknown category probabilities, or model frequencies $r = [r_1, \ldots, r_K] \in [0, 1]^K$:

$$ \label{eq:p-m-r}
m_i \sim \mathrm{Cat}(r)
\quad \mathrm{for} \quad
i = 1,\ldots,N \; .
$$

Finally, let the [prior distribution](/D/prior) over model frequencies be a [Dirichlet distribution](/D/dir) with known concentration $\alpha = [\alpha_1, \ldots, \alpha_K] \in \mathbb{R}^K$:

$$ \label{eq:p-r-a}
r \sim \mathrm{Dir}(\alpha) \; .
$$

Taken together, the probability distributions specified by \eqref{eq:p-y-m} and \eqref{eq:p-m-r} and \eqref{eq:p-r-a}, treating generative model as a [random effect](/D/rfx), are called random-effects Bayesian model selection (RFX BMS).