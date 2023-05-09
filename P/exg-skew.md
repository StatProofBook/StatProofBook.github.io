---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2023-04-21 12:00:00

title: "Skewness of the ex-Gaussian distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "ex-Gaussian distribution"
theorem: "Skewness"

sources:
  
proof_id: "P408"
shortcut: "exg-skew"
username: "tomfaulkenberry"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following an [ex-Gaussian distribution](/D/exg):

$$ \label{eq:exg}
X \sim \text{ex-Gaussian}(\mu, \sigma, \lambda) \; .
$$

Then the [skewness](/D/skew) of $X$ is

$$ \label{eq:exg-skew}
\mathrm{Skew}(X) = \frac{2}{\lambda^3\left( \sigma^2 + \frac{1}{\lambda^2}\right)^{\frac{3}{2}}} \; .
$$

**Proof:** 

To compute the skewness of $X$, we [partition the skewness into expected values](/P/skew-mean):

$$ \label{eq:skew-mean}
\mathrm{Skew}(X) = \frac{\mathrm{E}(X^3)-3\mu\sigma^2-\mu^3}{\sigma^3} \; ,
$$

where $\mu$ and $\sigma$ are the mean and standard deviation of $X$, respectively. To prevent confusion between the labels used for the ex-Gaussian parameters in \eqref{eq:exg} and the mean and standard deviation of $X$, we rewrite \eqref{eq:skew-mean} as

$$ \label{eq:skew-mean-alt}
\mathrm{Skew}(X) = \frac{\mathrm{E}(X^3) - 3\cdot \mathrm{E}(X)\cdot \mathrm{Var}(X) - \mathrm{E}(X)^3}{\mathrm{Var}(X)^{\frac{3}{2}}} \; .
$$

Since $X$ follows an [ex-Gaussian distribution](/D/exg), the [mean](/P/exg-mean) of $X$ is given by 

$$ \label{eq:exg-mean}
\mathrm{E}(X) = \mu + \frac{1}{\lambda}
$$

and the [variance](/P/exg-var) of $X$ is given by

$$ \label{eq:exg-var}
\mathrm{Var}(X) = \sigma^2 + \frac{1}{\lambda^2} \; .
$$

Thus, the primary work is to compute $\mathrm{E}(X^3)$. To do this, we use the [moment-generating function of the ex-Gaussian distribution](/P/exg-mgf) to calculate

$$ \label{eq:exg-moment}
\mathrm{E}(X^3) = M_X'''(0)
$$

based on the [relationship between raw moment and moment-generating function](/P/mom-mgf).

First, we differentiate the [moment-generating function of the ex-Gaussian distribution](/P/exg-mgf)

$$ \label{eq:exg-mgf}
M_X(t) = \left( \frac{\lambda}{\lambda-t} \right) \exp \left[ \mu t + \frac{1}{2}\sigma^2t^2 \right]
$$

with respect to $t$. Using the product rule and chain rule, we have:

$$ \label{eq:exg-skew-s1}
\begin{split}
M'_X(t) &= \frac{\lambda}{(\lambda-t)^2}\exp \left[ \mu t + \frac{1}{2}\sigma^2t^2\right] + \left(\frac{\lambda}{\lambda-t}\right)\exp\left[\mu t + \frac{1}{2}\sigma^2t^2\right] (\mu + \sigma^2t)\\
&= \left(\frac{\lambda}{\lambda-t}\right) \cdot \exp\left[\mu t + \frac{1}{2}\sigma^2t^2\right] \cdot \left[ \frac{1}{\lambda-t} +\mu +\sigma^2t \right] \\
&= M_X(t)\cdot \left[ \frac{1}{\lambda-t} + \mu + \sigma^2t\right] \; .
\end{split}
$$

We then use the product rule to obtain the second derivative:

$$ \label{eq:exg-skew-s2}
\begin{split}
M_X''(t) &= M_X'(t)\cdot \left[ \frac{1}{\lambda-t} + \mu + \sigma^2t\right] + M_X(t)\cdot \left[ \frac{1}{(\lambda-t)^2}+\sigma^2\right] \\
&= M_X(t)\cdot \left[ \frac{1}{\lambda-t} + \mu + \sigma^2t\right]^2 + M_X(t)\cdot \left[ \frac{1}{(\lambda-t)^2}+\sigma^2\right]\\
&= M_X(t) \cdot \left[ \left( \frac{1}{\lambda-t} + \mu + \sigma^2t\right)^2 + \frac{1}{(\lambda-t)^2} + \sigma^2\right] \; .
\end{split}
$$

Finally, we use the product rule and chain rule to obtain the third derivative:

$$ \label{eq:exg-skew-s3}
M_X'''(t) = M_X'(t)\left[\left(\frac{1}{\lambda-t}+\mu+\sigma^2t\right)^2 + \frac{1}{(\lambda-t)^2}+\sigma^2\right] + M_X(t)\left[2\left(\frac{1}{\lambda-t}+\mu+\sigma^2t\right)\left(\frac{1}{(\lambda-t)^2} + \sigma^2\right) + \frac{2}{(\lambda-t)^3}\right] \; .
$$

