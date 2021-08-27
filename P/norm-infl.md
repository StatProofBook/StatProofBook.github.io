---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-26 12:26:00

title: "Inflection points of the probability density function of the normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Inflection points"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-08-25"
    url: "https://en.wikipedia.org/wiki/Normal_distribution#Symmetries_and_derivatives"

proof_id: "P252"
shortcut: "norm-infl"
username: "JoramSoch"
---


**Theorem:** The [probability density function](/D/pdf) of the [normal distribution](/D/norm) with mean $\mu$ and variance $\sigma^2$ has two inflection points at $x = \mu - \sigma$ and $x = \mu + \sigma$, i.e. exactly one [standard deviation](/D/std) away from the [expected value](/D/mean).


**Proof:** The [probability density function of the normal distribution](/P/norm-pdf) is:

$$ \label{eq:norm-pdf}
f_X(x) = \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \; .
$$

The first three deriatives of this function are:

$$ \label{eq:norm-pdf-der1}
f'_X(x) = \frac{\mathrm{d}f_X(x)}{\mathrm{d}x} = \frac{1}{\sqrt{2 \pi} \sigma} \cdot \left( - \frac{x - \mu}{\sigma^2} \right) \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right]
$$

$$ \label{eq:norm-pdf-der2}
\begin{split}
f''_X(x) = \frac{\mathrm{d}^2f_X(x)}{\mathrm{d}x^2} &= \frac{1}{\sqrt{2 \pi} \sigma} \cdot \left( - \frac{1}{\sigma^2} \right) \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] + \frac{1}{\sqrt{2 \pi} \sigma} \cdot \left( \frac{x-\mu}{\sigma^2} \right)^2 \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \cdot \left[ \left( \frac{x-\mu}{\sigma^2} \right)^2 - \frac{1}{\sigma^2} \right] \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right]
\end{split}
$$

$$ \label{eq:norm-pdf-der3}
\begin{split}
f'''_X(x) = \frac{\mathrm{d}^3f_X(x)}{\mathrm{d}x^3} &= \frac{1}{\sqrt{2 \pi} \sigma} \cdot \left[ \frac{2}{\sigma^2} \left( \frac{x-\mu}{\sigma^2} \right) \right] \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] - \frac{1}{\sqrt{2 \pi} \sigma} \cdot \left[ \left( \frac{x-\mu}{\sigma^2} \right)^2 - \frac{1}{\sigma^2} \right] \cdot \left( \frac{x - \mu}{\sigma^2}  \right) \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \cdot \left[ -\left( \frac{x - \mu}{\sigma^2} \right)^3 + 3 \left( \frac{x - \mu}{\sigma^4} \right) \right] \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \; .
\end{split}
$$

The second derivative is zero, if and only if

$$ \label{eq:norm-pdf-der2-zero}
\begin{split}
0 &= \left[ \left( \frac{x-\mu}{\sigma^2} \right)^2 - \frac{1}{\sigma^2} \right] \\
0 &= \frac{x^2}{\sigma^4} - \frac{2 \mu x}{\sigma^4} + \frac{\mu^2}{\sigma^4} - \frac{1}{\sigma^2} \\
0 &= x^2 - 2 \mu x + (\mu^2 - \sigma^2) \\
x_{1/2} &= -\frac{-2 \mu}{2} \pm \sqrt{ \left(\frac{-2 \mu}{2}\right)^2 - (\mu^2 - \sigma^2)} \\
x_{1/2} &= \mu \pm \sqrt{ \mu^2 - \mu^2 + \sigma^2} \\
x_{1/2} &= \mu \pm \sigma \; .
\end{split}
$$

Since the third derivative is non-zero at this value

$$ \label{eq:norm-pdf-der3-infl}
\begin{split}
f'''_X(\mu \pm \sigma) &= \frac{1}{\sqrt{2 \pi} \sigma} \cdot \left[ -\left( \frac{\pm \sigma}{\sigma^2} \right)^3 + 3 \left( \frac{\pm \sigma}{\sigma^4} \right) \right] \cdot \exp \left[ -\frac{1}{2} \left( \frac{\pm \sigma}{\sigma} \right)^2 \right] \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \cdot \left( \pm \frac{2}{\sigma^3} \right) \cdot \exp \left( - \frac{1}{2} \right) \neq 0 \; ,
\end{split}
$$

there are inflection points at $x_{1/2} = \mu \pm \sigma$. Because $\mu$ is the mean and $\sigma^2$ is the variance of a [normal distribution](/D/norm), these points are exactly one [standard deviation](/D/std) away from the mean.
