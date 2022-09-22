---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-22 11:45:00

title: "Scaling of the covariance matrix upon multiplication with constant matrix"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
theorem: "Scaling upon multiplication with matrix"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Covariance matrix"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-09-22"
    url: "https://en.wikipedia.org/wiki/Covariance_matrix#Basic_properties"

proof_id: "P348"
shortcut: "covmat-scal"
username: "JoramSoch"
---


**Theorem:** The [covariance matrix](/D/covmat) $\Sigma_{XX}$ of a [random vector](/D/rvec) $X$ scales upon multiplication with a [constant matrix](/D/const) $A$:

$$ \label{eq:covmat-scal}
\Sigma(AX) = A \, \Sigma(X) A^\mathrm{T} \; .
$$


**Proof:** The [covariance matrix](/D/covmat) of $X$ [can be expressed](/P/covmat-mean) in terms of [expected values](/D/mean) as follows:

$$ \label{eq:covmat}
\Sigma_{XX} = \Sigma(X) = \mathrm{E}\left[ (X-\mathrm{E}[X]) (X-\mathrm{E}[X])^\mathrm{T} \right] \; .
$$

Using this and the [linearity of the expected value](/P/mean-lin), we can derive \eqref{eq:covmat-scal} as follows:

$$ \label{eq:covmat-scal-qed}
\begin{split}
\Sigma(AX) &\overset{\eqref{eq:covmat}}{=} \mathrm{E}\left[ ([AX]-\mathrm{E}[AX]) ([AX]-\mathrm{E}[AX])^\mathrm{T} \right] \\
&= \mathrm{E}\left[ (A[X-\mathrm{E}[X]]) (A[X-\mathrm{E}[X]])^\mathrm{T} \right] \\
&= \mathrm{E}\left[ A (X-\mathrm{E}[X]) (X-\mathrm{E}[X])^\mathrm{T} A^\mathrm{T} \right] \\
&= A \, \mathrm{E}\left[ (X-\mathrm{E}[X]) (X-\mathrm{E}[X])^\mathrm{T} \right] A^\mathrm{T} \\
&\overset{\eqref{eq:covmat}}{=} A \, \Sigma(X) A^\mathrm{T} \; .
\end{split}
$$