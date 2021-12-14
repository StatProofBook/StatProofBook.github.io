---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-12-14 02:31:00

title: "Correlation coefficient in terms of standard scores"
chapter: "General Theorems"
section: "Probability theory"
topic: "Correlation"
theorem: "Relationship to standard scores"

sources:
  - authors: "Wikipedia"
    year: 2021
    title: "Peason correlation coefficient"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2021-12-14"
    url: "https://en.wikipedia.org/wiki/Pearson_correlation_coefficient#For_a_sample"

proof_id: "P299"
shortcut: "corr-z"
username: "JoramSoch"
---


**Theorem:** Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ and $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ be [samples](/D/samp) from [random variables](/D/rvar) $X$ and $Y$. Then, the [sample correlation coefficient](/D/corr-samp) $r_{xy}$ can be expressed in terms of the [standard scores](/D/z) of $x$ and $y$:

$$ \label{eq:corr-z}
r_{xy} = \frac{1}{n-1} \sum_{i=1}^n z_i^{(x)} \cdot z_i^{(y)} = \frac{1}{n-1} \sum_{i=1}^n \left( \frac{x_i-\bar{x}}{s_x} \right) \left( \frac{y_i-\bar{y}}{s_y} \right)
$$

where $\bar{x}$ and $\bar{y}$ are the [sample means](/D/mean-samp) and $s_x$ and $s_y$ are the [sample variances](/D/var-samp).


**Proof:** The [sample correlation coefficient](/D/corr-samp) is defined as

$$ \label{eq:corr-samp}
r_{xy} = \frac{\sum_{i=1}^n (x_i-\bar{x}) (y_i-\bar{y})}{\sqrt{\sum_{i=1}^n (x_i-\bar{x})^2} \sqrt{\sum_{i=1}^n (y_i-\bar{y})^2}} \; .
$$

Using the [sample variances](/D/var-samp) of $x$ and $y$, we can write:

$$ \label{eq:corr-z-s1}
r_{xy} = \frac{\sum_{i=1}^n (x_i-\bar{x}) (y_i-\bar{y})}{\sqrt{(n-1) s_x^2} \sqrt{(n-1) s_y^2}} \; .
$$

Rearranging the terms, we arrive at:

$$ \label{eq:corr-z-s2}
r_{xy} = \frac{1}{(n-1) \, s_x \, s_y} \sum_{i=1}^n (x_i-\bar{x}) (y_i-\bar{y}) \; .
$$

Further simplifying, the result is:

$$ \label{eq:corr-z-s3}
r_{xy} = \frac{1}{n-1} \sum_{i=1}^n \left( \frac{x_i-\bar{x}}{s_x} \right) \left( \frac{y_i-\bar{y}}{s_y} \right) \; .
$$