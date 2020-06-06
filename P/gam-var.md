---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-19 07:20:00

title: "Variance of the gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Variance"

sources:
  - authors: "Turlapaty, Anish"
    year: 2013
    title: "Gamma random variable: mean & variance"
    in: "YouTube"
    pages: "retrieved on 2020-05-19"
    url: "https://www.youtube.com/watch?v=Sy4wP-Y2dmA"

proof_id: "P109"
shortcut: "gam-var"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [gamma distribution](/D/gam):

$$ \label{eq:gam}
X \sim \mathrm{Gam}(a, b) \; .
$$

Then, the [variance](/D/var) of $X$ is

$$ \label{eq:gam-var}
\mathrm{Var}(X) = \frac{a}{b^2} \; .
$$


**Proof:** The [variance](/D/var) can be expressed [in terms of expected values](/P/var-mean) as

$$ \label{eq:var-mean}
\mathrm{Var}(X) = \mathrm{E}(X^2) - \mathrm{E}(X)^2 \; .
$$

The [expected value of a gamma random variable](/P/gam-mean) is

$$ \label{eq:gam-mean}
\mathrm{E}(X) = \frac{a}{b} \; .
$$

With the [probability density function of the gamma distribution](/P/gam-pdf), the expected value of a squared gamma random variable is

$$ \label{eq:gam-sqr-mean-s1}
\begin{split}
\mathrm{E}(X^2) &= \int_{0}^{\infty} x^2 \cdot \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \, \mathrm{d}x \\
&= \int_{0}^{\infty} \frac{b^a}{\Gamma(a)} x^{(a+2)-1} \exp[-b x] \, \mathrm{d}x \\
&= \int_{0}^{\infty} \frac{1}{b^2} \cdot \frac{b^{a+2}}{\Gamma(a)} x^{(a+2)-1} \exp[-b x] \, \mathrm{d}x \; .
\end{split}
$$

Twice-applying the relation $\Gamma(x+1) = \Gamma(x) \cdot x$, we have

$$ \label{eq:gam-sqr-mean-s2}
\mathrm{E}(X^2) = \int_{0}^{\infty} \frac{a \, (a+1)}{b^2} \cdot \frac{b^{a+2}}{\Gamma(a+2)} x^{(a+2)-1} \exp[-b x] \, \mathrm{d}x
$$

and again using the [density of the gamma distribution](/P/gam-pdf), we get

$$ \label{eq:gam-sqr-mean-s3}
\begin{split}
\mathrm{E}(X^2) &= \frac{a \, (a+1)}{b^2} \int_{0}^{\infty} \mathrm{Gam}(x; a+2, b) \, \mathrm{d}x \\
&= \frac{a^2+a}{b^2} \; .
\end{split}
$$

Plugging \eqref{eq:gam-sqr-mean-s3} and \eqref{eq:gam-mean} into \eqref{eq:var-mean}, the variance of a gamma random variable finally becomes

$$ \label{eq:gam-var-qed}
\begin{split}
\mathrm{Var}(X) &= \frac{a^2+a}{b^2} - \left( \frac{a}{b} \right)^2 \\
&= \frac{a}{b^2} \; .
\end{split}
$$