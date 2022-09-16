---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-15 12:23:00

title: "Covariance matrices of the matrix-normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Covariance"

sources:
  - authors: "Wikipedia"
    year: 2022
    title: "Matrix normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2022-09-15"
    url: "https://en.wikipedia.org/wiki/Matrix_normal_distribution#Expected_values"

proof_id: "P342"
shortcut: "matn-cov"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n \times p$ [random matrix](/D/rmat) following a [matrix-normal distribution](/D/matn):

$$ \label{eq:matn}
X \sim \mathcal{MN}(M, U, V) \; .
$$

Then,

1) the [covariance matrix](/D/covmat) of each row of $X$ is a scalar multiple of $V$

$$ \label{eq:matn-cov-row}
\mathrm{Cov}(x_{i,\bullet}^\mathrm{T}) \propto V \quad \text{for all} \quad i = 1,\ldots,n \; ;
$$

2) the [covariance matrix](/D/covmat) of each column of $X$ is a scalar multiple of $U$

$$ \label{eq:matn-cov-col}
\mathrm{Cov}(x_{\bullet,j}) \propto U \quad \text{for all} \quad i = 1,\ldots,p \; .
$$


**Proof:**

1) The [marginal distribution](/D/dist-marg) of a given row of $X$ [is a multivariate normal distribution](/P/matn-marg)

$$ \label{eq:matn-marg-row}
x_{i,\bullet}^\mathrm{T} \sim \mathcal{N}(m_{i,\bullet}^\mathrm{T}, u_{ii} V) \; ,
$$

and [the covariance of this multivariate normal distribution](/P/mvn-cov) is

$$ \label{eq:matn-cov-row-qed}
\mathrm{Cov}(x_{i,\bullet}^\mathrm{T}) = u_{ii} V \propto V \; .
$$

2) The [marginal distribution](/D/dist-marg) of a given column of $X$ [is a multivariate normal distribution](/P/matn-marg)

$$ \label{eq:matn-marg-col}
x_{\bullet,j} \sim \mathcal{N}(m_{\bullet,j}, v_{jj} U) \; ,
$$

and [the covariance of this multivariate normal distribution](/P/mvn-cov) is

$$ \label{eq:matn-cov-col-qed}
\mathrm{Cov}(x_{\bullet,j}) = v_{jj} U \propto U \; .
$$