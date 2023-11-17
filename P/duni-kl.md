---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-11-17 15:19:37

title: "Kullback-Leibler divergence for the discrete uniform distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Discrete uniform distribution"
theorem: "Kullback-Leibler divergence"

sources:

proof_id: "P425"
shortcut: "duni-kl"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar). Assume two [discrete uniform distributions](/D/Duni) $P$ and $Q$ specifying the probability distribution of $X$ as

$$ \label{eq:dunis}
\begin{split}
P: \; X &\sim \mathcal{U}(a_1, b_1) \\
Q: \; X &\sim \mathcal{U}(a_2, b_2) \; .
\end{split}
$$

Then, the [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ is given by

$$ \label{eq:duni-KL}
\mathrm{KL}[P\,||\,Q] = \ln \frac{b_2-a_2+1}{b_1-a_1+1} \; .
$$


**Proof:** The [KL divergence for a discrete random variable](/D/kl) is given by

$$ \label{eq:KL-disc}
\mathrm{KL}[P\,||\,Q] = \sum_{x \in \mathcal{X}} p(x) \, \ln \frac{p(x)}{q(x)} \; .
$$

This means that the KL divergence of $P$ from $Q$ is only defined, if for all $x \in \mathcal{X}$, $q(x) = 0$ implies $p(x) = 0$. Thus, $\mathrm{KL}[P\,||\,Q]$ only exists, if $a_2 \leq a_1$ and $b_1 \leq b_2$, i.e. if $P$ only places non-zero probability where $Q$ also places non-zero probability, such that $q(x)$ is not zero for any $x \in \mathcal{X}$ where $p(x)$ is positive.

If this requirement is fulfilled, we can write

$$ \label{eq:duni-KL-s1}
\mathrm{KL}[P\,||\,Q] = \sum_{x=-\infty}^{a_1} p(x) \, \ln \frac{p(x)}{q(x)} + \sum_{x=a_1}^{b_1} p(x) \, \ln \frac{p(x)}{q(x)} + \sum_{x=b_1}^{+\infty} p(x) \, \ln \frac{p(x)}{q(x)}
$$

and because $p(x) = 0$ for any $x < a_1$ and any $x > b_1$, we have

$$ \label{eq:duni-KL-s2}
\mathrm{KL}[P\,||\,Q] = \sum_{x=-\infty}^{a_1} 0 \cdot \ln \frac{0}{q(x)} + \sum_{x=a_1}^{b_1} p(x) \, \ln \frac{p(x)}{q(x)} + \sum_{x=b_1}^{+\infty} 0 \cdot \ln \frac{0}{q(x)} \; .
$$

Now, $(0 \cdot \ln 0)$ is taken to be $0$ [by convention](/D/ent), such that

$$ \label{eq:duni-KL-s3}
\mathrm{KL}[P\,||\,Q] = \sum_{x=a_1}^{b_1} p(x) \, \ln \frac{p(x)}{q(x)}
$$

and we can use the [probability mass function of the discrete uniform distribution](/P/duni-pmf) to evaluate:

$$ \label{eq:duni-KL-s4}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \sum_{x=a_1}^{b_1} \frac{1}{b_1-a_1+1} \cdot \ln \frac{\frac{1}{b_1-a_1+1}}{\frac{1}{b_2-a_2+1}} \\
&= \frac{1}{b_1-a_1+1} \cdot \ln \frac{b_2-a_2+1}{b_1-a_1+1} \sum_{x=a_1}^{b_1} 1 \\
&= \frac{1}{b_1-a_1+1} \cdot \ln \frac{b_2-a_2+1}{b_1-a_1+1} \cdot (b_1-a_1+1) \\
&= \ln \frac{b_2-a_2+1}{b_1-a_1+1} \; .
\end{split}
$$