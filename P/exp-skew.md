---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2023-04-24 12:00:00

title: "Skewness of the exponential distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Exponential distribution"
theorem: "Skewness"

sources:
  
proof_id: "P409"
shortcut: "exp-skew"
username: "tomfaulkenberry"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following an [exponential distribution](/D/exp):

$$ \label{eq:exp}
X \sim \mathrm{Exp}(\lambda) \; .
$$

Then the [skewness](/D/skew) of $X$ is

$$ \label{eq:exp-skew}
\mathrm{Skew}(X) = 2 \; .
$$

**Proof:** 

To compute the skewness of $X$, we [partition the skewness into expected values](/P/skew-mean):

$$ \label{eq:skew-mean}
\mathrm{Skew}(X) = \frac{\mathrm{E}(X^3)-3\mu\sigma^2-\mu^3}{\sigma^3} \; ,
$$

where $\mu$ and $\sigma$ are the mean and standard deviation of $X$, respectively. Since $X$ follows an [exponential distribution](/D/exp), the [mean](/P/exp-mean) of $X$ is given by 

$$ \label{eq:exp-mean}
\mu = \mathrm{E}(X) = \frac{1}{\lambda}
$$

and the [standard deviation](/P/exp-var) of $X$ is given by

$$ \label{eq:exp-var}
\sigma = \sqrt{\mathrm{Var}(X)} = \sqrt{\frac{1}{\lambda^2}} = \frac{1}{\lambda} \; .
$$

Substituting \eqref{eq:exp-mean} and \eqref{eq:exp-var} into \eqref{eq:skew-mean} gives:

$$ \label{eq:skew-mean-alt}
\begin{split}
\mathrm{Skew}(X) &= \frac{\mathrm{E}(X^3)-3\mu\sigma^2-\mu^3}{\sigma^3}\\
&= \frac{\mathrm{E}(X^3)}{\sigma^3}-\frac{3\mu\sigma^2+\mu^3}{\sigma^3}\\
&= \frac{\mathrm{E}(X^3)}{\left(\frac{1}{\lambda}\right)^3}-\frac{3\left(\frac{1}{\lambda}\right)\left(\frac{1}{\lambda}\right)^2 + \left(\frac{1}{\lambda}\right)^3}{\left(\frac{1}{\lambda}\right)^3}\\
&= \lambda^3\cdot\mathrm{E}(X^3)-\frac{\frac{3}{\lambda^3}+\frac{1}{\lambda^3}}{\frac{1}{\lambda^3}}\\
&= \lambda^3\cdot\mathrm{E}(X^3)-4 \; .
\end{split}
$$

Thus, the remaining work is to compute $\mathrm{E}(X^3)$. To do this, we use the [moment-generating function of the exponential distribution](/P/exp-mgf) to calculate

$$ \label{eq:exp-moment}
\mathrm{E}(X^3) = M_X'''(0)
$$

based on the [relationship between raw moment and moment-generating function](/P/mom-mgf).

First, we differentiate the [moment-generating function of the exponential distribution](/P/exp-mgf)

$$ \label{eq:exp-mgf}
M_X(t) = \frac{\lambda}{\lambda-t} = \lambda(\lambda-t)^{-1}
$$

with respect to $t$. Using the chain rule gives:

$$ \label{eq:exp-skew-s1}
\begin{split}
M_X'(t) &= -1\cdot \lambda(\lambda-t)^{-2}\cdot (-1) \\
&= \lambda(\lambda-t)^{-2} \; .
\end{split}
$$

We continue using the chain rule to obtain the second derivative:

$$ \label{eq:exp-skew-s2}
\begin{split}
M_X''(t) &= -2\cdot \lambda(\lambda-t)^{-3}\cdot (-1) \\
&= 2\lambda(\lambda-t)^{-3} \; .
\end{split}
$$

Finally, one more application of the chain rule gives us the third derivative:

$$ \label{eq:exp-skew-s3}
\begin{split}
M_X'''(t) &= -3\cdot 2\lambda(\lambda-t)^{-4}\cdot (-1)\\
&= 6\lambda(\lambda-t)^{-4} \\
&= \frac{6\lambda}{(\lambda-t)^4} \; .
\end{split}
$$

Applying \eqref{eq:exp-moment}, together with \eqref{eq:exp-skew-s3}, yields

$$ \label{eq:exp-skew-s4}
\begin{split}
\mathrm{E}(X^3) &= M_X'''(0)\\
&= \frac{6\lambda}{(\lambda-0)^4}\\
&= \frac{6\lambda}{\lambda^4}\\
&= \frac{6}{\lambda^3} \; .
\end{split}
$$

We now substitute \eqref{eq:exp-skew-s4} into \eqref{eq:skew-mean-alt}, giving

$$ \label{eq:exp-skew-s5}
\begin{split}
\mathrm{Skew}(X) &= \lambda^3\cdot\mathrm{E}(X^3)-4 \\
&= \lambda^3\cdot \left(\frac{6}{\lambda^3}\right)-4\\
&= 6-4\\
&= 2 \; .
\end{split}
$$

This completes the proof of \eqref{eq:exp-skew}.