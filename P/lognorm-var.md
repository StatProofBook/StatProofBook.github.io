---
layout: proof
mathjax: true

author: "Maja Pavlovic"
affiliation: "Queen Mary University London"
e_mail: "m.pavlovic@se22.qmul.ac.uk"
date: 2022-10-02 09:02:00

title: "Variance of the log-normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Log-normal distribution"
theorem: "Variance"

sources:
  - authors: "Taboga, Marco"
    year: 2022
    title: "Log-normal distribution"
    in: "Lectures on probability theory and mathematical statistics"
    pages: "retrieved on 2022-10-01"
    url: "https://www.statlect.com/probability-distributions/log-normal-distribution"
  - authors: "Wikipedia"
    year: 2022
    title: "Variance"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-10-01"
    url: "https://en.wikipedia.org/wiki/Variance#Definition"

proof_id: "P355"
shortcut: "lognorm-var"
username: "majapavlo"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [log-normal distribution](/D/lognorm):

$$
X \sim \ln \mathcal{N}(\mu, \sigma^2) .
$$

Then, the [variance](/D/var) of $X$ is

$$ \label{eq:lognorm-var}
\mathrm{Var}(X) = \exp \left(2\mu +2\sigma^2\right) - \exp \left(2\mu + \sigma^2\right) \; .
$$


**Proof:**
[Variance](/D/var) is defined as: 

$$ \label{eq:var}
\mathrm{Var}(X) = \mathrm{E}\left[ (X-\mathrm{E}(X))^2 \right] 
$$

which, [ partitioned into expected values](/P/var-mean) reads:

$$ \label{eq:var2}
\mathrm{Var}(X) = \mathrm{E}\left[ X^2 \right] - \mathrm{E}\left[ X \right]^2
$$

The [expected value of the log-normal distribution](/P/lognorm-mean) is: 

$$ \label{eq:lognorm-mean-ref}
\mathrm{E}[X] = \exp \left( \mu + \frac{1}{2} \sigma^2  \right)
$$

The second moment $\mathrm{E}[X^2]$ can be derived as follows:

$$ \label{eq:second-moment}
\begin{split}
\mathrm{E} [X^2] = \int_{- \infty}^{+\infty} x^2 \cdot f_\mathrm{X}(x) \, \mathrm{d}x \\
&= \int_{0}^{+\infty} x^2 \cdot \frac{1}{x\sqrt{2 \pi \sigma^2} } \cdot \exp \left[ -\frac{1}{2}  \frac{\left(\ln x-\mu\right)^2}{\sigma^2} \right]  \mathrm{d}x \\
&= \frac{1}{\sqrt{2 \pi \sigma^2} } \int_{0}^{+\infty} x \cdot \exp \left[ -\frac{1}{2}  \frac{\left(\ln x-\mu\right)^2}{\sigma^2} \right]\mathrm{d}x
\end{split}
$$

Substituting $z = \frac{\ln x -\mu}{\sigma}$, i.e. $x = \exp \left( \mu + \sigma z \right )$, we have:

$$ \label{eq:second-moment-s2}
\begin{split}
\mathrm{E} [X^2] = \frac{1}{\sqrt{2 \pi \sigma^2} } \int_{(-\infty -\mu )/ (\sigma)}^{(\ln x -\mu )/ (\sigma)} \exp \left( \mu +\sigma z \right) \exp \left( -\frac{1}{2}  z^2 \right) \mathrm{d} \left[ \exp \left( \mu +\sigma z \right) \right] \\
&= \frac{1}{\sqrt{2 \pi \sigma^2} } \int_{-\infty}^{+\infty} \exp \left( -\frac{1}{2}  z^2 \right) \sigma \exp \left( 2\mu + 2 \sigma z \right) \mathrm{d}z \\
&= \frac{1}{\sqrt{2 \pi} } \int_{-\infty}^{+\infty} \exp \left[ -\frac{1}{2} \left(   z^2 - 4 \sigma z - 4 \mu  \right) \right] \mathrm{d}z \\
\end{split}
$$

Now multiplying by $\exp \left( 2 \sigma^2 \right)$ and $\exp \left(- 2 \sigma^2 \right)$, this becomes:

$$ \label{eq:second-moment-s3}
\begin{split}
\mathrm{E} [X^2] = \frac{1}{\sqrt{2 \pi} } \int_{-\infty}^{+\infty} \exp \left[ -\frac{1}{2} \left(   z^2 - 4 \sigma z + 4 \sigma^2 -4 \sigma^2 - 4 \mu  \right) \right] \mathrm{d}z \\
&= \frac{1}{\sqrt{2 \pi} } \int_{-\infty}^{+\infty} \exp \left[ -\frac{1}{2} \left( z^2 - 4\sigma z + 4\sigma^2 \right) \right] \exp \left( 2 \sigma^2 +2 \mu  \right) \mathrm{d}z \\
&= \exp \left( 2 \sigma^2 +2 \mu   \right) \int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi} } \exp \left[ -\frac{1}{2} \left( z - 2 \sigma \right)^2 \right] \mathrm{d}z \\
\end{split}
$$

The [probability density function of a normal distribution](/P/norm-pdf) is 

$$ 
f_X(x) = \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right]
$$

with $\mu = 2 \sigma$ and unit variance this reads:

$$ 
= \frac{1}{\sqrt{2 \pi}} \cdot \exp \left[ -\frac{1}{2} \left({x - 2 \sigma} \right)^2 \right]
$$

Using the definition of the [probability density function](/D/pdf) 

$$
\int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi}} \cdot \exp \left[ -\frac{1}{2} \left({x - 2 \sigma} \right)^2 \right]  \mathrm{d}x  = 1 
$$

and applying \eqref{eq:def-pdf} to \eqref{second-moment-s3}, we have:

$$ \label{eq:second-moment-4}
\mathrm{E}[X]^2 = \exp \left( 2 \sigma^2 +2 \mu   \right) \; .
$$

Applying \eqref{eq:second-moment-4} and \eqref{eq:lognorm-mean-ref} to \eqref{eq:var2}, we have:

$$ \label{eq:lognorm-var-2}
\begin{split}
\mathrm{Var}(X) = \mathrm{E}\left[ X^2 \right] - \mathrm{E}\left[ X \right]^2  \\
&= \exp \left(2\sigma^2 + 2\mu \right) - \left[ \exp \left(\mu + \frac{1}{2} \sigma^2 \right) \right]^2 \\
&= \exp \left(2\sigma^2 + 2\mu \right) - \exp \left(2\mu + \sigma^2\right) \; .
\end{split}
$$