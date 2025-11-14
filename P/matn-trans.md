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


**Theorem:** Let $X$ be an $n \times p$ [random matrix](/D/rmat) following a [matrix-normal distribution](/D/matn):

$$ \label{eq:matn}
X \sim \mathcal{MN}(M, U, V) \; .
$$

Then, the transpose of $X$ also has a matrix-normal distribution:

$$ \label{eq:matn-trans}
X^\mathrm{T} \sim \mathcal{MN}(M^\mathrm{T}, V, U) \; .
$$


**Proof:** For a [random vector](/D/rvec) $X \in \mathbb{R}^n$ with [probability density function](/D/pdf) $f_X(x)$, the [probability density function of the invertible function](/P/pdf-invfct) $Y = g(X)$ is

$$ \label{eq:pdf-invfct}
f_Y(y) = \left\{
\begin{array}{rl}
f_X(g^{-1}(y)) \, \left| J_{g^{-1}}(y) \right| \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y \notin \mathcal{Y}
\end{array}
\right.
$$

where $\lvert J_{g^{-1}}(y) \rvert$ is the determinant of the Jacobian matrix

$$ \label{eq:jac}
J_{g^{-1}}(y) = \left[ \begin{matrix}
\frac{\mathrm{d}x_1}{\mathrm{d}y_1} & \ldots & \frac{\mathrm{d}x_1}{\mathrm{d}y_n} \\
\vdots & \ddots & \vdots \\
\frac{\mathrm{d}x_n}{\mathrm{d}y_1} & \ldots & \frac{\mathrm{d}x_n}{\mathrm{d}y_n}
\end{matrix} \right]
$$

and $\mathcal{Y}$ is the set of possible outcomes of $Y$:

$$ \label{eq:Y-range}
\mathcal{Y} = \left\lbrace y = g(x): x \in \mathcal{X} \right\rbrace \; .
$$

In the present case, we have $Y = g(X) = X^\mathrm{T}$ and $X = g^{-1}(Y) = Y^\mathrm{T}$ and all $Y \in \mathcal{Y} = \mathbb{R}^{p \times n}$. For the vectorized matrices $X$ and $Y$, the Jacobian matrix is

$$ \label{eq:XY-jac}
J_{g^{-1}}(Y) = \left[ \begin{matrix}
\frac{\mathrm{d}x_{11}}{\mathrm{d}y_{11}} & \frac{\mathrm{d}x_{11}}{\mathrm{d}y_{21}} & \ldots & \frac{\mathrm{d}x_{11}}{\mathrm{d}y_{pn}} \\
\frac{\mathrm{d}x_{21}}{\mathrm{d}y_{11}} & \frac{\mathrm{d}x_{21}}{\mathrm{d}y_{21}} & \ldots & \frac{\mathrm{d}x_{21}}{\mathrm{d}y_{pn}} \\
\vdots                                    & \vdots                                    & \ddots & \vdots                                    \\
\frac{\mathrm{d}x_{np}}{\mathrm{d}y_{11}} & \frac{\mathrm{d}x_{np}}{\mathrm{d}y_{21}} & \ldots & \frac{\mathrm{d}x_{np}}{\mathrm{d}y_{pn}}
\end{matrix} \right] \in \mathbb{R}^{np} \; .
$$

Because by transposition, $y_{ji} = x_{ij}$, we have

$$ \label{eq:dxij-dyji}
\frac{\mathrm{d}x_{ij}}{\mathrm{d}y_{kl}} = \left\{
\begin{array}{rl}
1 \; , & \text{if} \; k = j \; \text{and} \; l = i \\
0 \; , & \text{otherwise} \; .
\end{array}
\right.
$$

Thus, $J_{g^{-1}}(Y)$ is row-equivalent to $I_{np}$ and $\lvert J_{g^{-1}}(Y) \rvert = \lvert I_{np} \rvert = 1$. Therefore, we have:

$$
\begin{split}
   f_Y(Y)
&= f_X(g^{-1}(Y)) \, \left| J_{g^{-1}}(Y) \right| \\
&= \mathcal{MN}(Y^\mathrm{T}; M, U, V) \, \left| I_{np} \right| \\
&= \mathcal{MN}(Y^\mathrm{T}; M, U, V) \; .
\end{split}
$$

The [probability density function of the matrix-normal distribution](/P/matn-pdf) is:

$$ \label{eq:matn-pdf-X}
f(X) = \mathcal{MN}(X; M, U, V) = \frac{1}{\sqrt{(2\pi)^{np} |V|^n |U|^p}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( V^{-1} (X-M)^\mathrm{T} \, U^{-1} (X-M) \right) \right] \; .
$$

Thus, substituting $X = Y^\mathrm{T}$, we get:

$$ \label{eq:matn-pdf-Y-s1}
f(Y) = \frac{1}{\sqrt{(2\pi)^{np} |U|^p |V|^n}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( V^{-1} (Y^\mathrm{T}-M)^\mathrm{T} \, U^{-1} (Y^\mathrm{T}-M) \right) \right] \; .
$$

Using $(A+B)^\mathrm{T} = (A^\mathrm{T} + B^\mathrm{T})$, we have:

$$ \label{eq:matn-pdf-Y-s2}
f(Y) = \frac{1}{\sqrt{(2\pi)^{np} |U|^p |V|^n}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( V^{-1} (Y-M^\mathrm{T}) \, U^{-1} (Y-M^\mathrm{T})^\mathrm{T} \right) \right] \; .
$$

Using $\mathrm{tr}(ABC) = \mathrm{tr}(CAB)$, we obtain

$$ \label{eq:matn-pdf-Y-s3}
f(Y) = \frac{1}{\sqrt{(2\pi)^{np} |U|^p |V|^n}} \cdot \exp\left[-\frac{1}{2} \mathrm{tr}\left( U^{-1} (Y-M^\mathrm{T})^\mathrm{T} \, V^{-1} (Y-M^\mathrm{T}) \right) \right]
$$

which is the [probability density function of a matrix-normal distribution](/P/matn-pdf) with mean $M^T$, covariance across rows $V$ and covariance across columns $U$:

$$ \label{eq:matn-pdf-Y-s4}
f(Y) = \mathcal{MN}(Y; M^\mathrm{T}, V, U) \; .
$$