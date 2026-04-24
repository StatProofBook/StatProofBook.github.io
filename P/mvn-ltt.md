---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2019-08-27 12:14:00

title: "Linear transformation theorem for the multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Linear transformation"

sources:
  - authors: "Taboga, Marco"
    year: 2010
    title: "Linear combinations of normal random variables"
    in: "Lectures on probability and statistics"
    pages: "retrieved on 2019-08-27"
    url: "https://www.statlect.com/probability-distributions/normal-distribution-linear-combinations"

proof_id: "P1"
shortcut: "mvn-ltt"
username: "JoramSoch"
---


**Theorem:** Let $X \in \mathbb{R}^n$ follow a [multivariate normal distribution](/D/mvn):

$$ \label{eq:mvn}
X \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, any linear transformation of $X$ is also multivariate normally distributed

$$ \label{eq:mvn-lt}
Y = AX + b \sim \mathcal{N}(A\mu + b, A \Sigma A^\mathrm{T})
$$

where $A$ is an $m \times n$ matrix and $b$ is an $m$-dimensional vector.


**Proof:** The [moment-generating function of a random vector](/D/mgf) $X$ is

$$ \label{eq:vect-mgf}
M_X(t) = \mathrm{E} \left( \exp \left[ t^\mathrm{T} X \right] \right)
$$

and therefore the moment-generating function of the random vector $Y$ is given by

$$ \label{eq:Y-mgf-s1}
\begin{split}
   M_Y(t)
&\overset{\eqref{eq:mvn-lt}}{=} \mathrm{E} \left( \exp \left[ t^\mathrm{T} (AX + b) \right] \right) \\
&= \mathrm{E} \left( \exp \left[ t^\mathrm{T} A X \right] \cdot \exp \left[ t^\mathrm{T} b \right] \right) \\
&= \exp \left[ t^\mathrm{T} b \right] \cdot \mathrm{E} \left( \exp \left[ t^\mathrm{T} A X \right] \right) \\
&\overset{\eqref{eq:vect-mgf}}{=} \exp \left[ t^\mathrm{T} b \right] \cdot M_X(A^\mathrm{T} t) \; .
\end{split}
$$

The [moment-generating function of the multivariate normal distribution](/P/mvn-mgf) is

$$ \label{eq:mvn-mgf}
M_X(t) = \exp \left[ t^\mathrm{T} \mu + \frac{1}{2} t^\mathrm{T} \Sigma t \right]
$$

and therefore the moment-generating function of the random vector $Y$ becomes

$$ \label{eq:Y-mgf-s2}
\begin{split}
   M_Y(t)
&\overset{\eqref{eq:Y-mgf-s1}}{=} \exp \left[ t^\mathrm{T} b \right] \cdot M_X(A^\mathrm{T} t) \\
&\overset{\eqref{eq:mvn-mgf}}{=} \exp \left[ t^\mathrm{T} b \right] \cdot \exp \left[ t^\mathrm{T} A \mu + \frac{1}{2} t^\mathrm{T} A \Sigma A^\mathrm{T} t \right] \\
&= \exp \left[ t^\mathrm{T} \left( A \mu + b \right) + \frac{1}{2} t^\mathrm{T} A \Sigma A^\mathrm{T} t \right] \; .
\end{split}
$$

Because moment-generating function and probability density function of a random variable are equivalent, this demonstrates that $Y$ is following a multivariate normal distribution with mean $A \mu + b$ and covariance $A \Sigma A^\mathrm{T}$.