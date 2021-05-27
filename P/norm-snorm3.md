---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-22 06:34:00

title: "Relationship between normal distribution and standard normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Relationship to standard normal distribution"

sources:

proof_id: "P180"
shortcut: "norm-snorm3"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [normal distribution](/D/norm) with mean $\mu$ and variance $\sigma^2$:

$$ \label{eq:X-norm}
X \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the quantity $Z = (X-\mu)/\sigma$ will have a [standard normal distribution](/D/snorm) with mean $0$ and variance $1$:

$$ \label{eq:Z-snorm}
Z = \frac{X-\mu}{\sigma} \sim \mathcal{N}(0, 1) \; .
$$


**Proof:** The [linear transformation theorem for multivariate normal distribution](/P/mvn-ltt) states

$$ \label{eq:mvn-ltt}
x \sim \mathcal{N}(\mu, \Sigma) \quad \Rightarrow \quad y = Ax + b \sim \mathcal{N}(A\mu + b, A \Sigma A^\mathrm{T})
$$

where $x$ is an $n \times 1$ [random vector](/D/rvec) following a [multivariate normal distribution](/D/mvn) with mean $\mu$ and covariance $\Sigma$, $A$ is an $m \times n$ matrix and $b$ is an $m \times 1$ vector. Note that

$$ \label{eq:Z-X}
Z = \frac{X-\mu}{\sigma} = \frac{X}{\sigma} - \frac{\mu}{\sigma}
$$

is a special case of \eqref{eq:mvn-ltt} with $x = X$, $\mu = \mu$, $\Sigma = \sigma^2$, $A = 1/\sigma$ and $b = \mu/\sigma$. Applying theorem \eqref{eq:mvn-ltt} to $Z$ as a function of $X$, we have

$$ \label{eq:mvn-ltt-norm}
X \sim \mathcal{N}(\mu, \sigma^2) \quad \Rightarrow \quad Z = \frac{X}{\sigma} - \frac{\mu}{\sigma} \sim \mathcal{N}\left( \frac{\mu}{\sigma} - \frac{\mu}{\sigma}, \frac{1}{\sigma} \cdot \sigma^2 \cdot \frac{1}{\sigma} \right)
$$

which results in the distribution:

$$ \label{eq:Z-snorm-qed}
Z \sim \mathcal{N}(0, 1) \; .
$$