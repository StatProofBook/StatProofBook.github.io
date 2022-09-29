---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-22 11:10:00

title: "Sampling from the normal-gamma distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Normal-gamma distribution"
theorem: "Drawing samples"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Normal-gamma distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-09-22"
    url: "https://en.wikipedia.org/wiki/Normal-gamma_distribution#Generating_normal-gamma_random_variates"

proof_id: "P346"
shortcut: "ng-samp"
username: "JoramSoch"
---


**Theorem:** Let $Z_1 \in \mathbb{R}^n$ be a [random vector](/D/rvec) with all entries independently following a [standard normal distribution](/D/snorm) and let $Z_2 \in \mathbb{R}$ be a [random variable](/D/rvar) following a [standard gamma distribution](/D/sgam) with shape $a$. Moreover, let $A \in \mathbb{R}^{n \times n}$ be a matrix, such that $A A^\mathrm{T} = \Lambda^{-1}$.

Then, $X = \mu + A Z_1 / \sqrt{Z_2/b}$ and $Y = Z_2/b$ jointly follow a [normal-gamma distribution](/D/ng) with [mean vector](/D/mean-rvec) $\mu$, [precision matrix](/D/precmat) $\Lambda$, shape parameter $a$ and rate parameter $b$:

$$ \label{eq:ng-samp}
\left( X = \mu + A Z_1 / \sqrt{Z_2/b}, \; Y = Z_2/b \right) \sim \mathrm{NG}(\mu, \Lambda, a, b) \; .
$$


**Proof:** If all entries of $Z_1$ are independent and [standard normally distributed](/D/snorm)

$$ \label{eq:zi-dist}
z_{1i} \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, 1) \quad \text{for all} \quad i = 1,\ldots,n \; ,
$$

this [implies a multivariate normal distribution with diagonal covariance matrix](/P/mvn-ind):

$$ \label{eq:Z1-dist}
Z_1 \sim \mathcal{N}\left(0_n, I_n \right)
$$

where $0_n$ is an $n \times 1$ matrix of zeros and $I_n$ is the $n \times n$ identity matrix.

If the distribution of $Z_2$ is a [standard gamma distribution](/D/sgam)

$$ \label{eq:Z2-dist}
Z_2 \sim \mathrm{Gam}(a, 1) \; ,
$$

then due to the [relationship between gamma and standard gamma distribution distribution](/P/gam-sgam), we have:

$$ \label{eq:Y-dist}
Y = \frac{Z_2}{b} \sim \mathrm{Gam}(a,b) \; .
$$

Moreover, using the [linear transformation theorem for the multivariate normal distribution](/P/mvn-ltt), it follows that:

$$ \label{eq:X-dist}
\begin{split}
Z_1 &\sim \mathcal{N}\left(0_n, I_n \right) \\
X = \mu + \frac{1}{\sqrt{Z_2/b}} A Z_1 &\sim \mathcal{N}\left(\mu + \frac{1}{\sqrt{Z_2/b}} A \, 0_n, \left( \frac{1}{\sqrt{Z_2/b}} A \right) I_n \left( \frac{1}{\sqrt{Z_2/b}} A \right)^\mathrm{T} \right) \\
X &\sim \mathcal{N}\left(\mu + 0_n, \left( \frac{1}{\sqrt{Y}} \right)^2 A A^\mathrm{T} \right) \\
X &\sim \mathcal{N}\left(\mu, \left( Y \Lambda \right)^{-1} \right) \; .
\end{split}
$$

Thus, $Y$ follows a [gamma distribution](/D/gam) and the distribution of $X$ conditional on $Y$ is a [multivariate normal distribution](/D/mvn):

$$ \label{eq:mvn-gam}
\begin{split}
X \vert Y &\sim \mathcal{N}(\mu, (Y \Lambda)^{-1}) \\
Y &\sim \mathrm{Gam}(a, b) \; .
\end{split}
$$

This means that, [by definition](/D/ng), $X$ and $Y$ jointly follow a [normal-gamma distribution](/D/ng):

$$ \label{eq:ng-samp-qed}
X,Y \sim \mathrm{NG}(\mu, \Lambda, a, b) \; ,
$$

Thus, given $Z_1$ defined by \eqref{eq:zi-dist} and $Z_2$ defined by \eqref{eq:Z2-dist}, $X$ and $Y$ defined by \eqref{eq:ng-samp} are a [sample](/D/samp) from $\mathrm{NG}(\mu, \Lambda, a, b)$.