---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-22 05:28:00

title: "Cumulative distribution function of the beta-binomial distribution"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Beta-binomial distribution"
theorem: "Cumulative distribution function"

sources:

proof_id: "P366"
shortcut: "betabin-cdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [beta-binomial distribution](/D/betabin):

$$ \label{eq:betabin}
X \sim \mathrm{BetBin}(n,\alpha,\beta) \; .
$$

Then, the [cumulative distribution function](/D/cdf) of $X$ is

$$ \label{eq:betabin-cdf}
F_X(x) = \frac{1}{\mathrm{B}(\alpha,\beta)} \cdot \frac{\Gamma(n+1)}{\Gamma(\alpha+\beta+n)} \cdot \sum_{i=0}^{x} \frac{\Gamma(\alpha+i) \cdot \Gamma(\beta+n-i)}{\Gamma(i+1) \cdot \Gamma(n-i+1)}
$$

where $\mathrm{B}(x,y)$ is the beta function and $\Gamma(x)$ is the gamma function.


**Proof:** The [cumulative distribution function](/D/cdf) is defined as

$$ \label{eq:cdf}
F_X(x) = \mathrm{Pr}(X \leq x)
$$

which, for a [discrete random variable](/D/rvar-disc), evaluates to

$$ \label{eq:cdf-disc}
F_X(x) = \sum_{i=-\infty}^{x} f_X(i) \; .
$$

With the [probability mass function of the beta-binomial distribution](/P/betabin-pmf), this becomes

$$ \label{eq:betabin-cdf-s1}
F_X(x) = \sum_{i=0}^{x} {n \choose i} \cdot \frac{\mathrm{B}(\alpha+i,\beta+n-i)}{\mathrm{B}(\alpha,\beta)} \; .
$$

Using the expression of binomial coefficients in terms of factorials

$$ \label{eq:bincoeff-facts}
{n \choose k} = \frac{n!}{k! \, (n-k)!} \; ,
$$

the relationship between factorials and the gamma function

$$ \label{eq:facts-gamfct}
n! = \Gamma(n+1)
$$

and the link between gamma function and beta function

$$ \label{eq:betafct-gamfct}
\mathrm{B}(\alpha,\beta) = \frac{\Gamma(\alpha) \, \Gamma(\beta)}{\Gamma(\alpha+\beta)} \; ,
$$

equation \eqref{eq:betabin-cdf-s1} can be further developped as follows:

$$ \label{eq:betabin-cdf-s2}
\begin{split}
F_X(x) &\overset{\eqref{eq:bincoeff-facts}}{=} \frac{1}{\mathrm{B}(\alpha,\beta)} \cdot \sum_{i=0}^{x} \frac{n!}{i! \, (n-i)!} \cdot \mathrm{B}(\alpha+i,\beta+n-i) \\
&\overset{\eqref{eq:betafct-gamfct}}{=} \frac{1}{\mathrm{B}(\alpha,\beta)} \cdot \sum_{i=0}^{x} \frac{n!}{i! \, (n-i)!} \cdot
\frac{\Gamma(\alpha+i) \cdot \Gamma(\beta+n-i)}{\Gamma(\alpha+\beta+n)} \\
&= \frac{1}{\mathrm{B}(\alpha,\beta)} \cdot \frac{n!}{\Gamma(\alpha+\beta+n)} \cdot \sum_{i=0}^{x}
\frac{\Gamma(\alpha+i) \cdot \Gamma(\beta+n-i)}{i! \, (n-i)!} \\
&\overset{\eqref{eq:facts-gamfct}}{=} \frac{1}{\mathrm{B}(\alpha,\beta)} \cdot \frac{\Gamma(n+1)}{\Gamma(\alpha+\beta+n)} \cdot \sum_{i=0}^{x}
\frac{\Gamma(\alpha+i) \cdot \Gamma(\beta+n-i)}{\Gamma(i+1) \cdot \Gamma(n-i+1)} \; .
\end{split}
$$

This completes the proof.