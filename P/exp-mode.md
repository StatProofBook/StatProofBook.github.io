---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-12 15:53:00

title: "Mode of the exponential distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Exponential distribution"
theorem: "Mode"

sources:

proof_id: "P51"
shortcut: "exp-mode"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a random variable following an [exponential distribution](/D/exp.html):

$$ \label{eq:exp}
X \sim \mathrm{Exp}(\lambda) \; .
$$

Then, the [mode](/D/mode.html) of $X$ is

$$ \label{eq:exp-mode}
\mathrm{mode}(X) = 0 \; .
$$


**Proof:**  The [mode](/D/mode.html) is the value which maximizes the probability density function:

$$ \label{eq:mode}
\mathrm{mode}(X) = \operatorname*{arg\,max}_x f_X(x) \; .
$$

The [probability density function of the exponential distribution](/P/exp-pdf.html) is:

$$ \label{eq:exp-pdf}
f_X(x) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; x < 0 \\
\lambda \exp[-\lambda x] \; , & \text{if} \; x \geq 0 \; .
\end{array}
\right.
$$

Since

$$ \label{eq:exp-pdf-eq0}
\lim_{x \to 0} f_X(x) = \infty
$$

and

$$ \label{eq:exp-pdf-neq0}
f_X(x) < \infty \quad \text{for any} \quad x \neq 0 \; ,
$$

it follows that

$$ \label{eq:exp-mode-qed}
\mathrm{mode}(X) = 0 \; .
$$