---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-20 21:09:00

title: "Equivalence of matrix-normal distribution and multivariate normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Equivalence to multivariate normal distribution"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Matrix normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-01-20"
    url: "https://en.wikipedia.org/wiki/Matrix_normal_distribution#Proof"

proof_id: "P26"
shortcut: "matn-mvn"
username: "JoramSoch"
---


**Theorem:** The matrix $X$ is [matrix-normally distributed](/D/matn)

$$ \label{eq:matn}
X \sim \mathcal{MN}(M, U, V) \; ,
$$

if and only if $\mathrm{vec}(X)$ is [multivariate normally distributed](/D/mvn)

$$ \label{eq:mvn}
\mathrm{vec}(X) \sim \mathcal{N}(\mathrm{vec}(M), V \otimes U)
$$

where $\mathrm{vec}(X)$ is the vectorization operator and $\otimes$ is the Kronecker product.


**Proof:** The [probability density function of the matrix-normal distribution](/P/matn-pdf) with $n \times p$ mean $M$, $n \times n$ covariance across rows $U$ and $p \times p$ covariance across columns $V$ is

$$ \label{eq:matn-pdf}
\mathcal{MN}(X; M, U, V) = \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( V^{-1} (X-M)^\mathrm{T} \, U^{-1} (X-M) \right) \right] \; .
$$

Using the trace property $\mathrm{tr}(ABC) = \mathrm{tr}(BCA)$, we have:

$$ \label{eq:matn-mvn-s1}
\mathcal{MN}(X; M, U, V) = \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( (X-M)^\mathrm{T} \, U^{-1} (X-M) \, V^{-1} \right) \right] \; .
$$

Using the trace-vectorization relation $\mathrm{tr}(A^\mathrm{T} B) = \mathrm{vec}(A)^\mathrm{T} \, \mathrm{vec}(B)$, we have:

$$ \label{eq:matn-mvn-s2}
\mathcal{MN}(X; M, U, V) = \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{vec}(X-M)^\mathrm{T} \, \mathrm{vec}\left( U^{-1} (X-M) \, V^{-1} \right) \right] \; .
$$

Using the vectorization-Kronecker relation $\mathrm{vec}(ABC) = \left( C^\mathrm{T} \otimes A \right) \mathrm{vec}(B)$, we have:

$$ \label{eq:matn-mvn-s3}
\mathcal{MN}(X; M, U, V) = \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{vec}(X-M)^\mathrm{T} \, \left( V^{-1} \otimes U^{-1} \right) \mathrm{vec}(X-M) \right] \; .
$$

Using the Kronecker product property $\left( A^{-1} \otimes B^{-1} \right) = \left( A \otimes B \right)^{-1}$, we have:

$$ \label{eq:matn-mvn-s4}
\mathcal{MN}(X; M, U, V) = \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{vec}(X-M)^\mathrm{T} \, \left( V \otimes U \right)^{-1} \mathrm{vec}(X-M) \right] \; .
$$

Using the vectorization property $\mathrm{vec}(A+B) = \mathrm{vec}(A) + \mathrm{vec}(B)$, we have:

$$ \label{eq:matn-mvn-s5}
\mathcal{MN}(X; M, U, V) = \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \left[ \mathrm{vec}(X) - \mathrm{vec}(M) \right]^\mathrm{T} \, \left( V \otimes U \right)^{-1} \left[ \mathrm{vec}(X) - \mathrm{vec}(M) \right] \right] \; .
$$

Using the Kronecker-determinant relation $\lvert A \otimes B \rvert = \lvert A \rvert^m \lvert B \rvert^n$, we have:

$$ \label{eq:matn-mvn-s6}
\mathcal{MN}(X; M, U, V) = \frac{1}{\sqrt{(2\pi)^{np} |V \otimes U|}} \cdot \exp\left[-\frac{1}{2} \left[ \mathrm{vec}(X) - \mathrm{vec}(M) \right]^\mathrm{T} \, \left( V \otimes U \right)^{-1} \left[ \mathrm{vec}(X) - \mathrm{vec}(M) \right] \right] \; .
$$

This is the [probability density function of the multivariate normal distribution](/P/mvn-pdf) with the $np \times 1$ mean vector $\mathrm{vec}(M)$ and the $np \times np$ covariance matrix $V \otimes U$:

$$ \label{eq:matn-mvn}
\mathcal{MN}(X; M, U, V) = \mathcal{N}(\mathrm{vec}(X); \mathrm{vec}(M), V \otimes U) \; .
$$

By showing that the [probability density functions](/D/pdf) are identical, it is proven that the associated [probability distributions](/D/dist) are equivalent.