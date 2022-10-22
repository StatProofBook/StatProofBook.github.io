---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-10-20 08:56:00

title: "Expression of the probability mass function of the beta-binomial distribution using only the gamma function"
chapter: "Probability Distributions"
section: "Univariate discrete distributions"
topic: "Beta-binomial distribution"
theorem: "Probability mass function in terms of gamma function"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Beta-binomial distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-10-20"
    url: "https://en.wikipedia.org/wiki/Beta-binomial_distribution#As_a_compound_distribution"

proof_id: "P365"
shortcut: "betabin-pmfitogf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [beta-binomial distribution](/D/betabin):

$$ \label{eq:betabin}
X \sim \mathrm{BetBin}(n,\alpha,\beta) \; .
$$

Then, the [probability mass function](/D/pmf) of $X$ can be expressed as

$$ \label{eq:betabin-pmfitogf}
f_X(x) = \frac{\Gamma(n+1)}{\Gamma(x+1) \, \Gamma(n-x+1)} \cdot \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \, \Gamma(\beta)} \cdot \frac{\Gamma(\alpha+x) \, \Gamma(\beta+n-x)}{\Gamma(\alpha+\beta+n)}
$$

where $\Gamma(x)$ is the gamma function.


**Proof:** The [probability mass function of the beta-binomial distribution](/P/betabin-pmf) is given by

$$ \label{eq:betabin-pmf}
f_X(x) = {n \choose x} \cdot \frac{\mathrm{B}(\alpha+x,\beta+n-x)}{\mathrm{B}(\alpha,\beta)} \; .
$$

Note that the binomial coefficient can be expressed in terms of factorials

$$ \label{eq:bincoeff-facts}
{n \choose x} = \frac{n!}{x! \, (n-x)!} \; ,
$$

that factorials are related to the gamma function via $n! = \Gamma(n+1)$

$$ \label{eq:facts-gamfct}
\frac{n!}{x! \, (n-x)!} = \frac{\Gamma(n+1)}{\Gamma(x+1) \, \Gamma(n-x+1)}
$$

and that the beta function is related to the gamma function via

$$ \label{eq:betafct-gamfct}
\mathrm{B}(\alpha,\beta) = \frac{\Gamma(\alpha) \, \Gamma(\beta)}{\Gamma(\alpha+\beta)} \; .
$$

Applying \eqref{eq:bincoeff-facts}, \eqref{eq:facts-gamfct} and \eqref{eq:betafct-gamfct} to \eqref{eq:betabin-pmf}, we get

$$ \label{eq:betabin-pmfitogf-qed}
f_X(x) = \frac{\Gamma(n+1)}{\Gamma(x+1) \, \Gamma(n-x+1)} \cdot \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha) \, \Gamma(\beta)} \cdot \frac{\Gamma(\alpha+x) \, \Gamma(\beta+n-x)}{\Gamma(\alpha+\beta+n)} \; .
$$

This completes the proof.