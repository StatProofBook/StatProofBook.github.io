---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-07 21:03:00

title: "Marginal distribution of a conditional binomial distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Binomial distribution"
theorem: "Conditional binomial"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Binomial distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-10-07"
    url: "https://en.wikipedia.org/wiki/Binomial_distribution#Conditional_binomials"

proof_id: "P358"
shortcut: "bin-margcond"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be two [random variables](/D/rvar) where $Y$ is [binomially distributed](/D/bin) [conditional on](/D/dist-cond) $X$

$$ \label{eq:Y-X-dist}
Y \vert X \sim \mathrm{Bin}(X, q)
$$

and $X$ also follows a [binomial distribution](/D/bin), but with different [success frequency](/D/bin):

$$ \label{eq:X-dist}
X \sim \mathrm{Bin}(n, p) \; .
$$

Then, the [maginal distribution](/D/dist-marg) of $Y$ unconditional on $X$ is again a [binomial distribution](/D/bin):

$$ \label{eq:Y-dist}
Y \sim \mathrm{Bin}(n, pq) \; .
$$


**Proof:** We are interested in the probability that $Y$ equals a number $m$. According to the [law of marginal probability](/D/prob-marg) or the [law of total probability](/P/prob-tot), this probability can be expressed as:

$$ \label{eq:Y-dist-s1}
\mathrm{Pr}(Y = m) = \sum_{k=0}^{\infty} \mathrm{Pr}(Y = m \vert X = k) \cdot \mathrm{Pr}(X = k) \; .
$$

Since, by definitions \eqref{eq:X-dist} and \eqref{eq:Y-X-dist}, $\mathrm{Pr}(X = k) = 0$ when $k > n$ and $\mathrm{Pr}(Y = m \vert X = k) = 0$ when $k < m$, we have:

$$ \label{eq:Y-dist-s2}
\mathrm{Pr}(Y = m) = \sum_{k=m}^{n} \mathrm{Pr}(Y = m \vert X = k) \cdot \mathrm{Pr}(X = k) \; .
$$

Now we can take the [probability mass function of the binomial distribution](/P/bin-pmf) and plug it in for the terms in the sum of \eqref{eq:Y-dist-s2} to get:

$$ \label{eq:Y-dist-s3}
\mathrm{Pr}(Y = m) = \sum_{k=m}^{n} {k \choose m} \, q^m \, (1-q)^{k-m} \cdot {n \choose k} \, p^k \, (1-p)^{n-k} \; .
$$

Applying the binomial coefficient identity ${n \choose k} {k \choose m} = {n \choose m} {n-m \choose k-m}$ rearranging the terms, we have:

$$ \label{eq:Y-dist-s4}
\mathrm{Pr}(Y = m) = \sum_{k=m}^{n} {n \choose m} \, {n-m \choose k-m} \, p^k \, q^m \, (1-p)^{n-k} \, (1-q)^{k-m} \; .
$$

Now we partition $p^k = p^m \cdot p^{k-m}$ and pull all terms dependent on $k$ out of the sum:

$$ \label{eq:Y-dist-s5}
\begin{split}
\mathrm{Pr}(Y = m) &= {n \choose m} \, p^m \, q^m \sum_{k=m}^{n} {n-m \choose k-m} \, p^{k-m} \, (1-p)^{n-k} \, (1-q)^{k-m} \\
&= {n \choose m} \, (p q)^m \sum_{k=m}^{n} {n-m \choose k-m} \, \left( p (1-q) \right)^{k-m} \, (1-p)^{n-k} \; .
\end{split}
$$

Then we subsititute $i = k - m$, such that $k = i + m$:

$$ \label{eq:Y-dist-s6}
\mathrm{Pr}(Y = m) = {n \choose m} \, (p q)^m \sum_{i=0}^{n-m} {n-m \choose i} \, \left( p - pq \right)^{i} \, (1-p)^{n-m-i} \; .
$$

According to the binomial theorem

$$ \label{eq:bin-th}
(x+y)^n = \sum_{k=0}^{n} {n \choose k} \, x^{n-k} \, y^k \; ,
$$

the sum in equation \eqref{eq:Y-dist-s6} is equal to

$$ \label{eq:Y-dist-sum}
\sum_{i=0}^{n-m} {n-m \choose i} \, \left( p - pq \right)^{i} \, (1-p)^{n-m-i} = \left( (p-pq)+(1-p) \right)^{n-m} \; .
$$

Thus, \eqref{eq:Y-dist-s6} develops into

$$ \label{eq:Y-dist-s7}
\begin{split}
\mathrm{Pr}(Y = m) &= {n \choose m} \, (p q)^m (p - pq + 1 - p)^{n-m} \\
&= {n \choose m} \, (p q)^m (1 - pq)^{n-m}
\end{split}
$$

which is the [probability mass function of the binomial distribution](/P/bin-pmf), such that

$$ \label{eq:Y-dist-qed}
Y \sim \mathrm{Bin}(n, pq) \; .
$$