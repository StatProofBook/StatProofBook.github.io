---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2020-09-13 12:00:00

title: "Mean of the Wald distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Wald distribution"
theorem: "Mean"

sources:

proof_id: "P169"
shortcut: "wald-mean"
username: "tomfaulkenberry"
---


**Theorem:** Let $X$ be a positive [random variable](/D/rvar) following a [Wald distribution](/D/wald):

$$ \label{eq:wald}
X \sim \mathrm{Wald}(\gamma, \alpha) \; .
$$

Then, the [mean or expected value](/D/mean) of $X$ is

$$ \label{eq:wald-mean}
\mathrm{E}(X) = \frac{\alpha}{\gamma} \; .
$$


**Proof:** The mean or expected value $\mathrm{E}(X)$ is the first [moment](/D/mom) of $X$, so [we can use](/P/mom-mgf) the [moment-generating function of the Wald distribution](/P/wald-mgf) to calculate

$$ \label{eq:wald-moment}
\mathrm{E}(X) = M_X'(0) \; .
$$

First we differentiate

$$ \label{eq:wald-mgf}
M_X(t) = \exp\left[\alpha \gamma - \sqrt{\alpha^2(\gamma^2-2t)}\right]
$$

with respect to $t$. Using the chain rule gives

$$ \label{eq:wald-mean-s1}
\begin{split}
  M_X'(t) &= \exp\left[\alpha \gamma - \sqrt{\alpha^2(\gamma^2-2t)}\right] \cdot -\frac{1}{2}\left(\alpha^2(\gamma^2-2t)\right)^{-1/2}\cdot -2\alpha^2 \\
  &= \exp\left[\alpha \gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right] \cdot \frac{\alpha^2}{\sqrt{\alpha^2(\gamma^2-2t)}} \; .
\end{split}
$$

Evaluating \eqref{eq:wald-mean-s1} at $t=0$ gives the desired result:

$$ \label{eq:wald-mean-s2}
\begin{split}
  M_X'(0) &= \exp\left[\alpha \gamma-\sqrt{\alpha^2(\gamma^2-2(0))}\right] \cdot \frac{\alpha^2}{\sqrt{\alpha^2(\gamma^2-2(0))}} \\
          &= \exp\left[\alpha \gamma - \sqrt{\alpha^2 \cdot \gamma^2}\right]\cdot \frac{\alpha^2}{\sqrt{\alpha^2\cdot \gamma^2}} \\
          &= \exp[0] \cdot \frac{\alpha^2}{\alpha \gamma} \\
          &= \frac{\alpha}{\gamma} \; .
\end{split}
$$