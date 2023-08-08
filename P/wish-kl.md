---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-12-02 15:33:00

title: "Kullback-Leibler divergence for the Wishart distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Wishart distribution"
theorem: "Kullback-Leibler divergence"

sources:
  - authors: "Penny, William D."
    year: 2001
    title: "KL-Divergences of Normal, Gamma, Dirichlet and Wishart densities"
    in: "University College, London"
    pages: "pp. 2-3, eqs. 13/15"
    url: "https://www.fil.ion.ucl.ac.uk/~wpenny/publications/densities.ps"
  - authors: "Wikipedia"
    year: 2021
    title: "Wishart distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-12-02"
    url: "https://en.wikipedia.org/wiki/Wishart_distribution#KL-divergence"

proof_id: "P295"
shortcut: "wish-kl"
username: "JoramSoch"
---


**Theorem:** Let $S$ be a $p \times p$ [random matrix](/D/rmat). Assume two [Wishart distributions](/D/wish) $P$ and $Q$ specifying the probability distribution of $S$ as

$$ \label{eq:wishs}
\begin{split}
P: \; S &\sim \mathcal{W}(V_1, n_1) \\
Q: \; S &\sim \mathcal{W}(V_2, n_2) \; .
\end{split}
$$

Then, the [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ is given by

$$ \label{eq:wish-KL}
\mathrm{KL}[P\,||\,Q] = \frac{1}{2} \left[ n_2 \left( \ln |V_2| - \ln |V_1| \right) + n_1 \mathrm{tr}(V_2^{-1} V_1) + 2 \ln \frac{\Gamma_p\left(\frac{n_2}{2}\right)}{\Gamma_p\left(\frac{n_1}{2}\right)} + (n_1-n_2) \psi_p\left(\frac{n_1}{2}\right) - n_1 p \right]
$$

where $\Gamma_p(x)$ is the multivariate gamma function

$$ \label{eq:mult-gam-fct}
\Gamma_p(x) = \pi^{p(p-1)/4} \, \prod_{j=1}^k \Gamma\left(x - \frac{j-1}{2}\right)
$$

and $\psi_p(x)$ is the multivariate digamma function

$$ \label{eq:mult-psi-fct}
\psi_p(x) = \frac{\mathrm{d}\ln \Gamma_p(x)}{\mathrm{d}x} = \sum_{j=1}^k \psi\left(x - \frac{j-1}{2}\right) \; .
$$


**Proof:** The [KL divergence for a continuous random variable](/D/kl) is given by 

$$ \label{eq:KL-cont}
\mathrm{KL}[P\,||\,Q] = \int_{\mathcal{X}} p(x) \, \ln \frac{p(x)}{q(x)} \, \mathrm{d}x
$$

which, applied to the [Wishart distributions](/D/wish) in \eqref{eq:wishs}, yields

$$ \label{eq:wish-KL-s1}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \int_{\mathcal{S}^p} \mathcal{W}(S; V_1, n_1) \, \ln \frac{\mathcal{W}(S; V_1, n_1)}{\mathcal{W}(S; V_2, n_2)} \, \mathrm{d}S \\
&= \left\langle \ln \frac{\mathcal{W}(S; \alpha_1)}{\mathcal{W}(S; \alpha_1)} \right\rangle_{p(S)}
\end{split}
$$

where $\mathcal{S}^p$ is the set of all positive-definite symmetric $p \times p$ matrices.

Using the [probability density function of the Wishart distribution](/P/wish-pdf), this becomes:

$$ \label{eq:wish-KL-s2}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \left\langle \ln \frac{\frac{1}{\sqrt{2^{n_1 p} |V_1|^{n_1}} \Gamma_p \left( \frac{n_1}{2} \right)} \cdot |S|^{(n_1-p-1)/2} \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( V_1^{-1} S \right) \right]}{\frac{1}{\sqrt{2^{n_2 p} |V_2|^{n_2}} \Gamma_p \left( \frac{n_2}{2} \right)} \cdot |S|^{(n_2-p-1)/2} \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( V_2^{-1} S \right) \right]} \right\rangle_{p(S)} \\
&= \left\langle \ln \left( \sqrt{2^{(n_2-n_1)p} \cdot \frac{|V_2|^{n_2}}{|V_1|^{n_1}}} \cdot \frac{\Gamma_p\left( \frac{n_2}{2} \right)}{\Gamma_p\left( \frac{n_1}{2} \right)} \cdot |S|^{(n_1-n_2)/2} \cdot \exp\left[ -\frac{1}{2} \mathrm{tr}\left( V_1^{-1} S \right) -\frac{1}{2} \mathrm{tr}\left( V_2^{-1} S \right) \right] \right) \right\rangle_{p(S)} \\
&= \left\langle \frac{(n_2-n_1)p}{2} \ln 2 + \frac{n_2}{2} \ln |V_2| - \frac{n_1}{2} \ln |V_1| + \ln \frac{\Gamma_p\left( \frac{n_2}{2} \right)}{\Gamma_p\left( \frac{n_1}{2} \right)} \right. \\
&+ \left. \quad \frac{n_1-n_2}{2} \ln |S| - \frac{1}{2} \mathrm{tr}\left( V_1^{-1} S \right) - \frac{1}{2} \mathrm{tr}\left( V_2^{-1} S \right) \right\rangle_{p(S)} \\
&= \frac{(n_2-n_1)p}{2} \ln 2 + \frac{n_2}{2} \ln |V_2| - \frac{n_1}{2} \ln |V_1| + \ln \frac{\Gamma_p\left( \frac{n_2}{2} \right)}{\Gamma_p\left( \frac{n_1}{2} \right)} \\
&+ \frac{n_1-n_2}{2} \left\langle \ln |S| \right\rangle_{p(S)} - \frac{1}{2} \left\langle \mathrm{tr}\left( V_1^{-1} S \right) \right\rangle_{p(S)} - \frac{1}{2} \left\langle \mathrm{tr}\left( V_2^{-1} S \right) \right\rangle_{p(S)} \; .
\end{split}
$$

