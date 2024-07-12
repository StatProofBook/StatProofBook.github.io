---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-07-12 14:54:30

title: "Partition of sums of squares for simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Partition of sums of squares"

sources:
  - authors: "Ostwald, Dirk"
    year: 2023
    title: "Korrelation"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (2), Folien 19-23"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2023/Allgemeines+Lineares+Modell/2_Korrelation.pdf"
  - authors: "Manabu, Hayashi"
    year: 2021
    title: "TSS = RSS + ESS | Simple Linear Regression"
    in: "YouTube"
    pages: "retrieved on 2024-07-12"
    url: "https://www.youtube.com/watch?v=N7pHym1L9b0"

proof_id: "P461"
shortcut: "slr-pss"
username: "JoramSoch"
---


**Theorem:** Assume a [simple linear regression model](/D/slr) with independent observations

$$ \label{eq:slr}
y = \beta_0 + \beta_1 x + \varepsilon, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2), \; i = 1,\ldots,n
$$

where $\beta_0$ and $\beta_1$ are [intercept and slope parameter](/D/slr), respectively. Then, it holds that

$$ \label{eq:slr-pss}
\mathrm{TSS} = \mathrm{ESS} + \mathrm{RSS}
$$

where $\mathrm{TSS}$ is the [total sum of squares](/D/tss), $\mathrm{ESS}$ is the [explained sum of squares](/D/ess) and $\mathrm{RSS}$ is the [residual sum of squares](/D/rss).


**Proof:** For simple linear regression, [total, explained and residual sum squares are given by](/P/slr-sss)

$$ \label{eq:slr-sss}
\begin{split}
\mathrm{TSS} &= \sum_{i=1}^{n} (y_i - \bar{y})^2 \\
\mathrm{ESS} &= \sum_{i=1}^n (\hat{y}_i - \bar{y})^2 = \sum_{i=1}^n (\hat{\beta}_0 + \hat{\beta}_1 x_i - \bar{y})^2 \\
\mathrm{RSS} &= \sum_{i=1}^n (y_i - \hat{y}_i)^2  = \sum_{i=1}^n (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2
\end{split}
$$

where $\hat{\beta}_0$ and $\hat{\beta}_1$ are the [estimated regression coefficients obtained via ordinary least squares](/P/slr-ols)

$$ \label{eq:slr-ols}
\begin{split}
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1 \bar{x} \\
\hat{\beta}_1 &= \frac{s_{xy}}{s_x^2}
\end{split}
$$

where $\bar{x}$ and $\bar{y}$ are the [sample means](/D/mean-samp) of $x$ and $y$, $s_{xy}$ is the [unbiased sample covariance](/D/cov-samp) of $x$ and $y$ and $s_x^2$ is the [unbiased sample variance](/D/cov-samp) of $x$:

$$ \label{eq:cov-var-samp}
\begin{split}
s_{xy} &= \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x}) (y_i - \bar{y}) \\
s_x^2  &= \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2 \; .
\end{split}
$$

With that in mind, we start working out the total sum of squares:

$$ \label{eq:slr-tss}
\begin{split}
\mathrm{TSS}
&= \sum_{i=1}^{n} (y_i - \bar{y})^2 \\
&= \sum_{i=1}^{n} (y_i - \hat{y}_i + \hat{y}_i - \bar{y})^2 \\
&= \sum_{i=1}^{n} \left( (y_i - \hat{y}_i) + (\hat{y}_i - \bar{y}) \right)^2 \\
&= \sum_{i=1}^{n} \left( (y_i - \hat{y}_i)^2 + 2 (y_i - \hat{y}_i) (\hat{y}_i - \bar{y}) + (\hat{y}_i - \bar{y})^2 \right) \\
&= \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \sum_{i=1}^{n} 2 (y_i - \hat{y}_i) (\hat{y}_i - \bar{y}) + \sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2 \\
&\overset{\eqref{eq:slr-sss}}{=} \mathrm{ESS} + \mathrm{RSS} + \sum_{i=1}^{n} 2 (y_i - \hat{y}_i) (\hat{y}_i - \bar{y}) \; .
\end{split}
$$

