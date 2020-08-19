---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-08-19 06:39:00

title: "Full width at half maximum for the normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Full width at half maximum"

sources:
  - authors: "Wikipedia"
    year: 2020
    title: "Full width at half maximum"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2020-08-19"
    url: "https://en.wikipedia.org/wiki/Full_width_at_half_maximum"

proof_id: "P152"
shortcut: "norm-fwhm"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [normal distribution](/D/norm):

$$ \label{eq:norm}
X \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [full width at half maximum](/D/fwhm) (FWHM) of $X$ is

$$ \label{eq:norm-fwhm}
\mathrm{FWHM}(X) = 2 \sqrt{2 \ln 2} \sigma \; .
$$


**Proof:** The [probability density function of the normal distribution](/P/norm-pdf) is

$$ \label{eq:norm-pdf}
f_X(x) = \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right]
$$

and the [mode of the normal distribution](/P/norm-mode) is

$$ \label{eq:norm-mode}
\mathrm{mode}(X) = \mu \; ,
$$

such that

$$ \label{eq:norm-pdf-max}
f_\mathrm{max} = f_X(\mathrm{mode}(X)) \overset{\eqref{eq:norm-mode}}{=} f_X(\mu) \overset{\eqref{eq:norm-pdf}}{=} \frac{1}{\sqrt{2 \pi} \sigma} \; .
$$

The FWHM bounds [satisfy the equation](/D/fwhm)

$$ \label{eq:x-FHWM}
f_X(x_\mathrm{FWHM}) = \frac{1}{2} f_\mathrm{max} \overset{\eqref{eq:norm-pdf-max}}{=} \frac{1}{2 \sqrt{2 \pi} \sigma} \; .
$$

Using \eqref{eq:norm-pdf}, we can develop this equation as follows:

$$ \label{eq:x-FHWM-s1}
\begin{split}
\frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x_\mathrm{FWHM}-\mu}{\sigma} \right)^2 \right] &= \frac{1}{2 \sqrt{2 \pi} \sigma} \\
\exp \left[ -\frac{1}{2} \left( \frac{x_\mathrm{FWHM}-\mu}{\sigma} \right)^2 \right] &= \frac{1}{2} \\
-\frac{1}{2} \left( \frac{x_\mathrm{FWHM}-\mu}{\sigma} \right)^2 &= \ln \frac{1}{2} \\
\left( \frac{x_\mathrm{FWHM}-\mu}{\sigma} \right)^2 &= -2 \ln \frac{1}{2} \\
\frac{x_\mathrm{FWHM}-\mu}{\sigma} &= \pm \sqrt{2 \ln 2} \\
x_\mathrm{FWHM}-\mu &= \pm \sqrt{2 \ln 2} \sigma \\
x_\mathrm{FWHM} &= \pm \sqrt{2 \ln 2} \sigma + \mu \; .
\end{split}
$$

This implies the following two solutions for $x_\mathrm{FWHM}$

$$ \label{eq:x-FHWM-s2}
\begin{split}
x_1 &= \mu - \sqrt{2 \ln 2} \sigma \\
x_2 &= \mu + \sqrt{2 \ln 2} \sigma \; ,
\end{split}
$$

such that the [full width at half maximum](/D/fwhm) of $X$ is

$$ \label{eq:norm-fwhm-qed}
\begin{split}
\mathrm{FWHM}(X) &= \Delta x = x_2 - x_1 \\
&\overset{\eqref{eq:x-FHWM-s2}}{=} \left( \mu + \sqrt{2 \ln 2} \sigma \right) - \left( \mu - \sqrt{2 \ln 2} \sigma \right) \\
&= 2 \sqrt{2 \ln 2} \sigma \; .
\end{split}
$$