---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-14 20:09:00

title: "Differential entropy of the normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Differential entropy"

sources:
  - authors: "Wang, Peng-Hua"
    year: 2012
    title: "Differential Entropy"
    in: "National Taipei University"
    url: "https://web.ntpu.edu.tw/~phwang/teaching/2012s/IT/slides/chap08.pdf"

proof_id: "P101"
shortcut: "norm-dent"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [normal distribution](/D/norm):

$$ \label{eq:norm}
X \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [differential entropy](/D/dent) of $X$ is

$$ \label{eq:norm-dent}
\mathrm{h}(X) = \frac{1}{2} \ln\left( 2 \pi \sigma^2 e \right) \; .
$$

**Proof:** The [differential entropy](/D/dent) of a random variable is defined as

$$ \label{eq:dent}
\mathrm{h}(X) = - \int_{\mathcal{X}} p(x) \, \log_b p(x) \, \mathrm{d}x \; .
$$

To measure $h(X)$ in nats, we set $b = e$, [such that](/D/mean)

$$ \label{eq:dent-nats}
\mathrm{h}(X) = - \mathrm{E}\left[ \ln p(x) \right] \; .
$$

With the [probability density function of the normal distribution](/P/norm-pdf), the differential entropy of $X$ is:

$$ \label{eq:norm-dent-qed}
\begin{split}
\mathrm{h}(X) &= - \mathrm{E}\left[ \ln \left( \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \right) \right] \\
&= - \mathrm{E}\left[ - \frac{1}{2} \ln(2\pi\sigma^2) - \frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \\
&= \frac{1}{2} \ln(2 \pi \sigma^2) + \frac{1}{2} \, \mathrm{E}\left[ \left( \frac{x-\mu}{\sigma} \right)^2 \right] \\
&= \frac{1}{2} \ln(2 \pi \sigma^2) + \frac{1}{2} \cdot \frac{1}{\sigma^2} \cdot \mathrm{E}\left[ (x-\mu)^2 \right] \\
&= \frac{1}{2} \ln(2 \pi \sigma^2) + \frac{1}{2} \cdot \frac{1}{\sigma^2} \cdot \sigma^2 \\
&= \frac{1}{2} \ln(2 \pi \sigma^2) + \frac{1}{2} \\
&= \frac{1}{2} \ln(2 \pi \sigma^2 e) \; .
\end{split}
$$