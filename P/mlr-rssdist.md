---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-12-13 07:08:00

title: "Distribution of residual sum of squares in multiple linear regression with weighted least squares"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Distribution of residual sum of squares"

sources:
  - authors: "Koch, Karl-Rudolf"
    year: 2007
    title: "Estimation of the Variance Factor in Traditional Statistics"
    in: "Introduction to Bayesian Statistics"
    pages: "Springer, Berlin/Heidelberg, 2007, ch. 4.2.3, eq. 4.37"
    url: "https://www.springer.com/de/book/9783540727231"
    doi: "10.1007/978-3-540-72726-2"
  - authors: "Penny, William"
    year: 2006
    title: "Estimating error variance"
    in: "Mathematics for Brain Imaging"
    pages: "ch. 2.2, pp. 49-51, eqs. 2.4-2.8"
    url: "https://ueapsylabs.co.uk/sites/wpenny/mbi/mbi_course.pdf"
  - authors: "Wikipedia"
    year: 2022
    title: "Ordinary least squares"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-12-13"
    url: "https://en.wikipedia.org/wiki/Ordinary_least_squares#Estimation"

proof_id: "P390"
shortcut: "mlr-rssdist"
username: "JoramSoch"
---


**Theorem:** Assume a [linear regression model](/D/mlr) with correlated observations

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

and consider estimation using [weighted least squares](/P/mlr-wls). Then, the [residual sum of squares](/D/rss) $\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}$, divided by the true [error variance](/D/mlr) $\sigma^2$, follows a [chi-squared distribution](/D/chi2) with $n-p$ [degrees of freedom](/D/dof)

$$ \label{eq:mlr-rss-dist}
\frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{\sigma^2} \sim \chi^2(n-p)
$$

where $n$ and $p$ are the dimensions of the $n \times p$ [design matrix](/D/mlr) $X$.


**Proof:** Consider an $n \times n$ square matrix $W$, such that

$$ \label{eq:W-def}
W V W^\mathrm{T} = I_n \; .
$$

Then, left-multiplying the regression model in \eqref{eq:mlr} with $W$ gives

$$ \label{eq:mlr-W-s1}
Wy = WX\beta + W\varepsilon, \; W\varepsilon \sim \mathcal{N}(0, \sigma^2 W V W^\mathrm{T})
$$

which can be rewritten as

$$ \label{eq:mlr-W-s2}
\tilde{y} = \tilde{X}\beta + \tilde{\varepsilon}, \; \tilde{\varepsilon} \sim \mathcal{N}(0, \sigma^2 I_n)
$$

where $\tilde{y} = Wy$, $\tilde{X} = WX$ and $\tilde{\varepsilon} = W\varepsilon$. This [implies the distribution](/P/mvn-ltt)

$$ \label{eq:y-tilde-dist}
\tilde{y} \sim \mathcal{N}(\tilde{X} \beta, \sigma^2 I_n) \; .
$$

With that, we have obtained a [linear regression model](/D/mlr) with independent observations. [Cochran's theorem for multivariate normal variables](/P/mvn-cochran) states that, for an $n \times 1$ [normal random vector](/D/mvn) whose [covariance matrix](/D/covmat) is a scalar multiple of the identity matrix, a specific squared form will follow a [non-central chi-squared distribution](/D/ncchi2) where the degrees of freedom and the non-centrality paramter depend on the matrix in the quadratic form:

$$ \label{eq:mvn-cochran}
x \sim \mathcal{N}(\mu, \sigma^2 I_n) \quad \Rightarrow \quad y = x^\mathrm{T} A x /\sigma^2 \sim \chi^2\left( \mathrm{tr}(A), \mu^\mathrm{T} A \mu \right) \; .
$$

First, we [formulate the residuals](/P/mlr-mat) in terms of transformed measurements $\tilde{y}$:

$$ \label{eq:rss-y-s1}
\begin{array}{rlcl}
\hat{\varepsilon} & = \tilde{y} - \tilde{X} \hat{\beta} & \quad \text{where} \quad & \hat{\beta} = (\tilde{X}^\mathrm{T} \tilde{X})^{-1} \tilde{X}^\mathrm{T} \tilde{y} \\
& = (I_n - \tilde{P}) \tilde{y} & \quad \text{where} \quad & \tilde{P} = \tilde{X} (\tilde{X}^\mathrm{T} \tilde{X})^{-1} \tilde{X}^\mathrm{T} \\
& = \tilde{R} \tilde{y} & \quad \text{where} \quad & \tilde{R} = I_n - \tilde{P} \; .
\end{array}
$$

Next, we observe that the residual sum of squares can be represented as a quadratic form:

$$ \label{eq:rss-y-s2}
\frac{1}{\sigma^2} \sum_{i=1}^{n} \hat{\varepsilon}_i^2 = \frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{\sigma^2} = \tilde{y}^\mathrm{T} \tilde{R}^\mathrm{T} \tilde{R} \tilde{y} / \sigma^2
$$

Because the [residual-forming matrix](/D/rfmat) $\tilde{R}$ is [symmetric](/P/mlr-symm) and [idempotent](/P/mlr-idem), we have $\tilde{R}^\mathrm{T} = \tilde{R}$ and $\tilde{R}^2 = \tilde{R}$, such that:

$$ \label{eq:rss-y-s3}
\frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{\sigma^2} = \tilde{y}^\mathrm{T} \tilde{R} \tilde{y} / \sigma^2 \; .
$$

With that, we can apply Cochran's theorem given by \eqref{eq:mvn-cochran} which yields

$$ \label{eq:rss-dist}
\begin{split}
\frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{\sigma^2} &\sim \chi^2\left( \mathrm{tr}(I_n - \tilde{P}), \, \beta^\mathrm{T} \tilde{X}^\mathrm{T} \tilde{R} \tilde{X} \beta \right) \\
&\sim \chi^2\left( \mathrm{tr}(I_n) - \mathrm{tr}( \tilde{P} ), \, \beta^\mathrm{T} \tilde{X}^\mathrm{T} (I_n - \tilde{P}) \tilde{X} \beta \right) \\
&\sim \chi^2\left( \mathrm{tr}(I_n) - \mathrm{tr}( \tilde{X} (\tilde{X}^\mathrm{T} \tilde{X})^{-1} \tilde{X}^\mathrm{T} ), \, \beta^\mathrm{T} (\tilde{X}^\mathrm{T} \tilde{X} - \tilde{X}^\mathrm{T} \tilde{X} (\tilde{X}^\mathrm{T} \tilde{X})^{-1} \tilde{X}^\mathrm{T} \tilde{X}) \beta \right) \\
&\sim \chi^2\left( \mathrm{tr}(I_n) - \mathrm{tr}( \tilde{X}^\mathrm{T} \tilde{X} (\tilde{X}^\mathrm{T} \tilde{X})^{-1} ), \, \beta^\mathrm{T} (\tilde{X}^\mathrm{T} \tilde{X} - \tilde{X}^\mathrm{T} \tilde{X}) \beta \right) \\
&\sim \chi^2\left( \mathrm{tr}(I_n) - \mathrm{tr}(I_p), \, \beta^\mathrm{T} 0_{pp} \beta \right) \\
&\sim \chi^2\left( n - p, \, 0 \right) \; .
\end{split}
$$

Because a [non-central chi-squared distribution with non-centrality parameter of zero reduces to the central chi-squared distribution](/P/ncchi2-chi2), we obtain our final result:

$$ \label{eq:rss-dist-qed}
\frac{\hat{\varepsilon}^\mathrm{T} \hat{\varepsilon}}{\sigma^2} \sim \chi^2(n-p) \; .
$$