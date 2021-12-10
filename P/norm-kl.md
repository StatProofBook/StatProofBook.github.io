---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-19 07:08:00

title: "Kullback-Leibler divergence for the normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Kullback-Leibler divergence"

sources:

proof_id: "P193"
shortcut: "norm-kl"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar). Assume two [normal distributions](/D/norm) $P$ and $Q$ specifying the probability distribution of $X$ as

$$ \label{eq:norms}
\begin{split}
P: \; X &\sim \mathcal{N}(\mu_1, \sigma_1^2) \\
Q: \; X &\sim \mathcal{N}(\mu_2, \sigma_2^2) \; .
\end{split}
$$

Then, the [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ is given by

$$ \label{eq:norm-KL}
\mathrm{KL}[P\,||\,Q] = \frac{1}{2} \left[ \frac{(\mu_2 - \mu_1)^2}{\sigma_2^2} + \frac{\sigma_1^2}{\sigma_2^2} - \ln \frac{\sigma_1^2}{\sigma_2^2} - 1 \right] \; .
$$


**Proof:** The [KL divergence for a continuous random variable](/D/kl) is given by 

$$ \label{eq:KL-cont}
\mathrm{KL}[P\,||\,Q] = \int_{\mathcal{X}} p(x) \, \ln \frac{p(x)}{q(x)} \, \mathrm{d}x
$$

which, applied to the [normal distributions](/D/norm) in \eqref{eq:norms}, yields

$$ \label{eq:norm-KL-s1}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \int_{-\infty}^{+\infty} \mathcal{N}(x; \mu_1, \sigma_1^2) \, \ln \frac{\mathcal{N}(x; \mu_1, \sigma_1^2)}{\mathcal{N}(x; \mu_2, \sigma_2^2)} \, \mathrm{d}x \\
&= \left\langle \ln \frac{\mathcal{N}(x; \mu_1, \sigma_1^2)}{\mathcal{N}(x; \mu_2, \sigma_2^2)} \right\rangle_{p(x)} \; .
\end{split}
$$

Using the [probability density function of the normal distribution](/P/norm-pdf), this becomes:

$$ \label{eq:norm-KL-s2}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \left\langle \ln \frac{ \frac{1}{\sqrt{2 \pi} \sigma_1} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu_1}{\sigma_1} \right)^2 \right] }{ \frac{1}{\sqrt{2 \pi} \sigma_2} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu_2}{\sigma_2} \right)^2 \right] } \right\rangle_{p(x)} \\
&= \left\langle \ln \left( \sqrt \frac{\sigma_2^2}{\sigma_1^2} \cdot \exp\left[ -\frac{1}{2} \left( \frac{x-\mu_1}{\sigma_1} \right)^2 + \frac{1}{2} \left( \frac{x-\mu_2}{\sigma_2} \right)^2 \right] \right) \right\rangle_{p(x)} \\
&= \left\langle \frac{1}{2} \ln \frac{\sigma_2^2}{\sigma_1^2} -\frac{1}{2} \left( \frac{x-\mu_1}{\sigma_1} \right)^2 + \frac{1}{2} \left( \frac{x-\mu_2}{\sigma_2} \right)^2 \right\rangle_{p(x)} \\
&= \frac{1}{2} \left\langle - \left( \frac{x-\mu_1}{\sigma_1} \right)^2 + \left( \frac{x-\mu_2}{\sigma_2} \right)^2 - \ln \frac{\sigma_1^2}{\sigma_2^2} \right\rangle_{p(x)} \\
&= \frac{1}{2} \left\langle - \frac{(x-\mu_1)^2}{\sigma_1^2} + \frac{x^2 - 2 \mu_2 x + \mu_2^2}{\sigma_2^2} - \ln \frac{\sigma_1^2}{\sigma_2^2} \right\rangle_{p(x)} \; .
\end{split}
$$

Because the [expected value](/D/mean) [is a linear operator](/P/mean-lin), the expectation can be moved into the sum:

$$ \label{eq:norm-KL-s3}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \frac{1}{2} \left[ - \frac{\left\langle (x-\mu_1)^2 \right\rangle}{\sigma_1^2} + \frac{\left\langle x^2 - 2 \mu_2 x + \mu_2^2 \right\rangle}{\sigma_2^2} - \left\langle \ln \frac{\sigma_1^2}{\sigma_2^2} \right\rangle \right] \\
&= \frac{1}{2} \left[ - \frac{\left\langle (x-\mu_1)^2 \right\rangle}{\sigma_1^2} + \frac{\left\langle x^2 \right\rangle - \left\langle 2 \mu_2 x \right\rangle + \left\langle \mu_2^2 \right\rangle}{\sigma_2^2} - \ln \frac{\sigma_1^2}{\sigma_2^2} \right] \; .
\end{split}
$$

The first expectation corresponds to the [variance](/D/var)

$$ \label{eq:var}
\left\langle (X-\mu)^2 \right\rangle = \mathrm{E}[(X-\mathrm{E}(X))^2] = \mathrm{Var}(X)
$$

and the [variance of a normally distributed random variable](/P/norm-var) is

$$ \label{eq:norm-var}
X \sim \mathcal{N}(\mu, \sigma^2) \quad \Rightarrow \quad \mathrm{Var}(X) = \sigma^2 \; .
$$

Additionally applying the [raw moments of the normal distribution](/P/norm-mgf)

$$ \label{eq:norm-mom-raw}
X \sim \mathcal{N}(\mu, \sigma^2) \quad \Rightarrow \quad \left\langle x \right\rangle = \mu \quad \text{and} \quad \left\langle x^2 \right\rangle = \mu^2 + \sigma^2 \; ,
$$

the Kullback-Leibler divergence in \eqref{eq:norm-KL-s3} becomes

$$ \label{eq:norm-KL-s4}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \frac{1}{2} \left[ - \frac{\sigma_1^2}{\sigma_1^2} + \frac{\mu_1^2 + \sigma_1^2 - 2 \mu_2 \mu_1 + \mu_2^2}{\sigma_2^2} - \ln \frac{\sigma_1^2}{\sigma_2^2} \right] \\
&= \frac{1}{2} \left[ \frac{\mu_1^2 - 2 \mu_1 \mu_2 + \mu_2^2}{\sigma_2^2} + \frac{\sigma_1^2}{\sigma_2^2} - \ln \frac{\sigma_1^2}{\sigma_2^2} - 1 \right] \\
&= \frac{1}{2} \left[ \frac{(\mu_1 - \mu_2)^2}{\sigma_2^2} + \frac{\sigma_1^2}{\sigma_2^2} - \ln \frac{\sigma_1^2}{\sigma_2^2} - 1 \right]
\end{split}
$$

which is equivalent to \eqref{eq:norm-KL}.