---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-06-20 12:16:00

title: "Maximum likelihood estimation for bivariate normally distributed data"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "Multivariate Gaussian"
definition: "Maximum likelihood estimation (p = 2)"

sources:

proof_id: "P503"
shortcut: "bvn-mle"
username: "JoramSoch"
---


**Theorem:** Let there be a [bivariate normally distributed data set](/D/bvn-data) $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$:

$$ \label{eq:bvn-data}
y_i = \left[ \begin{matrix} y_{i1} \\ y_{i2} \end{matrix} \right] \sim \mathcal{N}\left( \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right], \left[ \begin{matrix} \sigma_1^2 & \rho \sigma_1 \sigma_2 \\ \rho \sigma_1 \sigma_2 & \sigma_2^2 \end{matrix} \right] \right), \quad i = 1, \ldots, n \; .
$$

Then, the [maximum likelihood estimates](/D/mle) of $\mu_1$, $\mu_2$, $\sigma_1^2$, $\sigma_2^2$ and $\rho$ are given by

$$ \label{eq:bvn-mle}
\begin{split}
\hat{\mu}_1      &= \frac{1}{n} \sum_{i=1}^n y_{i1} \\
\hat{\mu}_2      &= \frac{1}{n} \sum_{i=1}^n y_{i2} \\
\hat{\sigma}_1^2 &= \frac{1}{n} \sum_{i=1}^n (y_{i1} - \hat{\mu}_1)^2 \\
\hat{\sigma}_2^2 &= \frac{1}{n} \sum_{i=1}^n (y_{i2} - \hat{\mu}_2)^2 \\
\hat{\rho}       &= \frac{\frac{1}{n} \sum_{i=1}^n (y_{i1} - \hat{\mu}_1) (y_{i2} - \hat{\mu}_2)}{\sqrt{\hat{\sigma}_1^2} \sqrt{\hat{\sigma}_2^2}} \; .
\end{split}
$$


**Proof:** This is a special case of [multivariate normally distributed data](/D/mvn-data)

$$ \label{eq:mvn-data}
y_i = \left[ \begin{matrix} y_{i1} \\ \vdots \\ y_{ip} \end{matrix} \right] \sim \mathcal{N}\left( \mu, \Sigma \right), \quad i = 1, \ldots, n
$$

for which [maximum likelihood estimates are given by](/D/mvn-mle)

$$ \label{eq:mvn-mle}
\begin{split}
\hat{\mu}    &= \frac{1}{n} \sum_{i=1}^n y_i \\
\hat{\Sigma} &= \frac{1}{n} \sum_{i=1}^n (y_i - \hat{\mu}) (y_i - \hat{\mu})^\mathrm{T} \; .
\end{split}
$$

Applying this to \eqref{eq:bvn-data} by setting $p=2$, we obtain:

$$ \label{eq:bvn-mle-s1}
\begin{split}
\hat{\mu}    &= \left[ \begin{matrix} \frac{1}{n} \sum_{i=1}^n y_{i1} \\
                                      \frac{1}{n} \sum_{i=1}^n y_{i2} \end{matrix} \right] \\
\hat{\Sigma} &= \left[ \begin{matrix} \frac{1}{n} \sum_{i=1}^n (y_{i1}-\hat{\mu}_1) (y_{i1}-\hat{\mu}_1) &
									  \frac{1}{n} \sum_{i=1}^n (y_{i1}-\hat{\mu}_1) (y_{i2}-\hat{\mu}_2) \\
									  \frac{1}{n} \sum_{i=1}^n (y_{i2}-\hat{\mu}_2) (y_{i1}-\hat{\mu}_1) &
									  \frac{1}{n} \sum_{i=1}^n (y_{i2}-\hat{\mu}_2) (y_{i2}-\hat{\mu}_2) \end{matrix} \right] \; .
\end{split}
$$

Equating this with the [parametrized bivariate normal estimates](/P/bvn-snorm)

$$ \label{eq:bvn-mle-s2}
\hat{\mu}    = \left[ \begin{matrix} \hat{\mu}_1 \\ \hat{\mu}_2 \end{matrix} \right] \quad \text{and} \quad
\hat{\Sigma} = \left[ \begin{matrix} \hat{\sigma}_1^2 & \hat{\rho} \hat{\sigma}_1 \hat{\sigma}_2 \\
									 \hat{\rho} \hat{\sigma}_1 \hat{\sigma}_2 & \hat{\sigma}_2^2 \end{matrix} \right] \; ,
$$

we obtain ML estimates for the means as

$$ \label{eq:bvn-mle-mean}
\begin{split}
\hat{\mu}_1      &= \frac{1}{n} \sum_{i=1}^n y_{i1} \\
\hat{\mu}_2      &= \frac{1}{n} \sum_{i=1}^n y_{i2} \; ,
\end{split}
$$

we obtain ML estimates for the variances as

$$ \label{eq:bvn-mle-var}
\begin{split}
\hat{\sigma}_1^2 &= \frac{1}{n} \sum_{i=1}^n (y_{i1} - \hat{\mu}_1)^2 \\
\hat{\sigma}_2^2 &= \frac{1}{n} \sum_{i=1}^n (y_{i2} - \hat{\mu}_2)^2
\end{split}
$$

and we obtain an ML estimate for the correlation as:

$$ \label{eq:bvn-mle-corr}
\begin{split}
\hat{\rho} \hat{\sigma}_1 \hat{\sigma}_2 &= \frac{1}{n} \sum_{i=1}^n (y_{i1}-\hat{\mu}_1) (y_{i2}-\hat{\mu}_2) \\
\hat{\rho} &= \frac{\frac{1}{n} \sum_{i=1}^n (y_{i1}-\hat{\mu}_1) (y_{i2}-\hat{\mu}_2)}{\hat{\sigma}_1 \hat{\sigma}_2} \\
\hat{\rho} &= \frac{\frac{1}{n} \sum_{i=1}^n (y_{i1} - \hat{\mu}_1) (y_{i2} - \hat{\mu}_2)}{\sqrt{\hat{\sigma}_1^2} \sqrt{\hat{\sigma}_2^2}} \\
\hat{\rho} &= \frac{\frac{1}{n} \sum_{i=1}^n (y_{i1}-\hat{\mu}_1) (y_{i2}-\hat{\mu}_2)}{\sqrt{\frac{1}{n} \sum_{i=1}^n (y_{i1} - \hat{\mu}_1)^2} \sqrt{\frac{1}{n} \sum_{i=1}^n (y_{i2} - \hat{\mu}_2)^2}} \; .
\end{split}
$$

Together, \eqref{eq:bvn-mle-mean}, \eqref{eq:bvn-mle-var} and \eqref{eq:bvn-mle-corr} constitute the [maximum likelihood estimates](/D/mle) for [bivariate normally distributed data](/D/bvn-data).