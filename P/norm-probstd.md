---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-05-08 18:56:00

title: "Probability of normal random variable being within standard deviations from its mean"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Probability of being within standard deviations from mean"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "68-95-99.7 rule"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-05.08"
    url: "https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule"

proof_id: "P321"
shortcut: "norm-probstd"
username: "JoramSoch"
---


**Theorem:** (also called "68-95-99.7 rule") Let $X$ be a [random variable](/D/rvar) following a [normal distribution](/D/norm) with [mean](/D/mean) $\mu$ and [variance](/D/var) $\sigma^2$. Then, about $68\%$, $95\%$ and $99.7\%$ of the values of $X$ will fall within 1, 2 and 3 [standard deviations](/D/std) from the [mean](/D/mean), respectively:

$$ \label{eq:norm-probstd}
\begin{split}
\mathrm{Pr}(\mu-1\sigma \leq X \leq \mu+1\sigma) &\approx 68 \% \\
\mathrm{Pr}(\mu-2\sigma \leq X \leq \mu+2\sigma) &\approx 95 \% \\
\mathrm{Pr}(\mu-3\sigma \leq X \leq \mu+3\sigma) &\approx 99.7 \% \; .
\end{split}
$$


**Proof:** The [cumulative distribution function of a normally distributed](/P/norm-cdf) random variable $X$ is

$$ \label{eq:norm-cdf}
F_X(x) = \frac{1}{2} \left[ 1 + \mathrm{erf}\left( \frac{x-\mu}{\sqrt{2} \sigma} \right) \right]
$$

where $\mathrm{erf}(x)$ is the error function defined as

$$ \label{eq:erf}
\mathrm{erf}(x) = \frac{2}{\sqrt{\pi}} \int_{0}^{x} \exp(-t^2) \, \mathrm{d}t
$$

which exhibits a point-symmetry property:

$$ \label{eq:erf-symm}
\mathrm{erf}(-x) = -\mathrm{erf}(x) \; .
$$

Thus, the probability that $X$ falls between $\mu - a \cdot \sigma$ and $\mu + a \cdot \sigma$ is equal to:

$$ \label{eq:prob-std}
\begin{split}
p(a) &= \mathrm{Pr}(\mu-a\sigma \leq X \leq \mu+a\sigma) \\
&= F_X(\mu+a\sigma) - F_X(\mu-a\sigma) \\
&\overset{\eqref{eq:norm-cdf}}{=} \frac{1}{2} \left[ 1 + \mathrm{erf}\left( \frac{\mu+a\sigma-\mu}{\sqrt{2} \sigma} \right) \right] - \frac{1}{2} \left[ 1 + \mathrm{erf}\left( \frac{\mu-a\sigma-\mu}{\sqrt{2} \sigma} \right) \right] \\
&= \frac{1}{2} \left[ \mathrm{erf}\left( \frac{\mu+a\sigma-\mu}{\sqrt{2} \sigma} \right) - \mathrm{erf}\left( \frac{\mu-a\sigma-\mu}{\sqrt{2} \sigma} \right) \right] \\
&= \frac{1}{2} \left[ \mathrm{erf}\left( \frac{a}{\sqrt{2}} \right) - \mathrm{erf}\left( -\frac{a}{\sqrt{2}} \right) \right] \\
&\overset{\eqref{eq:erf-symm}}{=} \frac{1}{2} \left[ \mathrm{erf}\left( \frac{a}{\sqrt{2}} \right) + \mathrm{erf}\left( \frac{a}{\sqrt{2}} \right) \right] \\
&= \mathrm{erf}\left( \frac{a}{\sqrt{2}} \right) \\
\end{split}
$$

With that, we can use numerical implementations of the error function to calculate:

$$ \label{eq:norm-probstd-qed}
\begin{split}
\mathrm{Pr}(\mu-1\sigma \leq X \leq \mu+1\sigma) &= p(1) = 68.27 \% \\
\mathrm{Pr}(\mu-2\sigma \leq X \leq \mu+2\sigma) &= p(2) = 95.45 \% \\
\mathrm{Pr}(\mu-3\sigma \leq X \leq \mu+3\sigma) &= p(3) = 99.73 \% \; .
\end{split}
$$