---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-11-09 11:34:00

title: "Sums of squares for simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Sums of squares"

sources:

proof_id: "P284"
shortcut: "slr-sss"
username: "JoramSoch"
---


**Theorem:** Under [ordinary least squares](/P/slr-ols) for [simple linear regression](/D/slr), [total](/D/tss), [explained](/D/ess) and [residual](/D/rss) sums of squares are given by

$$ \label{eq:slr-sss}
\begin{split}
\mathrm{TSS} &= (n-1) \, s_y^2 \\
\mathrm{ESS} &= (n-1) \, \frac{s_{xy}^2}{s_x^2} \\
\mathrm{RSS} &= (n-1) \left( s_y^2 - \frac{s_{xy}^2}{s_x^2} \right)
\end{split}
$$

where $s_x^2$ and $s_y^2$ are the [sample variances](/D/var-samp) of $x$ and $y$ and $s_{xy}$ is the [sample covariance](/D/cov-samp) between $x$ and $y$.


**Proof:** The [ordinary least squares parameter estimates](/P/slr-ols) are given by

$$ \label{eq:slr-ols}
\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x} \quad \text{and} \quad \hat{\beta}_1 = \frac{s_{xy}}{s_x^2} \; .
$$

<br>
1) The [total sum of squares](/D/tss) is defined as

$$ \label{eq:TSS}
\mathrm{TSS} = \sum_{i=1}^{n} (y_i - \bar{y})^2
$$

which can be reformulated as follows:

$$ \label{eq:TSS-qed}
\begin{split}
\mathrm{TSS} &= \sum_{i=1}^{n} (y_i - \bar{y})^2 \\
&= (n-1) \frac{1}{n-1} \sum_{i=1}^{n} (y_i - \bar{y})^2 \\
&= (n-1) s_y^2 \; .
\end{split}
$$

<br>
2) The [explained sum of squares](/D/ess) is defined as

$$ \label{eq:ESS}
\mathrm{ESS} = \sum_{i=1}^n (\hat{y}_i - \bar{y})^2 \quad \text{where} \quad \hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i
$$

which, with the OLS parameter estimats, becomes:

$$ \label{eq:ESS-qed}
\begin{split}
\mathrm{ESS} &= \sum_{i=1}^n (\hat{y}_i - \bar{y})^2 \\
&= \sum_{i=1}^n (\hat{\beta}_0 + \hat{\beta}_1 x_i - \bar{y})^2 \\
&\overset{\eqref{eq:slr-ols}}{=} \sum_{i=1}^n (\bar{y} - \hat{\beta}_1 \bar{x} + \hat{\beta}_1 x_i - \bar{y})^2 \\
&= \sum_{i=1}^n \left( \hat{\beta}_1 (x_i - \bar{x}) \right)^2 \\
&\overset{\eqref{eq:slr-ols}}{=} \sum_{i=1}^n \left( \frac{s_{xy}}{s_x^2} (x_i - \bar{x}) \right)^2 \\
&= \left( \frac{s_{xy}}{s_x^2} \right)^2 \sum_{i=1}^n (x_i - \bar{x})^2 \\
&= \left( \frac{s_{xy}}{s_x^2} \right)^2 (n-1) s_x^2 \\
&= (n-1) \, \frac{s_{xy}^2}{s_x^2} \; .
\end{split}
$$

<br>
3) The [residual sum of squares](/D/rss) is defined as

$$ \label{eq:RSS}
\mathrm{RSS} = \sum_{i=1}^n (y_i - \hat{y}_i)^2 \quad \text{where} \quad \hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i
$$

which, with the OLS parameter estimats, becomes:

$$ \label{eq:RSS-qed}
\begin{split}
\mathrm{RSS} &= \sum_{i=1}^n (y_i - \hat{y}_i)^2 \\
&= \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2 \\
&\overset{\eqref{eq:slr-ols}}{=} \sum_{i=1}^n (y_i - \bar{y} + \hat{\beta}_1 \bar{x} - \hat{\beta}_1 x_i)^2 \\
&= \sum_{i=1}^n \left( (y_i - \bar{y}) - \hat{\beta}_1 (x_i - \bar{x}) \right)^2 \\
&= \sum_{i=1}^n \left( (y_i - \bar{y})^2 - 2 \hat{\beta}_1 (x_i - \bar{x}) (y_i - \bar{y}) + \hat{\beta}_1^2 (x_i - \bar{x})^2 \right) \\
&= \sum_{i=1}^n (y_i - \bar{y})^2 - 2 \hat{\beta}_1 \sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y}) + \hat{\beta}_1^2 \sum_{i=1}^n (x_i - \bar{x})^2 \\
&= (n-1) \, s_y^2 - 2 (n-1) \, \hat{\beta}_1 \, s_{xy} + (n-1) \, \hat{\beta}_1^2 \, s_x^2 \\
&\overset{\eqref{eq:slr-ols}}{=} (n-1) \, s_y^2 - 2 (n-1) \left( \frac{s_{xy}}{s_x^2} \right) s_{xy} + (n-1) \left( \frac{s_{xy}}{s_x^2} \right)^2 s_x^2 \\
&= (n-1) \, s_y^2 - (n-1) \, \frac{s_{xy}^2}{s_x^2} \\
&= (n-1) \left( s_y^2 - \frac{s_{xy}^2}{s_x^2} \right) \; .
\end{split}
$$