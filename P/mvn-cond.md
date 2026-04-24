---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-20 08:44:00

title: "Conditional distributions of the multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Conditional distributions"

sources:
  - authors: "Wang, Ruye"
    year: 2006
    title: "Marginal and conditional distributions of multivariate normal distribution"
    in: "Computer Image Processing and Analysis"
    pages: "retrieved on 2020-03-20"
    url: "http://fourier.eng.hmc.edu/e161/lectures/gaussianprocess/node7.html"
  - authors: "Dablander, Fabian"
    year: 2019
    title: "Two properties of the Gaussian distribution"
    in: "Fabian Dablander: Blog"
    pages: "retrieved on 2027-02-26"
    url: "https://fabiandablander.com/statistics/Two-Properties.html"
  - authors: "Hamilton, James D."
    year: 1994
    title: "The Kalman Filter"
    in: "Time Series Analysis"
    pages: "ch. 13, pp. 372ff."
    url: "https://github.com/MatthewK84/Time-Series-Textbooks/blob/main/Hamilton%20Time%20Series%20Analysis.pdf"
  - authors: "Wikipedia"
    year: 2026
    title: "Invertible matrix"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2026-02-27"
    url: "https://en.wikipedia.org/wiki/Invertible_matrix#Blockwise_inversion"
  - authors: "Wikipedia"
    year: 2026
    title: "Determinant"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2026-02-27"
    url: "https://en.wikipedia.org/wiki/Determinant#Block_matrices"

proof_id: "P88"
shortcut: "mvn-cond"
username: "JoramSoch"
---


**Theorem:** Let $X$ follow a [multivariate normal distribution](/D/mvn)

$$ \label{eq:mvn}
X \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, the [conditional distribution](/D/dist-cond) of any subset vector $X_1$, given the complement vector $X_2$, is also a multivariate normal distribution

$$ \label{eq:mvn-cond}
X_1|X_2 \sim \mathcal{N}(\mu_{1|2}, \Sigma_{1|2})
$$

where the conditional [mean](/D/mean) and [covariance](/D/cov) are

$$ \label{eq:mvn-cond-hyp}
\begin{split}
\mu_{1|2}    &= \mu_1 + \Sigma_{12} \Sigma_{22}^{-1} (x_2 - \mu_2) \\
\Sigma_{1|2} &= \Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21}
\end{split}
$$

with block-wise mean and covariance defined as

$$ \label{eq:mvn-joint-hyp}
\begin{split}
\mu    &= \begin{bmatrix} \mu_1 \\ \mu_2 \end{bmatrix} \\
\Sigma &= \begin{bmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{bmatrix} \; .
\end{split}
$$


**Proof:** Without loss of generality, we assume that, in parallel to \eqref{eq:mvn-joint-hyp},

$$ \label{eq:X}
X = \begin{bmatrix} X_1 \\ X_2 \end{bmatrix}
$$

where $X_1$ is an $n_1$-dimensional vector, $X_2$ is an $n_2$-dimensional vector and $X$ is an $(n_1 + n_2)$-dimensional vector.

By construction, the [joint distribution](/D/dist-joint) of $X_1$ and $X_2$ is:

$$ \label{eq:mvn-joint}
X_1,X_2 \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Moreover, the [marginal distribution](/D/dist-marg) of $X_2$ [follows from](/P/mvn-marg) \eqref{eq:mvn} and \eqref{eq:mvn-joint-hyp} as

$$ \label{eq:mvn-marg}
X_2 \sim \mathcal{N}(\mu_2, \Sigma_{22}) \; .
$$

According to the [law of conditional probability](/D/prob-cond), it holds that

$$ \label{eq:mvn-cond-s1}
p(x_1|x_2) = \frac{p(x_1,x_2)}{p(x_2)}
$$

Applying \eqref{eq:mvn-joint} and \eqref{eq:mvn-marg} to \eqref{eq:mvn-cond-s1}, we have:

$$ \label{eq:mvn-cond-s2}
p(x_1|x_2) = \frac{\mathcal{N}(x; \mu, \Sigma)}{\mathcal{N}(x_2; \mu_2, \Sigma_{22})} \; .
$$

Using the [probability density function of the multivariate normal distribution](/P/mvn-pdf), this becomes:

$$ \label{eq:mvn-cond-s3}
\begin{split}
p(x_1|x_2) &= \frac{1/\sqrt{(2 \pi)^n |\Sigma|} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right]}{1/\sqrt{(2 \pi)^{n_2} |\Sigma_{22}|} \cdot \exp \left[ -\frac{1}{2} (x_2-\mu_2)^\mathrm{T} \Sigma_{22}^{-1} (x_2-\mu_2) \right]} \\
&= \frac{1}{\sqrt{(2 \pi)^{n-n_2}}} \cdot \sqrt{\frac{|\Sigma_{22}|}{|\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) + \frac{1}{2} (x_2-\mu_2)^\mathrm{T} \Sigma_{22}^{-1} (x_2-\mu_2) \right] \; .
\end{split}
$$

