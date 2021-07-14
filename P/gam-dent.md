---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-07-14 07:37:00

title: "Differential entropy of the gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Differential entropy"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Gamma distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-07-14"
    url: "https://en.wikipedia.org/wiki/Gamma_distribution#Information_entropy"

proof_id: "P239"
shortcut: "gam-dent"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [gamma distribution](/D/gam):

$$ \label{eq:gam}
X \sim \mathrm{Gam}(a, b)
$$

Then, the [differential entropy](/D/dent) of $X$ in nats is

$$ \label{eq:gam-dent}
\mathrm{h}(X) = a + \ln \Gamma(a) + (1-a) \cdot \psi(a) + \ln b \; .
$$


**Proof:** The [differential entropy](/D/dent) of a random variable is defined as

$$ \label{eq:dent}
\mathrm{h}(X) = - \int_{\mathcal{X}} p(x) \, \log_b p(x) \, \mathrm{d}x \; .
$$

To measure $h(X)$ in nats, we set $b = e$, [such that](/D/mean)

$$ \label{eq:dent-nats}
\mathrm{h}(X) = - \mathrm{E}\left[ \ln p(x) \right] \; .
$$

With the [probability density function of the gamma distribution](/P/gam-pdf), the differential entropy of $X$ is:

$$ \label{eq:gam-dent-s1}
\begin{split}
\mathrm{h}(X) &= - \mathrm{E}\left[ \ln \left( \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \right) \right] \\
&= - \mathrm{E}\left[ a \cdot \ln b - \ln \Gamma(a) + (a-1) \ln x - b x \right] \\
&= - a \cdot \ln b + \ln \Gamma(a) - (a-1) \cdot \mathrm{E}(\ln x) + b \cdot \mathrm{E}(x) \; .
\end{split}
$$

Using the [mean](/P/gam-mean) and [logarithmic expectation](/P/gam-logmean) of the [gamma distribution](/D/gam)

$$ \label{eq:gam-mean-logmean}
X \sim \mathrm{Gam}(a, b) \quad \Rightarrow \quad \mathrm{E}(X) = \frac{a}{b} \quad \text{and} \quad \mathrm{E}(\ln X) = \psi(a) - \ln(b) \; ,
$$

the [differential entropy](/D/dent) of $X$ becomes:

$$ \label{eq:gam-dent-s2}
\begin{split}
\mathrm{h}(X) &= - a \cdot \ln b + \ln \Gamma(a) - (a-1) \cdot (\psi(a) - \ln b) + b \cdot \frac{a}{b} \\
&= - a \cdot \ln b + \ln \Gamma(a) + (1-a) \cdot \psi(a) + a \cdot \ln b - \ln b + a \\
&= a + \ln \Gamma(a) + (1-a) \cdot \psi(a) - \ln b \; .
\end{split}
$$