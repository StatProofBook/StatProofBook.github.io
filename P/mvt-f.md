---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-05-04 10:29:00

title: "Relationship between multivariate t-distribution and F-distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate t-distribution"
theorem: "Relationship to F-distribution"

sources:
  - authors: "Lin, Pi-Erh"
    year: 1972
    title: "Some Characterizations of the Multivariate t Distribution"
    in: "Journal of Multivariate Analysis"
    pages: "vol. 2, pp. 339-344, Lemma 2"
    url: "https://core.ac.uk/download/pdf/81139018.pdf"
    doi: "10.1016/0047-259X(72)90021-8"
  - authors: "Nadarajah, Saralees; Kotz, Samuel"
    year: 2005
    title: "Mathematical Properties of the Multivariate t Distribution"
    in: "Acta Applicandae Mathematicae"
    pages: "vol. 89, pp. 53-84, page 56"
    url: "https://link.springer.com/content/pdf/10.1007/s10440-005-9003-4.pdf"
    doi: "10.1007/s10440-005-9003-4"

proof_id: "P231"
shortcut: "mvt-f"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a $n \times 1$ [random vector](/D/rvec) following a [multivariate t-distribution](/D/mvt) with mean $\mu$, scale matrix $\Sigma$ and degrees of freedom $\nu$:

$$ \label{eq:X}
X \sim t(\mu, \Sigma, \nu) \; .
$$

Then, the centered, weighted and standardized quadratic form of $X$ follows an [F-distribution](/D/f) with degrees of freedom $n$ and $\nu$:

$$ \label{eq:mvt-f}
(X-\mu)^\mathrm{T} \, \Sigma^{-1} (X-\mu)/n \sim F(n, \nu) \; .
$$


**Proof:** The [linear transformation theorem for the multivariate t-distribution](/P/mvt-ltt) states

$$ \label{eq:mvt-ltt}
x \sim t(\mu, \Sigma, \nu) \quad \Rightarrow \quad y = Ax + b \sim t(A\mu + b, A \Sigma A^\mathrm{T}, \nu)
$$

where $x$ is an $n \times 1$ [random vector](/D/rvec) following a [multivariate t-distribution](/D/mvt), $A$ is an $m \times n$ matrix and $b$ is an $m \times 1$ vector. Define the following quantities

$$ \label{eq:YZ}
\begin{split}
Y = \Sigma^{-1/2} (X-\mu) = \Sigma^{-1/2} X - \Sigma^{-1/2} \mu \\
Z = Y^\mathrm{T} Y / n = (X-\mu)^\mathrm{T} \, \Sigma^{-1} (X-\mu)/n
\end{split}
$$

where $\Sigma^{-1/2}$ is a matrix square root of the inverse of $\Sigma$. Then, applying \eqref{eq:mvt-ltt} to \eqref{eq:YZ} with \eqref{eq:X}, one obtains the distribution of $Y$ as

$$ \label{eq:Y-dist}
\begin{split}
Y &\sim t(\Sigma^{-1/2} \mu - \Sigma^{-1/2} \mu, \Sigma^{-1/2} \Sigma \, \Sigma^{-1/2}, \nu) \\
&= t(0_n, \Sigma^{-1/2} \Sigma^{1/2} \Sigma^{1/2} \Sigma^{-1/2}, \nu) \\
&= t(0_n, I_n, \nu) \; ,
\end{split}
$$

i.e. $Y$ is an $n \times 1$ vector of [independent and identically distributed](/D/iid) [random variables](/D/rvar) following a [univariate t-distribution](/D/t) with $\nu$ degrees of freedom:

$$ \label{eq:yi-dist}
Y_i \sim t(\nu), \; i = 1,\ldots,n \; .
$$

Note that, when $X$ follows a t-distribution with $n$ degrees of freedom, [this is equivalent to](/D/t) an expression of $X$ in terms of a [standard normal](/D/snorm) random variable $Z$ and a [chi-squared](/D/chi2) random variable $V$:

$$ \label{eq:t}
X \sim t(n) \quad \Leftrightarrow \quad X = \frac{Z}{\sqrt{V/n}} \quad \text{with independent} \quad Z \sim \mathcal{N}(0,1) \quad \text{and} \quad V \sim \chi^2(n) \; .
$$

With that, $Z$ from \eqref{eq:YZ} can be rewritten as follows:

$$ \label{eq:Z-eq-s1}
\begin{split}
Z &\overset{\eqref{eq:YZ}}{=} Y^\mathrm{T} Y / n \\
&= \frac{1}{n} \sum_{i=1}^n Y_i^2 \\
&\overset{\eqref{eq:t}}{=} \frac{1}{n} \sum_{i=1}^n \left( \frac{Z_i}{\sqrt{V/\nu}} \right)^2 \\
&= \frac{\left( \sum_{i=1}^n Z_i^2 \right)/n}{V/\nu} \; .
\end{split}
$$

Because [by definition, the sum of squared standard normal random variables follows a chi-squared distribution](/D/chi2)

$$ \label{eq:chi2}
X_i \sim \mathcal{N}(0,1), \; i = 1,\ldots,n \quad \Rightarrow \quad \sum_{i=1}^n X_i^2 \sim \chi^2(n) \; ,
$$

the quantity $Z$ becomes a ratio of the following form

$$ \label{eq:Z-eq-s2}
Z = \frac{W/n}{V/\nu} \quad \text{with} \quad W \sim \chi^2(n) \quad \text{and} \quad V \sim \chi^2(\nu) \; ,
$$

such that $Z$, [by definition, follows an F-distribution](/D/f):

$$ \label{eq:Z-dist}
Z = \frac{W/n}{V/\nu} \sim F(n, \nu) \; .
$$