Writing the inverse of $\Sigma$ as

$$ \label{eq:Sigma-inv-def}
\Sigma^{-1} = \begin{bmatrix} \Sigma^{11} & \Sigma^{12} \\ \Sigma^{21} & \Sigma^{22} \end{bmatrix}
$$

and applying \eqref{eq:mvn-joint-hyp} to \eqref{eq:mvn-cond-s3}, we get:

$$ \label{eq:mvn-cond-s4}
\begin{split}
p(x_1|x_2) = &\frac{1}{\sqrt{(2 \pi)^{n-n_2}}} \cdot \sqrt{\frac{|\Sigma_{22}|}{|\Sigma|}} \cdot \\
&\exp \left[ -\frac{1}{2} \left( \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} - \begin{bmatrix} \mu_1 \\ \mu_2 \end{bmatrix} \right)^\mathrm{T} \begin{bmatrix} \Sigma^{11} & \Sigma^{12} \\ \Sigma^{21} & \Sigma^{22} \end{bmatrix} \left( \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} - \begin{bmatrix} \mu_1 \\ \mu_2 \end{bmatrix} \right) \right. \\
&\hphantom{\exp \left[\right.} \left. + \frac{1}{2} \, (x_2-\mu_2)^\mathrm{T} \, \Sigma_{22}^{-1} \, (x_2-\mu_2) \right] \; .
\end{split}
$$

Multiplying out within the exponent of \eqref{eq:mvn-cond-s4}, we have

$$ \label{eq:mvn-cond-s5}
\begin{split}
p(x_1|x_2) = &\frac{1}{\sqrt{(2 \pi)^{n-n_2}}} \cdot \sqrt{\frac{|\Sigma_{22}|}{|\Sigma|}} \cdot \\
&\exp \left[ -\frac{1}{2} \left( (x_1-\mu_1)^\mathrm{T} \Sigma^{11} (x_1-\mu_1) + 2 (x_1-\mu_1)^\mathrm{T} \Sigma^{12} (x_2-\mu_2) + (x_2-\mu_2)^\mathrm{T} \Sigma^{22} (x_2-\mu_2) \right) \right. \\
&\hphantom{\exp \left[\right.} \left. + \frac{1}{2} (x_2-\mu_2)^\mathrm{T} \Sigma_{22}^{-1} (x_2-\mu_2) \right]
\end{split}
$$

where we have used the fact that ${\Sigma^{21}}^\mathrm{T} = \Sigma^{12}$, because $\Sigma^{-1}$ is a symmetric matrix.

The inverse of a block matrix is

$$ \label{eq:block-inv}
\begin{bmatrix}
A & B \\
C & D
\end{bmatrix}^{-1} =
\begin{bmatrix} 
(A-BD^{-1}C)^{-1}          & -(A-BD^{-1}C)^{-1}BD^{-1}              \\
-D^{-1}C(A-BD^{-1}C)^{-1} & D^{-1}+D^{-1}C(A-BD^{-1}C)^{-1}BD^{-1}
\end{bmatrix} \; ,
$$

thus the inverse of $\Sigma$ in \eqref{eq:Sigma-inv-def} is

$$ \label{eq:Sigma-inv}
\begin{bmatrix}
\Sigma_{11} & \Sigma_{12} \\
\Sigma_{21} & \Sigma_{22}
\end{bmatrix}^{-1} =
\begin{bmatrix}
(\Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21})^{-1}                               & -(\Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21})^{-1} \Sigma_{12} \Sigma_{22}^{-1}                                                \\
-\Sigma_{22}^{-1} \Sigma_{21} (\Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21})^{-1} & \Sigma_{22}^{-1} + \Sigma_{22}^{-1} \Sigma_{21} (\Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21})^{-1} \Sigma_{12} \Sigma_{22}^{-1}
\end{bmatrix} \; .
$$

Plugging this into \eqref{eq:mvn-cond-s5}, we have:

