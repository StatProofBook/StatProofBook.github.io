---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-05 06:57:00

title: "Kullback-Leibler divergence for the multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Kullback-Leibler divergence"

sources:
  - authors: "Duchi, John"
    year: 2014
    title: "Derivations for Linear Algebra and Optimization"
    in: "University of California, Berkeley"
    url: "http://www.eecs.berkeley.edu/~jduchi/projects/general_notes.pdf"

proof_id: "P92"
shortcut: "mvn-kl"
username: "JoramSoch"
---


**Theorem:** Let $x$ be an $n \times 1$ [random vector](/D/rvec). Assume two [multivariate normal distributions](/D/mvn) $P$ and $Q$ specifying the probability distribution of $x$ as

$$ \label{eq:mvns}
\begin{split}
P: \; x &\sim \mathcal{N}(\mu_1, \Sigma_1) \\
Q: \; x &\sim \mathcal{N}(\mu_2, \Sigma_2) \; .
\end{split}
$$

Then, the [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ is given by

$$ \label{eq:mvn-KL}
\mathrm{KL}[P\,||\,Q] = \frac{1}{2} \left[ (\mu_2 - \mu_1)^T \Sigma_2^{-1} (\mu_2 - \mu_1) + \mathrm{tr}(\Sigma_2^{-1} \Sigma_1) - \ln \frac{|\Sigma_1|}{|\Sigma_2|} - n \right] \; .
$$


**Proof:** The [KL divergence for a continuous random variable](/D/kl) is given by 

$$ \label{eq:KL-cont}
\mathrm{KL}[P\,||\,Q] = \int_{\mathcal{X}} p(x) \, \ln \frac{p(x)}{q(x)} \, \mathrm{d}x
$$

which, applied to the [multivariate normal distributions](/D/mvn) in \eqref{eq:mvns}, yields

$$ \label{eq:mvn-KL-s1}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \int_{\mathbb{R}^n} \mathcal{N}(x; \mu_1, \Sigma_1) \, \ln \frac{\mathcal{N}(x; \mu_1, \Sigma_1)}{\mathcal{N}(x; \mu_2, \Sigma_2)} \, \mathrm{d}x \\
&= \left\langle \ln \frac{\mathcal{N}(x; \mu_1, \Sigma_1)}{\mathcal{N}(x; \mu_2, \Sigma_2)} \right\rangle_{p(x)} \; .
\end{split}
$$

Using the [probability density function of the multivariate normal distribution](/P/mvn-pdf), this becomes:

$$ \label{eq:mvn-KL-s2}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \left\langle \ln \frac{ \frac{1}{\sqrt{(2 \pi)^n |\Sigma_1|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu_1)^\mathrm{T} \Sigma_1^{-1} (x-\mu_1) \right] }{ \frac{1}{\sqrt{(2 \pi)^n |\Sigma_2|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu_2)^\mathrm{T} \Sigma_2^{-1} (x-\mu_2) \right] } \right\rangle_{p(x)} \\
&= \left\langle \frac{1}{2} \ln \frac{|\Sigma_2|}{|\Sigma_1|} - \frac{1}{2} (x-\mu_1)^\mathrm{T} \Sigma_1^{-1} (x-\mu_1) + \frac{1}{2} (x-\mu_2)^\mathrm{T} \Sigma_2^{-1} (x-\mu_2) \right\rangle_{p(x)} \\
&= \frac{1}{2} \left\langle \ln \frac{|\Sigma_2|}{|\Sigma_1|} - (x-\mu_1)^\mathrm{T} \Sigma_1^{-1} (x-\mu_1) + (x-\mu_2)^\mathrm{T} \Sigma_2^{-1} (x-\mu_2) \right\rangle_{p(x)} \; .
\end{split}
$$

Now, using the fact that $x = \mathrm{tr}(x)$, if $a$ is scalar, and the trace property $\mathrm{tr}(ABC) = \mathrm{tr}(BCA)$, we have:

$$ \label{eq:mvn-KL-s3}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \frac{1}{2} \left\langle \ln \frac{|\Sigma_2|}{|\Sigma_1|} - \mathrm{tr}\left[ \Sigma_1^{-1} (x-\mu_1) (x-\mu_1)^\mathrm{T} \right] + \mathrm{tr}\left[ \Sigma_2^{-1} (x-\mu_2) (x-\mu_2)^\mathrm{T} \right] \right\rangle_{p(x)} \\
&= \frac{1}{2} \left\langle \ln \frac{|\Sigma_2|}{|\Sigma_1|} - \mathrm{tr}\left[ \Sigma_1^{-1} (x-\mu_1) (x-\mu_1)^\mathrm{T} \right] + \mathrm{tr}\left[ \Sigma_2^{-1} \left( x x^\mathrm{T} - 2 \mu_2 x^\mathrm{T} + \mu_2 \mu_2^\mathrm{T} \right) \right] \right\rangle_{p(x)} \; .
\end{split}
$$

Because [trace function and expected value are both linear operators](/P/mean-tr), the expectation can be moved inside the trace:

$$ \label{eq:mvn-KL-s4}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \frac{1}{2} \left( \ln \frac{|\Sigma_2|}{|\Sigma_1|} - \mathrm{tr}\left[ \Sigma_1^{-1} \left\langle (x-\mu_1) (x-\mu_1)^\mathrm{T} \right\rangle_{p(x)} \right] + \mathrm{tr}\left[ \Sigma_2^{-1} \left\langle x x^\mathrm{T} - 2 \mu_2 x^\mathrm{T} + \mu_2 \mu_2^\mathrm{T} \right\rangle_{p(x)} \right] \right) \\
&= \frac{1}{2} \left( \ln \frac{|\Sigma_2|}{|\Sigma_1|} - \mathrm{tr}\left[ \Sigma_1^{-1} \left\langle (x-\mu_1) (x-\mu_1)^\mathrm{T} \right\rangle_{p(x)} \right] + \mathrm{tr}\left[ \Sigma_2^{-1} \left( \left\langle x x^\mathrm{T} \right\rangle_{p(x)} - \left\langle 2 \mu_2 x^\mathrm{T} \right\rangle_{p(x)} + \left\langle \mu_2 \mu_2^\mathrm{T} \right\rangle_{p(x)} \right) \right] \right) \; .
\end{split}
$$

Using the [expectation of a linear form for the multivariate normal distribution](/P/mvn-ltt)

$$ \label{eq:mvn-lfmean}
x \sim \mathcal{N}(\mu, \Sigma) \quad \Rightarrow \quad \left\langle A x \right\rangle = A \mu
$$

and the [expectation of a quadratic form for the multivariate normal distribution](/P/mean-qf)

$$ \label{eq:mvn-qfmean}
x \sim \mathcal{N}(\mu, \Sigma) \quad \Rightarrow \quad \left\langle x^\mathrm{T} A x \right\rangle = \mu^\mathrm{T} A \mu + \mathrm{tr}(A \Sigma) \; ,
$$

the Kullback-Leibler divergence from \eqref{eq:mvn-KL-s4} becomes:

$$ \label{eq:mvn-KL-s5}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \frac{1}{2} \left( \ln \frac{|\Sigma_2|}{|\Sigma_1|} - \mathrm{tr}\left[ \Sigma_1^{-1} \Sigma_1 \right] + \mathrm{tr}\left[ \Sigma_2^{-1} \left( \Sigma_1 + \mu_1 \mu_1^\mathrm{T} - 2 \mu_2 \mu_1^\mathrm{T} + \mu_2 \mu_2^\mathrm{T} \right) \right] \right) \\
&= \frac{1}{2} \left( \ln \frac{|\Sigma_2|}{|\Sigma_1|} - \mathrm{tr}\left[ I_n \right] + \mathrm{tr}\left[ \Sigma_2^{-1} \Sigma_1 \right] + \mathrm{tr}\left[ \Sigma_2^{-1} \left( \mu_1 \mu_1^\mathrm{T} - 2 \mu_2 \mu_1^\mathrm{T} + \mu_2 \mu_2^\mathrm{T} \right) \right] \right) \\
&= \frac{1}{2} \left( \ln \frac{|\Sigma_2|}{|\Sigma_1|} - n + \mathrm{tr}\left[ \Sigma_2^{-1} \Sigma_1 \right] + \mathrm{tr}\left[ \mu_1^\mathrm{T} \Sigma_2^{-1} \mu_1  - 2 \mu_1^\mathrm{T} \Sigma_2^{-1} \mu_2  + \mu_2^\mathrm{T} \Sigma_2^{-1} \mu_2 \right] \right) \\
&= \frac{1}{2} \left[ \ln \frac{|\Sigma_2|}{|\Sigma_1|} - n + \mathrm{tr}\left[ \Sigma_2^{-1} \Sigma_1 \right] + (\mu_2 - \mu_1)^T \Sigma_2^{-1} (\mu_2 - \mu_1) \right] \; .
\end{split}
$$

Finally, rearranging the terms, we get:

$$ \label{eq:mvn-KL-qed}
\mathrm{KL}[P\,||\,Q] = \frac{1}{2} \left[ (\mu_2 - \mu_1)^T \Sigma_2^{-1} (\mu_2 - \mu_1) + \mathrm{tr}(\Sigma_2^{-1} \Sigma_1) - \ln \frac{|\Sigma_1|}{|\Sigma_2|} - n \right] \; .
$$