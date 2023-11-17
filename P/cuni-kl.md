---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2023-10-27 12:32:26

title: "Kullback-Leibler divergence for the continuous uniform distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Continuous uniform distribution"
theorem: "Kullback-Leibler divergence"

sources:

proof_id: "P422"
shortcut: "cuni-kl"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar). Assume two [continuous uniform distributions](/D/cuni) $P$ and $Q$ specifying the probability distribution of $X$ as

$$ \label{eq:cunis}
\begin{split}
P: \; X &\sim \mathcal{U}(a_1, b_1) \\
Q: \; X &\sim \mathcal{U}(a_2, b_2) \; .
\end{split}
$$

Then, the [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ is given by

$$ \label{eq:cuni-KL}
\mathrm{KL}[P\,||\,Q] = \ln \frac{b_2-a_2}{b_1-a_1} \; .
$$


**Proof:** The [KL divergence for a continuous random variable](/D/kl) is given by 

$$ \label{eq:KL-cont}
\mathrm{KL}[P\,||\,Q] = \int_{\mathcal{X}} p(x) \, \ln \frac{p(x)}{q(x)} \, \mathrm{d}x \; .
$$

This means that the KL divergence of $P$ from $Q$ is only defined, if for all $x \in \mathcal{X}$, $q(x) = 0$ implies $p(x) = 0$. Thus, $\mathrm{KL}[P\,\vert\vert\,Q]$ only exists, if $a_2 \leq a_1$ and $b_1 \leq b_2$, i.e. if $P$ only places non-zero probability where $Q$ also places non-zero probability, such that $q(x)$ is not zero for any $x \in \mathcal{X}$ where $p(x)$ is positive.

If this requirement is fulfilled, we can write

$$ \label{eq:cuni-KL-s1}
\mathrm{KL}[P\,||\,Q] = \int_{-\infty}^{a_1} p(x) \, \ln \frac{p(x)}{q(x)} \, \mathrm{d}x + \int_{a_1}^{b_1} p(x) \, \ln \frac{p(x)}{q(x)} \, \mathrm{d}x + \int_{b_1}^{+\infty} p(x) \, \ln \frac{p(x)}{q(x)} \, \mathrm{d}x
$$

and because $p(x) = 0$ for any $x < a_1$ and any $x > b_1$, we have

$$ \label{eq:cuni-KL-s2}
\mathrm{KL}[P\,||\,Q] = \int_{-\infty}^{a_1} 0 \cdot \ln \frac{0}{q(x)} \, \mathrm{d}x + \int_{a_1}^{b_1} p(x) \, \ln \frac{p(x)}{q(x)} \, \mathrm{d}x + \int_{b_1}^{+\infty} 0 \cdot \ln \frac{0}{q(x)} \, \mathrm{d}x \; .
$$

Now, $(0 \cdot \ln 0)$ is taken to be [zero by convention](/D/ent), such that

$$ \label{eq:cuni-KL-s3}
\mathrm{KL}[P\,||\,Q] = \int_{a_1}^{b_1} p(x) \, \ln \frac{p(x)}{q(x)} \, \mathrm{d}x
$$

and we can use the [probability density function of the continuous uniform distribution](/P/cuni-pdf) to evaluate:

$$ \label{eq:cuni-KL-s4}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \int_{a_1}^{b_1} \frac{1}{b_1-a_1}\, \ln \frac{\frac{1}{b_1-a_1}}{\frac{1}{b_2-a_2}} \, \mathrm{d}x \\
&= \frac{1}{b_1-a_1}\, \ln \frac{b_2-a_2}{b_1-a_1} \int_{a_1}^{b_1} \, \mathrm{d}x \\
&= \frac{1}{b_1-a_1}\, \ln \frac{b_2-a_2}{b_1-a_1} \left[ x \right]_{a_1}^{b_1} \\
&= \frac{1}{b_1-a_1}\, \ln \frac{b_2-a_2}{b_1-a_1} (b_1-a_1) \\
&= \ln \frac{b_2-a_2}{b_1-a_1} \; .
\end{split}
$$