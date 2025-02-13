---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-02-06 12:35:52

title: "Mode of the gamma distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Gamma distribution"
theorem: "Mode"

sources:

proof_id: "P487"
shortcut: "gam-mode"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [gamma distribution](/D/gam):

$$ \label{eq:gam}
X \sim \mathrm{Gam}(a, b) \; .
$$

Then, the [mode](/D/mode) of $X$ is

$$ \label{eq:gam-mode}
\mathrm{mode}(X) = \left\{
\begin{array}{rl}
\frac{a-1}{b} \; , & \text{if} \; a \geq 1 \\
            0 \; , & \text{if} \; a < 1 \; .
\end{array}
\right.
$$


**Proof:** The [mode](/D/mode) is the value which maximizes the [probability density function](/D/pdf):

$$ \label{eq:mode}
\mathrm{mode}(X) = \operatorname*{arg\,max}_x f_X(x) \; .
$$

The [probability density function of the gamma distribution](/P/gam-pdf) is:

$$ \label{eq:gam-pdf}
f_X(x) = \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \; .
$$

The first two deriatives of this function are:

$$ \label{eq:gam-pdf-der1}
\begin{split}
   f'_X(x) = \frac{\mathrm{d}f_X(x)}{\mathrm{d}x}
&= \frac{b^a}{\Gamma(a)} \left( -b x^{a-1} \exp[-b x] + (a-1) x^{a-2} \exp[-b x] \right) \\
&= \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \left( \frac{a-1}{x} - b \right)
\end{split}
$$

$$ \label{eq:gam-pdf-der2}
\begin{split}
   f''_X(x) = \frac{\mathrm{d}^2f_X(x)}{\mathrm{d}x^2}
&= \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \left( -\frac{a-1}{x^2} \right)
 + \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \left( \frac{a-1}{x} - b \right)^2 \\
&= \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \left( \left( \frac{a-1}{x} - b \right)^2 - \frac{a-1}{x^2} \right) \; .
\end{split}
$$

We now calculate the root of the first derivative \eqref{eq:gam-pdf-der1}:

$$ \label{eq:gam-mode-s1}
\begin{split}
f'_X(x) = 0
   &= \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \left( \frac{a-1}{x} - b \right) \\
   &\Leftrightarrow \\
0  &= \frac{a-1}{x} - b \\
bx &= a-1 \\
x  &= \frac{a-1}{b} \; .
\end{split}
$$

By plugging this value into the second deriative \eqref{eq:gam-pdf-der2}, we find:

$$ \label{eq:gam-mode-s2}
\begin{split}
   f''_X\left( \frac{a-1}{b} \right)
&= \frac{b^a}{\Gamma(a)} \left( \frac{a-1}{b} \right)^{a-1} \exp\left[-b \left( \frac{a-1}{b} \right)\right] \left( \left( \frac{a-1}{\left( \frac{a-1}{b} \right)} - b \right)^2 - \frac{a-1}{\left( \frac{a-1}{b} \right)^2} \right) \\
&= \frac{b^a}{\Gamma(a)} \left( \frac{a-1}{b} \right)^{a-1} \exp\left[-(a-1)\right] \left( \left( b - b \right)^2 - \frac{b^2}{a-1} \right) \\
&= \frac{b^a}{\Gamma(a)} \left( \frac{a-1}{b} \right)^{a-1} \exp\left[-(a-1)\right] \left( -\frac{b^2}{a-1} \right) \; .
\end{split}
$$

Thus, if $a \geq 1$, then ${f''}_X\left( (a-1)/b \right)$ is negative, such that $f_X(x)$ reaches its maximum at $x = (a-1)/b$. However, if $a < 1$, this value is negative and [not in the support of the random variable](/D/gam) $X$. In this case, the mode of $X$ is $0$, since $f_X(x)$ tends towards infinity at $x=0$:

$$ \label{eq:gam-mode-s3}
\begin{split}
   \lim_{\substack{x \rightarrow 0 \\ a < 1}} f_X(x)
&= \lim_{\substack{x \rightarrow 0 \\ a < 1}} \frac{b^a}{\Gamma(a)} x^{a-1} \exp[-b x] \\
&= \frac{b^a}{\Gamma(a)} \lim_{\substack{x \rightarrow 0 \\ a < 1}} x^{a-1} = \infty \; .
\end{split}
$$