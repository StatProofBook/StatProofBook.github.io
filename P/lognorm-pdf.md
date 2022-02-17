---
layout: proof
mathjax: true

author: "Maja Pavlovic"
affiliation: ""
e_mail: "mpavlovic@uw.co.uk"
date: 2022-02-13 10:05:00

title: "Probability density function of the log-normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Log-normal distribution"
theorem: "Probability density function"

sources:
  - authors: "Taboga, Marco"
    year: 2021
    title: "Log-normal distribution"
    in: "Lectures on probability and statistics"
    pages: "retrieved on 2022-02-13"
    url: "https://www.statlect.com/probability-distributions/log-normal-distribution"

proof_id: "P310"
shortcut: "lognorm-pdf"
username: "majapavlo"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [log-normal distribution](/D/lognorm):

$$ \label{eq:lognorm}
X \sim \ln \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [probability density function](/D/pdf) of $X$ is given by:

$$ \label{eq:lognorm-pdf}
f_X(x) = \frac{1}{x \sigma \sqrt{2 \pi}} \cdot \mathrm{exp} \left[ -\frac{\left( \ln x -\mu \right)^2}{2 \sigma^2} \right] \; .
$$

**Proof:** A [log-normally distributed random variable](/D/lognorm) is defined as the exponential function of a [normal random variable](/D/norm):

$$ \label{eq:lognorm-def}
Y \sim \mathcal{N}(\mu,\sigma^2) \;  \quad \Rightarrow \quad X = \mathrm{exp} (Y) \sim \ln \mathcal{N}(\mu, \sigma^2) \; .
$$

The [probability density function of the normal distribution](/P/norm-pdf) is

$$ \label{eq:norm-pdf}
f_X(x) = \frac{1}{\sigma \sqrt{2 \pi}} \cdot \mathrm{exp} \left[ -\frac{\left( x -\mu \right)^2}{2 \sigma^2} \right] \; .
$$

Writing $X$ as a function of $Y$ we have

$$ \label{eq:X-Y}
X = g(Y) = \mathrm{exp} (Y) \;
$$

with the inverse function

$$ \label{eq:Y-X}
Y = g^{-1}(X) = \ln (X) \; .
$$

Because the derivative of $\exp (Y)$ is always positive, $g(Y)$ is strictly increasing and we can calculate the [probability density function of a strictly increasing function](/P/pdf-sifct) as

$$ \label{eq:pdf-sifct}
f_X(x) = \left\{
\begin{array}{rl}
f_Y(g^{-1}(x)) \, \frac{\mathrm{d}g^{-1}(x)}{\mathrm{d}x} \; , & \text{if} \; x \in \mathcal{X} \\
0 \; , & \text{if} \; x \notin \mathcal{X}
\end{array}
\right.
$$

where $\mathcal{X} = \left\lbrace x = g(y): y \in \mathcal{Y} \right\rbrace$. With the [probability density function of the normal distribution](/P/norm-pdf), we have

$$ \label{eq:pdf-X}
\begin{split}
f_X(x) &= f_Y(g^{-1}(x))\cdot \frac{dg^{-1}(x)}{dx}} \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{g^{-1}(x)-\mu}{\sigma} \right)^2 \right] \cdot \frac{\mathrm{d}g^{-1}(x)}{\mathrm{d}x} \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{(\ln x)-\mu}{\sigma} \right)^2 \right] \cdot \frac{\mathrm{d}(\ln x)}{\mathrm{d}x} \\
&= \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{ \ln x -\mu}{\sigma} \right)^2 \right] \cdot \frac{1}{x} \\
&= \frac{1}{x \sigma \sqrt{2 \pi}} \cdot \exp \left[ - \frac{\left( \ln x -\mu\right)^2}{2 \sigma^2} \right]
\end{split}
$$

which is the [probability density function](/D/pdf) of the [log-normal distribution](/D/lognorm).
