---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2025-05-21 13:12:00

title: "Mode of the multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Mode"

sources:

proof_id: "P498"
shortcut: "mvn-mode"
username: "JoramSoch"
---


**Theorem:** Let $X$ follow a [multivariate normal distribution](/D/mvn):

$$ \label{eq:mvn}
X \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, the [mode](/D/mode) of $X$ is

$$ \label{eq:mvn-mode}
\mathrm{mode}(X) = \mu \; .
$$


**Proof:** The [mode](/D/mode) is the value which maximizes the [probability density function](/D/pdf):

$$ \label{eq:mode}
\mathrm{mode}(X) = \operatorname*{arg\,max}_x f_X(x) \; .
$$

The [probability density function of the multivariate normal distribution](/P/mvn-pdf) is:

$$ \label{eq:mvn-pdf}
f_X(x) = \frac{1}{\sqrt{(2 \pi)^n |\Sigma|}} \cdot \exp \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] \; .
$$

The gradient of this function $\nabla_x f_X(x) \in \mathbb{R}^n$ is:

$$ \label{eq:mvn-pdf-grad}
\begin{split}
   \nabla_x f_X(x)
&= f_X(x) \cdot \nabla_x \left[ -\frac{1}{2} (x-\mu)^\mathrm{T} \Sigma^{-1} (x-\mu) \right] \\
&= f_X(x) \cdot \left[ -\frac{1}{2} \left( 2 \Sigma^{-1} (x-\mu) \right) \right] \\
&= f_X(x) \cdot \left[ -\Sigma^{-1} (x-\mu) \right] \; .
\end{split}
$$

The Hessian of this function $\nabla_x^2 f_X(x) \in \mathbb{R}^{n \times n}$ is:

$$ \label{eq:mvn-pdf-hess}
\begin{split}
   \nabla_x^2 f_X(x)
&= \nabla_x f_X(x) \cdot \left[ -\Sigma^{-1} (x-\mu) \right]^\mathrm{T} + f_X(x) \cdot \nabla_x \left[ -\Sigma^{-1} (x-\mu) \right] \\
&= f_X(x) \cdot \left[ -\Sigma^{-1} (x-\mu) \right] \left[ -(x-\mu)^\mathrm{T} \Sigma^{-1} \right] + f_X(x) \cdot \left[ -\Sigma^{-1} \right] \\
&= f_X(x) \cdot \left[ \Sigma^{-1} (x-\mu) (x-\mu)^\mathrm{T} \Sigma^{-1} - \Sigma^{-1} \right] \; .
\end{split}
$$

Setting the gradient \eqref{eq:mvn-pdf-grad} to zero, we calculate the root:

$$ \label{eq:mvn-mode-s1}
\begin{split}
    \nabla_x f_X(x) = 0 &= f_X(x) \cdot \left[ -\Sigma^{-1} (x-\mu) \right] \\
\Leftrightarrow \quad 0 &= -\Sigma^{-1} (x-\mu) \\
\Leftrightarrow \quad x &= \mu \; .
\end{split}
$$

Plugging this value into the Hessian \eqref{eq:mvn-pdf-hess}, we obtain:

$$ \label{eq:mvn-mode-s2}
\begin{split}
   \nabla_x^2 f_X(\mu)
&= f_X(\mu) \cdot \left[ \Sigma^{-1} (\mu-\mu) (\mu-\mu)^\mathrm{T} \Sigma^{-1} - \Sigma^{-1} \right] \\
&= -f_X(\mu) \cdot \Sigma^{-1} \; .
\end{split}
$$

Since $\Sigma$ is [positive-definite](/D/mvn), $\Sigma^{-1}$ is also [positive-definite](/D/mvn) and since $f_X(\mu)$ is positive, $-f_X(\mu) \cdot \Sigma^{-1}$ is a negative-definite matrix, so that $f_X(\mu)$ is a maximum. Taken together, this shows that

$$ \label{eq:mvn-mode-qed}
\mathrm{mode}(X) = \mu \; .
$$