---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-01-02 18:05:00

title: "Cumulative distribution function of the continuous uniform distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Continuous uniform distribution"
theorem: "Cumulative distribution function"

sources:

proof_id: "P38"
shortcut: "cuni-cdf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a random variable following a continuous uniform distribution:

$$ \label{eq:cuni}
X \sim \mathcal{U}(a, b) \; .
$$

Then, the cumulative distribution function of $X$ is

$$ \label{eq:cuni-cdf}
F_X(x) =
\begin{cases}
\;\; 0 & , \text{if} \; x < a \\
\frac{x-a}{b-a} & , \text{if} \; a \leq x \leq b \\
\;\; 1 & , \text{if} \; x > b \; .
\end{cases}
$$


**Proof:** The [probability density function of the continuous uniform distribution](/P/cuni-pdf.html) is:

$$ \label{eq:cuni-pdf}
\mathcal{U}(x; a, b) =
\begin{cases}
\frac{1}{b-a} & , \text{if} \; a \leq x \leq b \\
\;\; 0 & , \text{otherwise} \; .
\end{cases}
$$

Thus, the [cumulative distribution function](/D/cdf.html) is:

$$ \label{eq:cuni-cdf-s1}
F_X(x) = \int_{-\infty}^{x} \mathcal{U}(z; a, b) \, \mathrm{d}z
$$

If $x < a$, we have

$$ \label{eq:cuni-cdf-s2a}
F_X(x) = \int_{-\infty}^{x} 0 \, \mathrm{d}z = 0 \; .
$$

If $a \leq x \leq b$, we have

$$ \label{eq:cuni-cdf-s2b}
\begin{split}
F_X(x) &= \int_{-\infty}^{a} \mathcal{U}(z; a, b) \, \mathrm{d}z + \int_{a}^{x} \mathcal{U}(z; a, b) \, \mathrm{d}z \\
&= \int_{-\infty}^{a} 0 \, \mathrm{d}z + \int_{a}^{x} \frac{1}{b-a} \, \mathrm{d}z \\
&= 0 + \frac{1}{b-a} [z]_a^x \\
&= \frac{x-a}{b-a} \; .
\end{split}
$$

If $x > b$, we have

$$ \label{eq:cuni-cdf-s2c}
\begin{split}
F_X(x) &= \int_{-\infty}^{b} \mathcal{U}(z; a, b) \, \mathrm{d}z + \int_{b}^{x} \mathcal{U}(z; a, b) \, \mathrm{d}z \\
&= F_X(b) + \int_{b}^{x} 0 \, \mathrm{d}z \\
&= \frac{b-a}{b-a} + 0 \\
&= 1 \; .
\end{split}
$$

This completes the proof.