---
layout: proof
mathjax: true

author: "Thomas J. Faulkenberry"
affiliation: "Tarleton State University"
e_mail: "faulkenberry@tarleton.edu"
date: 2023-10-30 12:00:00

title: "Method of moments for Wald distributed data"
chapter: "Probability Distributions"
section: "Univariate continuous distributions"
topic: "Wald distribution"
theorem: "Method of moments"

sources:
  
proof_id: "P423"
shortcut: "wald-mome"
username: "tomfaulkenberry"
---
  
  

**Theorem:** Let $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ be a set of observed data [independent and identically distributed](/D/iid) according to a [Wald distribution](/D/wald) with drift rate $\gamma$ and threshold $\alpha$:

$$ \label{eq:wald}
y_i \sim \mathrm{Wald}(\gamma,\alpha), \quad i = 1, \ldots, n \; .
$$

Then, the [method-of-moments estimates](/D/mome) for the parameters $\gamma$ and $\alpha$ are given by

$$ \label{eq:wald-MoM}
\begin{split}
\hat{\gamma} &= \sqrt{\frac{\bar{y}}{\bar{v}}} \\
\hat{\alpha} &= \sqrt{\frac{\bar{y}^3}{\bar{v}}}
\end{split}
$$

where $\bar{y}$ is the [sample mean](/D/mean-samp) and $\bar{v}$ is the [unbiased sample variance](/D/var-samp):

$$ \label{eq:y-mean-var}
\begin{split}
\bar{y} &= \frac{1}{n} \sum_{i=1}^n y_i \\
\bar{v} &= \frac{1}{n-1} \sum_{i=1}^n (y_i - \bar{y})^2 \; .
\end{split}
$$


**Proof:** The [mean](/P/wald-mean) and [variance](/P/wald-var) of the [Wald distribution](/D/wald) in terms of the parameters $\gamma$ and $\alpha$ are given by

$$ \label{eq:wald-E-Var}
\begin{split}
\mathrm{E}(X) &= \frac{\alpha}{\gamma} \\
\mathrm{Var}(X) &= \frac{\alpha}{\gamma^3} \; .
\end{split}
$$

Thus, [matching the moments](/D/mome) requires us to solve the following system of equations for $\gamma$ and $\alpha$:

$$ \label{eq:wald-mean-var}
\begin{split}
\bar{y} &= \frac{\alpha}{\gamma} \\
\bar{v} &= \frac{\alpha}{\gamma^3} \; .
\end{split}
$$

To this end, our first step is to express the second equation of \eqref{eq:wald-mean-var} as follows:

$$ \label{eq:gamma-s1}
\begin{split}
\bar{v} &= \frac{\alpha}{\gamma^3} \\
& = \frac{\alpha}{\gamma} \cdot \gamma^{-2}\\
& = \bar{y} \cdot \gamma^{-2} \; .
\end{split}
$$

Rearranging \eqref{eq:gamma-s1} gives

$$ \label{eq:gamma-s2}
\gamma^2 = \frac{\bar{y}}{\bar{v}} \; ,
$$

or equivalently,

$$ \label{eq:gamma-s3}
\gamma = \sqrt{\frac{\bar{y}}{\bar{v}}} \; .
$$

Our final step is to solve the first equation of \eqref{eq:wald-mean-var} for $\alpha$ and substitute \eqref{eq:gamma-s3} for $\gamma$:

$$ \label{eq:alpha-s1}
\begin{split}
\alpha & = \bar{y} \cdot \gamma \\
& = \bar{y} \cdot \sqrt{\frac{\bar{y}}{\bar{v}}}\\
&= \sqrt{\bar{y}^2} \cdot \sqrt{\frac{\bar{y}}{\bar{v}}}\\
&= \sqrt{\frac{\bar{y}^3}{\bar{v}}} \; .
\end{split}
$$

Together, \eqref{eq:gamma-s3} and \eqref{eq:alpha-s1} constitute the method-of-moment estimates of $\gamma$ and $\alpha$.