Thus, what remains to be shown is that the following sum is zero:

$$ \label{eq:tss-sum}
\sum_{i=1}^{n} 2 (y_i - \hat{y}_i) (\hat{y}_i - \bar{y})
$$

Using the expression $\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i$ for the [fitted signal values](/D/regline), we proceed as follows:

$$ \label{eq:tss-sum-s1}
\begin{split}
\sum_{i=1}^{n} 2 (y_i - \hat{y}_i) (\hat{y}_i - \bar{y})
&= \sum_{i=1}^{n} 2 (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) (\hat{\beta}_0 + \hat{\beta}_1 x_i - \bar{y}) \\
&\overset{\eqref{eq:slr-ols}}{=} \sum_{i=1}^{n} 2 (y_i - \bar{y} + \hat{\beta}_1 \bar{x} - \hat{\beta}_1 x_i) (\bar{y} - \hat{\beta}_1 \bar{x} + \hat{\beta}_1 x_i - \bar{y}) \\
&= \sum_{i=1}^{n} 2 \left( (y_i - \bar{y}) - (\hat{\beta}_1 x_i - \hat{\beta}_1 \bar{x}) \right) (\hat{\beta}_1 x_i - \hat{\beta}_1 \bar{x}) \\
&= 2 \sum_{i=1}^{n} \left( (y_i - \bar{y}) - \hat{\beta}_1 (x_i - \bar{x}) \right) \hat{\beta}_1 (x_i - \bar{x}) \\
&= 2 \sum_{i=1}^{n} \left( (y_i - \hat{y}_i) \hat{\beta}_1 (x_i - \bar{x}) - \hat{\beta}_1 (x_i - \bar{x}) \hat{\beta}_1 (x_i - \bar{x}) \right) \\
&= 2 \left[ \hat{\beta}_1 \sum_{i=1}^{n} (y_i - \hat{y}_i) (x_i - \bar{x}) - \hat{\beta}_1^2 \sum_{i=1}^{n} (x_i - \bar{x}) (x_i - \bar{x}) \right] \; .
\end{split}
$$

Next, we recognize the sample covariance and sample variance terms from \eqref{eq:cov-var-samp}:

$$ \label{eq:tss-sum-s2}
\begin{split}
\sum_{i=1}^{n} 2 (y_i - \hat{y}_i) (\hat{y}_i - \bar{y})
&= 2 \left[ \hat{\beta}_1 (n-1) s_{xy} - \hat{\beta}_1^2 (n-1) s_x^2 \right] \\
&= 2 (n-1) \left[ \hat{\beta}_1 s_{xy} - \hat{\beta}_1^2 s_x^2 \right] \; .
\end{split}
$$

Now, we can apply to functional form of the estimate $\hat{\beta}_1$ from \eqref{eq:slr-ols} to get:

$$ \label{eq:tss-sum-s3}
\begin{split}
\sum_{i=1}^{n} 2 (y_i - \hat{y}_i) (\hat{y}_i - \bar{y})
&= 2 (n-1) \left[ \left( \frac{s_{xy}}{s_x^2} \right) s_{xy} - \left( \frac{s_{xy}}{s_x^2} \right)^2 s_x^2 \right] \\
&= 2 (n-1) \left[ \frac{s_{xy}^2}{s_x^2} - \frac{s_{xy}^2}{s_x^2} \right] \\
&= 2 (n-1) \cdot 0 \\
&= 0 \; .
\end{split}
$$

Plugging the result from \eqref{eq:tss-sum-s3} into \eqref{eq:slr-tss}, we finally get:

$$ \label{eq:slr-pss-qed}
\mathrm{TSS} = \mathrm{ESS} + \mathrm{RSS} \; .
$$