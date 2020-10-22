---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-22 09:31:00

title: "Maximum likelihood estimation for Dirichlet-distributed data"
chapter: "Statistical Models"
section: "Probability data"
topic: "Dirichlet-distributed data"
theorem: "Maximum likelihood estimation"

sources:
  - authors: "Minka TP"
    year: 2012
    title: "Estimating a Dirichlet distribution"
    in: "Papers by Tom Minka"
    pages: "retrieved on 2020-10-22"
    url: "https://tminka.github.io/papers/dirichlet/minka-dirichlet.pdf"

proof_id: "P182"
shortcut: "dir-mle"
username: "JoramSoch"
---


**Theorem:** Let there be a [Dirichlet-distributed data](/D/dir-data) set $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$:

$$ \label{eq:Dir}
y_i \sim \mathrm{Dir}(\alpha), \quad i = 1, \ldots, n \; .
$$

Then, the [maximum likelihood estimate](/D/mle) for the concentration parameters $\alpha$ can be obtained by iteratively computing

$$ \label{eq:Dir-MLE}
\alpha_j^{\text{(new)}} = \psi^{-1}\left[ \psi\left( \sum_{j=1}^k \alpha_j^{\text{(old)}} \right) + \log \bar{y}_j \right]
$$

where $\psi(x)$ is the digamma function and $\log \bar{y}_j$ is given by:

$$ \label{eq:log-pi}
\log \bar{y}_j = \frac{1}{n} \sum_{i=1}^n \log y_{ij} \; .
$$


**Proof:** The [likelihood function](/D/lf) for each observation is given by the [probability density function of the Dirichlet distribution](/P/dir-pdf)

$$ \label{eq:Dir-yi}
p(y_i|\alpha) = \frac{\Gamma\left( \sum_{j=1}^k \alpha_j \right)}{\prod_{j=1}^k \Gamma(\alpha_j)} \, \prod_{j=1}^k {y_{ij}}^{\alpha_j-1}
$$

and because observations are [independent](/D/ind), the likelihood function for all observations is the product of the individual ones:

$$ \label{eq:Dir-LF}
p(y|\alpha) = \prod_{i=1}^n p(y_i|\alpha) = \prod_{i=1}^n \left[ \frac{\Gamma\left( \sum_{j=1}^k \alpha_j \right)}{\prod_{j=1}^k \Gamma(\alpha_j)} \, \prod_{j=1}^k {y_{ij}}^{\alpha_j-1} \right] \; .
$$

Thus, the [log-likelihood function](/D/llf) is

$$ \label{eq:Dir-LL}
\mathrm{LL}(\alpha) = \log p(y|\alpha) = \log \prod_{i=1}^n \left[ \frac{\Gamma\left( \sum_{j=1}^k \alpha_j \right)}{\prod_{j=1}^k \Gamma(\alpha_j)} \, \prod_{j=1}^k {y_{ij}}^{\alpha_j-1} \right]
$$

which can be developed into

$$ \label{eq:Dir-LL-der}
\begin{split}
\mathrm{LL}(\alpha) &= \sum_{i=1}^n \log \Gamma\left( \sum_{j=1}^k \alpha_j \right) - \sum_{i=1}^n \sum_{j=1}^k \log \Gamma(\alpha_j) + \sum_{i=1}^n \sum_{j=1}^k (\alpha_j-1) \log y_{ij} \\
&= n \log \Gamma\left( \sum_{j=1}^k \alpha_j \right) - n \sum_{j=1}^k \log \Gamma(\alpha_j) + n \sum_{j=1}^k (\alpha_j-1) \, \frac{1}{n} \sum_{i=1}^n \log y_{ij} \\
&= n \log \Gamma\left( \sum_{j=1}^k \alpha_j \right) - n \sum_{j=1}^k \log \Gamma(\alpha_j) + n \sum_{j=1}^k (\alpha_j-1) \, \log \bar{y}_j
\end{split}
$$

where we have specified

$$ \label{eq:log-pi-reit}
\log \bar{y}_j = \frac{1}{n} \sum_{i=1}^n \log y_{ij} \; .
$$

The derivative of the log-likelihood with respect to a particular parameter $\alpha_j$ is

