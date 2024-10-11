---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-10-11 11:52:29

title: "Marginally normal does not imply jointly normal"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Marginally normal does not imply jointly normal"

sources:
  - authors: "Wikipedia"
    year: 2024
    title: "Misconceptions about the normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-10-11"
    url: "https://en.wikipedia.org/wiki/Misconceptions_about_the_normal_distribution#A_symmetric_example"

proof_id: "P474"
shortcut: "norm-margjoint"
username: "JoramSoch"
---


**Theorem:** Consider two [random variables](/D/rvar) $X$ and $Y$. If the [marginal distribution](/D/dist-marg) of each of them is a [normal distribution](/D/norm), then the [joint distribution](/D/dist-joint) $X$ and $Y$ is not necessarily a [(multivariate) normal distribution](/D/mvn).


**Proof:** Consider [the example used to show that normally distributed and uncorrelated does not imply independent](/P/norm-corrind). This is characterized by the [random variables](/D/rvar)

$$ \label{eq:V-W}
\begin{split}
V &\sim \mathrm{Bern}\left( \frac{1}{2} \right) \\
W &= 2V-1 \; .
\end{split}
$$

and

$$ \label{eq:X-Y}
\begin{split}
X &\sim \mathcal{N}(0,1) \\
Y &= WX \; .
\end{split}
$$

Under these conditions, [it can be shown that](/P/norm-corrind)

$$ \label{eq:X-Y-dist}
X \sim \mathcal{N}(0,1)
\quad \text{and} \quad
Y \sim \mathcal{N}(0,1) \; .
$$

The [linear transformation theorem for the multivariate normal distribution](/P/mvn-ltt)

$$ \label{eq:mvn-ltt}
x \sim \mathcal{N}(\mu, \Sigma) \quad \Rightarrow \quad y = Ax + b \sim \mathcal{N}(A\mu + b, A \Sigma A^\mathrm{T})
$$

implies that, for [bivariate normal random variables](/D/bvn) $X_1$ and $X_2$,

$$ \label{eq:bvn}
\left[ \begin{matrix} X_1 \\ X_2 \end{matrix} \right] \sim
\mathcal{N}\left(
\left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right],
\left[ \begin{matrix} \sigma_1^2 & \sigma_{12} \\ \sigma_{12} & \sigma_2^2 \end{matrix} \right]
\right) \; .
$$

any linear combination of $X_1$ and $X_2$ with non-zero coefficients

$$ \label{eq:bvn-Z}
Z = a X_1 + b X_2, \; a \neq 0, \; b \neq 0
$$

[follows a univariate normal distribution](/P/bvn-lincomb):

$$ \label{eq:bvn-lincomb}
Z \sim \mathcal{N}\left( a \mu_1 + b \mu_2, a^2 \sigma_1^2 + 2 a b \sigma_{12} + b^2 \sigma_2^2 \right) \; .
$$

Consider the sum of $X$ and $Y$ defined by \eqref{eq:X-Y}:

$$ \label{eq:Z}
Z = X + Y = a X + b Y
\quad \text{with} \quad
a = b = 1 \; .
$$

If $X$ and $Y$ were [bivariate normally distributed](/D/bvn), then this sum should be [univariate normally distributed](/D/norm). However, this sum cannot be normally distributed, since

$$ \label{eq:Z-dist}
\mathrm{Pr}(X + Y = 0)  = \frac{1}{2}
\quad \text{and} \quad
\mathrm{Pr}(X + Y = 2X) = \frac{1}{2} \; ,
$$

because

$$ \label{eq:Y-dist}
Y = \left\{
\begin{array}{rl}
 X \; , & \text{with probability} \; 1/2 \\
-X \; , & \text{with probability} \; 1/2
\end{array}
\right. \; .
$$

Thus, $X$ and $Y$ are not following a [bivariate normal distribution](/D/bvn). Therefore, $X$ and $Y$ defined by \eqref{eq:X-Y} and \eqref{eq:V-W} constitute an example for two [random variables](/D/rvar) that are [marginally normal](/D/norm), but not [jointly normal](/D/mvn).