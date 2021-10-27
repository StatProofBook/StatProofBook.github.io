---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-27 12:38:00

title: "Effects of mean-centering on parameter estimates for simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Effects of mean-centering"

sources:

proof_id: "P274"
shortcut: "slr-meancent"
username: "JoramSoch"
---


**Theorem:** In [simple linear regression](/D/slr), when the independent variable $y$ and/or the dependent variable $x$ are [mean-centered](/D/mean), the [ordinary least squares](/P/slr-ols) estimate for the intercept changes, but that of the slope does not.

**Proof:**

1) Under unaltered $y$ and $x$, [ordinary least squares estimates for simple linear regression](/P/slr-ols) are

$$ \label{eq:slr-ols}
\begin{split}
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1 \bar{x} \\
\hat{\beta}_1 &= \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} = \frac{s_{xy}}{s_x^2}
\end{split}
$$

with [sample means](/D/mean-samp) $\bar{x}$ and $\bar{y}$, [sample variance](/D/var-samp) $s_x^2$ and [sample covariance](/D/cov-samp) $s_{xy}$, such that $\beta_0$ estimates "the mean $y$ at $x = 0$".

<br>
2) Let $\tilde{x}$ be the mean-centered [covariate vector](/D/slr):

$$ \label{eq:slr-meancent-x}
\tilde{x}_i = x_i - \bar{x} \quad \Rightarrow \quad \bar{\tilde{x}} = 0 \; .
$$

Under this condition, the parameter estimates become

$$ \label{eq:slr-ols-meancent-x}
\begin{split}
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1 \bar{\tilde{x}} \\
&= \bar{y} \\
\hat{\beta}_1 &= \frac{\sum_{i=1}^n (\tilde{x}_i - \bar{\tilde{x}}) (y_i - \bar{y})}{\sum_{i=1}^n (\tilde{x}_i - \bar{\tilde{x}})^2} \\
&= \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} = \frac{s_{xy}}{s_x^2}
\end{split}
$$

and we can see that $\hat{\beta}_1(\tilde{x},y) = \hat{\beta}_1(x,y)$, but $\hat{\beta}_0(\tilde{x},y) \neq \hat{\beta}_0(x,y)$, specifically $\beta_0$ now estimates "the mean $y$ at the mean $x$".


<br> 
3) Let $\tilde{y}$ be the mean-centered [data vector](/D/slr):

$$ \label{eq:slr-meancent-y}
\tilde{y}_i = y_i - \bar{y} \quad \Rightarrow \quad \bar{\tilde{y}} = 0 \; .
$$

Under this condition, the parameter estimates become

$$ \label{eq:slr-ols-meancent-y}
\begin{split}
\hat{\beta}_0 &= \bar{\tilde{y}} - \hat{\beta}_1 \bar{x} \\
&= - \hat{\beta}_1 \bar{x} \\
\hat{\beta}_1 &= \frac{\sum_{i=1}^n (x_i - \bar{x}) (\tilde{y}_i - \bar{\tilde{y}})}{\sum_{i=1}^n (x_i - \bar{x})^2} \\
&= \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} = \frac{s_{xy}}{s_x^2}
\end{split}
$$

and we can see that $\hat{\beta}_1(x,\tilde{y}) = \hat{\beta}_1(x,y)$, but $\hat{\beta}_0(x,\tilde{y}) \neq \hat{\beta}_0(x,y)$, specifically $\beta_0$ now estimates "the mean $x$, multiplied with the negative slope".

<br> 
4) Finally, consider mean-centering both $x$ and $y$::

$$ \label{eq:slr-meancent-xy}
\begin{split}
\tilde{x}_i = x_i - \bar{x} \quad &\Rightarrow \quad \bar{\tilde{x}} = 0 \\
\tilde{y}_i = y_i - \bar{y} \quad &\Rightarrow \quad \bar{\tilde{y}} = 0 \; .
\end{split}
$$

Under this condition, the parameter estimates become

$$ \label{eq:slr-ols-meancent-xy}
\begin{split}
\hat{\beta}_0 &= \bar{\tilde{y}} - \hat{\beta}_1 \bar{\tilde{x}} \\
&= 0 \\
\hat{\beta}_1 &= \frac{\sum_{i=1}^n (\tilde{x}_i - \bar{\tilde{x}}) (\tilde{y}_i - \bar{\tilde{y}})}{\sum_{i=1}^n (\tilde{x}_i - \bar{\tilde{x}})^2} \\
&= \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} = \frac{s_{xy}}{s_x^2}
\end{split}
$$

and we can see that $\hat{\beta}_1(\tilde{x},\tilde{y}) = \hat{\beta}_1(x,y)$, but $\hat{\beta}_0(\tilde{x},\tilde{y}) \neq \hat{\beta}_0(x,y)$, specifically $\beta_0$ is now forced to become zero.