$$ \label{eq:Dir-dLLdaj}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\alpha)}{\mathrm{d}\alpha_j} &= \frac{\mathrm{d}}{\mathrm{d}\alpha_j} \left[ n \log \Gamma\left( \sum_{j=1}^k \alpha_j \right) - n \sum_{j=1}^k \log \Gamma(\alpha_j) + n \sum_{j=1}^k (\alpha_j-1) \, \log \bar{y}_j \right] \\
&= \frac{\mathrm{d}}{\mathrm{d}\alpha_j} \left[ n \log \Gamma\left( \sum_{j=1}^k \alpha_j \right) \right] - \frac{\mathrm{d}}{\mathrm{d}\alpha_j} \left[ n \log \Gamma(\alpha_j) \right] + \frac{\mathrm{d}}{\mathrm{d}\alpha_j} \left[ n (\alpha_j-1) \, \log \bar{y}_j \right] \\
&= n \psi\left( \sum_{j=1}^k \alpha_j \right) - n \psi(\alpha_j) + n \log \bar{y}_j
\end{split}
$$

where we have used the digamma function

$$ \label{eq:digamma-fct}
\psi(x) = \frac{\mathrm{d}\log \Gamma(x)}{\mathrm{d}x} \; .
$$

Setting this derivative to zero, we obtain:

$$ \label{eq:Dir-dLLdaj-0}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\alpha)}{\mathrm{d}\alpha_j} &= 0 \\
0 &= n \psi\left( \sum_{j=1}^k \alpha_j \right) - n \psi(\alpha_j) + n \log \bar{y}_j \\
0 &= \psi\left( \sum_{j=1}^k \alpha_j \right) - \psi(\alpha_j) + \log \bar{y}_j \\
\psi(\alpha_j) &= \psi\left( \sum_{j=1}^k \alpha_j \right) + \log \bar{y}_j \\
\alpha_j &= \psi^{-1} \left[ \psi\left( \sum_{j=1}^k \alpha_j \right) + \log \bar{y}_j \right] \; .
\end{split}
$$

In the following, we will use a fixed-point iteration to maximize $\mathrm{LL}(\alpha)$. Given an initial guess for $\alpha$, we construct a lower bound on the likelihood function \eqref{eq:Dir-LL-der} which is tight at $\alpha$. The maximum of this bound is computed and it becomes the new guess. Because the [Dirichlet distribution](/D/dir) belongs to the [exponential family](/D/dist-expfam), the log-likelihood function is convex in $\alpha$ ánd the maximum is the only stationary point, such that the procedure is guaranteed to converge to the maximum.

In our case, we use a bound on the gamma function

$$ \label{eq:gamma-fct-bound}
\begin{split}
\Gamma(x) &\geq \Gamma(\hat{x}) \cdot \mathrm{exp}\left[(x-\hat{x}) \, \psi(\hat{x}) \right] \\
\log \Gamma(x) &\geq \log \Gamma(\hat{x}) + (x-\hat{x}) \, \psi(\hat{x})
\end{split}
$$

and apply it to $\Gamma\left( \sum_{j=1}^k \alpha_j \right)$ in \eqref{eq:Dir-LL-der} to yield

$$ \label{eq:Dir-LL-bound}
\begin{split}
\frac{1}{n} \mathrm{LL}(\alpha) &= \log \Gamma\left( \sum_{j=1}^k \alpha_j \right) - \sum_{j=1}^k \log \Gamma(\alpha_j) + \sum_{j=1}^k (\alpha_j-1) \, \log \bar{y}_j \\
\frac{1}{n} \mathrm{LL}(\alpha) &\geq \log \Gamma\left(\sum_{j=1}^k \hat{\alpha}_j\right) + \left(\sum_{j=1}^k \alpha_j - \sum_{j=1}^k \hat{\alpha}_j\right) \psi\left(\sum_{j=1}^k \hat{\alpha}_j\right) - \sum_{j=1}^k \log \Gamma(\alpha_j) + \sum_{j=1}^k (\alpha_j-1) \, \log \bar{y}_j \\
\frac{1}{n} \mathrm{LL}(\alpha) &\geq \left(\sum_{j=1}^k \alpha_j\right) \psi\left(\sum_{j=1}^k \hat{\alpha}_j\right) - \sum_{j=1}^k \log \Gamma(\alpha_j) + \sum_{j=1}^k (\alpha_j-1) \, \log \bar{y}_j + \mathrm{const.}
\end{split}
$$

which leads to the following fixed-point iteration using \eqref{eq:Dir-dLLdaj-0}:

$$ \label{eq:Dir-MLE-qed}
\alpha_j^{\text{(new)}} = \psi^{-1}\left[ \psi\left( \sum_{j=1}^k \alpha_j^{\text{(old)}} \right) + \log \bar{y}_j \right] \; .
$$