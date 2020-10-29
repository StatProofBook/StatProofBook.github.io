---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-20 04:26:00

title: "Expression of the cumulative distribution function of the normal distribution without the error function"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Cumulative distribution function without error function"

sources:
  - authors: "Soch J"
    year: 2015
    title: "Solution for the Indefinite Integral of the Standard Normal Probability Density Function"
    in: "arXiv stat.OT"
    pages: "arXiv:1512.04858"
    url: "https://arxiv.org/abs/1512.04858"
  - authors: "Wikipedia"
    year: 2020
    title: "Normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-03-20"
    url: "https://en.wikipedia.org/wiki/Normal_distribution#Cumulative_distribution_function"

proof_id: "P86"
shortcut: "norm-cdfwerf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [normal distribution](/D/norm):

$$ \label{eq:norm}
X \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [cumulative distribution function](/D/cdf) of $X$ can be expressed as

$$ \label{eq:norm-cdf}
f_X(x) = \Phi_{\mu,\sigma}(x) = \varphi\left( \frac{x-\mu}{\sigma} \right) \cdot \sum_{i=1}^{\infty} \frac{\left( \frac{x-\mu}{\sigma} \right)^{2i-1}}{(2i-1)!!} + \frac{1}{2}
$$

where $\varphi(x)$ is the [probability density function](/D/pdf) of the [standard normal distribution](/D/snorm) and $n!!$ is a double factorial.


**Proof:**

1) First, consider the [standard normal distribution](/D/snorm) $\mathcal{N}(0, 1)$ which [has the probability density function](/P/norm-pdf)

$$ \label{eq:snorm-pdf}
\varphi(x) = \frac{1}{\sqrt{2 \pi}} \cdot e^{-\frac{1}{2} x^2} \; .
$$

Let $T(x)$ be the indefinite integral of this function. It can be obtained using infinitely repeated integration by parts as follows:

$$ \label{eq:snorm-pdf-ii-s1}
\begin{split}
T(x) &= \int \varphi(x) \, \mathrm{d}x \\
&= \int \frac{1}{\sqrt{2 \pi}} \cdot e^{-\frac{1}{2} x^2} \, \mathrm{d}x \\
&= \frac{1}{\sqrt{2 \pi}} \int 1 \cdot e^{-\frac{1}{2} x^2} \, \mathrm{d}x \\
&= \frac{1}{\sqrt{2 \pi}} \cdot \left[ x \cdot e^{-\frac{1}{2} x^2} + \int x^2 \cdot e^{-\frac{1}{2} x^2} \, \mathrm{d}x \right] \\
&= \frac{1}{\sqrt{2 \pi}} \cdot \left[ x \cdot e^{-\frac{1}{2} x^2} + \left[ \frac{1}{3} x^3 \cdot e^{-\frac{1}{2} x^2} + \int \frac{1}{3} x^4 \cdot e^{-\frac{1}{2} x^2} \, \mathrm{d}x \right] \right] \\
&= \frac{1}{\sqrt{2 \pi}} \cdot \left[ x \cdot e^{-\frac{1}{2} x^2} + \left[ \frac{1}{3} x^3 \cdot e^{-\frac{1}{2} x^2} + \left[ \frac{1}{15} x^5 \cdot e^{-\frac{1}{2} x^2} + \int \frac{1}{15} x^6 \cdot e^{-\frac{1}{2} x^2} \, \mathrm{d}x \right] \right] \right] \\
&= \ldots \\
&= \frac{1}{\sqrt{2 \pi}} \cdot \left[ \sum_{i=1}^{n} \left( \frac{x^{2i-1}}{(2i-1)!!} \cdot e^{-\frac{1}{2} x^2} \right) + \int \left( \frac{x^{2n}}{(2n-1)!!} \cdot e^{-\frac{1}{2} x^2} \right) \, \mathrm{d}x \right] \\
&= \frac{1}{\sqrt{2 \pi}} \cdot \left[ \sum_{i=1}^{\infty} \left( \frac{x^{2i-1}}{(2i-1)!!} \cdot e^{-\frac{1}{2} x^2} \right) + \lim_{n \to \infty} \int \left( \frac{x^{2n}}{(2n-1)!!} \cdot e^{-\frac{1}{2} x^2} \right) \, \mathrm{d}x \right] \; .
\end{split}
$$

Since $(2n-1)!!$ grows faster than $x^{2n}$, it holds that

$$ \label{eq:int-const}
\frac{1}{\sqrt{2 \pi}} \cdot \lim_{n \to \infty} \int \left( \frac{x^{2n}}{(2n-1)!!} \cdot e^{-\frac{1}{2} x^2} \right) \, \mathrm{d}x = \int 0 \, \mathrm{d}x = c
$$

for constant $c$, such that the indefinite integral becomes

$$ \label{eq:snorm-pdf-ii-s2}
\begin{split}
T(x) &= \frac{1}{\sqrt{2 \pi}} \cdot \sum_{i=1}^{\infty} \left( \frac{x^{2i-1}}{(2i-1)!!} \cdot e^{-\frac{1}{2} x^2} \right) + c \\
&= \frac{1}{\sqrt{2 \pi}} \cdot e^{-\frac{1}{2} x^2} \cdot \sum_{i=1}^{\infty} \frac{x^{2i-1}}{(2i-1)!!} + c \\
&\overset{\eqref{eq:snorm-pdf}}{=} \varphi(x) \cdot \sum_{i=1}^{\infty} \frac{x^{2i-1}}{(2i-1)!!} + c \; .
\end{split}
$$

2) Next, let $\Phi(x)$ be the [cumulative distribution function](/D/cdf) of the [standard normal distribution](/D/snorm):

$$ \label{eq:snorm-cdf}
\Phi(x) = \int_{-\infty}^x \varphi(x) \, \mathrm{d}x \; .
$$

It can be obtained by matching $T(0)$ to $\Phi(0)$ which is $1/2$, because the standard normal distribution is symmetric around zero:

$$ \label{eq:snorm-cdf-c}
\begin{split}
T(0) = \varphi(0) \cdot \sum_{i=1}^{\infty} \frac{0^{2i-1}}{(2i-1)!!} + c &= \frac{1}{2} = \Phi(0) \\
\Leftrightarrow c &= \frac{1}{2} \\
\Rightarrow \Phi(x) = \varphi(x) \cdot \sum_{i=1}^{\infty} \frac{x^{2i-1}}{(2i-1)!!} + \frac{1}{2} \! &\; .
\end{split}
$$

3) Finally, the [cumulative distribution functions](/D/cdf) of the [standard normal distribution](/D/snorm) and the general [normal distribution](/D/norm) [are related to each other](/P/norm-snorm) as

$$ \label{eq:norm-snorm-cdf}
\Phi_{\mu,\sigma}(x) = \Phi\left( \frac{x-\mu}{\sigma} \right) \; .
$$

Combining \eqref{eq:norm-snorm-cdf} with \eqref{eq:snorm-cdf-c}, we have:

$$ \label{eq:norm-cdf-qed}
\Phi_{\mu,\sigma}(x) = \varphi\left( \frac{x-\mu}{\sigma} \right) \cdot \sum_{i=1}^{\infty} \frac{\left( \frac{x-\mu}{\sigma} \right)^{2i-1}}{(2i-1)!!} + \frac{1}{2} \; .
$$