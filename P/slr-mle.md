---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-11-16 08:34:00

title: "Maximum likelihood estimation for simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Maximum likelihood estimation"

sources:

proof_id: "P287"
shortcut: "slr-mle"
username: "JoramSoch"
---


**Theorem:** Given a [simple linear regression model](/D/mlr) with independent observations

$$ \label{eq:slr}
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2), \; i = 1,\ldots,n \; ,
$$

the [maximum likelihood estimates](/D/mle) of $\beta_0$, $\beta_1$ and $\sigma^2$ are given by

$$ \label{eq:slr-mle}
\begin{split}
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1 \bar{x} \\
\hat{\beta}_1 &= \frac{s_{xy}}{s_x^2} \\
\hat{\sigma}^2 &= \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2
\end{split}
$$

where $\bar{x}$ and $\bar{y}$ are the [sample means](/D/mean-samp), $s_x^2$ is the [sample variance](/D/var-samp) of $x$ and $s_{xy}$ is the [sample covariance](/D/cov-samp) between $x$ and $y$.


**Proof:** With the [probability density function of the normal distribution](/P/norm-pdf) and [probability under independence](/D/ind), the linear regression equation \eqref{eq:slr} implies the following [likelihood function](/D/lf)

$$ \label{eq:slr-lf}
\begin{split}
p(y|\beta_0,\beta_1,\sigma^2) &= \prod_{i=1}^n p(y_i|\beta_0,\beta_1,\sigma^2) \\
&= \prod_{i=1}^n \mathcal{N}(y_i; \beta_0 + \beta_1 x_i, \sigma^2) \\
&= \prod_{i=1}^n \frac{1}{\sqrt{2 \pi \sigma}} \cdot \exp \left[ -\frac{(y_i - \beta_0 - \beta_1 x_i)^2}{2 \sigma^2} \right] \\
&= \frac{1}{\sqrt{(2 \pi \sigma^2)^n}} \cdot \exp\left[ -\frac{1}{2 \sigma^2} \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2 \right]
\end{split}
$$

and the [log-likelihood function](/D/llf)

$$ \label{eq:slr-ll}
\begin{split}
\mathrm{LL}(\beta_0,\beta_1,\sigma^2) &= \log p(y|\beta_0,\beta_1,\sigma^2) \\
&= -\frac{n}{2} \log(2\pi) - \frac{n}{2} \log (\sigma^2) -\frac{1}{2 \sigma^2} \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)^2 \; .
\end{split}
$$

<br>
The derivative of the log-likelihood function \eqref{eq:slr-ll} with respect to $\beta_0$ is

$$ \label{eq:dLL-dbeta0}
\frac{\mathrm{d}\mathrm{LL}(\beta_0,\beta_1,\sigma^2)}{\mathrm{d}\beta_0} = \frac{1}{\sigma^2} \sum_{i=1}^n (y_i - \beta_0 - \beta_1 x_i)
$$

and setting this derivative to zero gives the MLE for $\beta_0$:

$$ \label{eq:beta0-mle}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\beta}_0,\hat{\beta}_1,\hat{\sigma}^2)}{\mathrm{d}\beta_0} &= 0 \\
0 &= \frac{1}{\hat{\sigma}^2} \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) \\
0 &= \sum_{i=1}^n y_i - n \hat{\beta}_0 - \hat{\beta}_1 \sum_{i=1}^n x_i \\
\hat{\beta}_0 &= \frac{1}{n} \sum_{i=1}^n y_i - \hat{\beta}_1 \frac{1}{n} \sum_{i=1}^n x_i \\
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1 \bar{x} \; .
\end{split}
$$

<br>
The derivative of the log-likelihood function \eqref{eq:slr-ll} at $\hat{\beta}_0$ with respect to $\beta_1$ is

$$ \label{eq:dLL-dbeta1}
\frac{\mathrm{d}\mathrm{LL}(\hat{\beta}_0,\beta_1,\sigma^2)}{\mathrm{d}\beta_1} = \frac{1}{\sigma^2} \sum_{i=1}^n (x_i y_i - \hat{\beta}_0 x_i - \beta_1 x_i^2) \\
$$

and setting this derivative to zero gives the MLE for $\beta_1$:

$$ \label{eq:beta1-mle}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\beta}_0,\hat{\beta}_1,\hat{\sigma}^2)}{\mathrm{d}\beta_1} &= 0 \\
0 &= \frac{1}{\hat{\sigma}^2} \sum_{i=1}^n (x_i y_i - \hat{\beta}_0 x_i - \hat{\beta}_1 x_i^2) \\
0 &= \sum_{i=1}^n x_i y_i - \hat{\beta}_0 \sum_{i=1}^n x_i - \hat{\beta}_1 \sum_{i=1}^n x_i^2) \\
0 &\overset{\eqref{eq:beta0-mle}}{=} \sum_{i=1}^n x_i y_i - (\bar{y} - \hat{\beta}_1 \bar{x}) \sum_{i=1}^n x_i - \hat{\beta}_1 \sum_{i=1}^n x_i^2 \\
0 &= \sum_{i=1}^n x_i y_i - \bar{y} \sum_{i=1}^n x_i + \hat{\beta}_1 \bar{x} \sum_{i=1}^n x_i - \hat{\beta}_1 \sum_{i=1}^n x_i^2 \\
0 &= \sum_{i=1}^n x_i y_i - n \bar{x} \bar{y} + \hat{\beta}_1 n \bar{x}^2 - \hat{\beta}_1 \sum_{i=1}^n x_i^2 \\
\hat{\beta}_1 &= \frac{\sum_{i=1}^n x_i y_i - \sum_{i=1}^n \bar{x} \bar{y}}{\sum_{i=1}^n x_i^2 - \sum_{i=1}^n \bar{x}^2} \\
\hat{\beta}_1 &= \frac{\sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2} \\
\hat{\beta}_1 &= \frac{s_{xy}}{s_x^2} \; .
\end{split}
$$

<br>
The derivative of the log-likelihood function \eqref{eq:slr-ll} at $(\hat{\beta}_0,\hat{\beta}_1)$ with respect to $\sigma^2$ is

$$ \label{eq:dLL-ds2}
\frac{\mathrm{d}\mathrm{LL}(\hat{\beta}_0,\hat{\beta}_1,\sigma^2)}{\mathrm{d}\sigma^2} = - \frac{n}{2\sigma^2} + \frac{1}{2(\sigma^2)^2} \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2
$$

and setting this derivative to zero gives the MLE for $\sigma^2$:

$$ \label{eq:s2-mle}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\beta}_0,\hat{\beta}_1,\hat{\sigma}^2)}{\mathrm{d}\sigma^2} &= 0 \\
0 &= - \frac{n}{2\hat{\sigma}^2} + \frac{1}{2(\hat{\sigma}^2)^2} \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2 \\
\frac{n}{2\hat{\sigma}^2} &= \frac{1}{2(\hat{\sigma}^2)^2} \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2 \\
\hat{\sigma}^2 &= \frac{1}{n} \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2 \; .
\end{split}
$$

<br>
Together, \eqref{eq:beta0-mle}, \eqref{eq:beta1-mle} and \eqref{eq:s2-mle} constitute the MLE for simple linear regression.