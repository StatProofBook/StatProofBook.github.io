---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-09-29 09:45:10

title: "Probability density function of the bivariate normal distribution in terms of correlation coefficient"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Bivariate normal distribution"
theorem: "Probability density function in terms of correlation coefficient"

sources:
  - authors: "Wikipedia"
    year: 2023
    title: "Multivariate normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2023-09-29"
    url: "https://en.wikipedia.org/wiki/Multivariate_normal_distribution#Bivariate_case"

proof_id: "P417"
shortcut: "bvn-pdfcorr"
username: "JoramSoch"
---


**Theorem:** Let $X = \left[ \begin{matrix} X_1 \\\\ X_2 \end{matrix} \right]$ follow a [bivariate normal distribution](/D/bvn):

$$ \label{eq:bvn}
X \sim \mathcal{N}\left( \mu = \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right], \Sigma = \left[ \begin{matrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{matrix} \right] \right) \; .
$$

Then, the [probability density function](/D/pdf) of $X$ is

$$ \label{eq:bvn-pdf}
f_X(x) = \frac{1}{2 \pi \, \sigma_1 \sigma_2 \sqrt{1 - \rho^2}} \cdot \exp \left[ -\frac{1}{2 (1 - \rho^2)} \left( \left( \frac{x_1-\mu_1}{\sigma_1} \right)^2 - 2 \rho \frac{(x_1-\mu_1) (x_2-\mu_2)}{\sigma_1 \sigma_2} + \left( \frac{x_2-\mu_2}{\sigma_2} \right)^2 \right) \right]
$$

where $\rho$ is the [correlation](/D/corr) between $X_1$ and $X_2$.


**Proof:** Since $X$ follows a special case of the [multivariate normal distribution, its covariance matrix is](/P/mvn-cov)

$$ \label{eq:cov-X}
\mathrm{Cov}(X) = \Sigma = \left[ \begin{matrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{matrix} \right]
$$

and [the covariance matrix can be decomposed into correlation matrix and standard deviations](/P/covmat-corrmat):

$$ \label{eq:Sigma}
\begin{split}
\Sigma &= \left[ \begin{matrix} \sigma_1^2 & \rho \, \sigma_1 \sigma_2 \\ \rho \, \sigma_1 \sigma_2 & \sigma_2^2 \end{matrix} \right] \\
&= \left[ \begin{matrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{matrix} \right] \left[ \begin{matrix} 1 & \rho \\ \rho & 1 \end{matrix} \right] \left[ \begin{matrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{matrix} \right] \; .
\end{split}
$$

The determinant of this matrix is

$$ \label{eq:Sigma-det}
\begin{split}
\left| \Sigma \right| &= \left| \left[ \begin{matrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{matrix} \right] \left[ \begin{matrix} 1 & \rho \\ \rho & 1 \end{matrix} \right] \left[ \begin{matrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{matrix} \right] \right| \\
&= \left| \left[ \begin{matrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{matrix} \right] \right| \cdot \left| \left[ \begin{matrix} 1 & \rho \\ \rho & 1 \end{matrix} \right] \right| \cdot \left| \left[ \begin{matrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{matrix} \right] \right| \\
&= (\sigma_1 \sigma_2) (1 - \rho^2) (\sigma_1 \sigma_2) \\
&= \sigma_1^2 \sigma_2^2 (1 - \rho^2)
\end{split}
$$

and the inverse of this matrix is

$$ \label{eq:Sigma-inv}
\begin{split}
\Sigma^{-1} &= \left( \left[ \begin{matrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{matrix} \right] \left[ \begin{matrix} 1 & \rho \\ \rho & 1 \end{matrix} \right] \left[ \begin{matrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{matrix} \right] \right)^{-1} \\
&= \left[ \begin{matrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{matrix} \right]^{-1} \left[ \begin{matrix} 1 & \rho \\ \rho & 1 \end{matrix} \right]^{-1} \left[ \begin{matrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{matrix} \right]^{-1} \\
&= \frac{1}{1 - \rho^2} \left[ \begin{matrix} 1/\sigma_1 & 0 \\ 0 & 1/\sigma_2 \end{matrix} \right] \left[ \begin{matrix} 1 & -\rho \\ -\rho & 1 \end{matrix} \right] \left[ \begin{matrix} 1/\sigma_1 & 0 \\ 0 & 1/\sigma_2 \end{matrix} \right] \; .
\end{split}
$$

The [probability density function of the multivariate normal distribution](/P/mvn-pdf) for an $n$-dimensional [random vector](/D/rvec) $x$ is:

$$ \label{eq:mvn-pdf}
f_X(x) = \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] \; .
$$

Plugging in $n = 2$, $\mu$ from \eqref{eq:bvn} and $\Sigma$ from \eqref{eq:Sigma-det} and \eqref{eq:Sigma-inv}, the probability density function becomes:

$$ \label{eq:bvn-pdf-corr}
\begin{split}
f_X(x) &= \frac{1}{\sqrt{(2 \pi)^2 \sigma_1^2 \sigma_2^2 (1 - \rho^2)}} \cdot \exp \left[ -\frac{1}{2} \left( \left[ \begin{matrix} x_1 \\ x_2 \end{matrix} \right] - \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right] \right)^\mathrm{T} \frac{1}{1 - \rho^2} \left[ \begin{matrix} 1/\sigma_1 & 0 \\ 0 & 1/\sigma_2 \end{matrix} \right] \left[ \begin{matrix} 1 & -\rho \\ -\rho & 1 \end{matrix} \right] \left[ \begin{matrix} 1/\sigma_1 & 0 \\ 0 & 1/\sigma_2 \end{matrix} \right] \left( \left[ \begin{matrix} x_1 \\ x_2 \end{matrix} \right] - \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right] \right) \right] \\
&= \frac{1}{2 \pi \, \sigma_1 \sigma_2 \sqrt{1 - \rho^2}} \cdot \exp \left[ -\frac{1}{2 (1 - \rho^2)} \left[ \begin{matrix} \frac{x_1-\mu_1}{\sigma_1} & \frac{x_2-\mu_2}{\sigma_2} \end{matrix} \right] \left[ \begin{matrix} 1 & -\rho \\ -\rho & 1 \end{matrix} \right] \left[ \begin{matrix} \frac{x_1-\mu_1}{\sigma_1} \\ \frac{x_2-\mu_2}{\sigma_2} \end{matrix} \right]  \right] \\
&= \frac{1}{2 \pi \, \sigma_1 \sigma_2 \sqrt{1 - \rho^2}} \cdot \exp \left[ -\frac{1}{2 (1 - \rho^2)} \left[ \begin{matrix} \left( \frac{x_1-\mu_1}{\sigma_1} - \rho \frac{x_2-\mu_2}{\sigma_2} \right) & \left( \frac{x_2-\mu_2}{\sigma_2} - \rho \frac{x_1-\mu_1}{\sigma_1} \right) \end{matrix} \right] \left[ \begin{matrix} \frac{x_1-\mu_1}{\sigma_1} \\ \frac{x_2-\mu_2}{\sigma_2} \end{matrix} \right]  \right] \\
&= \frac{1}{2 \pi \, \sigma_1 \sigma_2 \sqrt{1 - \rho^2}} \cdot \exp \left[ -\frac{1}{2 (1 - \rho^2)} \left( \left( \frac{x_1-\mu_1}{\sigma_1} \right)^2 - 2 \rho \frac{(x_1-\mu_1) (x_2-\mu_2)}{\sigma_1 \sigma_2} + \left( \frac{x_2-\mu_2}{\sigma_2} \right)^2 \right) \right] \; .
\end{split}
$$