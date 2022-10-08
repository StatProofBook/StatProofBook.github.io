---
layout: proof
mathjax: true

author: "Maja Pavlovic"
affiliation: "Queen Mary University London"
e_mail: "m.pavlovic@se22.qmul.ac.uk"
date: 2022-10-02 09:46:00

title: "Mean of the log-normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Log-normal distribution"
theorem: "Mean"

sources:
  - authors: "Taboga, Marco"
    year: 2022
    title: "Log-normal distribution"
    in: "Lectures on probability theory and mathematical statistics"
    pages: "retrieved on 2022-10-01"
    url: "https://www.statlect.com/probability-distributions/log-normal-distribution"

proof_id: "P354"
shortcut: "lognorm-mean"
username: "majapavlo"
---

**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [log-normal distribution](/D/lognorm):

$$ \label{eq:lognorm}
X \sim \ln  \mathcal{N}(\mu, \sigma^2) 
$$

Then, the [mean or expected value](/D/mean) of $X$ is

$$
\mathrm{E}(X) = \exp \left( \mu + \frac{1}{2} \sigma^2 \right) 
$$


**Proof:** The [expected value](/D/mean) is the probability-weighted average over all possible values:

$$ \label{eq:mean}
\mathrm{E}(X) = \int_{\mathcal{X}} x \cdot f_X(x) \, \mathrm{d}x 
$$

With the [probability density function of the log-normal distribution](/P/lognorm-pdf), this is:

$$ \label{eq:lognorm-mean-s1}
\begin{split}
\mathrm{E}(X) &= \int_{0}^{+\infty} x \cdot \frac{1}{x\sqrt{2 \pi \sigma^2} } \cdot \exp \left[ -\frac{1}{2}  \frac{\left(\ln x-\mu\right)^2}{\sigma^2} \right]  \mathrm{d}x \\
&= \frac{1}{\sqrt{2 \pi \sigma^2} } \int_{0}^{+\infty} \exp \left[ -\frac{1}{2}  \frac{\left(\ln x-\mu\right)^2}{\sigma^2} \right] \mathrm{d}x
\end{split}
$$

Substituting $z = \frac{\ln x -\mu}{\sigma}$, i.e. $x = \exp \left( \mu + \sigma z \right )$ we have:

$$ \label{eq:lognorm-mean-s2}
\begin{split}
\mathrm{E}(X) &= \frac{1}{\sqrt{2 \pi \sigma^2} } \int_{(-\infty -\mu )/ (\sigma)}^{(\ln x -\mu )/ (\sigma)} \exp \left( -\frac{1}{2}  z^2 \right) \mathrm{d} \left[ \exp \left( \mu +\sigma z \right) \right] \\
&= \frac{1}{\sqrt{2 \pi \sigma^2} } \int_{-\infty}^{+\infty} \exp \left( -\frac{1}{2}  z^2 \right) \sigma \exp \left( \mu +\sigma z \right) \mathrm{d}z \\
&= \frac{1}{\sqrt{2 \pi} } \int_{-\infty}^{+\infty} \exp \left( -\frac{1}{2}  z^2 + \sigma z + \mu \right)  \mathrm{d}z \\
&= \frac{1}{\sqrt{2 \pi} } \int_{-\infty}^{+\infty} \exp \left[  -\frac{1}{2} \left(  z^2  - 2 \sigma z - 2 \mu \right) \right]  \mathrm{d}z
\end{split}
$$

Now multiplying $\exp \left( \frac{1}{2} \sigma^2 \right)$ and $\exp \left( -\frac{1}{2} \sigma^2 \right)$, we have:

$$ \label{eq:lognorm-mean-s3}
\begin{split}
\mathrm{E}(X) &= \frac{1}{\sqrt{2 \pi} } \int_{-\infty}^{+\infty} \exp \left[  -\frac{1}{2} \left(  z^2  - 2 \sigma z + \sigma^2 - 2 \mu - \sigma^2 \right) \right]  \mathrm{d}z \\
&= \frac{1}{\sqrt{2 \pi} } \int_{-\infty}^{+\infty} \exp \left[ -\frac{1}{2} \left( z^2 - 2\sigma z + \sigma^2 \right) \right] \exp \left( \mu + \frac{1}{2} \sigma^2  \right) \mathrm{d}z \\
&= \exp \left( \mu + \frac{1}{2} \sigma^2  \right) \int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi} } \exp \left[ -\frac{1}{2} \left( z - \sigma \right)^2 \right] \mathrm{d}z
\end{split}
$$

The [probability density function of a normal distribution](/P/norm-pdf) reads: 

$$ \label{eq:norm-pdf}
f_X(x) = \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right]
$$

With unit variance this reads:

$$
= \frac{1}{\sqrt{2 \pi}} \cdot \exp \left[ -\frac{1}{2} \left({x-\mu} \right)^2 \right]
$$

Using the definition of the [probability density function](/D/pdf)

$$ \label{eq:def-pdf}
\int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi}} \cdot \exp \left[ -\frac{1}{2} \left({x-\mu} \right)^2 \right]  \mathrm{d}x  = 1
$$

and applying \eqref{eq:def-pdf} to \eqref{eq:lognorm-mean-s3}, we have:

$$ \label{eq:lognorm-mean}
\mathrm{E}(X) = \exp \left( \mu + \frac{1}{2} \sigma^2  \right) .
$$