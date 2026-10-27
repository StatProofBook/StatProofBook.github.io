---
layout: proof
mathjax: true

author: "Kenneth Petrykowski"
affiliation: "University of Warsaw"
e_mail: "kenneth.petrykowski@gmail.com"
date: 2026-10-19 22:00:00

title: "Expectation and variance of the sample mean obtained from a finite population"
chapter: "General Theorems"
section: "Estimation theory"
topic: "Point estimates"
theorem: "Finite-population correction for the variance of a sample mean"

sources:
  - authors: "John A. Rice"
    year: 2007
    title: "Simple random sampling"
    in: "Mathematical Statistics and Data Analysis"
    pages: "Third edition, Section 7.3.1, pp. 203-208"

proof_id: "P563"
shortcut: "meansamp-varcorr"
username: "kjpetrykowski"
---


**Theorem:** Let $y_1,\ldots,y_N$ be [fixed real values](/D/data) for $N \geq 2$ labeled population members. The labels distinguish members, even if some values are equal. Define

$$ \label{eq:srs-meanvar-population}
\bar{y}_N = \frac{1}{N} \sum_{j=1}^N y_j, \qquad
S_N^2 = \frac{1}{N-1} \sum_{j=1}^N (y_j-\bar{y}_N)^2 \; .
$$

Take a [simple random sample](/D/samp) without replacement of size $1 \leq n \leq N$, i.e. $s \subset \lbrace 1,\ldots,N \rbrace$ with $\lvert s \rvert = n$. Let $\bar{Y}_s$ be the [sample mean](/D/mean-samp) of the $n$ data points included in this sample. Then,

$$ \label{eq:srs-meanvar-result}
\mathrm{E}(\bar{Y}_s) = \bar{y}_N,\qquad
\mathrm{Var}(\bar{Y}_s) = \left(1-\frac{n}{N}\right)\frac{S_N^2}{n} \; .
$$


**Proof:** Generate a uniformly random permutation $(J_1,\ldots,J_N)$ of all labels and define $Y_i=y_{J_i}$. Any specified subset of $n$ labels occupies the first $n$ positions in $n!(N-n)!$ of the $N!$ permutations, so it has [probability](/D/prob) $1/\binom{N}{n}$. Thus, the first $n$ labels form a [simple random sample](/D/samp), and $\bar{Y}\_s = 1/n \sum\_{i=1}^n Y_i$.

Each $J_i$ [is uniform](/D/duni) on $\lbrace 1,\ldots,N \rbrace$. Consequently,

$$ \label{eq:srs-meanvar-one-draw}
\mathrm{E}(Y_i) = \bar{y}_N, \qquad
\mathrm{Var}(Y_i) = \frac{1}{N} \sum_{j=1}^N (y_j-\bar{y}_N)^2 =\frac{N-1}{N}S_N^2 \; .
$$

For any two different positions $i$ and $\ell$ in the permutation, the ordered pair $(J_i,J_{\ell})$ [is uniform](/D/duni) over the $N(N-1)$ pairs of different labels. Put $z_j=y_j-\bar{y}_N$, so $\sum_j z_j=0$. Then,

$$ \label{eq:srs-meanvar-covariance}
\begin{split}
   \mathrm{Cov}(Y_i,Y_\ell)
&= \frac{1}{N(N-1)}\sum_{j\neq k}z_jz_k\\
&= \frac{(\sum_jz_j)^2-\sum_jz_j^2}{N(N-1)}\\
&=-\frac{(N-1)S_N^2}{N(N-1)}
 =-\frac{S_N^2}{N} \; .
\end{split}
$$

This negative [covariance](/D/cov) is the effect of sampling without replacement. Using the [linearity of the expected value](/P/mean-lin) gives $\mathrm{E}(\bar{Y}_s)=\bar{y}_N$. Using the [variance of a sum](/P/var-sum) gives:

$$ \label{eq:srs-meanvar-expand}
\begin{split}
   \mathrm{Var}(\bar{Y}_s)
&= \frac{1}{n^2} \left[\sum_{i=1}^n \mathrm{Var}(Y_i) + \sum_{i\neq\ell} \mathrm{Cov}(Y_i,Y_\ell) \right] \\
&= \frac{1}{n^2} \left[n \frac{N-1}{N} S_N^2 - n(n-1) \frac{S_N^2}{N} \right] \\
&= \frac{N-n}{Nn} S_N^2
 = \left(1-\frac{n}{N}\right) \frac{S_N^2}{n} \; .
\end{split}
$$

The off-diagonal sum has $n(n-1)$ ordered terms. Counting unordered pairs instead would require multiplying the covariance sum by two. This proves \eqref{eq:srs-meanvar-result}.

For a census with $n=N$, the formula gives zero variance, because the [observed mean](/D/mean-samp) is always the fixed [population mean](/D/mean). For $n=1$, it gives $(N-1)S_N^2/N$, the [variance](/D/var) of one uniform draw. If all population values are equal, $S_N^2=0$ and every [sample mean is constant](/P/var-const).