---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-19 22:00:00

title: "Finite population correction for the variance of a sample mean"
chapter: "General Theorems"
section: "Estimation theory"
topic: "Point estimates"
theorem: "Sample mean moments under sampling without replacement"

sources:
  - authors: "John A. Rice"
    year: 2007
    title: "Simple random sampling"
    in: "Mathematical Statistics and Data Analysis"
    pages: "Third edition, Section 7.3.1, pp. 203-208"

proof_id: "P563"
shortcut: "srs-meanvar"
username: "kjpetrykowski"
---

**Theorem:** Let $y\_1,\ldots,y\_N$ be fixed real values for $N\geq2$ labeled population members. The labels distinguish members even if some values are equal. Define

$$ \label{eq:srs-meanvar-population}
\bar y_N=\frac{1}{N}\sum_{j=1}^N y_j,\qquad
S_N^2=\frac{1}{N-1}\sum_{j=1}^N(y_j-\bar y_N)^2 \; .
$$

Take a simple random sample without replacement of size $1\leq n\leq N$. This means each subset of $n$ labels has probability $1/\binom{N}{n}$. Let $\bar Y\_s$ be the average of its values. Then

$$ \label{eq:srs-meanvar-result}
\mathrm{E}(\bar Y_s)=\bar y_N,\qquad
\mathrm{Var}(\bar Y_s)=\left(1-\frac{n}{N}\right)\frac{S_N^2}{n} \; .
$$



**Proof:** Generate a uniformly random permutation $(J\_1,\ldots,J\_N)$ of all labels and define $Y\_i=y\_{J\_i}$. Any specified subset of $n$ labels occupies the first $n$ positions in $n!(N-n)!$ of the $N!$ permutations, so it has probability $1/\binom Nn$. Thus the first $n$ labels form a simple random sample, and $\bar Y\_s=n^{-1}\sum\_{i=1}^nY\_i$.

Each $J\_i$ is uniform on $\lbrace 1,\ldots,N\rbrace $. Consequently,

$$ \label{eq:srs-meanvar-one-draw}
\mathrm{E}(Y_i)=\bar y_N,\qquad
\mathrm{Var}(Y_i)=\frac{1}{N}\sum_{j=1}^N(y_j-\bar y_N)^2
=\frac{N-1}{N}S_N^2 \; .
$$

For any two different positions $i$ and $\ell$ in the permutation, the ordered pair $(J\_i,J\_{\ell})$ is uniform over the $N(N-1)$ pairs of different labels. Put $z\_j=y\_j-\bar y\_N$, so $\sum\_jz\_j=0$. Then

$$ \label{eq:srs-meanvar-covariance}
\begin{split}
\mathrm{Cov}(Y_i,Y_\ell)
&=\frac{1}{N(N-1)}\sum_{j\neq k}z_jz_k\\
&=\frac{(\sum_jz_j)^2-\sum_jz_j^2}{N(N-1)}\\
&=-\frac{(N-1)S_N^2}{N(N-1)}
=-\frac{S_N^2}{N} \; .
\end{split}
$$

This negative covariance is the effect of sampling without replacement. Linearity gives $\mathrm{E}(\bar Y\_s)=\bar y\_N$. Using the [variance of a sum](/P/var-sum) gives:

$$ \label{eq:srs-meanvar-expand}
\begin{split}
\mathrm{Var}(\bar Y_s)
&=\frac{1}{n^2}
 \left[\sum_{i=1}^n\mathrm{Var}(Y_i)
 +\sum_{i\neq\ell}\mathrm{Cov}(Y_i,Y_\ell)\right]\\
&=\frac{1}{n^2}
 \left[n\frac{N-1}{N}S_N^2-n(n-1)\frac{S_N^2}{N}\right]\\
&=\frac{N-n}{Nn}S_N^2
=\left(1-\frac{n}{N}\right)\frac{S_N^2}{n} \; .
\end{split}
$$

The off-diagonal sum has $n(n-1)$ ordered terms. Counting unordered pairs instead would require multiplying the covariance sum by two. This proves \eqref{eq:srs-meanvar-result}.

For a census, $n=N$, the formula gives zero variance, because the observed mean is always the fixed population mean. For $n=1$, it gives $(N-1)S\_N^2/N$, the variance of one uniform draw. If all population values are equal, $S\_N^2=0$ and every sample mean is constant.

Some books use $\sigma\_N^2=N^{-1}\sum\_j(y\_j-\bar y\_N)^2$. With that convention, the same result is $\mathrm{Var}(\bar Y\_s)=\sigma\_N^2(N-n)/[n(N-1)]$. The conversion is $\sigma\_N^2=(N-1)S\_N^2/N$. The different denominators explain the different-looking correction factors.
