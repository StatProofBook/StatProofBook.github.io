---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-09 15:58:00

title: "Mode of the normal distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Normal distribution"
theorem: "Mode"

sources:

proof_id: "P17"
shortcut: "norm-mode"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [normal distribution](/D/norm):

$$ \label{eq:norm}
X \sim \mathcal{N}(\mu, \sigma^2) \; .
$$

Then, the [mode](/D/mode) of $X$ is

$$ \label{eq:norm-mode}
\mathrm{mode}(X) = \mu \; .
$$


**Proof:** The [mode](/D/mode) is the value which maximizes the [probability density function](/D/pdf):

$$ \label{eq:mode}
\mathrm{mode}(X) = \operatorname*{arg\,max}_x f_X(x) \; .
$$

The [probability density function of the normal distribution](/P/norm-pdf) is:

$$ \label{eq:norm-pdf}
f_X(x) = \frac{1}{\sqrt{2 \pi} \sigma} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \; .
$$

The first two deriatives of this function are:

$$ \label{eq:norm-pdf-der1}
f'_X(x) = \frac{\mathrm{d}f_X(x)}{\mathrm{d}x} = \frac{1}{\sqrt{2 \pi} \sigma^3} \cdot (-x + \mu) \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right]
$$

$$ \label{eq:norm-pdf-der2}
f''_X(x) = \frac{\mathrm{d}^2f_X(x)}{\mathrm{d}x^2} = -\frac{1}{\sqrt{2 \pi} \sigma^3} \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] + \frac{1}{\sqrt{2 \pi} \sigma^5} \cdot (-x + \mu)^2 \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \; .
$$

We now calculate the root of the first derivative \eqref{eq:norm-pdf-der1}:

$$ \label{eq:norm-mode-s1}
\begin{split}
f'_X(x) = 0 &= \frac{1}{\sqrt{2 \pi} \sigma^3} \cdot (-x + \mu) \cdot \exp \left[ -\frac{1}{2} \left( \frac{x-\mu}{\sigma} \right)^2 \right] \\
0 &= -x + \mu \\
x &= \mu \; .
\end{split}
$$

By plugging this value into the second deriative \eqref{eq:norm-pdf-der2},

$$ \label{eq:norm-mode-s2}
\begin{split}
f''_X(\mu) &= -\frac{1}{\sqrt{2 \pi} \sigma^3} \cdot \exp(0) + \frac{1}{\sqrt{2 \pi} \sigma^5} \cdot (0)^2 \cdot \exp(0) \\
&= -\frac{1}{\sqrt{2 \pi} \sigma^3} < 0 \; ,
\end{split}
$$

we confirm that it is in fact a maximum which shows that

$$ \label{eq:norm-mode-qed}
\mathrm{mode}(X) = \mu \; .
$$