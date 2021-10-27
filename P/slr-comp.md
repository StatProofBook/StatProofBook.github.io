---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-27 12:52:00

title: "The regression line goes through the center of mass point"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Regression line includes center of mass"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Simple linear regression"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-27"
    url: "https://en.wikipedia.org/wiki/Simple_linear_regression#Numerical_properties"

proof_id: "P275"
shortcut: "slr-comp"
username: "JoramSoch"
---


**Theorem:** In [simple linear regression](/D/slr), the [regression line](/D/regline) estimated using [ordinary least squares](/P/slr-ols) includes the point $M(\bar{x},\bar{y})$.

**Proof:** The [fitted regression line](/D/regline) is described by the equation

$$ \label{eq:slr-ols-regline}
y = \hat{\beta}_0 + \hat{\beta}_1 x \quad \text{where} \quad x,y \in \mathbb{R} \; .
$$

Plugging in the coordinates of $M$ and the [ordinary least squares estimate of the intercept](/P/slr-ols), we obtain

$$ \label{eq:slr-ols}
\begin{split}
\bar{y} &= \hat{\beta}_0 + \hat{\beta}_1 \bar{x} \\
\bar{y} &= \bar{y} - \hat{\beta}_1 \bar{x} + \hat{\beta}_1 \bar{x} \\
\bar{y} &= \bar{y} \; .
\end{split}
$$

which is a true statement. Thus, the [regression line](/D/regline) goes through the center of mass point $(\bar{x},\bar{y})$, if [the model](/D/slr) includes an intercept term $\beta_0$.