$$ \label{eq:mvn-cond-s6}
\begin{split}
p(x_1|x_2) = &\frac{1}{\sqrt{(2 \pi)^{n-n_2}}} \cdot \sqrt{\frac{|\Sigma_{22}|}{|\Sigma|}} \cdot \\
&\exp \left[ -\frac{1}{2} \left( (x_1-\mu_1)^\mathrm{T} (\Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21})^{-1} (x_1-\mu_1) \right. \right. - \\
&\hphantom{\exp \left[ -\frac{1}{2} \left( \right. \right.} 2 (x_1-\mu_1)^\mathrm{T} (\Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21})^{-1} \Sigma_{12} \Sigma_{22}^{-1} (x_2-\mu_2) + \\
&\hphantom{\exp \left[ -\frac{1}{2} \left( \right. \right.} \left. (x_2-\mu_2)^\mathrm{T} \left[ \Sigma_{22}^{-1} + \Sigma_{22}^{-1} \Sigma_{21} (\Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21})^{-1} \Sigma_{12} \Sigma_{22}^{-1} \right] (x_2-\mu_2) \right) \\
&\hphantom{\exp \left[\right.} \left. + \frac{1}{2} \left( (x_2-\mu_2)^\mathrm{T} \Sigma_{22}^{-1} (x_2-\mu_2) \right) \right] \; .
\end{split}
$$

Eliminating some terms, we have:

$$ \label{eq:mvn-cond-s7}
\begin{split}
p(x_1|x_2) = &\frac{1}{\sqrt{(2 \pi)^{n-n_2}}} \cdot \sqrt{\frac{|\Sigma_{22}|}{|\Sigma|}} \cdot \\
&\exp \left[ -\frac{1}{2} \left( (x_1-\mu_1)^\mathrm{T} (\Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21})^{-1} (x_1-\mu_1) \right. \right. - \\
&\hphantom{\exp \left[ -\frac{1}{2} \left( \right. \right.} 2 (x_1-\mu_1)^\mathrm{T} (\Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21})^{-1} \Sigma_{12} \Sigma_{22}^{-1} (x_2-\mu_2) + \\
&\hphantom{\exp \left[ -\frac{1}{2} \left( \right. \right.} \left. \left. (x_2-\mu_2)^\mathrm{T} \Sigma_{22}^{-1} \Sigma_{21} (\Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21})^{-1} \Sigma_{12} \Sigma_{22}^{-1} (x_2-\mu_2) \right) \right] \; .
\end{split}
$$

Rearranging the terms, we have

$$ \label{eq:mvn-cond-s8}
\begin{split}
p(x_1|x_2) = &\frac{1}{\sqrt{(2 \pi)^{n-n_2}}} \cdot \sqrt{\frac{|\Sigma_{22}|}{|\Sigma|}} \cdot \exp \left[ -\frac{1}{2} \cdot \right. \\
&\! \left. \left[ (x_1-\mu_1) - \Sigma_{12} \Sigma_{22}^{-1} (x_2-\mu_2) \right]^\mathrm{T} (\Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21})^{-1} \left[ (x_1-\mu_1) - \Sigma_{12} \Sigma_{22}^{-1} (x_2-\mu_2) \right] \right] \\
= &\frac{1}{\sqrt{(2 \pi)^{n-n_2}}} \cdot \sqrt{\frac{|\Sigma_{22}|}{|\Sigma|}} \cdot \exp \left[ -\frac{1}{2} \cdot \right. \\
&\! \left. \left[ x_1 - \left( \mu_1 + \Sigma_{12} \Sigma_{22}^{-1} (x_2-\mu_2) \right) \right]^\mathrm{T} (\Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21})^{-1} \left[ x_1 - \left( \mu_1 + \Sigma_{12} \Sigma_{22}^{-1} (x_2-\mu_2) \right) \right] \right]
\end{split}
$$

where we have used [the fact that](/P/covmat-symm) $\Sigma_{21} = \Sigma_{12}^\mathrm{T}$, because $\Sigma$ is a [covariance matrix](/D/covmat).

The determinant of a block matrix is

$$ \label{eq:Block-det}
\begin{vmatrix} A & B \\ C & D \end{vmatrix} = |D| \cdot | A - B D^{-1} C | \; ,
$$

such that we have for $\Sigma$ that

$$ \label{eq:Sigma-det}
\begin{vmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \end{vmatrix} = |\Sigma_{22}| \cdot | \Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} | \; .
$$

With this and $n - n_2 = n_1$, we finally arrive at

$$ \label{eq:mvn-cond-s9}
\begin{split}
p(x_1|x_2) = &\frac{1}{\sqrt{(2 \pi)^{n_1} | \Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21} |}} \cdot \exp \left[ -\frac{1}{2} \cdot \right. \\
&\! \left. \left[ x_1 - \left( \mu_1 + \Sigma_{12} \Sigma_{22}^{-1} (x_2-\mu_2) \right) \right]^\mathrm{T} (\Sigma_{11} - \Sigma_{12} \Sigma_{22}^{-1} \Sigma_{21})^{-1} \left[ x_1 - \left( \mu_1 + \Sigma_{12} \Sigma_{22}^{-1} (x_2-\mu_2) \right) \right] \right]
\end{split}
$$

which is the [probability density function of a multivariate normal distribution](/P/mvn-pdf)

$$ \label{eq:mvn-cond-s10}
p(x_1|x_2) = \mathcal{N}(x_1; \mu_{1|2}, \Sigma_{1|2})
$$

with the [mean](/D/mean) $\mu_{1 \vert 2}$ and [covariance](/D/cov) $\Sigma_{1 \vert 2}$ given by \eqref{eq:mvn-cond-hyp}.