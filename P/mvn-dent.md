---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-14 19:49:00

title: "Differential entropy of the multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Differential entropy"

sources:
  - authors: "Kiuhnm"
    year: 2018
    title: "Entropy of the multivariate Gaussian"
    in: "StackExchange Mathematics"
    pages: "retrieved on 2020-05-14"
    url: "https://math.stackexchange.com/questions/2029707/entropy-of-the-multivariate-gaussian"

proof_id: "P100"
shortcut: "mvn-dent"
username: "JoramSoch"
---


**Theorem:** Let $x$ follow a [multivariate normal distribution](/D/mvn)

$$ \label{eq:mvn}
x \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, the [differential entropy](/D/dent) of $x$ in nats is

$$ \label{eq:mvn-dent}
\mathrm{h}(x) = \frac{n}{2} \ln(2\pi) + \frac{1}{2} \ln|\Sigma| + \frac{1}{2} n \; .
$$


**Proof:** The [differential entropy](/D/dent) of a random variable is defined as

$$ \label{eq:dent}
\mathrm{h}(X) = - \int_{\mathcal{X}} p(x) \, \log_b p(x) \, \mathrm{d}x \; .
$$

To measure $h(X)$ in nats, we set $b = e$, [such that](/D/mean)

$$ \label{eq:dent-nats}
\mathrm{h}(X) = - \mathrm{E}\left[ \ln p(x) \right] \; .
$$

With the [probability density function of the multivariate normal distribution](/P/mvn-pdf), the differential entropy of $x$ is:

$$ \label{eq:mvn-dent-s1}
\begin{split}
\mathrm{h}(x) &= - \mathrm{E}\left[ \ln \left( \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] \right) \right] \\
&= - \mathrm{E}\left[ - \frac{n}{2} \ln(2\pi) - \frac{1}{2} \ln|\Sigma| - \frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] \\
&= \frac{n}{2} \ln(2\pi) + \frac{1}{2} \ln|\Sigma| + \frac{1}{2} \, \mathrm{E}\left[ (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] \; .
\end{split}
$$

The last term can be evaluted as

$$ \label{eq:mvn-dent-t3}
\begin{split}
\mathrm{E}\left[ (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] &= \mathrm{E}\left[ \mathrm{tr}\left( (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right) \right] \\
&= \mathrm{E}\left[ \mathrm{tr}\left( \Sigma^{-1} (x-\mu) (x-\mu)^\mathrm{T} \right) \right] \\
&= \mathrm{tr}\left( \Sigma^{-1} \mathrm{E}\left[ (x-\mu) (x-\mu)^\mathrm{T} \right] \right) \\
&= \mathrm{tr}\left( \Sigma^{-1} \Sigma \right) \\
&= \mathrm{tr}\left( I_n \right) \\
&= n \; , \\
\end{split}
$$

such that the differential entropy is

$$ \label{eq:mvn-dent-qed}
\mathrm{h}(x) = \frac{n}{2} \ln(2\pi) + \frac{1}{2} \ln|\Sigma| + \frac{1}{2} \, n \; .
$$
