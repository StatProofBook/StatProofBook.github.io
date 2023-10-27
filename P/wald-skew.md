---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2023-10-24 12:00:00

title: "Skewness of the Wald distribution"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Wald distribution"
theorem: "Skewness"

sources:
  
proof_id: "P421"
shortcut: "wald-skew"
username: "tomfaulkenberry"
---
  


**Theorem:** Let $X$ be a [random variable](/D/rvar) following a [Wald distribution](/D/wald):

$$ \label{eq:wald}
X \sim \mathrm{Wald}(\gamma,\alpha) \; .
$$

Then the [skewness](/D/skew) of $X$ is

$$ \label{eq:wald-skew}
\mathrm{Skew}(X) = \frac{3}{\sqrt{\alpha\gamma}} \; .
$$

**Proof:** 

To compute the skewness of $X$, we [partition the skewness into expected values](/P/skew-mean):

$$ \label{eq:skew-mean}
\mathrm{Skew}(X) = \frac{\mathrm{E}(X^3)-3\mu\sigma^2-\mu^3}{\sigma^3} \; ,
$$

where $\mu$ and $\sigma$ are the mean and standard deviation of $X$, respectively. Since $X$ follows an [Wald distribution](/D/wald), the [mean](/P/wald-mean) of $X$ is given by 

$$ \label{eq:wald-mean}
\mu = \mathrm{E}(X) = \frac{\alpha}{\gamma}
$$

and the [standard deviation](/P/wald-var) of $X$ is given by

$$ \label{eq:wald-var}
\sigma = \sqrt{\mathrm{Var}(X)} = \sqrt{\frac{\alpha}{\gamma^3}}\; .
$$

Substituting \eqref{eq:wald-mean} and \eqref{eq:wald-var} into \eqref{eq:skew-mean} gives:

$$ \label{eq:skew-mean-alt}
\begin{split}
\mathrm{Skew}(X) &= \frac{\mathrm{E}(X^3)-3\mu\sigma^2-\mu^3}{\sigma^3}\\
&= \frac{\mathrm{E}(X^3) - 3\left(\frac{\alpha}{\gamma}\right)\left(\frac{\alpha}{\gamma^3}\right)-\left(\frac{\alpha}{\gamma}\right)^3}{\left(\sqrt{\frac{\alpha}{\gamma^3}}\right)^3}\\
&= \frac{\gamma^{9/2}}{\alpha^{3/2}}\left[\mathrm{E}(X^3) - \frac{3\alpha^2}{\gamma^4}-\frac{\alpha^3}{\gamma^3}\right] \; .
\end{split}
$$

Thus, the remaining work is to compute $\mathrm{E}(X^3)$. To do this, we use the [moment-generating function of the Wald distribution](/P/wald-mgf) to calculate

$$ \label{eq:wald-moment}
\mathrm{E}(X^3) = M_X'''(0)
$$

based on the [relationship between raw moment and moment-generating function](/P/mom-mgf). First, we differentiate the moment-generating function

$$ \label{eq:wald-mgf}
M_X(t) = \exp\left[\alpha \gamma - \sqrt{\alpha^2(\gamma^2-2t)}\right]
$$

with respect to $t$. Using the chain rule, we have:

$$ \label{eq:wald-skew-s1}
\begin{split}
  M_X'(t) &= \exp\left[\alpha \gamma - \sqrt{\alpha^2(\gamma^2-2t)}\right] \cdot -\frac{1}{2}\left(\alpha^2(\gamma^2-2t)\right)^{-1/2}\cdot -2\alpha^2 \\
          &= \exp\left[\alpha \gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right] \cdot \frac{\alpha^2}{\sqrt{\alpha^2(\gamma^2-2t)}} \\
          &= \alpha \cdot \exp\left[\alpha \gamma -\sqrt{\alpha^2(\gamma^2-2t)}\right] \cdot (\gamma^2-2t)^{-1/2} \; .
\end{split}
$$

Now we use the product rule to obtain the second derivative:

$$ \label{eq:wald-skew-s2}
\begin{split}
  M_X''(t) &= \alpha \cdot \exp\left[\alpha \gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right]\cdot (\gamma^2-2t)^{-1/2}\cdot -\frac{1}{2}\left(\alpha^2(\gamma^2-2t)\right)^{-1/2}\cdot -2\alpha^2 \\
           &+ \alpha \cdot \exp\left[\alpha \gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right]\cdot -\frac{1}{2}(\gamma^2-2t)^{-3/2}\cdot -2 \\
           &= \alpha^2\cdot \exp\left[\alpha \gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right]\cdot (\gamma^2-2t)^{-1} \\
           &+ \alpha\cdot \exp\left[\alpha\gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right]\cdot (\gamma^2-2t)^{-3/2} \\
           & = \frac{\alpha^2}{\gamma^2-2t}\exp\left[\alpha\gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right] + \frac{\alpha}{(\gamma^2-2t)^{3/2}}\exp\left[\alpha\gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right] \; .
\end{split}
$$

Finally, one more application of the chain rule will give us the third derivative. To start, we will decompose the second derivative obtained in \eqref{eq:wald-skew-s2} as

$$ \label{eq:wald-skew-s3}
M''(t) = f(t) + g(t)
$$

where

$$ \label{eq:wald-skew-split1}
f(t) = \frac{\alpha^2}{\gamma^2-2t}\exp\left[\alpha\gamma-\sqrt{\alpha^2(\gamma^2-t2)}\right]
$$

and

$$ \label{eq:wald-skew-split2}
g(t) = \frac{\alpha}{(\gamma^2-2t)^{3/2}}\exp\left[\alpha\gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right] \; .
$$

With this decomposition, $M_X'''(t) = f'(t) + g'(t)$. Applying the product rule to $f$ gives:

$$ \label{eq:wald-skew-f}
\begin{split}
  f'(t) &= 2\alpha^2(\gamma^2-2t)^{-2}\exp\left[\alpha\gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right] \\
  &+ \alpha^2(\gamma^2-2t)^{-1}\exp\left[\alpha\gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right]\cdot -\frac{1}{2}\left[\alpha^2(\gamma^2-2t)\right]^{-1/2}\cdot -2\alpha^2\\
  &= \frac{2\alpha^2}{(\gamma^2-2t)^2}\exp\left[\alpha\gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right] \\
  &+ \frac{\alpha^3}{(\gamma^2-2t)^{3/2}}\exp\left[\alpha\gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right] \; .
\end{split}
$$

Similarly, applying the product rule to $g$ gives:

$$ \label{eq:wald-skew-g}
\begin{split}
  g'(t) &= -\frac{3}{2}\alpha(\gamma^2-2t)^{-5/2}(-2)\exp\left[\alpha\gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right] \\
  &+ \alpha(\gamma^2-2t)^{-3/2}\exp\left[\alpha\gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right]\cdot -\frac{1}{2}\left[\alpha^2(\gamma^2-2t)\right]^{-1/2}\cdot -2\alpha^2\\
&= \frac{3\alpha}{(\gamma^2-2t)^{5/2}}\exp\left[\alpha\gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right] \\
&+ \frac{\alpha^2}{(\gamma^2-2t)^2}\exp\left[\alpha\gamma-\sqrt{\alpha^2(\gamma^2-2t)}\right] \; .
\end{split}\\
$$

Applying \eqref{eq:wald-moment}, together with \eqref{eq:wald-skew-f} and \eqref{eq:wald-skew-g}, yields

$$ \label{eq:wald-skew-s4}
\begin{split}
\mathrm{E}(X^3) &= M_X'''(0)\\
 &= f'(0) + g'(0)\\
 &= \left[\frac{2\alpha^2}{\gamma^4}+\frac{\alpha^3}{\gamma^3}\right] + \left[\frac{3\alpha}{\gamma^5}+\frac{\alpha^2}{\gamma^4}\right]\\
 &= \frac{3\alpha^2}{\gamma^4} + \frac{\alpha^3}{\gamma^3} + \frac{3\alpha}{\gamma^5} \; .
\end{split}
$$

We now substitute \eqref{eq:wald-skew-s4} into \eqref{eq:skew-mean-alt}, giving

$$ \label{eq:wald-skew-s5}
\begin{split}
\mathrm{Skew}(X) &= \frac{\gamma^{9/2}}{\alpha^{3/2}}\left[\mathrm{E}(X^3) - \frac{3\alpha^2}{\gamma^4}-\frac{\alpha^3}{\gamma^3}\right] \\
&= \frac{\gamma^{9/2}}{\alpha^{3/2}}\left[\frac{3\alpha^2}{\gamma^4} + \frac{\alpha^3}{\gamma^3} + \frac{3\alpha}{\gamma^5} - \frac{3\alpha^2}{\gamma^4}-\frac{\alpha^3}{\gamma^3}\right] \\
&= \frac{\gamma^{9/2}}{\alpha^{3/2}} \cdot \frac{3\alpha}{\gamma^5}\\
&= \frac{3}{\alpha^{1/2}\cdot \gamma^{1/2}}\\
&= \frac{3}{\sqrt{\alpha\gamma}} \; .
\end{split}
$$

This completes the proof of \eqref{eq:wald-skew}.
