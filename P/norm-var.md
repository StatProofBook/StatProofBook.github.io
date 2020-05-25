---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-09 22:47:00

title: "Variance of the normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Variance"

sources:
  - authors: "Papadopoulos, Alecos"
    year: 2013
    title: "How to derive the mean and variance of Gaussian random variable?"
    in: "StackExchange Mathematics"
    pages: "retrieved on 2020-01-09"
    url: "https://math.stackexchange.com/questions/518281/how-to-derive-the-mean-and-variance-of-a-gaussian-random-variable"

proof_id: "P18"
shortcut: "norm-var"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [normal distribution](/D/norm):

$$ \label{eq:norm}
X \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [variance](/D/var) of $X$ is

$$ \label{eq:norm-var}
\mathrm{Var}(X) = \sigma^2 \; .
$$


**Proof:** The [variance](/D/var) is the probability-weighted average of the squared deviation from the [mean](/D/mean):

$$ \label{eq:var}
\mathrm{Var}(X) = \int_{\mathbb{R}} (x - \mathrm{E}(X))^2 \cdot f_\mathrm{X}(x) \, \mathrm{d}x \; .
$$

With the [expected value](/P/norm-mean) and [probability density function](/P/norm-pdf) of the normal distribution, this reads:

$$ \label{eq:norm-var-s1}
\begin{split}
\mathrm{Var}(X) &= \int_{-\infty}^{+\infty} (x - \mu)^2 \cdot \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \, \mathrm{d}x \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \int_{-\infty}^{+\infty} (x - \mu)^2 \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \, \mathrm{d}x \; .
\end{split}
$$

Substituting $z = x -\mu$, we have:

$$ \label{eq:norm-var-s2}
\begin{split}
\mathrm{Var}(X) &= \frac{1}{\sqrt{2 \pi} \sigma} \int_{-\infty-\mu}^{+\infty-\mu} z^2 \cdot \exp \left[ -\frac{1}{2} \left( \frac{z}{\sigma} \right)^2 \right] \, \mathrm{d}(z + \mu) \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \int_{-\infty}^{+\infty} z^2 \cdot \exp \left[ -\frac{1}{2} \left( \frac{z}{\sigma} \right)^2 \right] \, \mathrm{d}z \; .
\end{split}
$$

Now substituting $z = \sqrt{2} \sigma x$, we have:

$$ \label{eq:norm-var-s3}
\begin{split}
\mathrm{Var}(X) &= \frac{1}{\sqrt{2 \pi} \sigma} \int_{-\infty}^{+\infty} (\sqrt{2} \sigma x)^2 \cdot \exp \left[ -\frac{1}{2} \left( \frac{\sqrt{2} \sigma x}{\sigma} \right)^2 \right] \, \mathrm{d}(\sqrt{2} \sigma x) \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \cdot 2 \sigma^2 \cdot \sqrt{2} \sigma \int_{-\infty}^{+\infty} x^2 \cdot \exp \left[ -x^2 \right] \, \mathrm{d}x \\
&= \frac{2 \sigma^2}{\sqrt{\pi}} \int_{-\infty}^{+\infty} x^2 \cdot e^{-x^2} \, \mathrm{d}x \; .
\end{split}
$$

Since the integrand is symmetric with respect to $x = 0$, we can write:

$$ \label{eq:norm-var-s4}
\mathrm{Var}(X) = \frac{4 \sigma^2}{\sqrt{\pi}} \int_{0}^{\infty} x^2 \cdot e^{-x^2} \, \mathrm{d}x \; .
$$

If we define $z = x^2$, then $x = \sqrt{z}$ and $\mathrm{d}x = 1/2 \, z^{-1/2} \, \mathrm{d}z$. Substituting this into the integral

$$ \label{eq:norm-var-s5}
\mathrm{Var}(X) = \frac{4 \sigma^2}{\sqrt{\pi}} \int_{0}^{\infty} z \cdot e^{-z} \cdot \frac{1}{2} z^{-\frac{1}{2}} \, \mathrm{d}z = \frac{2 \sigma^2}{\sqrt{\pi}} \int_{0}^{\infty} z^{\frac{3}{2}-1} \cdot e^{-z} \, \mathrm{d}z
$$

and using the definition of the gamma function

$$ \label{eq:gam-fct}
\Gamma(x) = \int_{0}^{\infty} z^{x-1} \cdot e^{-z} \, \mathrm{d}z \; ,
$$

we can finally show that

$$ \label{eq:norm-var-s6}
\mathrm{Var}(X) = \frac{2 \sigma^2}{\sqrt{\pi}} \cdot \Gamma\!\left(\frac{3}{2}\right) = \frac{2 \sigma^2}{\sqrt{\pi}} \cdot \frac{\sqrt{\pi}}{2} = \sigma^2 \; .
$$
