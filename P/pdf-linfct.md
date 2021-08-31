---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-08-30 07:46:00

title: "Probability density function of a linear function of a continuous random vector"
chapter: "General Theorems"
section: "Probability theory"
topic: "Probability functions"
theorem: "Probability density function of linear transformation"

sources:
  - authors: "Taboga, Marco"
    year: 2017
    title: "Functions of random vectors and their distribution"
    in: "Lectures on probability and mathematical statistics"
    pages: "retrieved on 2021-08-30"
    url: "https://www.statlect.com/fundamentals-of-probability/functions-of-random-vectors"

proof_id: "P255"
shortcut: "pdf-linfct"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n \times 1$ [random vector](/D/rvec) of [continuous random variables](/D/rvar-disc) with possible outcomes $\mathcal{X} \subseteq \mathbb{R}^n$ and let $Y = \Sigma X + \mu$ be a linear transformation of this random variable with [constant](/D/const) $n \times 1$ vector $\mu$ and [constant](/D/const) $n \times n$ matrix $\Sigma$. Then, the [probability density function](/D/pdf) of $Y$ is

$$ \label{eq:pdf-linfct}
f_Y(y) = \left\{
\begin{array}{rl}
\frac{1}{\left| \Sigma \right|} f_X(\Sigma^{-1}(y-\mu)) \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y \notin \mathcal{Y}
\end{array}
\right.
$$

where $\lvert \Sigma \rvert$ is the determinant of $\Sigma$ and $\mathcal{Y}$ is the set of possible outcomes of $Y$:

$$ \label{eq:Y-range}
\mathcal{Y} = \left\lbrace y = \Sigma x + \mu: x \in \mathcal{X} \right\rbrace \; .
$$


**Proof:** Because the linear function $g(X) = \Sigma X + \mu$ is invertible and differentiable, we can determine the [probability density function of an invertible function of a continuous random vector](/P/pdf-invfct) using the relation

$$ \label{eq:pdf-invfct}
f_Y(y) = \left\{
\begin{array}{rl}
f_X(g^{-1}(y)) \, \left| J_{g^{-1}}(y) \right| \; , & \text{if} \; y \in \mathcal{Y} \\
0 \; , & \text{if} \; y \notin \mathcal{Y}
\end{array}
\right. \; .
$$

The inverse function is

$$ \label{eq:g-inv}
X = g^{-1}(Y) = \Sigma^{-1}(Y-\mu) = \Sigma^{-1} Y - \Sigma^{-1} \mu
$$

and the Jacobian matrix is

$$ \label{eq:J-g-inv}
J_{g^{-1}}(y) = \left[ \begin{matrix}
\frac{\mathrm{d}x_1}{\mathrm{d}y_1} & \ldots & \frac{\mathrm{d}x_1}{\mathrm{d}y_n} \\
\vdots & \ddots & \vdots \\
\frac{\mathrm{d}x_n}{\mathrm{d}y_1} & \ldots & \frac{\mathrm{d}x_n}{\mathrm{d}y_n}
\end{matrix} \right] = \Sigma^{-1} \; .
$$

Plugging \eqref{eq:g-inv} and \eqref{eq:J-g-inv} into \eqref{eq:pdf-invfct} and applying the determinant property $\lvert A^{-1} \rvert = \lvert A \rvert^{-1}$, we obtain

$$ \label{eq:pdf-linfct-qed}
f_Y(y) = \frac{1}{\left| \Sigma \right|} f_X(\Sigma^{-1}(y-\mu)) \; .
$$