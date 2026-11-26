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

**Theorem:** Let $y\_1,\ldots,y\_N$ be fixed real values attached to $N\geq2$ distinct population labels. Define the population mean and variance by

$$ \label{eq:srs-meanvar-population}
\bar y_N=\frac{1}{N}\sum_{j=1}^N y_j,\qquad
S_N^2=\frac{1}{N-1}\sum_{j=1}^N(y_j-\bar y_N)^2 \; .
$$

Draw a [simple random sample without replacement](/D/samp-srs) of $n$ labels, where $1\leq n\leq N$. Thus every subset of $n$ labels has the same probability. Let $S$ be the random selected subset, and define its [sample mean](/D/mean-samp) by

$$ \label{eq:sample-mean}
\bar Y_S=\frac{1}{n}\sum_{j\in S}y_j \; .
$$

Then

$$ \label{eq:srs-meanvar-result}
\mathrm{E}(\bar Y_S)=\bar y_N,\qquad
\mathrm{Var}(\bar Y_S)=\left(1-\frac{n}{N}\right)\frac{S_N^2}{n} \; .
$$


**Proof:** The population values are fixed; only the selected labels are random. Different labels can have the same value. Generate a uniformly random permutation $(J\_1,\ldots,J\_N)$ of the labels and select its first $n$ positions.

For any specified subset $s$ of $n$ labels, its members can occupy the first $n$ positions in $n!$ orders. The remaining labels can occupy the other positions in $(N-n)!$ orders. Hence

$$ \label{eq:subset-probability}
\mathrm{Pr}(S=s)
=\frac{n!(N-n)!}{N!}
=\frac{1}{\binom{N}{n}} \; .
$$

This produces the required sampling design. Put $Y\_i=y\_{J\_i}$, so

$$ \label{eq:ordered-sample-mean}
\bar Y_S=\frac{1}{n}\sum_{i=1}^nY_i \; .
$$

At each position, every label has probability $1/N$. Thus

$$ \label{eq:srs-meanvar-one-draw}
\begin{split}
\mathrm{E}(Y_i)&=\frac{1}{N}\sum_{j=1}^Ny_j=\bar y_N,\\
\mathrm{Var}(Y_i)&=\frac{1}{N}\sum_{j=1}^N(y_j-\bar y_N)^2
=\frac{N-1}{N}S_N^2 \; .
\end{split}
$$

For two different positions $i,\ell$, the first label is uniform over $N$ labels. Given that label, the second is uniform over the remaining $N-1$. Each ordered pair of distinct labels therefore has probability $(1/N)[1/(N-1)]$. Write $z\_j=y\_j-\bar y\_N$. Since the deviations from the population mean sum to zero,

$$ \label{eq:deviations}
\sum_{j=1}^Nz_j=0,\qquad
\sum_{j=1}^Nz_j^2=(N-1)S_N^2 \; .
$$

The [covariance](/D/cov) of the two draws is therefore

$$ \label{eq:srs-meanvar-covariance}
\begin{split}
\mathrm{Cov}(Y_i,Y_\ell)
&=\frac{1}{N(N-1)}\sum_{j\ne k}z_jz_k\\
&=\frac{(\sum_jz_j)^2-\sum_jz_j^2}{N(N-1)}\\
&=-\frac{(N-1)S_N^2}{N(N-1)}
=-\frac{S_N^2}{N} \; .
\end{split}
$$

In the second line we expanded the square of $\sum\_jz\_j$ and removed the diagonal terms $z\_j^2$. The covariance is nonpositive, and it is strictly negative unless all population values are equal.

[Linearity of expectation](/P/mean-lin) gives the sample-mean expectation:

$$ \label{eq:sample-mean-expectation}
\mathrm{E}(\bar Y_S)=\frac{1}{n}\sum_{i=1}^n\mathrm{E}(Y_i)
=\frac{n\bar y_N}{n}=\bar y_N \; .
$$

For the variance, apply the [two-variable variance-of-a-sum identity](/P/var-sum) repeatedly. There are $n$ variance terms and $n(n-1)$ ordered covariance terms:

$$ \label{eq:srs-meanvar-expand}
\begin{split}
\mathrm{Var}(\bar Y_S)
&=\frac{1}{n^2}\left[
  \sum_{i=1}^n\mathrm{Var}(Y_i)
 +\sum_{i\ne\ell}\mathrm{Cov}(Y_i,Y_\ell)\right]\\
&=\frac{1}{n^2}\left[
 n\frac{N-1}{N}S_N^2-n(n-1)\frac{S_N^2}{N}\right]\\
&=\frac{N-n}{Nn}S_N^2
=\left(1-\frac{n}{N}\right)\frac{S_N^2}{n} \; .
\end{split}
$$

For $n=N$, the sample contains the entire population and the variance is zero. For $n=1$, there are no covariance terms, and the formula gives the variance of one draw. The denominator in the definition of $S\_N^2$ is $N-1$; the stated correction uses that convention.
