---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-03 22:21:00

title: "Transposition of a matrix-normal random variable"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Transposition"

sources:

proof_id: "P144"
shortcut: "matn-trans"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random matrix](/D/rmat) following a [matrix-normal distribution](/D/matn):

$$ \label{eq:matn}
X \sim \mathcal{MN}(M, U, V) \; .
$$

Then, the transpose of $X$ also has a matrix-normal distribution:

$$ \label{eq:matn-trans}
X^\mathrm{T} \sim \mathcal{MN}(M^\mathrm{T}, V, U) \; .
$$


**Proof:** The [probability density function of the matrix-normal distribution](/P/matn-pdf) is:

$$ \label{eq:matn-pdf-X}
f(X) = \mathcal{MN}(X; M, U, V) = \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( V^{-1} (X-M)^\mathrm{T} \, U^{-1} (X-M) \right) \right] \; .
$$

Define $Y = X^\mathrm{T}$. Then, $X = Y^\mathrm{T}$ and we can substitute:

$$ \label{eq:matn-pdf-Y-s1}
f(Y) = \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( V^{-1} (Y^\mathrm{T}-M)^\mathrm{T} \, U^{-1} (Y^\mathrm{T}-M) \right) \right] \; .
$$

Using $(A+B)^\mathrm{T} = (A^\mathrm{T} + B^\mathrm{T})$, we have:

$$ \label{eq:matn-pdf-Y-s2}
f(Y) = \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( V^{-1} (Y-M^\mathrm{T}) \, U^{-1} (Y-M^\mathrm{T})^\mathrm{T} \right) \right] \; .
$$

Using $\mathrm{tr}(ABC) = \mathrm{tr}(CAB)$, we obtain

$$ \label{eq:matn-pdf-Y-s3}
f(Y) = \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( U^{-1} (Y-M^\mathrm{T})^\mathrm{T} \, V^{-1} (Y-M^\mathrm{T}) \right) \right]
$$

which is the [probability density function of a matrix-normal distribution](/P/matn-pdf) with mean $M^T$, covariance across rows $V$ and covariance across columns $U$.