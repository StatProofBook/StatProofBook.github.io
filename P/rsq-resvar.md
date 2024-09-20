---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-03-08 10:57:03

title: "Expression of R² in terms of residual variances"
chapter: "Model Selection"
section: "Goodness-of-fit measures"
topic: "R-squared"
theorem: "Relationship to residual variance"

sources:

proof_id: "P440"
shortcut: "rsq-resvar"
username: "JoramSoch"
---


**Theorem:** Given a [linear regression model with independent observations](/D/mlr)

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; ,
$$

the [coefficient of determination](/D/rsq) can be expressed in terms of [residual variances](/D/resvar) as

$$ \label{eq:rsq-resvar}
R^2 = 1 - \frac{(n-p) \cdot \hat{\sigma}^2}{(n-1) \cdot s^2}
$$

where $n$ is the number of observations, $p$ is the number of predictors, $\hat{\sigma}^2$ is an [unbiased estimate of the noise variance](/P/resvar-unbp) $\sigma^2$ and $s^2$ is the [unbiased sample variance](/D/var-samp) of $y$.


**Proof:** The [coefficient of determination](/P/rsq-der) is given by

$$ \label{eq:rsq}
R^2 = 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}}
$$

where $\mathrm{RSS}$ is the [residual sum of squares](/D/rss)

$$ \label{eq:rss}
\mathrm{RSS} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 \quad \text{where} \quad \hat{y} = X \hat{\beta}
$$

and $\mathrm{TSS}$ is the [total sum of squares](/D/tss)

$$ \label{eq:tss}
\mathrm{TSS} = \sum_{i=1}^n (y_i - \bar{y})^2 \quad \text{where} \quad \bar{y} = \frac{1}{n} \sum_{i=1}^n y_i \; .
$$

Note that the residual sum of squares can be written as:

$$ \label{eq:rss-dev}
\mathrm{RSS} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 = \sum_{i=1}^n (y_i - (X \hat{\beta})_i)^2 = (y-X\hat{\beta})^\mathrm{T} (y-X\hat{\beta}) \; .
$$

The [unbiased estimate of the noise variance](/P/resvar-unbp) is

$$ \label{eq:sigma-unb}
\hat{\sigma}^2 = \frac{1}{n-p} (y-X\hat{\beta})^\mathrm{T} (y-X\hat{\beta})
$$

and the [unbiased sample variance of the dependent variable](/D/var-samp) is

$$ \label{eq:var-samp-unb}
s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (y_i - \bar{y})^2 \; ,
$$

Combining \eqref{eq:rsq}, \eqref{eq:rss} and \eqref{eq:tss}, the coefficient of determination can be rewritten as follows:

$$ \label{eq:rsq-resvar-qed}
\begin{split}
R^2 &\overset{\eqref{eq:rsq}}{=} 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}} \\
&\overset{\eqref{eq:tss}}{=} 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \\
&\overset{\eqref{eq:rss-dev}}{=} 1 - \frac{(y-X\hat{\beta})^\mathrm{T} (y-X\hat{\beta})}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \\
&= 1 - \frac{(n-p) \cdot \frac{1}{n-p} (y-X\hat{\beta})^\mathrm{T} (y-X\hat{\beta})}{(n-1) \cdot \frac{1}{n-1} \sum_{i=1}^{n} (y_i - \bar{y})^2} \\
&\overset{\eqref{eq:sigma-unb}}{=} 1 - \frac{(n-p) \cdot \hat{\sigma}^2}{(n-1) \cdot \frac{1}{n-1} \sum_{i=1}^{n} (y_i - \bar{y})^2} \\
&\overset{\eqref{eq:var-samp-unb}}{=} 1 - \frac{(n-p) \cdot \hat{\sigma}^2}{(n-1) \cdot s^2} \; .
\end{split}
$$

This completes the proof.