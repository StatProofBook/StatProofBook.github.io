---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-06-06 05:31:00

title: "Partition of a covariance matrix into expected values"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
theorem: "Covariance matrix and expected values"

sources:
  - authors: "Taboga, Marco"
    year: 2010
    title: "Covariance matrix"
    in: "Lectures on probability and statistics"
    pages: "retrieved on 2020-06-06"
    url: "https://www.statlect.com/fundamentals-of-probability/covariance-matrix"

proof_id: "P120"
shortcut: "covmat-mean"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec). Then, the [covariance matrix](/D/covmat) of $X$ is equal to the [mean](/D/mean) of the outer product of $X$ with itself minus the outer product of the [mean](/D/mean) of $X$ with itself:

$$ \label{eq:covmat-mean}
\Sigma_{XX} = \mathrm{E}(X X^\mathrm{T}) - \mathrm{E}(X) \mathrm{E}(X)^\mathrm{T} \; .
$$


**Proof:** The [covariance matrix](/D/covmat) of $X$ is defined as

$$ \label{eq:covmat1}
\Sigma_{XX} =
\begin{bmatrix}
\mathrm{E}\left[ (X_1-\mathrm{E}[X_1]) (X_1-\mathrm{E}[X_1]) \right] & \ldots & \mathrm{E}\left[ (X_1-\mathrm{E}[X_1]) (X_n-\mathrm{E}[X_n]) \right] \\
\vdots & \ddots & \vdots \\
\mathrm{E}\left[ (X_n-\mathrm{E}[X_n]) (X_1-\mathrm{E}[X_1]) \right] & \ldots & \mathrm{E}\left[ (X_n-\mathrm{E}[X_n]) (X_n-\mathrm{E}[X_n]) \right]
\end{bmatrix}
$$

which can also be expressed using matrix multiplication as

$$ \label{eq:covmat2}
\Sigma_{XX} = \mathrm{E}\left[ (X-\mathrm{E}[X]) (X-\mathrm{E}[X])^\mathrm{T} \right]
$$

Due to the [linearity of the expected value](/P/mean-lin), this can be rewritten as

$$ \label{eq:covmat-mean-qed}
\begin{split}
\Sigma_{XX} &= \mathrm{E}\left[ (X-\mathrm{E}[X]) (X-\mathrm{E}[X])^\mathrm{T} \right] \\
&= \mathrm{E}\left[ X X^\mathrm{T} - X \, \mathrm{E}(X)^\mathrm{T} - \mathrm{E}(X) \, X^\mathrm{T} + \mathrm{E}(X) \mathrm{E}(X)^\mathrm{T} \right] \\
&= \mathrm{E}(X X^\mathrm{T}) - \mathrm{E}(X) \mathrm{E}(X)^\mathrm{T} - \mathrm{E}(X) \mathrm{E}(X)^\mathrm{T} + \mathrm{E}(X) \mathrm{E}(X)^\mathrm{T} \\
&= \mathrm{E}(X X^\mathrm{T}) - \mathrm{E}(X) \mathrm{E}(X)^\mathrm{T} \; .
\end{split}
$$