---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-22 08:39:00

title: "Differential entropy for the matrix-normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Differential entropy"

sources:

proof_id: "P344"
shortcut: "matn-dent"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n \times p$ [random matrix](/D/rmat) following a [matrix-normal distribution](/D/matn)

$$ \label{eq:matn}
X \sim \mathcal{MN}(M, U, V) \; .
$$

Then, the [differential entropy](/D/dent) of $X$ in nats is

$$ \label{eq:matn-dent}
\mathrm{h}(X) = \frac{np}{2} \ln(2\pi) + \frac{n}{2} \ln|V| + \frac{p}{2} \ln|U| + \frac{np}{2} \; .
$$


**Proof:** The [matrix-normal distribution is equivalent to the multivariate normal distribution](/P/matn-mvn),

$$ \label{eq:matn-mvn}
X \sim \mathcal{MN}(M, U, V) \quad \Leftrightarrow \quad \mathrm{vec}(X) \sim \mathcal{N}(\mathrm{vec}(M), V \otimes U) \; ,
$$

and the [differential entropy for the multivariate normal distribution](/P/mvn-dent) in nats is

$$ \label{eq:mvn-dent}
X \sim \mathcal{N}(\mu, \Sigma) \quad \Rightarrow \quad \mathrm{h}(X) = \frac{n}{2} \ln(2\pi) + \frac{1}{2} \ln|\Sigma| + \frac{1}{2} n
$$

where $X$ is an $n \times 1$ [random vector](/D/rvec).

Thus, we can plug the distribution parameters from \eqref{eq:matn} into the differential entropy in \eqref{eq:mvn-dent} using the relationship given by \eqref{eq:matn-mvn}

$$ \label{eq:matn-dent-s1}
\mathrm{h}(X) = \frac{np}{2} \ln(2\pi) + \frac{1}{2} \ln|V \otimes U| + \frac{1}{2} np \; .
$$

Using the Kronecker product property

$$ \label{eq:kron-det}
|A \otimes B| = |A|^m \, |B|^n \quad \text{where} \quad A \in \mathbb{R}^{n \times n} \quad \text{and} \quad B \in \mathbb{R}^{m \times m} \; ,
$$

the differential entropy from \eqref{eq:matn-dent-s1} becomes:

$$ \label{eq:matn-dent-s2}
\begin{split}
\mathrm{h}(X) &= \frac{np}{2} \ln(2\pi) + \frac{1}{2} \ln\left(|V|^n |U|^p\right) + \frac{1}{2} np \\
&= \frac{np}{2} \ln(2\pi) + \frac{n}{2} \ln|V| + \frac{p}{2} \ln|U| + \frac{np}{2} \; .
\end{split}
$$