---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-12-07 08:43:00

title: "Sampling from the matrix-normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Drawing samples"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Matrix normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-12-07"
    url: "https://en.wikipedia.org/wiki/Matrix_normal_distribution#Drawing_values_from_the_distribution"

proof_id: "P297"
shortcut: "matn-samp"
username: "JoramSoch"
---


**Theorem:** Let $X \in \mathbb{R}^{n \times p}$ be a [random matrix](/D/rmat) with all entries independently following a [standard normal distribution](/D/snorm). Moreover, let $A \in \mathbb{R}^{n \times n}$ and $B \in \mathbb{R}^{p \times p}$, such that $A A^\mathrm{T} = U$ and $B^\mathrm{T} B = V$. Then, $Y = M + A X B$ follows a [matrix-normal distribution](/D/matn) with [mean](/D/mean-rmat) $M$, [covariance](/D/covmat) across rows $U$ and [covariance](/D/covmat) across rows $U$:

$$ \label{eq:matn-samp}
Y = M + A X B \sim \mathcal{MN}(M, U, V) \; .
$$


**Proof:** If all entries of $X$ are independent and [standard normally distributed](/D/snorm)

$$ \label{eq:xij-dist}
x_{ij} \sim \mathcal{N}(0, 1) \quad \text{ind. for all} \quad i = 1,\ldots,n \quad \text{and} \quad j = 1,\ldots,p \; ,
$$

this [implies a multivariate normal distribution with diagonal covariance matrix](/P/mvn-ind):

$$ \label{eq:vecX-dist}
\begin{split}
\mathrm{vec}(X) &\sim \mathcal{N}\left(\mathrm{vec}(0_{np}), I_{np} \right) \\
&\sim \mathcal{N}\left(\mathrm{vec}(0_{np}), I_p \otimes I_n \right) \; .
\end{split}
$$

where $0_{np}$ is an $n \times p$ matrix of zeros and $I_n$ is the $n \times n$ identity matrix.

Due to the [relationship between multivariate and matrix-normal distribution](/P/matn-mvn), we have:

$$ \label{eq:X-dist}
X \sim \mathcal{MN}(0_{np}, I_n, I_p) \; .
$$

Thus, [with the linear transformation theorem for the matrix-normal distribution](/P/matn-ltt), it follows that

$$ \label{eq:matn-samp-qed}
\begin{split}
Y = M + AXB &\sim \mathcal{MN}\left(M + A 0_{np} B, A I_n A^\mathrm{T}, B^\mathrm{T} I_p B \right) \\
&\sim \mathcal{MN}\left(M, A A^\mathrm{T}, B^\mathrm{T} B \right) \\
&\sim \mathcal{MN}\left(M, U, V \right) \; .
\end{split}
$$

Thus, given $X$ defined by \eqref{eq:xij-dist}, $Y$ defined by \eqref{eq:matn-samp} is a [sample](/D/samp) from $\mathcal{N}\left(M, U, V \right)$.