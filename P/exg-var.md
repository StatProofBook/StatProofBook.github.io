---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: "2023-04-19 12:00:00"

title: "Variance of the ex-Gaussian distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "ex-Gaussian distribution"
theorem: "Variance"

sources:
  
proof_id: P406
shortcut: "exg-var"
username: "tomfaulkenberry"


**Theorem:** Let $X$ be a [random variable](/D/rvar) following an [ex-Gaussian distribution](/D/exg):

$$ \label{eq:exg}
X \sim \text{ex-Gaussian}(\mu, \sigma, \lambda) \; .
$$

Then the [variance](/D/var) of $X$ is 

$$ \label{eq:exg-var}
\mathrm{Var}(X) = \sigma^2 + \frac{1}{\lambda^2} \; .
$$


**Proof:** To compute the variance of $X$, we [partition the variance into expected values](/P/var-mean):

$$ \label{eq:var-mean}
\mathrm{Var}(X) = \mathrm{E}(X^2)-\mathrm{E}(X)^2 \; .
$$

We then use the [moment-generating function of the ex-Gaussian distribution](/P/exg-mgf) to calculate

$$ \label{eq:exg-moment}
\mathrm{E}(X^2) = M_X''(0) \; .
$$

First we differentiate

$$ \label{eq:exg-mgf}
M_X(t) = \left( \frac{\lambda}{\lambda-t} \right) \exp \left[ \mu t + \frac{1}{2}\sigma^2t^2 \right] \; .
$$

with respect to $t$. Using the product rule and chain rule gives

$$ \label{eq:exg-var-s1}
\begin{split}
M'_X(t) &= \frac{\lambda}{(\lambda-t)^2}\exp \left[ \mu t + \frac{1}{2}\sigma^2t^2\right] + \left(\frac{\lambda}{\lambda-t}\right)\exp\left[\mu t + \frac{1}{2}\sigma^2t^2\right] (\mu + \sigma^2t)\\
&= \left(\frac{\lambda}{\lambda-t}\right) \cdot \exp\left[\mu t + \frac{1}{2}\sigma^2t^2\right] \cdot \left[ \frac{1}{\lambda-t} +\mu +\sigma^2t \right] \\
&= M_X(t)\cdot \left[ \frac{1}{\lambda-t} + \mu + \sigma^2t\right] \; .
\end{split}
$$

We now use the product rule to obtain the second derivative:

$$ \label{eq:exg-var-s2}
\begin{split}
M_X''(t) &= M_X'(t)\cdot \left[ \frac{1}{\lambda-t} + \mu + \sigma^2t\right] + M_X(t)\cdot \left[ \frac{1}{(\lambda-t)^2}+\sigma^2\right] \\
&\overset{\eqref{eq:exg-var-s1}}{=} M_X(t)\cdot \left[ \frac{1}{\lambda-t} + \mu + \sigma^2t\right]^2 + M_X(t)\cdot \left[ \frac{1}{(\lambda-t)^2}+\sigma^2\right]\\
&= M_X(t) \cdot \left[ \left( \frac{1}{\lambda-t} + \mu + \sigma^2t\right)^2 + \frac{1}{(\lambda-t)^2} + \sigma^2\right] \\
&= \left(\frac{\lambda}{\lambda-t}\right)\cdot \exp\left[\mu t + \frac{1}{2}\sigma^2t^2\right]\cdot \left[ \left( \frac{1}{\lambda-t} + \mu + \sigma^2t\right)^2 + \frac{1}{(\lambda-t)^2} + \sigma^2\right]
\end{split}
$$

Applying \eqref{exg-moment} yields

$$ \label{eq:exg-var-s3}
\begin{split}
\mathrm{E}(X^2) &= M_X''(0) \\
&= \left(\frac{\lambda}{\lambda-0}\right) \cdot \exp\left[\mu\cdot 0 + \frac{1}{2}\sigma^2\cdot 0^2\right] \cdot \left[\left(\frac{1}{\lambda-0}+\mu + \sigma^2\cdot 0\right)^2 + \frac{1}{(\lambda-0)^2}+\sigma^2\right]\\
&= 1\cdot 1 \cdot \left[\left(\frac{1}{\lambda} + \mu\right)^2 + \frac{1}{\lambda^2}+\sigma^2 \right]\\
&= \frac{1}{\lambda^2} + \frac{2\mu}{\lambda} + \mu^2 + \frac{1}{\lambda^2} + \sigma^2\\
&= \frac{2}{\lambda^2} + \frac{2\mu}{\lambda} + \mu^2 + \sigma^2 \; .
\end{split}
$$

Since the [mean of an ex-Gaussian distribution](/P/exg-mean) is given by

$$ \label{exg-mean}
\mathrm{E}(X) = \mu + \frac{1}{\lambda} \; ,
$$

we can apply \eqref{eq:var-mean} to show

$$ \label{eq:exg-var-s4}
\begin{split}
\mathrm{Var}(X) &= \mathrm{E}(X^2) - \mathrm{E}(X)^2 \\
&= \left[\frac{2}{\lambda^2} + \frac{2\mu}{\lambda} + \mu^2+\sigma^2\right] - \left(\mu+\frac{1}{\lambda}\right)^2\\
&= \frac{2}{\lambda^2} + \frac{2\mu}{\lambda} + \mu^2+\sigma^2 - \mu^2 - \frac{2\mu}{\lambda} - \frac{1}{\lambda^2}\\
&= \sigma^2+\frac{1}{\lambda^2} \; .
\end{split}
$$

This completes the proof of \eqref{eq:exg-var}.
