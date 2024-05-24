---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-05-24 13:19:05

title: "Statistical test for comparing simple linear regression model with and without slope parameter"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "F-test for model comparison"

sources:

proof_id: "P453"
shortcut: "slr-fcomp"
username: "JoramSoch"
---


**Theorem:** Consider a [simple linear regression model](/D/slr) with independent observations

$$ \label{eq:slr}
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2), \; i = 1,\ldots,n \; ,
$$

and the [parameter estimates](/P/slr-mle)

$$ \label{eq:slr-est}
\begin{split}
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1 \bar{x} \\
\hat{\beta}_1 &= \frac{s_{xy}}{s_x^2} \\
\hat{\sigma}^2 &= \frac{1}{n-2} \sum_{i=1}^{n} (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2 \; .
\end{split}
$$

Then, the [test statistic](/D/tstat)

$$ \label{eq:slr-f-comp}
F = \frac{s_{xy}^2/s_x^2}{\hat{\sigma}^2/(n-1)}
$$

follows an [F-distribution](/D/f)

$$ \label{eq:slr-f-comp-dist}
F \sim \mathrm{F}(1, n-2)
$$

under the scenario that the data were generated using a model in which the [slope parameter](/D/slr) is zero:

$$ \label{eq:slr-f-comp-h0}
H_0: \; \beta_1 = 0 \; .
$$


**Proof:** In [multiple linear regression](/D/mlr), the [contrast-based F-test](/P/mlr-f) is based on the [F-statistic](/D/tstat)

$$ \label{eq:mlr-f}
F = \hat{\beta}^\mathrm{T} C \left( \hat{\sigma}^2 C^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C \right)^{-1} C^\mathrm{T} \hat{\beta} / q
$$

which follows an [F-distribution](/D/f) under the [null hypothesis](/D/h0) that the product of the [contrast matrix](/D/fcon) $C \in \mathbb{R}^{p \times q}$ and the [regression coefficients](/D/mlr) is a zero vector: 

$$ \label{eq:mlr-f-dist-h0}
F \sim \mathrm{F}(q, n-p), \quad \text{if} \quad C^\mathrm{T} \beta = 0_q = \left[ 0, \ldots, 0 \right]^\mathrm{T} \; .
$$

Since [simple linear regression is a special case of multiple linear regression](/P/slr-mlr), we have the following quantities, if we want to compare the regression model against a model without the slope parameter:

$$ \label{eq:slr-mlr}
\beta = \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right], \;
\hat{\beta} = \left[ \begin{matrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{matrix} \right], \;
C = \left[ \begin{matrix} 0 \\ 1 \end{matrix} \right], \;
X = \left[ \begin{matrix} 1_n & x \end{matrix} \right], \;
V = I_n \; .
$$

Thus, we have the null hypothesis

$$ \label{eq:slr-f-comp-h0-qed}
H_0: \; C^\mathrm{T} \beta = \left[ \begin{matrix} 0 \\ 1 \end{matrix} \right]^\mathrm{T} \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right] = \beta_1 = 0
$$

and the contrast estimate

$$ \label{eq:slr-f-comp-CTb}
C^\mathrm{T} \hat{\beta} = \left[ \begin{matrix} 0 \\ 1 \end{matrix} \right]^\mathrm{T} \left[ \begin{matrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{matrix} \right] = \hat{\beta}_1 = \frac{s_{xy}}{s_x^2} \; .
$$

Moreover, when [deriving the distribution of ordinary least squares parameter estimates for simple linear regression with independent observations](/P/slr-olsdist), we have identified the parameter covariance matrix as

$$ \label{eq:slr-XTX-inv}
(X^\mathrm{T} X)^{-1} = \frac{1}{(n-1) \, s_x^2} \cdot \left[ \begin{matrix} x^\mathrm{T}x/n & -\bar{x} \\ -\bar{x} & 1 \end{matrix} \right] \; .
$$

Plugging \eqref{eq:slr-mlr}, \eqref{eq:slr-f-comp-CTb}, \eqref{eq:slr-XTX-inv} and \eqref{eq:slr-est} into \eqref{eq:mlr-f}, the test statistic becomes

$$ \label{eq:slr-f-comp-qed}
\begin{split}
F &= \hat{\beta}^\mathrm{T} C \left( \hat{\sigma}^2 C^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C \right)^{-1} C^\mathrm{T} \hat{\beta} / q \\
&= \left( \frac{s_{xy}}{s_x^2} \right) \left( \hat{\sigma}^2 \left[ \begin{matrix} 0 & 1 \end{matrix} \right] \left( \frac{1}{(n-1) \, s_x^2} \cdot \left[ \begin{matrix} x^\mathrm{T}x/n & -\bar{x} \\ -\bar{x} & 1 \end{matrix} \right] \right) \left[ \begin{matrix} 0 & 1 \end{matrix} \right]^\mathrm{T} \right)^{-1} \left( \frac{s_{xy}}{s_x^2} \right) / 1 \\
&= \frac{s_{xy}^2/(s_x^2)^2}{\hat{\sigma}^2/((n-1) \, s_x^2)} \\
&= \frac{s_{xy}^2/s_x^2}{\hat{\sigma}^2/(n-1)} \; .
\end{split}
$$

Finally, because $C = \left[ \begin{matrix} 0 & 1 \end{matrix} \right]^\mathrm{T} \in \mathbb{R}^{2 \times 1}$ and $X = \left[ \begin{matrix} 1_n & x \end{matrix} \right] \in \mathbb{R}^{n \times 2}$, we have $p = 2$ and $q = 1$, such that from \eqref{eq:mlr-f-dist-h0} it follows that

$$ \label{eq:slr-f-comp-dist-qed}
\begin{split}
F \sim \mathrm{F}(1, n-2), \quad \text{if} \quad \beta_1 = 0 \; .
\end{split}
$$