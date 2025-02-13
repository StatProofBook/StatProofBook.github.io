---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2023-04-19 12:00:00

title: "Mean of the ex-Gaussian distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "ex-Gaussian distribution"
theorem: "Mean"

sources:
  
proof_id: "P405"
shortcut: "exg-mean"
username: "tomfaulkenberry"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following an [ex-Gaussian distribution](/D/exg):

$$ \label{eq:exg}
X \sim \mathrm{ex-Gaussian}(\mu, \sigma, \lambda) \; .
$$

Then, the [mean or expected value](/D/mean) of $X$ is 

$$ \label{eq:exg-mean}
\mathrm{E}(X) = \mu + \frac{1}{\lambda} \; .
$$


**Proof:** The mean or expected value $\mathrm{E}(X)$ is the first raw [moment](/D/mom) of $X$, so [we can use](/P/mom-mgf) the [moment-generating function of the ex-Gaussian distribution](/P/exg-mgf) to calculate

$$ \label{eq:mean-from-mgf}
\mathrm{E}(X) = M_X'(0) \; .
$$

First, we differentiate

$$ \label{eq:exg-mgf}
M_X(t) = \left( \frac{\lambda}{\lambda-t} \right) \exp \left[ \mu t + \frac{1}{2}\sigma^2t^2 \right]
$$

with respect to $t$. Using the product rule and chain rule gives:

$$ \label{eq:exg-mean-s1}
\begin{split}
M'_X(t) &= \frac{\lambda}{(\lambda-t)^2}\exp \left[ \mu t + \frac{1}{2}\sigma^2t^2\right] + \left(\frac{\lambda}{\lambda-t}\right)\exp\left[\mu t + \frac{1}{2}\sigma^2t^2\right] (\mu + \sigma^2t)\\
&= \left(\frac{\lambda}{\lambda-t}\right) \cdot \exp\left[\mu t + \frac{1}{2}\sigma^2t^2\right] \cdot \left[ \frac{1}{\lambda-t} +\mu +\sigma^2t \right] \; .
\end{split}
$$

Evaluating \eqref{eq:exg-mean-s1} at $t=0$ gives the desired result:

$$ \label{eq:exg-mean-s2}
\begin{split}
M'_X(0) &= \left(\frac{\lambda}{\lambda-0}\right) \cdot \exp\left[\mu\cdot 0 + \frac{1}{2}\sigma^2\cdot 0^2\right] \cdot \left[ \frac{1}{\lambda-0} + \mu + \sigma^2\cdot 0 \right] \\
&= 1\cdot 1 \cdot \left[ \frac{1}{\lambda} + \mu \right]\\
&= \mu + \frac{1}{\lambda} \; .
\end{split}
$$