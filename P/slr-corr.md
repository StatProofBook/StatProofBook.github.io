---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-27 14:58:00

title: "Relationship between correlation coefficient and slope estimate in simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Correlation coefficient in terms of slope estimate"

sources:
  - authors: "Penny, William"
    year: 2006
    title: "Relation to correlation"
    in: "Mathematics for Brain Imaging"
    pages: "ch. 1.2.3, p. 18, eq. 1.27"
    url: "https://ueapsylabs.co.uk/sites/wpenny/mbi/mbi_course.pdf"
  - authors: "Wikipedia"
    year: 2021
    title: "Simple linear regression"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-27"
    url: "https://en.wikipedia.org/wiki/Simple_linear_regression#Fitting_the_regression_line"

proof_id: "P279"
shortcut: "slr-corr"
username: "JoramSoch"
---


**Theorem:** Assume a [simple linear regression model](/D/slr) with independent observations

$$ \label{eq:slr}
y = \beta_0 + \beta_1 x + \varepsilon, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2), \; i = 1,\ldots,n
$$

and consider estimation using [ordinary least squares](/P/slr-ols). Then, [correlation coefficient](/D/corr) and the estimated value of the [slope parameter](/D/slr) are related to each other via the sample [standard deviations](/D/std):

$$ \label{eq:slr-corr}
r_{xy} = \frac{s_x}{s_y} \, \hat{\beta}_1 \; .
$$


**Proof:** The [ordinary least squares estimate of the slope](/P/slr-ols) is given by

$$ \label{eq:slr-ols-sl}
\hat{\beta}_1 = \frac{s_{xy}}{s_x^2} \; .
$$

Using the [relationship between covariance and correlation](/P/cov-corr)

$$ \label{eq:cov-corr}
\mathrm{Cov}(X,Y) = \sigma_X \, \mathrm{Corr}(X,Y) \, \sigma_Y
$$

which also holds for sample [correlation](/D/corr) and [sample covariance](/D/cov-samp)

$$ \label{eq:cov-corr-samp}
s_{xy} = s_x \, r_{xy} \, s_y \; ,
$$

we get the final result:

$$ \label{eq:slr-corr-qed}
\begin{split}
\hat{\beta}_1 &= \frac{s_{xy}}{s_x^2} \\
\hat{\beta}_1 &= \frac{s_x \, r_{xy} \, s_y}{s_x^2} \\
\hat{\beta}_1 &= \frac{s_y}{s_x} \, r_{xy} \\
\Leftrightarrow \quad r_{xy} &= \frac{s_x}{s_y} \, \hat{\beta}_1 \; .
\end{split}
$$