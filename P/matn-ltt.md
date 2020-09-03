---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-03 22:24:00

title: "Linear transformation theorem for the matrix-normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Linear transformation"

sources:

proof_id: "P145"
shortcut: "matn-ltt"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n \times p$ [random matrix](/D/rmat) following a [matrix-normal distribution](/D/matn):

$$ \label{eq:matn}
X \sim \mathcal{MN}(M, U, V) \; .
$$

Then, a linear transformation of $X$ is also matrix-normally distributed

$$ \label{eq:matn-trans}
Y = AXB + C \sim \mathcal{MN}(AMB+C, AUA^\mathrm{T}, B^\mathrm{T}VB)
$$

where $A$ us ab $r \times n$ matrix of full rank $r \leq b$ and $B$ is a $p \times s$ matrix of full rank $s \leq p$ and $C$ is an $r \times s$ matrix.


**Proof:** The [matrix-normal distribution is equivalent to the multivariate normal distribution](/P/matn-mvn),

$$ \label{eq:matn-mvn}
X \sim \mathcal{MN}(M, U, V) \quad \Leftrightarrow \quad \mathrm{vec}(X) \sim \mathcal{N}(\mathrm{vec}(M), V \otimes U) \; ,
$$

and the [linear transformation theorem for the multivariate normal distribution](/P/mvn-ltt) states:

$$ \label{eq:mvn-ltt}
x \sim \mathcal{N}(\mu, \Sigma) \quad \Rightarrow \quad y = Ax + b \sim \mathcal{N}(A\mu + b, A \Sigma A^\mathrm{T}) \; .
$$

The vectorization of $Y = AXB + C$ is

$$ \label{eq:vec-Y-s1}
\begin{split}
\mathrm{vec}(Y) &= \mathrm{vec}(AXB + C) \\
&= \mathrm{vec}(AXB) + \mathrm{vec}(C) \\
&= (B^\mathrm{T} \otimes A)\mathrm{vec}(X) + \mathrm{vec}(C) \; .
\end{split}
$$

Using \eqref{eq:matn-mvn} and \eqref{eq:mvn-ltt}, we have

$$ \label{eq:vec-Y-s2}
\begin{split}
\mathrm{vec}(Y) &\sim \mathcal{N}((B^\mathrm{T} \otimes A) \mathrm{vec}(M) + \mathrm{vec}(C), (B^\mathrm{T} \otimes A) (V \otimes U) (B^\mathrm{T} \otimes A)^\mathrm{T}) \\
&= \mathcal{N}(\mathrm{vec}(AMB) + \mathrm{vec}(C), (B^\mathrm{T}V \otimes AU) (B^\mathrm{T} \otimes A)^\mathrm{T}) \\
&= \mathcal{N}(\mathrm{vec}(AMB + C), B^\mathrm{T}VB \otimes AUA^\mathrm{T}) \; .
\end{split}
$$

Using \eqref{eq:matn-mvn}, we finally have:

$$ \label{eq:matn-ltt-qed}
Y \sim \mathcal{MN}(AMB + C, AUA^\mathrm{T} ,B^\mathrm{T}VB) \; .
$$