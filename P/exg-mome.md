---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2023-10-23 12:00:00

title: "Method of moments for ex-Gaussian distributed data"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "ex-Gaussian distribution"
theorem: "Method of moments"

sources:
  
proof_id: "P424"
shortcut: "exg-mome"
username: "tomfaulkenberry"
---
  
  

**Theorem:** Let $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ be a set of observed data [independent and identically distributed](/D/iid) according to an [ex-Gaussian distribution](/D/exg) with parameters $\mu$, $\sigma$, and $\lambda$:

$$ \label{eq:exq}
y_i \sim \mathrm{ex-Gaussian}(\mu,\sigma,\lambda), \quad i = 1, \ldots, n \; .
$$

Then, the [method-of-moments estimates](/D/mome) for the parameters $\mu$, $\sigma$, and $\lambda$ are given by

$$ \label{eq:exg-MoM}
\begin{split}
\hat{\mu} &= \bar{y} - \sqrt[3]{\frac{\bar{s}\cdot \bar{v}^{3/2}}{2}}\\
\hat{\sigma} &= \sqrt{\bar{v}\cdot\left(1 - \sqrt[3]{\frac{\bar{s}^2}{4}}\right)}\\
\hat{\lambda} &= \sqrt[3]{\frac{2}{\bar{s}\cdot \bar{v}^{3/2}}} \; ,
\end{split}
$$

where $\bar{y}$ is the [sample mean](/D/mean-samp) and $\bar{v}$ is the [sample variance](/D/var-samp), and $\bar{s}$ is the [sample skewness](/D/skew-samp)

$$ \label{eq:y-mean-var-skew}
\begin{split}
\bar{y} &= \frac{1}{n} \sum_{i=1}^n y_i \\
\bar{v} &= \frac{1}{n-1} \sum_{i=1}^n (y_i - \bar{y})^2 \\
\bar{s} &= \frac{\frac{1}{n}\sum_{i=1}^n (y_i-\bar{y})^3}{\left[\frac{1}{n}\sum_{i=1}^n(y_i-\bar{y})^2\right]^{3/2}} \; .
\end{split}
$$


**Proof:** The [mean](/P/exg-mean), [variance](/P/exg-var), and [skewness](/P/exg-skew) of the [ex-Gaussian distribution](/D/exg) in terms of the parameters $\mu$, $\sigma$, and $\lambda$ are given by

$$ \label{eq:exg-E-Var-Skew}
\begin{split}
\mathrm{E}(X) &= \mu + \frac{1}{\lambda} \\
\mathrm{Var}(X) &= \sigma^2 + \frac{1}{\lambda^2}\\
\mathrm{Skew}(X) &= \frac{2}{\lambda^3\left(\sigma^2+\frac{1}{\lambda^2}\right)^{3/2}} \; .
\end{split}
$$

Thus, [matching the moments](/D/mome) requires us to solve the following system of equations for $\mu$, $\sigma$, and $\lambda$:

$$ \label{eq:exg-mean-var-skew}
\begin{split}
\bar{y} &= \mu + \frac{1}{\lambda} \\
\bar{v} &= \sigma^2 + \frac{1}{\lambda^2}\\
\bar{s} &= \frac{2}{\lambda^3\left(\sigma^2+\frac{1}{\lambda^2}\right)^{3/2}} \; .
\end{split}
$$

To this end, our first step is to substitute the second equation of \eqref{eq:exg-mean-var-skew} into the third equation:

$$ \label{eq:lambda-s1}
\begin{split}
\bar{s} &= \frac{2}{\lambda^3\left(\sigma^2+\frac{1}{\lambda^2}\right)^{3/2}} \\
&= \frac{2}{\lambda^3\cdot \bar{v}^{3/2}} \; .
\end{split}
$$

Re-expressing \eqref{eq:lambda-s1} in terms of $\lambda^3$ and taking the cube root gives:

$$ \label{eq:lambda-s2}
\lambda = \sqrt[3]{\frac{2}{\bar{s}\cdot \bar{v}^{3/2}}} \; .
$$

Next, we solve the first equation of \eqref{eq:exg-mean-var-skew} for $\mu$ and substitute \eqref{eq:lambda-s2}:

$$ \label{eq:mu-s1}
\begin{split}
\mu &= \bar{y} - \frac{1}{\lambda}\\
&= \bar{y} - \sqrt[3]{\frac{\bar{s}\cdot\bar{v}^{3/2}}{2}} \; .
\end{split}
$$

Finally, we solve the second equation of \eqref{eq:exg-mean-var-skew} for $\sigma$:

$$ \label{eq:sigma-s1}
\sigma^2 = \bar{v} - \frac{1}{\lambda^2} \; .
$$

Taking the square root gives and substituting \eqref{eq:lambda-s2} gives:

$$ \label{eq:sigma-s2}
\begin{split}
\sigma &= \sqrt{\bar{v}-\frac{1}{\lambda^2}} \\
&= \sqrt{\bar{v} - \left(\sqrt[3]{\frac{\bar{s}\cdot \bar{v}^{3/2}}{2}}\right)^2} \\
&= \sqrt{\bar{v} - \bar{v}\cdot\sqrt[3]{\frac{\bar{s}^2}{4}}} \\
&= \sqrt{\bar{v}\cdot \left(1- \sqrt[3]{\frac{\bar{s}^2}{4}}\right)} \; .
\end{split}
$$

Together, \eqref{eq:mu-s1}, \eqref{eq:sigma-s2}, and \eqref{eq:lambda-s2} constitute the method-of-moment estimates of $\mu$, $\sigma$, and $\lambda$.
