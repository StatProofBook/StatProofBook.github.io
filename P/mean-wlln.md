---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-09-13 11:02:05

title: "Weak law of large numbers"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Weak law of large numbers"

sources:
  - authors: "Ostwald, Dirk"
    year: 2023
    title: "Ungleichungen und Grenzwerte"
    in: "Wahrscheinlichkeitstheorie und Frequentistische Inferenz"
    pages: "Einheit (6), Folie 19-20"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Wintersemester+2324/Wahrscheinlichkeitstheorie+und+Frequentistische+Inferenz/6_Ungleichungen_und_Grenzwerte.pdf"
  - authors: "Wikipedia"
    year: 2024
    title: "Law of large numbers"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-09-13"
    url: "https://en.wikipedia.org/wiki/Law_of_large_numbers#Proof_of_the_weak_law"

proof_id: "P468"
shortcut: "mean-wlln"
username: "JoramSoch"
---


**Theorem:** Let $X_1, \ldots, X_n$ be [independent and identically distributed](/D/iid) [random variables](/D/rvar) with [expected value](/D/mean) $\mathrm{E}(X_i) = \mu$ and finite [variance](/D/var) $\mathrm{Var}(X_i) < \infty$ for $i = 1,\ldots,n$. The [sample mean](/D/mean-samp) is defined as

$$ \label{eq:mean-samp}
\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i \; .
$$

Then, for any positive number $\epsilon > 0$, the probability that the absolute difference of the [sample mean](/D/mean-samp) from the [expected value](/D/mean) $\mu$ is smaller than $\epsilon$ will approach one, as [sample size](/D/samp-size) goes to infinity:

$$ \label{eq:mean-wlln}
\lim_{n \rightarrow \infty} \mathrm{Pr}\left( \left| \bar{X} - \mu \right| < \epsilon \right) = 1 \; .
$$


**Proof:** Since $X_1, \ldots, X_n$ are [independent and identically distributed](/D/iid), they have the same mean, denoted as $\mu$, and the same variance, denoted as $\sigma^2$. Using the [linearity of the expected value](/P/mean-lin), the expected value of the sample mean becomes:

$$ \label{eq:mean-samp-mean}
\begin{split}
\mathrm{E}\left( \bar{X} \right)
&= \mathrm{E}\left( \frac{1}{n} \sum_{i=1}^{n} X_i \right) \\
&= \frac{1}{n} \sum_{i=1}^{n} \mathrm{E}\left( X_i \right) \\
&= \frac{1}{n} n \mathrm{E}\left( X_i \right) \\
&= \mu \; .
\end{split}
$$

Moreover, with the [scaling of the variance upon multiplication](/P/var-scal) and the [additivity of the variance under independence](/P/var-add), the variance of the sample mean becomes:

$$ \label{eq:mean-samp-var}
\begin{split}
\mathrm{Var}\left( \bar{X} \right)
&= \mathrm{Var}\left( \frac{1}{n} \sum_{i=1}^{n} X_i \right) \\
&= \frac{1}{n^2} \mathrm{Var}\left( \sum_{i=1}^{n} X_i \right) \\
&= \frac{1}{n^2} \sum_{i=1}^{n} \mathrm{Var}\left( X_i \right) \\
&= \frac{1}{n^2} n \sigma^2 \\
&= \frac{\sigma^2}{n} \; .
\end{split}
$$

[Chebyshev's inequality](/P/cheb-ineq) makes a statement about a random variable $X$ in relation to its mean and variance for any positive number $x > 0$:

$$ \label{eq:cheb-ineq}
\mathrm{Pr}\left( \left| X - \mathrm{E}(\bar{X}) \right| \geq x \right) \le \frac{\mathrm{Var}(X)}{x^2} \; .
$$

Applying this inequality to the [random variable](/D/rvar) $\bar{X}$, we have:

$$ \label{eq:mean-wlln-s1}
\begin{split}
\mathrm{Pr}\left( \left| \bar{X} - \mathrm{E}(\bar{X}) \right| \geq x \right) &\le \frac{\mathrm{Var}(\bar{X})}{x^2} \\
\mathrm{Pr}\left( \left| \bar{X} - \mu \right| \geq \epsilon \right) &le \frac{\sigma^2}{n \epsilon} \; .
\end{split}
$$

Since [the cumulative distribution function can be used to relate probabilities of inverse events](/P/cdf-probexc), i.e. $\mathrm{Pr}\left( X \geq x \right) = 1 - \mathrm{Pr}\left( X < x \right)$, we have:

$$ \label{eq:mean-wlln-s2}
\begin{split}
1 - \mathrm{Pr}\left( \left| \bar{X} - \mu \right| < \epsilon \right) &\le \frac{\sigma^2}{n \epsilon} \\
\mathrm{Pr}\left( \left| \bar{X} - \mu \right| < \epsilon \right) &\ge 1 - \frac{\sigma^2}{n \epsilon} \; .
\end{split}
$$

Now taking the limit for $n \rightarrow \infty$ on both sides, while considering that $\epsilon$ and $\sigma^2$ are finite, gives:

$$ \label{eq:mean-wlln-s3}
\begin{split}
\lim_{n \rightarrow \infty} \mathrm{Pr}\left( \left| \bar{X} - \mu \right| < \epsilon \right)
&\ge \lim_{n \rightarrow \infty} \left( 1 - \frac{\sigma^2}{n \epsilon} \right) \\
&\ge 1 - \lim_{n \rightarrow \infty} \frac{\sigma^2 / \epsilon}{n} \\
&\ge 1 \; .
\end{split}
$$
