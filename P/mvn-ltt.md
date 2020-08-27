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


**Theorem:** Let $x$ follow a [multivariate normal distribution](/D/mvn):

$$ \label{eq:mvn}
x \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, any linear transformation of $x$ is also multivariate normally distributed:

$$ \label{eq:mvn-lt}
y = Ax + b \sim \mathcal{N}(A\mu + b, A \Sigma A^\mathrm{T}) \; .
$$


**Proof:** The [moment-generating function of a random vector](/D/mgf) $x$ is

$$ \label{eq:vect-mgf}
M_x(t) = \mathbb{E} \left( \exp \left[ t^\mathrm{T} x \right] \right)
$$

and therefore the moment-generating function of the random vector $y$ is given by

$$ \label{eq:y-mgf-s1}
\begin{split}
M_y(t) &\overset{\eqref{eq:mvn-lt}}{=} \mathbb{E} \left( \exp \left[ t^\mathrm{T} (Ax + b) \right] \right) \\
&= \mathbb{E} \left( \exp \left[ t^\mathrm{T} A x \right] \cdot \exp \left[ t^\mathrm{T} b \right] \right) \\
&= \exp \left[ t^\mathrm{T} b \right] \cdot \mathbb{E} \left( \exp \left[ t^\mathrm{T} A x \right] \right) \\
&\overset{\eqref{eq:vect-mgf}}{=} \exp \left[ t^\mathrm{T} b \right] \cdot M_x(At) \; .
\end{split}
$$

The [moment-generating function of the multivariate normal distribution](/P/mvn-mgf) is

$$ \label{eq:mvn-mgf}
M_x(t) = \exp \left[ t^\mathrm{T} \mu + \frac{1}{2} t^\mathrm{T} \Sigma t \right]
$$

and therefore the moment-generating function of the random vector $y$ becomes

$$ \label{eq:y-mgf-s2}
\begin{split}
M_y(t) &\overset{\eqref{eq:y-mgf-s1}}{=} \exp \left[ t^\mathrm{T} b \right] \cdot M_x(At) \\
&\overset{\eqref{eq:mvn-mgf}}{=} \exp \left[ t^\mathrm{T} b \right] \cdot \exp \left[ t^\mathrm{T} A \mu + \frac{1}{2} t^\mathrm{T} A \Sigma A^\mathrm{T} t \right] \\
&= \exp \left[ t^\mathrm{T} \left( A \mu + b \right) + \frac{1}{2} t^\mathrm{T} A \Sigma A^\mathrm{T} t \right] \; .
\end{split}
$$

Because moment-generating function and probability density function of a random variable are equivalent, this demonstrates that $y$ is following a multivariate normal distribution with mean $A \mu + b$ and covariance $A \Sigma A^\mathrm{T}$.