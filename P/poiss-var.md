---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-04-29 09:59:00

title: "Variance of the Poisson distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Poisson distribution"
theorem: "Variance"

sources:
  - authors: "jbstatistics"
    year: 2013
    title: "The Poisson Distribution: Mathematically Deriving the Mean and Variance"
    in: "YouTube"
    pages: "retrieved on 2021-04-29"
    url: "https://www.youtube.com/watch?v=65n_v92JZeE"

proof_id: "P230"
shortcut: "poiss-var"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [Poisson distribution](/D/poiss):

$$ \label{eq:poiss}
X \sim \mathrm{Poiss}(\lambda) \; .
$$

Then, the [variance](/D/var) of $X$ is

$$ \label{eq:poiss-var}
\mathrm{Var}(X) = \lambda \; .
$$


**Proof:** The [variance](/D/var) can be expressed [in terms of expected values](/P/var-mean) as

$$ \label{eq:var-mean}
\mathrm{Var}(X) = \mathrm{E}(X^2) - \mathrm{E}(X)^2 \; .
$$

The [expected value of a Poisson random variable](/P/poiss-mean) is

$$ \label{eq:poiss-mean}
\mathrm{E}(X) = \lambda \; .
$$

Let us now consider the [expectation](/D/mean) of $X \, (X-1)$ which is defined as

$$ \label{eq:mean}
\mathrm{E}[X \, (X-1)] = \sum_{x \in \mathcal{X}} x \, (x-1) \cdot f_X(x) \; ,
$$

such that, with the [probability mass function of the Poisson distribution](/P/poiss-pmf), we have:

$$ \label{eq:poiss-x2x-mean-s1}
\begin{split}
\mathrm{E}[X \, (X-1)] &= \sum_{x=0}^\infty x \, (x-1) \cdot \frac{\lambda^x \, e^{-\lambda}}{x!} \\
&= \sum_{x=2}^\infty x \, (x-1) \cdot \frac{\lambda^x \, e^{-\lambda}}{x!} \\
&= e^{-\lambda} \cdot \sum_{x=2}^\infty x \, (x-1) \cdot \frac{\lambda^x}{x \cdot (x-1) \cdot (x-2)!} \\
&= \lambda^2 \cdot e^{-\lambda} \cdot \sum_{x=2}^\infty \frac{\lambda^{x-2}}{(x-2)!} \; .
\end{split}
$$

Substituting $z = x-2$, such that $x = z+2$, we get:

$$ \label{eq:poiss-x2x-mean-s2}
\mathrm{E}[X \, (X-1)] = \lambda^2 \cdot e^{-\lambda} \cdot \sum_{z=0}^\infty \frac{\lambda^z}{z!} \; .
$$

Using the power series expansion of the exponential function

$$ \label{eq:exp-ps}
e^x = \sum_{n=0}^\infty \frac{x^n}{n!} \; ,
$$

the expected value of $X \, (X-1)$ finally becomes

$$ \label{eq:poiss-x2x-mean-s3}
\mathrm{E}[X \, (X-1)] = \lambda^2 \cdot e^{-\lambda} \cdot e^{\lambda} = \lambda^2 \; .
$$

Note that this expectation can be written as

$$ \label{eq:poiss-x2-mean-s1}
\mathrm{E}[X \, (X-1)] = \mathrm{E}(X^2 - X) = \mathrm{E}(X^2) - \mathrm{E}(X) \; ,
$$

such that, with \eqref{eq:poiss-x2x-mean-s3} and \eqref{eq:poiss-mean}, we have:

$$ \label{eq:poiss-x2-mean-s2}
\mathrm{E}(X^2) - \mathrm{E}(X) = \lambda^2 \quad \Rightarrow \quad \mathrm{E}(X^2) = \lambda^2 + \lambda \; .
$$

Plugging \eqref{eq:poiss-x2-mean-s2} and \eqref{eq:poiss-mean} into \eqref{eq:var-mean}, the variance of a Poisson random variable finally becomes

$$ \label{eq:poiss-var-qed}
\mathrm{Var}(X) = \lambda^2 + \lambda - \lambda^2 = \lambda \; .
$$