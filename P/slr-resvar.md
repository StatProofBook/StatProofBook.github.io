---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-10-27 14:37:00

title: "Relationship between residual variance and sample variance in simple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Residual variance in terms of sample variance"

sources:
  - authors: "Penny, William"
    year: 2006
    title: "Relation to correlation"
    in: "Mathematics for Brain Imaging"
    pages: "ch. 1.2.3, p. 18, eq. 1.28"
    url: "https://ueapsylabs.co.uk/sites/wpenny/mbi/mbi_course.pdf"
  - authors: "Wikipedia"
    year: 2021
    title: "Simple linear regression"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-10-27"
    url: "https://en.wikipedia.org/wiki/Simple_linear_regression#Numerical_properties"

proof_id: "P278"
shortcut: "slr-resvar"
username: "JoramSoch"
---


**Theorem:** Assume a [simple linear regression model](/D/slr) with independent observations

$$ \label{eq:slr}
y = \beta_0 + \beta_1 x + \varepsilon, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2), \; i = 1,\ldots,n
$$

and consider estimation using [ordinary least squares](/P/slr-ols). Then, [residual variance](/D/resvar) and [sample variance](/D/var-samp) are related to each other via the [correlation coefficient](/D/corr):

$$ \label{eq:slr-vars}
\hat{\sigma}^2 = \left( 1 - r_{xy}^2 \right) s_y^2 \; .
$$


**Proof:** The [residual variance](/D/resvar) can be expressed in terms of the [residual sum of squares](/D/rss):

$$ \label{eq:slr-res}
\hat{\sigma}^2 = \frac{1}{n-1} \, \mathrm{RSS}(\hat{\beta}_0,\hat{\beta}_1)
$$

and [the residual sum of squares for simple linear regression](/P/slr-sss) is

$$ \label{eq:slr-rss}
\mathrm{RSS}(\hat{\beta}_0,\hat{\beta}_1) = (n-1) \left( s_y^2 - \frac{s_{xy}^2}{s_x^2} \right) \; .
$$

Combining \eqref{eq:slr-res} and \eqref{eq:slr-rss}, we obtain:

$$ \label{eq:slr-vars-s1}
\begin{split}
\hat{\sigma}^2 &= \left( s_y^2 - \frac{s_{xy}^2}{s_x^2} \right) \\
&= \left( 1 - \frac{s_{xy}^2}{s_x^2 s_y^2} \right) s_y^2 \\
&= \left( 1 - \left( \frac{s_{xy}}{s_x \, s_y} \right)^2 \right) s_y^2 \; .
\end{split}
$$

Using the [relationship between correlation, covariance and standard deviation](/D/corr)

$$ \label{eq:corr-cov-std}
\mathrm{Corr}(X,Y) = \frac{\mathrm{Cov}(X,Y)}{\sqrt{\mathrm{Var}(X)} \sqrt{\mathrm{Var}(Y)}}
$$

which also holds for sample correlation, [sample covariance](/D/cov-samp) and sample [standard deviation](/D/std)

$$ \label{eq:corr-cov-std-samp}
r_{xy} = \frac{s_{xy}}{s_x \, s_y} \; ,
$$

we get the final result:

$$ \label{eq:slr-vars-s2}
\hat{\sigma}^2 = \left( 1 - r_{xy}^2 \right) s_y^2 \; .
$$