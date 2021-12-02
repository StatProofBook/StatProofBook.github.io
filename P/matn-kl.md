---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-12-02 20:22:00

title: "Kullback-Leibler divergence for the matrix-normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Kullback-Leibler divergence"

sources:

proof_id: "P296"
shortcut: "matn-kl"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n \times p$ [random matrix](/D/rmat). Assume two [matrix-normal distributions](/D/matn) $P$ and $Q$ specifying the probability distribution of $X$ as

$$ \label{eq:matns}
\begin{split}
P: \; X &\sim \mathcal{MN}(M_1, U_1, V_1) \\
Q: \; X &\sim \mathcal{MN}(M_2, U_2, V_2) \; .
\end{split}
$$

Then, the [Kullback-Leibler divergence](/D/kl) of $P$ from $Q$ is given by

$$ \label{eq:matn-KL}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \frac{1}{2} \left[ \mathrm{vec}(M_2 - M_1)^\mathrm{T} \mathrm{vec}\left(U_2^{-1} (M_2 - M_1) V_2^{-1}\right) \right. \\
&+ \left. \mathrm{tr}\left( (V_2^{-1}V_1) \otimes (U_2^{-1}U_1) \right) - n \ln \frac{|V_1|}{|V_2|} - p \ln \frac{|U_1|}{|U_2|} - n p \right] \; .
\end{split}
$$


**Proof:** The [matrix-normal distribution is equivalent to the multivariate normal distribution](/P/matn-mvn),

$$ \label{eq:matn-mvn}
X \sim \mathcal{MN}(M, U, V) \quad \Leftrightarrow \quad \mathrm{vec}(X) \sim \mathcal{N}(\mathrm{vec}(M), V \otimes U) \; ,
$$

and the [Kullback-Leibler divergence for the multivariate normal distribution](/P/mvn-kl) is

$$ \label{eq:mvn-KL}
\mathrm{KL}[P\,||\,Q] = \frac{1}{2} \left[ (\mu_2 - \mu_1)^T \Sigma_2^{-1} (\mu_2 - \mu_1) + \mathrm{tr}(\Sigma_2^{-1} \Sigma_1) - \ln \frac{|\Sigma_1|}{|\Sigma_2|} - n \right]
$$

where $X$ is an $n \times 1$ [random vector](/D/rvec).

Thus, we can plug the distribution parameters from \eqref{eq:matns} into the KL divergence in \eqref{eq:mvn-KL} using the relationship given by \eqref{eq:matn-mvn}

$$ \label{eq:matn-KL-s1}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \frac{1}{2} \left[ (\mathrm{vec}(M_2) - \mathrm{vec}(M_1))^T (V_2 \otimes U_2)^{-1} (\mathrm{vec}(M_2) - \mathrm{vec}(M_1)) \right. \\
&+ \left. \mathrm{tr}\left( (V_2 \otimes U_2)^{-1} (V_1 \otimes U_1) \right) - \ln \frac{|V_1 \otimes U_1|}{|V_2 \otimes U_2|} - n p \right] \; .
\end{split}
$$

Using the vectorization operator and Kronecker product properties

$$ \label{eq:vec-add}
\mathrm{vec}(A) + \mathrm{vec}(B) = \mathrm{vec}(A+B)
$$

$$ \label{eq:kron-inv}
(A \otimes B)^{-1} = A^{-1} \otimes B^{-1}
$$

$$ \label{eq:kron-prod}
(A \otimes B) (C \otimes D) = (AC) \otimes (BD)
$$

$$ \label{eq:kron-det}
|A \otimes B| = |A|^m \, |B|^n \quad \text{where} \quad A \in \mathbb{R}^{n \times n} \quad \text{and} \quad B \in \mathbb{R}^{m \times m} \; ,
$$

the Kullback-Leibler divergence from \eqref{eq:matn-KL-s1} becomes:

$$ \label{eq:matn-KL-s2}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \frac{1}{2} \left[ \mathrm{vec}(M_2 - M_1)^\mathrm{T} \, (V_2^{-1} \otimes U_2^{-1}) \, \mathrm{vec}(M_2 - M_1) \right. \\
&+ \left. \mathrm{tr}\left( (V_2^{-1}V_1) \otimes (U_2^{-1}U_1) \right) - n \ln \frac{|V_1|}{|V_2|} - p \ln \frac{|U_1|}{|U_2|} - n p \right] \; .
\end{split}
$$

Using the relationship between Kronecker product and vectorization operator

$$ \label{eq:kron-vec}
(C^\mathrm{T} \otimes A) \, \mathrm{vec}(B) = \mathrm{vec}(ABC) \; ,
$$

we finally have:

$$ \label{eq:matn-KL-s3}
\begin{split}
\mathrm{KL}[P\,||\,Q] &= \frac{1}{2} \left[ \mathrm{vec}(M_2 - M_1)^\mathrm{T} \mathrm{vec}\left(U_2^{-1} (M_2 - M_1) V_2^{-1}\right) \right. \\
&+ \left. \mathrm{tr}\left( (V_2^{-1}V_1) \otimes (U_2^{-1}U_1) \right) - n \ln \frac{|V_1|}{|V_2|} - p \ln \frac{|U_1|}{|U_2|} - n p \right] \; .
\end{split}
$$