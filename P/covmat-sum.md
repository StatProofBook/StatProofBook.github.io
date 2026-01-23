---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-26 10:37:00

title: "Covariance matrix of the sum of two random vectors"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance matrix"
theorem: "Covariance matrix of a sum"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Covariance matrix"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-09-26"
    url: "https://en.wikipedia.org/wiki/Covariance_matrix#Basic_properties"

proof_id: "P349"
shortcut: "covmat-sum"
username: "JoramSoch"
---


**Theorem:** The [covariance matrix](/D/covmat) of the sum of two [random vectors](/D/rvec) of the same dimension equals the sum of the covariances of those random vectors, plus the sum of their [cross-covariances](/D/covmat-cross):

$$ \label{eq:covmat-sum}
\Sigma(X+Y) = \Sigma_{XX} + \Sigma_{YY} + \Sigma_{XY} + \Sigma_{YX} \; .
$$


**Proof:** The [covariance matrix](/D/covmat) of $X$ [can be expressed](/P/covmat-mean) in terms of [expected values](/D/mean) as follows

$$ \label{eq:covmat}
\Sigma_{XX} = \Sigma(X) = \mathrm{E}\left[ (X-\mathrm{E}[X]) (X-\mathrm{E}[X])^\mathrm{T} \right]
$$

and the [cross-covariance matrix](/D/covmat-cross) of $X$ and $Y$ can similarly be written as

$$ \label{eq:covmat-cross}
\Sigma_{XY} = \Sigma(X,Y) = \mathrm{E}\left[ (X-\mathrm{E}[X]) (Y-\mathrm{E}[Y])^\mathrm{T} \right]
$$

Using this and the [linearity of the expected value](/P/mean-lin) as well as the definitions of [covariance matrix](/D/covmat) and [cross-covariance matrix](/D/covmat-cross), we can derive \eqref{eq:covmat-sum} as follows:

$$ \label{eq:covmat-sum-qed}
\begin{split}
\Sigma(X+Y) &\overset{\eqref{eq:covmat}}{=} \mathrm{E}\left[ ([X+Y]-\mathrm{E}[X+Y]) ([X+Y]-\mathrm{E}[X+Y])^\mathrm{T} \right] \\
&= \mathrm{E}\left[ ([X-\mathrm{E}(X)] + [Y-\mathrm{E}(Y)]) ([X-\mathrm{E}(X)] + [Y-\mathrm{E}(Y)])^\mathrm{T} \right] \\
&= \mathrm{E}\left[ (X-\mathrm{E}[X]) (X-\mathrm{E}[X])^\mathrm{T} + (X-\mathrm{E}[X]) (Y-\mathrm{E}[Y])^\mathrm{T} + (Y-\mathrm{E}[Y]) (X-\mathrm{E}[X])^\mathrm{T} + (Y-\mathrm{E}[Y]) (Y-\mathrm{E}[Y])^\mathrm{T} \right] \\
&= \mathrm{E}\left[ (X-\mathrm{E}[X]) (X-\mathrm{E}[X])^\mathrm{T} \right] + \mathrm{E}\left[ (X-\mathrm{E}[X]) (Y-\mathrm{E}[Y])^\mathrm{T} \right] + \mathrm{E}\left[ (Y-\mathrm{E}[Y]) (X-\mathrm{E}[X])^\mathrm{T} \right] + \mathrm{E}\left[ (Y-\mathrm{E}[Y]) (Y-\mathrm{E}[Y])^\mathrm{T} \right] \\
&\overset{\eqref{eq:covmat}}{=} \Sigma_{XX} + \Sigma_{YY} + \mathrm{E}\left[ (X-\mathrm{E}[X]) (Y-\mathrm{E}[Y])^\mathrm{T} \right] + \mathrm{E}\left[ (Y-\mathrm{E}[Y]) (X-\mathrm{E}[X])^\mathrm{T} \right] \\
&\overset{\eqref{eq:covmat-cross}}{=} \Sigma_{XX} + \Sigma_{YY} + \Sigma_{XY} + \Sigma_{YX} \; .
\end{split}
$$