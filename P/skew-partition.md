---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: "2023-04-20 12:00:00"

title: "Partition of skewness into expected values "
chapter: "General Theorems"
section: "Probability theory"
topic: "Skewness"
theorem: "Partition into expected values"

sources:
  - authors: "Wikipedia"
    year: 2023
    title: "Skewness"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2023-04-20"
    url: "https://en.wikipedia.org/wiki/Skewness"

proof_id: "P407"
shortcut: "skew-partition"
username: "tomfaulkenberry"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) with [expected value](/D/mean) $\mu$ and [standard deviation](/D/std) $\sigma$. Then, the [skewness](/D/skew) of $X$ can be computed as:

$$ \label{eq:skew-partition}
\mathrm{Skew}(X) = \frac{\mathrm{E}(X^3)-3\mu\sigma^2-\mu^3}{\sigma^3} \; .
$$

**Proof:** 

The [skewness](/D/skew) of $X$ is defined as 

$$ \label{eq:skew}
\mathrm{Skew}(X) = \frac{\mathrm{E}[(X-\mu)^3]}{\sigma^3} \; .
$$

Because [expected value is a linear operator](/P/mean-lin), we can rewrite \eqref{eq:skew} as

$$ \label{eq:partition}
\begin{split}
\mathrm{Skew}(X) &= \frac{\mathrm{E}[(X-\mu)^3]}{\sigma^3}\\
&= \frac{\mathrm{E}[X^3-3X^2\mu + 3X\mu^2 - \mu^3]}{\sigma^3}\\
&= \frac{\mathrm{E}(X^3) -3\mathrm{E}(X^2)\mu + 3\mathrm{E}(X)\mu^2 - \mu^3}{\sigma^3}\\
&= \frac{\mathrm{E}(X^3) -3\mu\left[\mathrm{E}(X^2)-\mathrm{E}(X)\mu\right]-\mu^3}{\sigma^3}\\
&= \frac{\mathrm{E}(X^3) -3\mu\left[\mathrm{E}(X^2)-\mathrm{E}(X)^2\right]-\mu^3}{\sigma^3} \; .
\end{split}
$$

Because the [variance can be written in terms of expected values](/P/var-mean) as

$$ \label{eq:var-partition}
\sigma^2 = \mathrm{E}(X^2)-\mathrm{E}(X)^2 \; ,
$$

we can rewrite \eqref{eq:partition} as

$$ \label{eq:partition-2}
\mathrm{Skew}(X) = \frac{\mathrm{E}(X^3) -3\mu\sigma^2-\mu^3}{\sigma^3} \; .
$$

This finishes the proof of \eqref{eq:skew-partition}.
