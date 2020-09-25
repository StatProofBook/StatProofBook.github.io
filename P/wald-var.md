---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2020-09-13 12:00:00

title: "Variance of the Wald distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Wald distribution"
theorem: "Variance"

sources:

proof_id: "P170"
shortcut: "wald-var"
username: "tomfaulkenberry"
---


**Theorem:** Let $X$ be a positive [random variable](/D/rvar) following a [Wald distribution](/D/wald):

$$ \label{eq:wald}
X \sim \mathrm{Wald}(\gamma, \alpha) \; .
$$

Then, the [variance](/D/var) of $X$ is

$$ \label{eq:wald-var}
\mathrm{Var}(X) = \frac{\alpha}{\gamma^3} \; .
$$


**Proof:** To compute the variance of $X$, we [partition the variance into expected values](/P/var-mean):

$$ \label{eq:var-mean}
\mathrm{Var}(X) = \mathrm{E}(X^2)-\mathrm{E}(X)^2.
$$

We then use the [moment-generating function of the Wald distribution](/P/wald-mgf) to calculate

$$ \label{eq:wald-moment}
\mathrm{E}(X^2) = M_X''(0) \; .
$$

First we differentiate

$$ \label{eq:wald-mgf}
M_X(t) = \exp\left[\alpha \gamma - \sqrt{\alpha^2(\gamma^2-2t)}\right]
$$

with respect to $t$. Using the chain rule gives

$$ \label{eq:wald-var-s1}
\begin{split}
  M_X'(t) &= \exp\left[\alpha \gamma - \sqrt{\alpha^2(\gamma^2-2t)}\right] \cdot -\frac{1}{2}\left(\alpha^2(\gamma^2-2t)\right)^{-1/2}\cdot -2\alpha^2 \\
          &= \exp\left[\alpha \gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right] \cdot \frac{\alpha^2}{\sqrt{\alpha^2(\gamma^2-2t)}} \\
          &= \alpha \cdot \exp\left[\alpha \gamma -\sqrt{\alpha^2(\gamma^2-2t)}\right] \cdot (\gamma^2-2t)^{-1/2} \; .
\end{split}
$$

Now we use the product rule to obtain the second derivative:

$$ \label{eq:wald-var-s2}
\begin{split}
  M_X''(t) &= \alpha \cdot \exp\left[\alpha \gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right]\cdot (\gamma^2-2t)^{-1/2}\cdot -\frac{1}{2}\left(\alpha^2(\gamma^2-2t)\right)^{-1/2}\cdot -2\alpha^2 \\
           &+ \alpha \cdot \exp\left[\alpha \gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right]\cdot -\frac{1}{2}(\gamma^2-2t)^{-3/2}\cdot -2 \\
           &= \alpha^2\cdot \exp\left[\alpha \gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right]\cdot (\gamma^2-2t)^{-1} \\
           &+ \alpha\cdot \exp\left[\alpha \gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right]\cdot (\gamma^2-2t)^{-3/2} \\
           &= \alpha \cdot \exp\left[\alpha \gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right]\left[\frac{\alpha}{\gamma^2-2t}+\frac{1}{\sqrt{(\gamma^2-2t)^3}}\right] \; .
\end{split}
$$

Applying \eqref{eq:wald-moment} yields

$$ \label{eq:wald-var-s3}
\begin{split}
  \mathrm{E}(X^2) &= M_X''(0) \\
                  &= \alpha \cdot \exp\left[\alpha \gamma-\sqrt{\alpha^2(\gamma^2-2(0))}\right]\left[\frac{\alpha}{\gamma^2-2(0)}+\frac{1}{\sqrt{(\gamma^2-2(0))^3}}\right] \\
                  &= \alpha \cdot \exp\left[\alpha \gamma - \alpha \gamma\right] \cdot \left[\frac{\alpha}{\gamma^2} + \frac{1}{\gamma^3}\right] \\
                  &= \frac{\alpha^2}{\gamma^2} + \frac{\alpha}{\gamma^3} \; .
\end{split}
$$

Since the [mean of a Wald distribution](/P/wald-mean) is given by $\mathrm{E}(X)=\alpha/\gamma$, we can apply \eqref{eq:var-mean} to show

$$ \label{eq:wald-var-s4}
\begin{split}
  \mathrm{Var}(X) &= \mathrm{E}(X^2) - \mathrm{E}(X)^2 \\
                  &= \frac{\alpha^2}{\gamma^2} + \frac{\alpha}{\gamma^3} - \left(\frac{\alpha}{\gamma}\right)^2 \\
                  &= \frac{\alpha}{\gamma^3}
\end{split}
$$

which completes the proof of \eqref{eq:wald-var}.