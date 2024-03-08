---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-02-23 14:31:54

title: "Moment-generating function of the gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Moment-generating function"

sources:

proof_id: "P437"
shortcut: "gam-mgf"
username: "JoramSoch"
---


**Theorem:** Let $X$ follow a [gamma distribution](/D/gam):

$$ \label{eq:gam}
X \sim \mathrm{Gam}(a, b) \; .
$$

Then, the [moment-generating function](/D/mgf) of $X$ is

$$ \label{eq:gam-mgf}
M_X(t) = \left( 1 - \frac{t}{b} \right)^{-a} \; .
$$


**Proof:** The [moment-generating function of a random variable](/D/mgf) $X$ is defined as:

$$ \label{eq:mgf}
M_X(t) = \mathrm{E} \left[ e^{tX} \right], \quad t \in \mathbb{R} \; .
$$

Applying the [law of the unconscious statistician](/P/mean-lotus), we have:

$$ \label{eq:gam-mgf-s1}
M_X(t) = \int_{\mathcal{X}} e^{tx} \cdot f_X(x) \, \mathrm{d}x \; .
$$

With the [probability density function of the gamma distribution](/P/gam-pdf), we have:

$$ \label{eq:gam-mgf-s2}
M_X(t) = \int_{\mathbb{R}} \exp[t x] \cdot \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \, \mathrm{d}x \; .
$$

Now we summarize the two exponential functions inside the integral:

$$ \label{eq:gam-mgf-s3}
\begin{split}
M_X(t) &= \int_{\mathbb{R}} \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-(b-t) x] \, \mathrm{d}x \\
&= \int_{\mathbb{R}} \frac{(b-t)^a}{(b-t)^a} \cdot \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-(b-t) x] \, \mathrm{d}x \\
&= \int_{\mathbb{R}} \frac{b^a}{(b-t)^a} \cdot \frac{(b-t)^a}{\Gamma(a)} x^{a-1} \exp[-(b-t) x] \, \mathrm{d}x \\
&= \left( \frac{b}{b-t} \right)^a \int_{\mathbb{R}} \frac{(b-t)^a}{\Gamma(a)} x^{a-1} \exp[-(b-t) x] \, \mathrm{d}x \; .
\end{split}
$$

The integrand is equal to the [probability density function of a gamma distribution](/P/gam-pdf):

$$ \label{eq:gam-mgf-s4}
M_X(t) = \left( \frac{b}{b-t} \right)^a \int_{\mathbb{R}} \mathrm{Gam}(x; a, b-t) \, \mathrm{d}x \; .
$$

Because [the entire probability density integrates to one](/D/pdf), we finally have:

$$ \label{eq:gam-mgf-s5}
M_X(t) = \left( \frac{b}{b-t} \right)^a = \left( \frac{b-t}{b} \right)^{-a} = \left( \frac{b}{b} - \frac{t}{b} \right)^{-a} = \left( 1 - \frac{t}{b} \right)^{-a} \; .
$$