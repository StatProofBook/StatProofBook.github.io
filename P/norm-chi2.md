---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-05-20 10:18:00

title: "Relationship between normal distribution and chi-squared distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Relationship to chi-squared distribution"

sources:
  - authors: "Glen_b"
    year: 2014
    title: "Why is the sampling distribution of variance a chi-squared distribution?"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2021-05-20"
    url: "https://stats.stackexchange.com/questions/121662/why-is-the-sampling-distribution-of-variance-a-chi-squared-distribution"
  - authors: "Wikipedia"
    year: 2021
    title: "Cochran's theorem"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-05-20"
    url: "https://en.wikipedia.org/wiki/Cochran%27s_theorem#Sample_mean_and_sample_variance"

proof_id: "P233"
shortcut: "norm-chi2"
username: "JoramSoch"
---


**Theorem:** Let $X_1, \ldots, X_n$ be [independent](/D/ind) [random variables](/D/rvar) where each of them is following a [normal distribution](/D/norm) with mean $\mu$ and variance $\sigma^2$:

$$ \label{eq:norm}
X_i \sim \mathcal{N}(\mu, \sigma^2) \quad \text{for} \quad i = 1, \ldots, n \; .
$$

Define the [sample mean](/D/mean-samp)

$$ \label{eq:mean-samp}
\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i
$$

and the [unbiased sample variance](/D/var-samp)

$$ \label{eq:var-samp}
s^2 = \frac{1}{n-1} \sum_{i=1}^{n} \left( X_i - \bar{X} \right)^2 \; .
$$

Then, the [sampling distribution](/D/dist-samp) of the sample variance is given by a [chi-squared distribution](/D/chi2) with $n-1$ degrees of freedom:

$$ \label{eq:norm-chi2}
V = (n-1) \, \frac{s^2}{\sigma^2} \sim \chi^2(n-1) \; .
$$


**Proof:** Consider the [random variable](/D/rvar) $U_i$ defined as

$$ \label{eq:Ui}
U_i = \frac{X_i - \mu}{\sigma}
$$

which [follows a standard normal distribution](/P/norm-snorm)

$$ \label{eq:norm-snorm}
U_i \sim \mathcal{N}(0,1) \; .
$$

Then, the sum of squared random variables $U_i$ can be rewritten as

$$ \label{eq:sum-Ui2-s1}
\begin{split}
\sum_{i=1}^{n} U_i^2 &= \sum_{i=1}^{n} \left( \frac{X_i - \mu}{\sigma} \right)^2 \\
&= \sum_{i=1}^{n} \left( \frac{(X_i - \bar{X}) + (\bar{X} - \mu)}{\sigma} \right)^2 \\
&= \sum_{i=1}^{n} \frac{(X_i - \bar{X})^2}{\sigma^2} + \sum_{i=1}^{n} \frac{(\bar{X} - \mu)^2}{\sigma^2} + \sum_{i=1}^{n} \frac{(X_i - \bar{X})(\bar{X} - \mu)}{\sigma^2} \\
&= \sum_{i=1}^{n} \left( \frac{X_i - \bar{X}}{\sigma^2} \right)^2 + \sum_{i=1}^{n} \left( \frac{\bar{X} - \mu}{\sigma^2} \right)^2 + \frac{(\bar{X} - \mu)}{\sigma^2} \sum_{i=1}^{n} (X_i - \bar{X}) \; .
\end{split}
$$

Because the following sum is zero

$$ \label{eq:Xi-Xb}
\begin{split}
\sum_{i=1}^{n} (X_i - \bar{X}) &= \sum_{i=1}^{n} X_i - n \bar{X} \\
&= \sum_{i=1}^{n} X_i - n \cdot \frac{1}{n} \sum_{i=1}^{n} X_i \\
&= \sum_{i=1}^{n} X_i - \sum_{i=1}^{n} X_i \\
&= 0 \; ,
\end{split}
$$

the third term disappears, i.e.

$$ \label{eq:sum-Ui2-s2}
\sum_{i=1}^{n} U_i^2 = \sum_{i=1}^{n} \left( \frac{X_i - \bar{X}}{\sigma^2} \right)^2 + \sum_{i=1}^{n} \left( \frac{\bar{X} - \mu}{\sigma^2} \right)^2 \; .
$$

[Cochran's theorem](/P/snorm-cochran) states that, if a sum of squared [standard normal](/D/snorm) [random variables](/D/rvar) can be written as a sum of squared forms

$$ \label{eq:cochran-p1}
\begin{split}
\sum_{i=1}^{n} U_i^2 = \sum_{j=1}^{m} Q_j \quad &\text{where} \quad Q_j = \sum_{k=1}^{n} \sum_{l=1}^{n} U_k B^{(j)}_{kl} U_l \\
&\text{with} \quad \sum_{j=1}^{m} B^{(j)} = I_n \\
&\text{and} \quad r_j = \mathrm{rank}(B^{(j)}) \; ,
\end{split}
$$

then the terms $Q_j$ are [independent](/D/ind) and each term $Q_j$ follows a [chi-squared distribution](/D/chi2) with $r_j$ degrees of freedom:

$$ \label{eq:cochran-p2}
Q_j \sim \chi^2(r_j) \; .
$$

We observe that \eqref{eq:sum-Ui2-s2} can be represented as

$$ \label{eq:sum-Ui2-s3}
\begin{split}
\sum_{i=1}^{n} U_i^2 &= \sum_{i=1}^{n} \left( \frac{X_i - \bar{X}}{\sigma^2} \right)^2 + \sum_{i=1}^{n} \left( \frac{\bar{X} - \mu}{\sigma^2} \right)^2 \\
= Q_1 + Q_2 &= \sum_{i=1}^{n} \left( U_i - \frac{1}{n} \sum_{j=1}^n U_j \right)^2 + \frac{1}{n} \left( \sum_{i=1}^{n} U_i \right)^2
\end{split}
$$

where, with the $n \times n$ matrix of ones $J_n$, the matrices $B^{(j)}$ are

$$ \label{eq:sum-Ui2-s3-Bj}
B^{(1)} = I_n - \frac{J_n}{n} \quad \text{and} \quad B^{(2)} = \frac{J_n}{n} \; .
$$

Because all columns of $B^{(2)}$ are identical, it has rank $r_2 = 1$. Because the $n$ columns of $B^{(1)}$ add up to zero, it has rank $r_1 = n-1$. Thus, the conditions of [Cochran's theorem](/P/snorm-cochran) are met and the squared form

$$ \label{eq:Q1}
Q_1 = \sum_{i=1}^{n} \left( \frac{X_i - \bar{X}}{\sigma^2} \right)^2 = (n-1) \, \frac{1}{\sigma^2} \, \frac{1}{n-1} \sum_{i=1}^{n} \left( X_i - \bar{X} \right)^2 = (n-1) \, \frac{s^2}{\sigma^2}
$$

follows a [chi-squared distribution](/D/chi2) with $n-1$ degrees of freedom:

$$ \label{eq:norm-chi2-qed}
(n-1) \, \frac{s^2}{\sigma^2} \sim \chi^2(n-1) \; .
$$
