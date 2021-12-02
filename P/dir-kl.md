---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-12-02 14:28:00

title: "Kullback-Leibler divergence for the Dirichlet distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Dirichlet distribution"
theorem: "Kullback-Leibler divergence"

sources:
  - authors: "Penny, William D."
    year: 2001
    title: "KL-Divergences of Normal, Gamma, Dirichlet and Wishart densities"
    in: "University College, London"
    pages: "p. 2, eqs. 8-9"
    url: "https://www.fil.ion.ucl.ac.uk/~wpenny/publications/densities.ps"

proof_id: "P294"
shortcut: "dir-kl"
username: "JoramSoch"
---


**Theorem:** Let $x$ be an $k \times 1$ [random vector](/D/rvec). Assume two [Dirichlet distributions](/D/dir) $P$ and $Q$ specifying the probability distribution of $x$ as

$$ \label{eq:dirs}
\begin{split}
P: \; x &\sim \mathrm{Dir}(\alpha_1) \\
Q: \; x &\sim \mathrm{Dir}(\alpha_2) \; .
\end{split}
$$

Then, the [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ is given by

$$ \label{eq:dir-KL}
\mathrm{KL}[P\,||\,Q] = \ln \frac{\Gamma\left(\sum_{i=1}^{k} \alpha_{1i}\right)}{\Gamma\left(\sum_{i=1}^{k} \alpha_{2i}\right)} + \sum_{i=1}^{k} \ln \frac{\Gamma(\alpha_{2i})}{\Gamma(\alpha_{1i})} + \sum_{i=1}^{k} \left( \alpha_{1i} - \alpha_{2i} \right) \left[ \psi(\alpha_{1i}) - \psi\left(\sum_{i=1}^{k} \alpha_{1i}\right) \right] \; .
$$


**Proof:** The [KL divergence for a continuous random variable](/D/kl) is given by 

$$ \label{eq:KL-cont}
\mathrm{KL}[P\,||\,Q] = \int_{\mathcal{X}} p(x) \, \ln \frac{p(x)}{q(x)} \, \mathrm{d}x
$$

which, applied to the [Dirichlet distributions](/D/mvn) in \eqref{eq:dirs}, yields

$$ \label{eq:dir-KL-s1}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \int_{\mathcal{X}^k} \mathrm{Dir}(x; \alpha_1) \, \ln \frac{\mathrm{Dir}(x; \alpha_1)}{\mathrm{Dir}(x; \alpha_2)} \, \mathrm{d}x \\
&= \left\langle \ln \frac{\mathrm{Dir}(x; \alpha_1)}{\mathrm{Dir}(x; \alpha_2)} \right\rangle_{p(x)}
\end{split}
$$

where $\mathcal{X}^k$ is the set $\left\lbrace x \in \mathbb{R}^k \; \vert \; \sum_{i=1}^{k} x_i = 1, \; 0 \leq x_i \leq 1, \; i = 1,\ldots,k \right\rbrace$.

Using the [probability density function of the Dirichlet distribution](/P/dir-pdf), this becomes:

$$ \label{eq:dir-KL-s2}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \left\langle \ln \frac{ \frac{\Gamma\left( \sum_{i=1}^k \alpha_{1i} \right)}{\prod_{i=1}^k \Gamma(\alpha_{1i})} \, \prod_{i=1}^k {x_i}^{\alpha_{1i}-1} }{ \frac{\Gamma\left( \sum_{i=1}^k \alpha_{2i} \right)}{\prod_{i=1}^k \Gamma(\alpha_{2i})} \, \prod_{i=1}^k {x_i}^{\alpha_{2i}-1} } \right\rangle_{p(x)} \\
&= \left\langle \ln \left( \frac{\Gamma\left( \sum_{i=1}^k \alpha_{1i} \right)}{\Gamma\left( \sum_{i=1}^k \alpha_{2i} \right)} \cdot \frac{\prod_{i=1}^k \Gamma(\alpha_{2i})}{\prod_{i=1}^k \Gamma(\alpha_{1i})} \cdot \prod_{i=1}^k {x_i}^{\alpha_{1i}-\alpha_{2i}} \right) \right\rangle_{p(x)} \\
&= \left\langle \ln \frac{\Gamma\left( \sum_{i=1}^k \alpha_{1i} \right)}{\Gamma\left( \sum_{i=1}^k \alpha_{2i} \right)} + \sum_{i=1}^k \ln \frac{\Gamma(\alpha_{2i})}{\Gamma(\alpha_{1i})} + \sum_{i=1}^k (\alpha_{1i}-\alpha_{2i}) \cdot \ln (x_i) \right\rangle_{p(x)} \\
&= \ln \frac{\Gamma\left( \sum_{i=1}^k \alpha_{1i} \right)}{\Gamma\left( \sum_{i=1}^k \alpha_{2i} \right)} + \sum_{i=1}^k \ln \frac{\Gamma(\alpha_{2i})}{\Gamma(\alpha_{1i})} + \sum_{i=1}^k (\alpha_{1i}-\alpha_{2i}) \cdot \left\langle \ln x_i \right\rangle_{p(x)} \; .
\end{split}
$$

Using the [expected value of a logarithmized Dirichlet variate](/P/dir-logmean)

$$ \label{eq:dir-logmean}
x \sim \mathrm{Dir}(\alpha) \quad \Rightarrow \quad \left\langle \ln x_i \right\rangle = \psi(\alpha_i) - \psi\left(\sum_{i=1}^{k} \alpha_i\right) \; ,
$$

the Kullback-Leibler divergence from \eqref{eq:dir-KL-s2} becomes:

$$ \label{eq:dir-KL-s3}
\mathrm{KL}[P\,||\,Q] = \ln \frac{\Gamma\left( \sum_{i=1}^k \alpha_{1i} \right)}{\Gamma\left( \sum_{i=1}^k \alpha_{2i} \right)} + \sum_{i=1}^k \ln \frac{\Gamma(\alpha_{2i})}{\Gamma(\alpha_{1i})} + \sum_{i=1}^k (\alpha_{1i}-\alpha_{2i}) \cdot \left[ \psi(\alpha_{1i}) - \psi\left(\sum_{i=1}^{k} \alpha_{1i}\right) \right]
$$