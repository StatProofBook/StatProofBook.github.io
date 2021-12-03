---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-05 08:41:00

title: "Kullback-Leibler divergence for the gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Kullback-Leibler divergence"

sources:
  - authors: "Penny, William D."
    year: 2001
    title: "KL-Divergences of Normal, Gamma, Dirichlet and Wishart densities"
    in: "University College, London"
    url: "https://www.fil.ion.ucl.ac.uk/~wpenny/publications/densities.ps"

proof_id: "P93"
shortcut: "gam-kl"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar). Assume two [gamma distributions](/D/gam) $P$ and $Q$ specifying the probability distribution of $X$ as

$$ \label{eq:gams}
\begin{split}
P: \; X &\sim \mathrm{Gam}(a_1, b_1) \\
Q: \; X &\sim \mathrm{Gam}(a_2, b_2) \; .
\end{split}
$$

Then, the [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ is given by

$$ \label{eq:gam-KL}
\mathrm{KL}[P\,||\,Q] = a_2 \, \ln \frac{b_1}{b_2} - \ln \frac{\Gamma(a_1)}{\Gamma(a_2)} + (a_1 - a_2) \, \psi(a_1) - (b_1 - b_2) \, \frac{a_1}{b_1} \; .
$$


**Proof:** The [KL divergence for a continuous random variable](/D/kl) is given by 

$$ \label{eq:KL-cont}
\mathrm{KL}[P\,||\,Q] = \int_{\mathcal{X}} p(x) \, \ln \frac{p(x)}{q(x)} \, \mathrm{d}x
$$

which, applied to the [gamma distributions](/D/gam) in \eqref{eq:gams}, yields

$$ \label{eq:gam-KL-s1}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \int_{-\infty}^{+\infty} \mathrm{Gam}(x; a_1, b_1) \, \ln \frac{\mathrm{Gam}(x; a_1, b_1)}{\mathrm{Gam}(x; a_2, b_2)} \, \mathrm{d}x \\
&= \left\langle \ln \frac{\mathrm{Gam}(x; a_1, b_1)}{\mathrm{Gam}(x; a_2, b_2)} \right\rangle_{p(x)} \; .
\end{split}
$$

Using the [probability density function of the gamma distribution](/P/gam-pdf), this becomes:

$$ \label{eq:gam-KL-s2}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \left\langle \ln \frac{ \frac{ {b_1}^{a_1}}{\Gamma(a_1)} x^{a_1-1} \exp[-b_1 x] }{ \frac{ {b_2}^{a_2}}{\Gamma(a_2)} x^{a_2-1} \exp[-b_2 x] } \right\rangle_{p(x)} \\
&= \left\langle \ln \left( \frac{ {b_1}^{a_1}}{ {b_2}^{a_2}} \cdot \frac{\Gamma(a_2)}{\Gamma(a_1)} \cdot x^{a_1-a_2} \cdot \exp[-(b_1-b_2) x] \right) \right\rangle_{p(x)} \\
&= \left\langle a_1 \cdot \ln b_1 - a_2 \cdot \ln b_2 - \ln \Gamma(a_1) + \ln \Gamma(a_2) + (a_1-a_2) \cdot \ln x - (b_1-b_2) \cdot x \right\rangle_{p(x)} \; .
\end{split}
$$

Using the [mean of the gamma distribution](/P/gam-mean) and the [expected value of a logarithmized gamma variate](/P/gam-logmean)

$$ \label{eq:gam-means}
\begin{split}
x \sim \mathrm{Gam}(a,b) \quad \Rightarrow \quad &\left\langle x \right\rangle = \frac{a}{b} \quad \text{and} \\
&\left\langle \ln x \right\rangle = \psi(a) - \ln(b) \; ,
\end{split}
$$

the Kullback-Leibler divergence from \eqref{eq:gam-KL-s2} becomes:

$$ \label{eq:gam-KL-s3}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= a_1 \cdot \ln b_1 - a_2 \cdot \ln b_2 - \ln \Gamma(a_1) + \ln \Gamma(a_2) + (a_1-a_2) \cdot \left( \psi(a_1) - \ln(b_1) \right) - (b_1-b_2) \cdot \frac{a_1}{b_1} \\
&= a_2 \cdot \ln b_1 - a_2 \cdot \ln b_2 - \ln \Gamma(a_1) + \ln \Gamma(a_2) + (a_1-a_2) \cdot \psi(a_1) - (b_1-b_2) \cdot \frac{a_1}{b_1} \; .
\end{split}
$$

Finally, combining the logarithms, we get:

$$ \label{eq:gam-KL-qed}
\mathrm{KL}[P\,||\,Q] = a_2 \, \ln \frac{b_1}{b_2} - \ln \frac{\Gamma(a_1)}{\Gamma(a_2)} + (a_1 - a_2) \, \psi(a_1) - (b_1 - b_2) \, \frac{a_1}{b_1} \; .
$$