---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-02-16 15:03:20

title: "Moment-generating function of the multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Moment-generating function"

sources:

proof_id: "P436"
shortcut: "mvn-mgf"
username: "JoramSoch"
---


**Theorem:** Let $x$ follow a [multivariate normal distribution](/D/mvn):

$$ \label{eq:mvn}
x \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, the [moment-generating function](/D/mgf) of $x$ is

$$ \label{eq:mvn-mgf}
M_x(t) = \exp \left[ t^\mathrm{T} \mu + \frac{1}{2} t^\mathrm{T} \Sigma t \right] \; .
$$


**Proof:** The [moment-generating function of a random vector](/D/mgf) $X$ is defined as:

$$ \label{eq:mgf}
M_X(t) = \mathrm{E} \left[ e^{t^\mathrm{T}X} \right], \quad t \in \mathbb{R}^n \; .
$$

Applying the [law of the unconscious statistician](/P/mean-lotus), we have:

$$ \label{eq:mvn-mgf-s1}
M_x(t) = \int_{\mathcal{X}} e^{t^\mathrm{T}x} \cdot f_X(x) \, \mathrm{d}x \; .
$$

With the [probability density function of the multivariate normal distribution](/P/mvn-pdf), we have:

$$ \label{eq:mvn-mgf-s2}
M_x(t) = \int_{\mathbb{R}^n} \exp \left[ t^\mathrm{T}x \right] \cdot \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] \, \mathrm{d}x \; .
$$

Now we summarize the two exponential functions inside the integral:

$$ \label{eq:mvn-mgf-s3}
\begin{split}
M_x(t) &= \int_{\mathbb{R}^n} \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) + t^\mathrm{T}x \right] \, \mathrm{d}x \\
&= \int_{\mathbb{R}^n} \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} \left( x^\mathrm{T} \Sigma^{-1} x - 2 \mu^\mathrm{T} \Sigma^{-1} x + \mu^\mathrm{T} \Sigma^{-1} \mu - 2 t^\mathrm{T}x \right) \right] \, \mathrm{d}x \\
&= \int_{\mathbb{R}^n} \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} \left( x^\mathrm{T} \Sigma^{-1} x - 2 (\mu + \Sigma t)^\mathrm{T} \Sigma^{-1} x + \mu^\mathrm{T} \Sigma^{-1} \mu \right) \right] \, \mathrm{d}x \\
&= \int_{\mathbb{R}^n} \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} \left( (x - [\mu + \Sigma t])^\mathrm{T} \Sigma^{-1} (x - [\mu + \Sigma t]) - 2 t^\mathrm{T} \mu - t^\mathrm{T} \Sigma t \right) \right] \, \mathrm{d}x \\
&= \exp \left[ t^\mathrm{T} \mu + t^\mathrm{T} \Sigma t \right] \int_{\mathbb{R}^n} \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (x - [\mu + \Sigma t])^\mathrm{T} \Sigma^{-1} (x - [\mu + \Sigma t]) \right] \, \mathrm{d}x \; .
\end{split}
$$

The integrand is equal to the [probability density function of a multivariate normal distribution](/P/mvn-pdf):

$$ \label{eq:mvn-mgf-s4}
M_x(t) = \exp \left[ t^\mathrm{T} \mu + t^\mathrm{T} \Sigma t \right] \int_{\mathbb{R}^n} \mathcal{N}(x; \mu + \Sigma t, \Sigma) \, \mathrm{d}x \; .
$$

Because [the entire probability density integrates to one](/D/pdf), we finally have:

$$ \label{eq:mvn-mgf-s5}
M_x(t) = \exp \left[ t^\mathrm{T} \mu + t^\mathrm{T} \Sigma t \right] \; .
$$