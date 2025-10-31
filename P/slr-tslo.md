---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2024-05-17 12:33:03

title: "Statistical test for slope parameter in simple linear regression model"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "t-test for slope parameter"

sources:

proof_id: "P452"
shortcut: "slr-tslo"
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

where $\bar{x}$ and $\bar{y}$ are the [sample means](/D/mean-samp) of the $x_i$ and $y_i$, $s_{xy}$ is the [sample covariance](/D/cov-samp) of the $x_i$ and $y_i$ and $s_x^2$ is the [sample variance](/D/var-samp) of the $x_i$.

Then, the [test statistic](/D/tstat)

$$ \label{eq:slr-t-slo}
t_1 = \frac{s_{xy}/s_x^2}{\sqrt{\hat{\sigma}^2 \; \sigma_1}}
$$

with $\sigma_1$ equal to the first diagonal element of the [parameter covariance matrix](/P/slr-olsdist)

$$ \label{eq:slr-t-slo-sig}
\sigma_1 = \frac{1}{\sum_{i=1}^{n} \left( x_i - \bar{x} \right)^2}
$$

follows a [t-distribution](/D/t)

$$ \label{eq:slr-t-slo-dist}
t_1 \sim \mathrm{t}(n-2)
$$

under the [null hypothesis](/D/h0) that the [slope parameter](/D/slr) is zero:

$$ \label{eq:slr-t-slo-h0}
H_0: \; \beta_1 = 0 \; .
$$


**Proof:** In [multiple linear regression](/D/mlr), the [contrast-based t-test](/P/mlr-t) is based on the [t-statistic](/D/tstat)

$$ \label{eq:mlr-t}
t = \frac{c^\mathrm{T} \hat{\beta}}{\sqrt{\hat{\sigma}^2 c^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} c}}
$$

which follows a [t-distribution](/D/t) under the [null hypothesis](/D/h0) that the scalar product of the [contrast vector](/D/tcon) and the [regression coefficients](/D/mlr) is zero: 

$$ \label{eq:mlr-t-dist-h0}
t \sim \mathrm{t}(n-p), \quad \text{if} \quad c^\mathrm{T} \beta = 0 \; .
$$

Since [simple linear regression is a special case of multiple linear regression](/P/slr-mlr), in the present case we have the following quantities:

$$ \label{eq:slr-mlr}
\beta = \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right], \;
\hat{\beta} = \left[ \begin{matrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{matrix} \right], \;
c_1 = \left[ \begin{matrix} 0 \\ 1 \end{matrix} \right], \;
X = \left[ \begin{matrix} 1_n & x \end{matrix} \right], \;
V = I_n \; .
$$

Thus, we have the null hypothesis

$$ \label{eq:slr-t-slo-h0-qed}
H_0: \; c_1^\mathrm{T} \beta = \left[ \begin{matrix} 0 \\ 1 \end{matrix} \right]^\mathrm{T} \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right] = \beta_1 = 0
$$

and the contrast estimate

$$ \label{eq:slr-t-slo-cTb}
c_1^\mathrm{T} \hat{\beta} = \left[ \begin{matrix} 0 \\ 1 \end{matrix} \right]^\mathrm{T} \left[ \begin{matrix} \hat{\beta}_0 \\ \hat{\beta}_1 \end{matrix} \right] = \hat{\beta}_1 = \frac{s_{xy}}{s_x^2} \; .
$$

Moreover, when [deriving the distribution of ordinary least squares parameter estimates for simple linear regression with independent observations](/P/slr-olsdist), we have identified the parameter covariance matrix as

$$ \label{eq:slr-XTX-inv}
(X^\mathrm{T} X)^{-1} = \frac{1}{(n-1) \, s_x^2} \cdot \left[ \begin{matrix} x^\mathrm{T}x/n & -\bar{x} \\ -\bar{x} & 1 \end{matrix} \right] \; .
$$

Plugging \eqref{eq:slr-mlr}, \eqref{eq:slr-t-slo-cTb}, \eqref{eq:slr-XTX-inv} and \eqref{eq:slr-est} into \eqref{eq:mlr-t}, the test statistic becomes

$$ \label{eq:slr-t-slo-qed}
\begin{split}
t_1 &= \frac{c_1^\mathrm{T} \hat{\beta}}{\sqrt{\hat{\sigma}^2 \; c_1^\mathrm{T} (X^\mathrm{T} X)^{-1} c_1}} \\
&= \frac{\left[ \begin{matrix} 0 & 1 \end{matrix} \right] \left[ \begin{matrix} \hat{\beta}_0 & \hat{\beta}_1 \end{matrix} \right]^\mathrm{T}}{\sqrt{\hat{\sigma}^2 \left[ \begin{matrix} 0 & 1 \end{matrix} \right] (X^\mathrm{T} X)^{-1} \left[ \begin{matrix} 0 & 1 \end{matrix} \right]^\mathrm{T}}} \\
&= \frac{\left[ \begin{matrix} 0 & 1 \end{matrix} \right] \left[ \begin{matrix} \hat{\beta}_0 & \hat{\beta}_1 \end{matrix} \right]^\mathrm{T}}{\sqrt{\hat{\sigma}^2 \left[ \begin{matrix} 0 & 1 \end{matrix} \right] \left( \frac{1}{(n-1) \, s_x^2} \cdot \left[ \begin{matrix} x^\mathrm{T}x/n & -\bar{x} \\ -\bar{x} & 1 \end{matrix} \right] \right) \left[ \begin{matrix} 0 & 1 \end{matrix} \right]^\mathrm{T}}} \\
&= \frac{\hat{\beta}_1}{\sqrt{\hat{\sigma}^2 \left( \frac{1}{(n-1) \, s_x^2} \right)}} \\
&= \frac{\hat{\beta}_1}{\sqrt{\hat{\sigma}^2 / \sum_{i=1}^{n} \left( x_i - \bar{x} \right)^2}} \\
&= \frac{s_{xy}/s_x^2}{\sqrt{\hat{\sigma}^2 \; \sigma_1}} \; .
\end{split}
$$

Finally, because $X = \left[ \begin{matrix} 1_n & x \end{matrix} \right]$ is an $n \times 2$ matrix, we have $p = 2$, such that from \eqref{eq:mlr-t-dist-h0} it follows that

$$ \label{eq:slr-t-slo-dist-qed}
\begin{split}
t_1 \sim \mathrm{t}(n-2), \quad \text{if} \quad \beta_1 = 0 \; .
\end{split}
$$