Applying \eqref{eq:exg-moment}, together with \eqref{eq:exg-skew-s3}, yields:

$$ \label{eq:exg-skew-s4}
\begin{split}
\mathrm{E}(X^3) &= M_X'''(0)\\
&= M_X'(0)\left[\left(\frac{1}{\lambda}+\mu\right)^2 + \frac{1}{\lambda^2} + \sigma^2\right] + M_X(0)\left[2\left(\frac{1}{\lambda}+\mu\right)\left(\frac{1}{\lambda^2}+\sigma^2\right)+\frac{2}{\lambda^3}\right]\\
&= \left(\mu + \frac{1}{\lambda}\right)\left(\frac{1}{\lambda^2}+\frac{2\mu}{\lambda} + \mu^2 + \frac{1}{\lambda^2}+\sigma^2\right) + \left(\frac{2}{\lambda^3}+\frac{2\sigma^2}{\lambda} + \frac{2\mu}{\lambda^2}+2\mu\sigma^2 + \frac{2}{\lambda^3}\right)\\
&= \left(\mu+\frac{1}{\lambda}\right)\left(\frac{2}{\lambda^2}+\frac{2\mu}{\lambda} + \mu^2+\sigma^2\right) + \left(\frac{4}{\lambda^3}+\frac{2\sigma^2}{\lambda} + \frac{2\mu}{\lambda^2} + 2\mu\sigma^2\right)\\
&= \frac{2\mu}{\lambda^2} + \frac{2\mu^2}{\lambda} + \mu^3 + \mu\sigma^2 + \frac{2}{\lambda^3} + \frac{2\mu}{\lambda^2} + \frac{\mu^2}{\lambda} + \frac{\sigma^2}{\lambda} + \frac{4}{\lambda^3} + \frac{2\sigma^2}{\lambda} + \frac{2\mu}{\lambda^2} + 2\mu\sigma^2\\
&= \frac{6\mu}{\lambda^2} + \frac{6}{\lambda^3} + \frac{3\mu^2+ 3\sigma^2}{\lambda} + 3\mu\sigma^2 + \mu^3 \; .
\end{split}
$$

We now substitute \eqref{eq:exg-skew-s4}, \eqref{eq:exg-mean}, and \eqref{eq:exg-var} into the numerator of \eqref{eq:skew-mean-alt}, giving

$$ \label{eq:exg-skew-s5}
\begin{split}
\mathrm{E}(X^3) - 3\cdot \mathrm{E}(X)\cdot \mathrm{Var}(X) - \mathrm{E}(X)^3 &= \left(\frac{6\mu}{\lambda^2} + \frac{6}{\lambda^3} + \frac{3\mu^2+ 3\sigma^2}{\lambda} + 3\mu\sigma^2 + \mu^3\right) - 3\left(\mu+\frac{1}{\lambda}\right)\left(\sigma^2+\frac{1}{\lambda^2}\right)- \left(\mu+\frac{1}{\lambda}\right)^3\\
&= \frac{6\mu}{\lambda^2} + \frac{6}{\lambda^3} + \frac{3\mu^2+ 3\sigma^2}{\lambda} + 3\mu\sigma^2 + \mu^3 - 3\mu\sigma^2 - \frac{3\mu}{\lambda^2} - \frac{3\sigma^2}{\lambda} - \frac{3}{\lambda^3} - \mu^3 - \frac{3\mu^2}{\lambda} - \frac{3\mu}{\lambda^2}-\frac{1}{\lambda^3}\\
&= \frac{2}{\lambda^3} \; .
\end{split}
$$

Thus, we have:

$$ \label{eq:exg-skew-s6}
\begin{split}
\mathrm{Skew}(X) &= \frac{\mathrm{E}(X^3) - 3\cdot \mathrm{E}(X)\cdot \mathrm{Var}(X) - \mathrm{E}(X)^3}{\mathrm{Var}(X)^{\frac{3}{2}}}\\
&= \frac{\frac{2}{\lambda^3}}{\left(\sigma^2 + \frac{1}{\lambda^2}\right)^{\frac{3}{2}}}\\
&= \frac{2}{\lambda^3\left(\sigma^2+\frac{1}{\lambda^2}\right)^{\frac{3}{2}}} \; .
\end{split}
$$

This completes the proof of \eqref{eq:exg-skew}.