Using the [expected value of a Wishart random matrix](/P/wish-mean)

$$ \label{eq:wish-mean}
S \sim \mathcal{W}(V,n) \quad \Rightarrow \quad \left\langle S \right\rangle = n V \; ,
$$

such that the [expected value of the matrix trace](/P/mean-tr) becomes

$$ \label{eq:wish-trmean}
\left\langle \mathrm{tr}(AS) \right\rangle = \mathrm{tr}\left( \left\langle AS \right\rangle \right) = \mathrm{tr}\left( A \left\langle S \right\rangle \right) = \mathrm{tr}\left( A \cdot (nV) \right) = n \cdot \mathrm{tr}(AV) \; ,
$$

and the [expected value of a Wishart log-determinant](/P/wish-logdetmean)

$$ \label{eq:wish-logdetmean}
S \sim \mathcal{W}(V,n) \quad \Rightarrow \quad \left\langle \ln |S| \right\rangle = \psi_p\left(\frac{n}{2}\right) + p \cdot \ln 2 + \ln |V| \; ,
$$

the Kullback-Leibler divergence from \eqref{eq:wish-KL-s2} becomes:

$$ \label{eq:wish-KL-s3}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \frac{(n_2-n_1)p}{2} \ln 2 + \frac{n_2}{2} \ln |V_2| - \frac{n_1}{2} \ln |V_1| + \ln \frac{\Gamma_p\left( \frac{n_2}{2} \right)}{\Gamma_p\left( \frac{n_1}{2} \right)} \\
&+ \frac{n_1-n_2}{2} \left[ \psi_p\left(\frac{n_1}{2}\right) + p \cdot \ln 2 + \ln |V_1| \right] - \frac{n_1}{2} \mathrm{tr}\left( V_1^{-1} V_1 \right) - \frac{n_1}{2} \mathrm{tr}\left( V_2^{-1} V_1 \right) \\
&= \frac{n_2}{2} \left( \ln |V_2| - \ln |V_1| \right) + \ln \frac{\Gamma_p\left( \frac{n_2}{2} \right)}{\Gamma_p\left( \frac{n_1}{2} \right)} + \frac{n_1-n_2}{2} \psi_p\left(\frac{n_1}{2}\right) - \frac{n_1}{2} \mathrm{tr}\left( I_p \right) - \frac{n_1}{2} \mathrm{tr}\left( V_2^{-1} V_1 \right) \\
& = \frac{1}{2} \left[ n_2 \left( \ln |V_2| - \ln |V_1| \right) + n_1 \mathrm{tr}(V_2^{-1} V_1) + 2 \ln \frac{\Gamma_p\left(\frac{n_2}{2}\right)}{\Gamma_p\left(\frac{n_1}{2}\right)} + (n_1-n_2) \psi_p\left(\frac{n_1}{2}\right) - n_1 p \right] \; .
\end{split}
$$