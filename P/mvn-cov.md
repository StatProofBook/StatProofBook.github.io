---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-15 08:41:00

title: "Covariance matrix of the multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Covariance"

sources:
  - authors: "Rosenfeld, Meni"
    year: 2016
    title: "Deriving the Covariance of Multivariate Gaussian"
    in: "StackExchange Mathematics"
    pages: "retrieved on 2022-09-15"
    url: "https://math.stackexchange.com/questions/1905977/deriving-the-covariance-of-multivariate-gaussian"

proof_id: "P340"
shortcut: "mvn-cov"
username: "JoramSoch"
---


**Theorem:** Let $x$ follow a [multivariate normal distribution](/D/mvn):

$$ \label{eq:mvn}
x \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, the [covariance matrix](/D/covmat) of $x$ is

$$ \label{eq:mvn-cov}
\mathrm{Cov}(x) = \Sigma \; .
$$


**Proof:**

1) First, consider a set of [independent](/D/ind) and [standard normally](/D/snorm) distributed [random variables](/D/rvar):

$$ \label{eq:zi}
z_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0,1), \quad i = 1,\ldots,n \; .
$$

Then, [these variables together form a multivariate normally](/P/mvn-ind) distributed [random vector](/D/rvec):

$$ \label{eq:z}
z \sim \mathcal{N}(0_n, I_n) \; .
$$

Because the [covariance is zero for independent random variables](/P/cov-ind), we have

$$ \label{eq:zij-cov}
\mathrm{Cov}(z_i,z_j) = 0 \quad \text{for all} \quad i \neq j \; .
$$

Moreover, as the [variance of all entries of the vector is one](/P/norm-var), we have

$$ \label{eq:zi-var}
\mathrm{Var}(z_i) = 1 \quad \text{for all} \quad i = 1, \ldots, n \; .
$$

Taking \eqref{eq:zij-cov} and \eqref{eq:zi-var} together, the [covariance matrix](/D/covmat) of $z$ is

$$ \label{eq:z-cov}
\mathrm{Cov}(z) = \left[ \begin{array}{ccc} 1 & \cdots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \cdots & 1 \end{array} \right] = I_n \; .
$$

2) Next, consider an $n \times n$ matrix $A$ solving the equation $A A^\mathrm{T} = \Sigma$. Such a matrix exists, because $\Sigma$ [is defined to be positive definite](/D/mvn). Then, $x$ [can be represented as a linear transformation of](/P/mvn-ltt) $z$:

$$ \label{eq:x-z}
x = Az + \mu \sim \mathcal{N}(A 0_n + \mu, A I_n A^\mathrm{T}) = \mathcal{N}(\mu, \Sigma) \; .
$$

Thus, the [covariance](/D/cov) of $x$ can be written as:

$$ \label{eq:x-mean}
\mathrm{Cov}(x) = \mathrm{Cov}( Az + \mu ) \; .
$$

With the [invariance of the covariance matrix under addition](/P/cov-inv)

$$ \label{eq:cov-inv}
\mathrm{Cov}(x + a) = \mathrm{Cov}(x)
$$

and the [scaling of the covariance matrix upon multiplication](/P/cov-scal)

$$ \label{eq:cov-scal}
\mathrm{Cov}(Ax) = A \mathrm{Cov}(x) A^\mathrm{T} \; ,
$$

this becomes:

$$ \label{eq:mvn-cov-qed}
\begin{split}
\mathrm{Cov}(x) &= \mathrm{Cov}( Az + \mu ) \\
&\overset{\eqref{eq:cov-inv}}{=} \mathrm{Cov}(Az) \\
&\overset{\eqref{eq:cov-scal}}{=} A \, \mathrm{Cov}(z) A^\mathrm{T} \\
&\overset{\eqref{eq:z-cov}}{=} A I_n A^\mathrm{T} \\
&= A A^\mathrm{T} \\
&= \Sigma \; .
\end{split}
$$