---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-15 11:41:00

title: "Marginal distributions for the matrix-normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Marginal distributions"

sources:

proof_id: "P343"
shortcut: "matn-marg"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n \times p$ [random matrix](/D/rmat) following a [matrix-normal distribution](/D/matn):

$$ \label{eq:matn}
X \sim \mathcal{MN}(M, U, V) \; .
$$

Then,

1) the [marginal distribution](/D/dist-marg) of any subset matrix $X_{I,J}$, obtained by dropping some rows and/or columns from $X$, is also a [matrix-normal distribution](/D/matn)

$$ \label{eq:matn-marg-subs}
X_{I,J} \sim \mathcal{MN}(M_{I,J}, U_{I,I}, V_{J,J})
$$

where $I \subseteq \left\lbrace 1, \ldots, n \right\rbrace$ is an (ordered) subset of all row indices and $J \subseteq \left\lbrace 1, \ldots, p \right\rbrace$ is an (ordered) subset of all column indices, such that $M_{I,J}$ is the matrix dropping the irrelevant rows and columns (the ones not in the subset, i.e. marginalized out) from the mean matrix $M$; $U_{I,I}$ is the matrix dropping rows not in $I$ from $U$; and $V_{J,J}$ is the matrix dropping columns not in $J$ from $V$;

2) the [marginal distribution](/D/dist-marg) of each row vector is a [multivariate normal distribution](/D/mvn)

$$ \label{eq:matn-marg-row}
x_{i,\bullet}^\mathrm{T} \sim \mathcal{N}(m_{i,\bullet}^\mathrm{T}, u_{ii} V)
$$

where $m_{i,\bullet}$ is the $i$-th row of $M$ and $u_{ii}$ is the $i$-th diagonal entry of $U$;

3) the [marginal distribution](/D/dist-marg) of each column vector is a [multivariate normal distribution](/D/mvn)

$$ \label{eq:matn-marg-col}
x_{\bullet,j} \sim \mathcal{N}(m_{\bullet,j}, v_{jj} U)
$$

where $m_{\bullet,j}$ is the $j$-th column of $M$ and $v_{jj}$ is the $j$-th diagonal entry of $V$; and

4) the [marginal distribution](/D/dist-marg) of one element of $X$ is a [univariate normal distribution](/D/norm)

$$ \label{eq:matn-marg-elem}
x_{ij} \sim \mathcal{N}(m_{ij}, u_{ii} v_{jj})
$$

where $m_{ij}$ is the $(i,j)$-th entry of $M$.


**Proof:**

1) Define a selector matrix $A$, such that $a_{ij} = 1$, if the $i$-th row in the subset matrix should be the $j$-th row from the original matrix (and $a_{ij} = 0$ otherwise)

$$ \label{eq:A}
A \in \mathbb{R}^{\lvert I \rvert \times n}, \quad \text{s.t.} \quad a_{ij} = \left\{
\begin{array}{rl}
1 \; , & \text{if} \; I_i = j \\
0 \; , & \text{otherwise}
\end{array}
\right.
$$

and define a selector matrix $B$, such that $b_{ij} = 1$, if the $j$-th column in the subset matrix should be the $i$-th column from the original matrix (and $b_{ij} = 0$ otherwise)

$$ \label{eq:B}
B \in \mathbb{R}^{p \times \lvert J \rvert}, \quad \text{s.t.} \quad b_{ij} = \left\{
\begin{array}{rl}
1 \; , & \text{if} \; J_j = i \\
0 \; , & \text{otherwise} \; .
\end{array}
\right.
$$

Then, $X_{I,J}$ can be expressed as

$$ \label{eq:XIJ}
X_{I,J} = A X B
$$

and we can apply the [linear transformation theorem](/P/matn-ltt) to give

$$ \label{eq:XIJ-marg}
X_{I,J} \sim \mathcal{MN}(A M B, A U A^\mathrm{T}, B^\mathrm{T} V B) \; .
$$

Finally, we see that $A M B = M_{I,J}$, $A U A^\mathrm{T} = U_{I,I}$ and $B^\mathrm{T} V B = V_{J,J}$.

2) This is a special case of 1). Setting $A$ to the $i$-th elementary row vector in $n$ dimensions and $B$ to the $p \times p$ identity matrix

$$ \label{eq:AB-row}
A = e_i, \; B = I_p \; ,
$$

the $i$-th row of $X$ can be expressed as

$$ \label{eq:xi-marg}
\begin{split}
x_{i,\bullet} &= AXB = e_i X I_p = e_i X \\
&\overset{\eqref{eq:XIJ-marg}}{\sim} \mathcal{MN}(m_{i,\bullet}, u_{ii}, V) \; .
\end{split}
$$

Thus, the [transpose of the row vector is distributed as](/P/matn-trans)

$$ \label{eq:xi-marg-trans}
x_{i,\bullet}^\mathrm{T} \sim \mathcal{MN}(m_{i,\bullet}^\mathrm{T}, V, u_{ii})
$$

which [is equivalent to a multivariate normal distribution](/P/matn-mvn):

$$ \label{eq:xi-marg-trans-mvn}
x_{i,\bullet}^\mathrm{T} \sim \mathcal{N}(m_{i,\bullet}^\mathrm{T}, u_{ii} V) \; .
$$

3) This is a special case of 1). Setting $A$ to the $n \times n$ identity matrix and $B$ to the $j$-th elementary row vector in $p$ dimensions

$$ \label{eq:AB-col}
A = I_n, \; B = e_j^\mathrm{T} \; ,
$$

the $j$-th column of $X$ can be expressed as

$$ \label{eq:xj-marg}
\begin{split}
x_{\bullet,j} &= AXB = I_n X e_j^\mathrm{T} = X e_j^\mathrm{T} \\
&\overset{\eqref{eq:XIJ-marg}}{\sim} \mathcal{MN}(m_{\bullet,j}, U, v_{jj})
\end{split}
$$

which [is equivalent to a multivariate normal distribution](/P/matn-mvn):

$$ \label{eq:xj-marg-mvn}
x_{\bullet,j} \sim \mathcal{N}(m_{\bullet,j}, v_{jj} U) \; .
$$

4) This is a special case of 2) and 3). Setting $A$ to the $i$-th elementary row vector in $n$ dimensions and $B$ to the $j$-th elementary row vector in $p$ dimensions

$$ \label{eq:AB-elem}
A = e_i, \; B = e_j^\mathrm{T} \; ,
$$

the $(i,j)$-th entry of $X$ can be expressed as

$$ \label{eq:xij-marg}
\begin{split}
x_{ij} &= AXB = e_i X e_j^\mathrm{T} \\
&\overset{\eqref{eq:XIJ-marg}}{\sim} \mathcal{MN}(m_{ij}, u_{ii}, v_{jj}) \; .
\end{split}
$$

As $x_{ij}$ is a scalar, this is equivalent to [a univariate normal distribution](/D/norm) as [a special case](/P/norm-mvn) of [the matrix-normal distribution](/P/mvn-matn):

$$ \label{eq:xij-marg-norm}
x_{ij} \sim \mathcal{N}(m_{ij}, u_{ii} v_{jj}) \; .
$$