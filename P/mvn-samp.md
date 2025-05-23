---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-05-21 16:14:00

title: "Sampling from the matrix-normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Drawing samples"

sources:
  - authors: "Wikipedia"
    year: 2025
    title: "Multivariate normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-05-23"
    url: "https://en.wikipedia.org/wiki/Multivariate_normal_distribution#Drawing_values_from_the_distribution"

proof_id: "P501"
shortcut: "mvn-samp"
username: "JoramSoch"
---


**Theorem:** Let $X \in \mathbb{R}^n$ be a [random vector](/D/rvec) with all entries independently following a [standard normal distribution](/D/snorm). Moreover, let $A$ be an $n \times n$ matrix, such that $A A^\mathrm{T} = \Sigma$.

Then, $Y = \mu + A X$ follows a [multivariate normal distribution](/D/mvn) with [mean](/D/mean-rvec) $\mu$ and [covariance](/D/covmat) $\Sigma$:

$$ \label{eq:mvn-samp}
Y = \mu + A X \sim \mathcal{N}(\mu, \Sigma) \; .
$$


**Proof:** If all entries of $X$ are independent and [standard normally distributed](/D/snorm)

$$ \label{eq:Xi-dist}
X_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, 1) \quad \text{for all} \quad i = 1,\ldots,n \; ,
$$

this [implies a multivariate normal distribution with diagonal covariance matrix](/P/mvn-ind):

$$ \label{eq:X-dist}
X \sim \mathcal{N}\left( 0_n, I_n \right) \; .
$$

Thus, with the [linear transformation theorem for the multivariate normal distribution](/P/mvn-ltt), it follows that

$$ \label{eq:mvn-samp-qed}
\begin{split}
      Y = \mu + A X
&\sim \mathcal{N}\left(A 0_n + \mu, A I_n A^\mathrm{T} \right) \\
&\sim \mathcal{N}\left(\mu, A A^\mathrm{T} \right) \\
&\sim \mathcal{N}\left(\mu, \Sigma \right) \; .
\end{split}
$$

Thus, given $X$ defined by \eqref{eq:Xi-dist}, $Y$ defined by \eqref{eq:mvn-samp} is a [sample](/D/samp) from $\mathcal{N}\left( \mu, \Sigma \right)$.
