---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-06-24 12:21:00

title: "Redundancy of parameters describing the matrix-normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Redundancy of parameters"

sources:
  - authors: "Glanz, Hunter; Carvalho, Luis"
    year: 2013
    title: "An Expectation-Maximization Algorithm for the Matrix Normal Distribution"
    in: "arXiv stat.ME"
    pages: "sect. 2.1, p. 3"
    url: "https://arxiv.org/abs/1309.6609"
    doi: "10.48550/arXiv.1309.6609"

proof_id: "P506"
shortcut: "matn-red2"
username: "JoramSoch"
---


**Theorem:** The [covariance parameters of the matrix-normal distribution](/D/matn) are redundant up to a scalar factor, i.e. the two [probability distributions](/D/dist)

$$ \label{eq:matn-red}
\begin{split}
X &\sim \mathcal{MN}(M, U, V) \\
X &\sim \mathcal{MN}\left( M, a \cdot U, \frac{1}{a} \cdot V \right)
\end{split}
$$

are equivalent for any $a \in \mathbb{R}$ with $a > 0$ where $X \in \mathbb{R}^{n \times p}$ is a [random matrix](/D/rmat) and $U \in \mathbb{R}^{n \times n}$ and $V \in \mathbb{R}^{p \times p}$ are positive-definite matrices.


**Proof:** The [probability density function of the matrix-normal distribution](/P/matn-pdf) is

$$ \label{eq:matn}
\begin{split}
X &\sim \mathcal{MN}(M, U, V) \\
\Rightarrow \quad
f(X) &= \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( V^{-1} (X-M)^\mathrm{T} \, U^{-1} (X-M) \right) \right] \; .
\end{split}
$$

Using the inverse matrix property $(cA)^{-1} = (1/c) A^{-1}$ and the matrix determinant property $\lvert cA \rvert = c^n \lvert A \rvert$, the [probability density function](/D/pdf) of the second distribution in \eqref{eq:matn-red} becomes

$$ \label{eq:matn-red-qed}
\begin{split}
   p(X)
&= \frac{1}{\sqrt{(2\pi)^{np} \left| \frac{1}{a} V \right|^n \left| a U \right|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( \left( \frac{1}{a} V \right)^{-1} (X-M)^\mathrm{T} \, \left( a U \right)^{-1} (X-M) \right) \right] \\
&= \frac{1}{\sqrt{(2\pi)^{np} \left( \left( \frac{1}{a} \right)^p |V| \right)^n \left( a^n |U| \right)^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( \frac{a}{a} V^{-1} (X-M)^\mathrm{T} \, U^{-1} (X-M) \right) \right] \\
&= \frac{1}{\sqrt{(2\pi)^{np} \left( \frac{1}{a} \right)^{np} a^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( V^{-1} (X-M)^\mathrm{T} \, U^{-1} (X-M) \right) \right] \\
&= \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( V^{-1} (X-M)^\mathrm{T} \, U^{-1} (X-M) \right) \right]
\end{split}
$$

which is equal to the [probability density function](/D/pdf) of the first distribution in \eqref{eq:matn-red}.