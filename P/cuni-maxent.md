---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-08-25 11:20:00

title: "Continuous uniform distribution maximizes differential entropy for fixed range"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Continuous uniform distribution"
theorem: "Maximum entropy distribution"

sources:
  - authors: "Wikipedia"
    year: 2023
    title: "Maximum entropy probability distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2023-08-25"
    url: "https://en.wikipedia.org/wiki/Maximum_entropy_probability_distribution#Uniform_and_piecewise_uniform_distributions"

proof_id: "P412"
shortcut: "cuni-maxent"
username: "JoramSoch"
---


**Theorem:** The [continuous uniform distribution](/D/cuni) maximizes [differential entropy](/D/dent) for a [random variable](/D/rvar) with a fixed range.


**Proof:** Without loss of generality, let us assume that the random variable $X$ is in the following range: $a \leq X \leq b$.

Let $g(x)$ be the [probability density function](/D/pdf) of a [continuous uniform distribution](/D/cuni) with minimum $a$ and maximum $b$ and let $f(x)$ be an arbitrary [probability density function](/D/pdf) defined on the same support $\mathcal{X} = [a,b]$.

For a [random variable](/D/rvar) $X$ with set of possible values $\mathcal{X}$ and [probability density function](/D/pdf) $p(x)$, the [differential entropy](/D/dent) is defined as:

$$ \label{eq:dent}
\mathrm{h}(X) = - \int_{\mathcal{X}} p(x) \log p(x) \, \mathrm{d}x
$$

Consider the [Kullback-Leibler divergence](/D/kl) of distribution $f(x)$ from distribution $g(x)$ [which is non-negative](/P/kl-nonneg):

$$ \label{eq:kl-fg}
\begin{split}
0 \leq \mathrm{KL}[f||g] &= \int_{\mathcal{X}} f(x) \log \frac{f(x)}{g(x)} \, \mathrm{d}x \\
&= \int_{\mathcal{X}} f(x) \log f(x) \, \mathrm{d}x - \int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x \\
&\overset{\eqref{eq:dent}}{=} - \mathrm{h}[f(x)] - \int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x \; .
\end{split}
$$

By plugging the [probability density function of the continuous uniform distribution](/P/cuni-pdf) into the second term, we obtain:

$$ \label{eq:int-fg-s1}
\begin{split}
\int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x &= \int_{\mathcal{X}} f(x) \log \frac{1}{b-a} \, \mathrm{d}x \\
&= \log \frac{1}{b-a} \int_{\mathcal{X}} f(x) \, \mathrm{d}x \\
&= -\log(b-a) \; .
\end{split}
$$

This is actually the negative of the [differential entropy of the continuous uniform distribution](/P/cuni-dent), such that:

$$ \label{eq:int-fg-s2}
\int_{\mathcal{X}} f(x) \log g(x) \, \mathrm{d}x = -\mathrm{h}[\mathcal{U}(a,b)] = -\mathrm{h}[g(x)] \; .
$$

Combining \eqref{eq:kl-fg} with \eqref{eq:int-fg-s2}, we can show that

$$ \label{eq:cuni-maxent}
\begin{split}
0 &\leq \mathrm{KL}[f||g] \\
0 &\leq - \mathrm{h}[f(x)] - \left( -\mathrm{h}[g(x)] \right) \\
\mathrm{h}[g(x)] &\geq \mathrm{h}[f(x)]
\end{split}
$$

which means that the [differential entropy](/D/dent) of the [continuous uniform distribution](/D/cuni) $\mathcal{U}(a,b)$ will be larger than or equal to any other [distribution](/D/dist) defined in the same range.