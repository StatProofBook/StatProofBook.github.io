---
layout: proof
mathjax: true

author: "Maja Pavlovic"
affiliation: ""
e_mail: "mpavlovic@uw.co.uk"
date: 2022-02-13 10:15:00

title: "Mode of the log-normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Log-normal distribution"
theorem: "Mode"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Log-normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-02-12"
    url: "https://en.wikipedia.org/wiki/Log-normal_distribution#Mode"
  - authors: "Mdoc"
    year: 2015
    title: "Mode of lognormal distribution"
    in: "Mathematics Stack Exchange"
    pages: "retrieved on 2022-02-12"
    url: "https://math.stackexchange.com/questions/1321221/mode-of-lognormal-distribution/1321626"

proof_id: "P311"
shortcut: "lognorm-mode"
username: "majapavlo"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [log-normal distribution](/D/lognorm):

$$ \label{eq:lognorm}
X \sim \ln \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [mode](/D/mode) of $X$ is

$$ \label{eq:lognorm-mode}
\mathrm{mode}(X) = e^\left( \mu -\sigma^2 \right) \; .
$$

**Proof:** The [mode](/D/mode) is the value which maximizes the [probability density function](/D/pdf):

$$ \label{eq:mode}
\mathrm{mode}(X) = \operatorname*{arg\,max}_x f_X(x) \; .
$$

The [probability density function of the log-normal distribution](/P/lognorm-pdf) is:

$$ \label{eq:lognorm-pdf}
f_X(x) = \frac{1}{x \sigma \sqrt{2 \pi}} \cdot \mathrm{exp} \left[ -\frac{\left( \ln x -\mu \right)^2}{2 \sigma^2} \right] \; .
$$

The first two derivatives of this function are:

$$ \label{eq:lognorm-pdf-der1}
f'_X(x) = -\frac{1}{x^2 \sigma \sqrt{2 \pi}} \cdot \mathrm{exp} \left[ -\frac{\left( \ln x -\mu \right)^2}{2 \sigma^2} \right] \cdot \left(1 + \frac{\ln x -\mu}{\sigma^2} \right)
$$

$$ \label{eq:lognorm-pdf-der2}
\begin{split}
f''_X(x) &= \frac{1}{\sqrt{2\pi}\sigma^2x^3} \mathrm{exp} \left[ -\frac{\left( \ln x -\mu \right)^2}{2 \sigma^2} \right] \cdot \left( \ln x -\mu \right) \cdot \left(1 + \frac{ \ln x -\mu}{\sigma^2}\right) \\
&+ \frac{\sqrt{2}}{\sqrt{\pi}x^3}\mathrm{exp} \left[ -\frac{\left( \ln x -\mu \right)^2}{2 \sigma^2} \right] \cdot \left(1 + \frac{ \ln x -\mu}{\sigma^2}\right) \\
&- \frac{1}{\sqrt{2\pi}\sigma^2x^3} \mathrm{exp} \left[ -\frac{\left( \ln x -\mu \right)^2}{2 \sigma^2} \right] \; .
\end{split}
$$

We now calculate the root of the first derivative \eqref{eq:lognorm-pdf-der1}:

$$ \label{eq:lognorm-mode-s1}
\begin{split}
f'_X(x) = 0 &= -\frac{1}{x^2 \sigma \sqrt{2 \pi}} \cdot \mathrm{exp} \left[ -\frac{\left( \ln x -\mu \right)^2}{2 \sigma^2} \right] \cdot \left(1 + \frac{\ln x -\mu}{\sigma^2} \right) \\
-1 &= \frac{\ln x -\mu}{\sigma^2} \\
x &= e^\left( \mu -\sigma^2 \right) \; .
\end{split}
$$

By plugging this value into the second derivative \eqref{eq:lognorm-pdf-der2},

$$ \label{eq:lognorm-mode-s2}
\begin{split}
f''_X(e^{(\mu-\sigma^2)}) &= \frac{1}{\sqrt{2\pi}\sigma^2(e^{(\mu-\sigma^2)})^3} \mathrm{exp} \left[ -\frac{\sigma^2}{2} \right] \cdot \left( \sigma^2 \right) \cdot \left(0\right) \\
&+ \frac{\sqrt{2}}{\sqrt{\pi}(e^{(\mu-\sigma^2)})^3} \mathrm{exp} \left[ -\frac{\sigma^2}{2} \right] \cdot \left(0 \right) \\
&- \frac{1}{\sqrt{2\pi}\sigma^2(e^{(\mu-\sigma^2)})^3} \mathrm{exp} \left[ -\frac{\sigma^2}{2} \right] \\
&= - \frac{1}{\sqrt{2\pi}\sigma^2(e^{(\mu-\sigma^2)})^3} \mathrm{exp} \left[ -\frac{\sigma^2}{2} \right] < 0 \; ,
\end{split}
$$

we confirm that it is a maximum, showing that

$$ \label{eq:lognorm-mode-qed}
\mathrm{mode}(X) = e^\left( \mu -\sigma^2 \right) \; .
$$