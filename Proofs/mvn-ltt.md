---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2019-05-02 14:45:00

title: "Linear transformation theorem for the multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Linear transformation theorem"

dependencies:
  - title: moment-generating function of a random vector
  - title: joint moment-generating function of the multivariate normal distribution

proof_id: "P1"
shortcut: "mvn-ltt"
username: "JoramSoch"
---


**Theorem:** Let $x$ follow a multivariate normal distribution:

$$ \label{eq:mvn}
x \sim \mathrm{N}(\mu, \Sigma) \; .
$$

Then, any linear transformation of $x$ is also multivariate normally distributed:

$$ \label{eq:mvn-lt}
y = Ax + b \sim \mathrm{N}(A\mu + b, A \Sigma A^T) \; .
$$


**Proof:** The moment-generating function of a random vector $x$ is

$$ \label{eq:vect-mgf}
M_x(t) = \mathbb{E} \left( \exp \left[ t^\mathrm{T} x \right] \right)
$$

and therefore the moment-generating function of the random vector $y$ is given by

$$ \label{eq:y-mfg-s1}
\begin{split}
M_y(t) &= \mathbb{E} \left( \exp \left[ t^\mathrm{T} (Ax + b) \right] \right) \\
&= \mathbb{E} \left( \exp \left[ t^\mathrm{T} A x \right] \cdot \exp \left[ t^\mathrm{T} b \right] \right) \\
&= \exp \left[ t^\mathrm{T} b \right] \cdot \mathbb{E} \left( \exp \left[ t^\mathrm{T} A x \right] \right) \\
&= \exp \left[ t^\mathrm{T} b \right] \cdot M_x(At) \; .
\end{split}
$$

The joint moment-generating function of the multivariate normal distribution is

$$ \label{eq:mvn-mgf}
M_x(t) = \exp \left[ t^\mathrm{T} \mu + \frac{1}{2} t^\mathrm{T} \Sigma t \right]
$$

and therefore the moment-generating function of the random vector $y$ becomes

$$ \label{eq:y-mfg-ss}
\begin{split}
M_y(t) &= \exp \left[ t^\mathrm{T} b \right] \cdot M_x(At) \\
&= \exp \left[ t^\mathrm{T} b \right] \cdot \exp \left[ t^\mathrm{T} A \mu + \frac{1}{2} t^\mathrm{T} A \Sigma A^\mathrm{T} t \right] \\
&= \exp \left[ t^\mathrm{T} \left( A \mu + b \right) + \frac{1}{2} t^\mathrm{T} A \Sigma A^\mathrm{T} t \right] \; .
\end{split}
$$

Because moment-generating function and probability density function of a random variable are equivalent, this demonstrates that $y$ is following a multivariate normal distribution with mean $A \mu + b$ and covariance $A \Sigma A^\mathrm{T}$.

<div align="right">&#8718;</div>


**Dependencies:**
- moment-generating function of a random vector
- joint moment-generating function of the multivariate normal distribution


**Source:**
- Taboga, Marco (2010): "Linear combinations of normal random variables"; in: *Lectures on probability and statistics*; URL: <https://www.statlect.com/probability-distributions/normal-distribution-linear-combinations>.