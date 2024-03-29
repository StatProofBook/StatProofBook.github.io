---
layout: proof
mathjax: true

# author: "Joram Soch"
# affiliation: "BCCN Berlin"
# e_mail: "joram.soch@bccn-berlin.de"
date: 2020-02-12 15:53:00

author: "Heiner Atze"
affiliation: "n/a"
e_mail: "heiner.atze@gmx.net"
# date: 2022-04-07 17:16

title: "Mode of the exponential distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Exponential distribution"
theorem: "Mode"

sources:

proof_id: "P51"
shortcut: "exp-mode"
# username: "JoramSoch"
username: "kantundpeterpan"
---


**Theorem:** Let $X$ be a [random variable](/D/rvar) following an [exponential distribution](/D/exp):

$$ \label{eq:exp}
X \sim \mathrm{Exp}(\lambda) \; .
$$

Then, the [mode](/D/mode) of $X$ is

$$ \label{eq:exp-mode}
\mathrm{mode}(X) = 0 \; .
$$


**Proof:**  The [mode](/D/mode) is the value which maximizes the [probability density function](/D/pdf):

$$ \label{eq:mode}
\mathrm{mode}(X) = \operatorname*{arg\,max}_x f_X(x) \; .
$$

The [probability density function of the exponential distribution](/P/exp-pdf) is:

$$ \label{eq:exp-pdf}
f_X(x) = \left\{
\begin{array}{rl}
0 \; , & \text{if} \; x < 0 \\
\lambda e^{-\lambda x} \; , & \text{if} \; x \geq 0 \; .
\end{array}
\right.
$$

Since

$$ \label{eq:exp-pdf-eq0}
f_X(0) = \lambda
$$

and

$$ \label{eq:exp-pdf-neq0}
0 < e^{-\lambda x} < 1 \quad \text{for any} \quad x > 0 \; ,
$$

it follows that

$$ \label{eq:exp-mode-qed}
\mathrm{mode}(X) = 0 \; .
$$