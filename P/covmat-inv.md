---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-22 11:29:00

title: "Invariance of the covariance matrix under addition of constant vector"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance matrix"
theorem: "Invariance under addition of vector"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Covariance matrix"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-09-22"
    url: "https://en.wikipedia.org/wiki/Covariance_matrix#Basic_properties"

proof_id: "P347"
shortcut: "covmat-inv"
username: "JoramSoch"
---


**Theorem:** The [covariance matrix](/D/covmat) $\Sigma_{XX}$ of a [random vector](/D/rvec) $X$ is invariant under addition of a [constant vector](/D/const) $a$:

$$ \label{eq:covmat-inv}
\Sigma(X+a) = \Sigma(X) \; .
$$


**Proof:** The [covariance matrix](/D/covmat) of $X$ [can be expressed](/P/covmat-mean) in terms of [expected values](/D/mean) as follows:

$$ \label{eq:covmat}
\Sigma_{XX} = \Sigma(X) = \mathrm{E}\left[ (X-\mathrm{E}[X]) (X-\mathrm{E}[X])^\mathrm{T} \right] \; .
$$

Using this and the [linearity of the expected value](/P/mean-lin), we can derive \eqref{eq:covmat-inv} as follows:

$$ \label{eq:covmat-inv-qed}
\begin{split}
\Sigma(X+a) &\overset{\eqref{eq:covmat}}{=} \mathrm{E}\left[ ([X+a]-\mathrm{E}[X+a]) ([X+a]-\mathrm{E}[X+a])^\mathrm{T} \right] \\
&= \mathrm{E}\left[ (X + a - \mathrm{E}[X] - a) (X + a - \mathrm{E}[X] - a)^\mathrm{T} \right] \\
&= \mathrm{E}\left[ (X - \mathrm{E}[X]) (X - \mathrm{E}[X])^\mathrm{T} \right] \\
&\overset{\eqref{eq:covmat}}{=} \Sigma(X) \; .
\end{split}
$$