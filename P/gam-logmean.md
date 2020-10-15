---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-05-25 21:28:00

title: "Logarithmic expectation of the gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Logarithmic expectation"

sources:
  - authors: "whuber"
    year: 2018
    title: "What is the expected value of the logarithm of Gamma distribution?"
    in: "StackExchange CrossValidated"
    pages: "retrieved on 2020-05-25"
    url: "https://stats.stackexchange.com/questions/370880/what-is-the-expected-value-of-the-logarithm-of-gamma-distribution"

proof_id: "P110"
shortcut: "gam-logmean"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [gamma distribution](/D/gam):

$$ \label{eq:gam}
X \sim \mathrm{Gam}(a, b) \; .
$$

Then, the [expectation](/D/mean) of the natural logarithm of $X$ is

$$ \label{eq:gam-logmean}
\mathrm{E}(\ln X) = \psi(a) - \ln(b)
$$

where $\psi(x)$ is the digamma function.


**Proof:** Let $Y = \ln(X)$, such that $\mathrm{E}(Y) = \mathrm{E}(\ln X)$ and consider the special case that $b = 1$. In this case, the [probability density function of the gamma distribution](/P/gam-pdf) is

$$ \label{eq:X-pdf-s1}
f_X(x) = \frac{1}{\Gamma(a)} \, x^{a-1} \, \mathrm{exp} [-x] \; .
$$

Multiplying this function with $\mathrm{d}x$, we obtain

$$ \label{eq:X-pdf-s2}
f_X(x) \, \mathrm{d}x = \frac{1}{\Gamma(a)} \, x^a \, \mathrm{exp} [-x] \, \frac{\mathrm{d}x}{x} \; .
$$

Substituting $y = \ln x$, i.e. $x = e^y$, such that $\mathrm{d}x/\mathrm{d}y = x$, i.e. $\mathrm{d}x/x = \mathrm{d}y$, we get

$$ \label{eq:Y-pdf-s1}
\begin{split}
f_Y(y) \, \mathrm{d}y &= \frac{1}{\Gamma(a)} \, \left( e^y \right)^a \, \mathrm{exp} [-e^y] \, \mathrm{d}y \\
&= \frac{1}{\Gamma(a)} \, \mathrm{exp}\left[ ay - e^y \right] \, \mathrm{d}y \; .
\end{split}
$$

Because $f_Y(y)$ integrates to one, we have

$$ \label{eq:Y-pdf-s2}
\begin{split}
1 &= \int_{\mathbb{R}} f_Y(y) \, \mathrm{d}y \\
1 &= \int_{\mathbb{R}} \frac{1}{\Gamma(a)} \, \mathrm{exp}\left[ ay - e^y \right] \, \mathrm{d}y \\
\Gamma(a) &= \int_{\mathbb{R}} \mathrm{exp}\left[ ay - e^y \right] \, \mathrm{d}y \; .
\end{split}
$$

Note that the integrand in \eqref{eq:Y-pdf-s2} is differentiable with respect to $a$:

$$ \label{eq:dfy-da}
\begin{split}
\frac{\mathrm{d}}{\mathrm{d}a} \mathrm{exp}\left[ ay - e^y \right] \, \mathrm{d}y &= y \, \mathrm{exp}\left[ ay - e^y \right] \, \mathrm{d}y \\
&\overset{\eqref{eq:Y-pdf-s1}}{=} \Gamma(a) \, y \, f_Y(y) \, \mathrm{d}y \; .
\end{split}
$$

Now we can calculate the expected value of $Y = \ln(X)$:

$$ \label{eq:E-Y-s1}
\begin{split}
\mathrm{E}(Y) &= \int_{\mathbb{R}} y \, f_Y(y) \, \mathrm{d}y \\
&\overset{\eqref{eq:dfy-da}}{=} \frac{1}{\Gamma(a)} \int_{\mathbb{R}} \frac{\mathrm{d}}{\mathrm{d}a} \mathrm{exp}\left[ ay - e^y \right] \, \mathrm{d}y \\
&= \frac{1}{\Gamma(a)} \frac{\mathrm{d}}{\mathrm{d}a} \int_{\mathbb{R}} \mathrm{exp}\left[ ay - e^y \right] \, \mathrm{d}y \\
&\overset{\eqref{eq:Y-pdf-s2}}{=} \frac{1}{\Gamma(a)} \frac{\mathrm{d}}{\mathrm{d}a} \Gamma(a) \\
&= \frac{\Gamma'(a)}{\Gamma(a)} \; .
\end{split}
$$

Using the derivative of a logarithmized function

$$ \label{eq:log-der}
\frac{\mathrm{d}}{\mathrm{d}x} \ln f(x) = \frac{f'(x)}{f(x)}
$$

and the definition of the digamma function

$$ \label{eq:psi}
\psi(x) = \frac{\mathrm{d}}{\mathrm{d}x} \ln \Gamma(x) \; ,
$$

we have

$$ \label{eq:E-Y-s2}
\mathrm{E}(Y) = \psi(a) \; .
$$

Finally, noting that $1/b$ [acts as a scaling parameter](/P/gam-sgam) on a [gamma-distributed](/D/gam) [random variable](/D/rvar),

$$ \label{eq:gam-sgam}
X \sim \mathrm{Gam}(a,1) \quad \Rightarrow \quad \frac{1}{b} X \sim \mathrm{Gam}(a,b) \; ,
$$

and that a scaling parameter acts additively on the logarithmic expectation of a random variable,

$$ \label{eq:logmean}
\mathrm{E}\left[\ln(cX)\right] = \mathrm{E}\left[\ln(X) + \ln(c)\right] = \mathrm{E}\left[\ln(X)\right] + \ln(c) \; ,
$$

it follows that

$$ \label{eq:E-Y-s3}
X \sim \mathrm{Gam}(a,b) \quad \Rightarrow \quad \mathrm{E}(\ln X) = \psi(a) - \ln(b) \; .
$$