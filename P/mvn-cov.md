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


**Theorem:** Let $X$ follow a [multivariate normal distribution](/D/mvn):

$$ \label{eq:mvn}
X \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, the [covariance matrix](/D/covmat) of $X$ is

$$ \label{eq:mvn-cov}
\mathrm{Cov}(X) = \Sigma \; .
$$


**Proof:**

1) First, consider a set of [independent](/D/ind) and [standard normally](/D/snorm) distributed [random variables](/D/rvar):

$$ \label{eq:Zi}
Z_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0,1), \quad i = 1,\ldots,n \; .
$$

Then, [these variables together form a multivariate normally](/P/mvn-ind) distributed [random vector](/D/rvec):

$$ \label{eq:Z}
Z \sim \mathcal{N}(0_n, I_n) \; .
$$

Because the [covariance is zero for independent random variables](/P/cov-ind), we have

$$ \label{eq:Zij-cov}
\mathrm{Cov}(Z_i,Z_j) = 0 \quad \text{for all} \quad i \neq j \; .
$$

Moreover, as the [variance of all entries of the vector is one](/P/norm-var), we have

$$ \label{eq:Zi-var}
\mathrm{Var}(Z_i) = 1 \quad \text{for all} \quad i = 1, \ldots, n \; .
$$

Taking \eqref{eq:Zij-cov} and \eqref{eq:Zi-var} together, the [covariance matrix](/D/covmat) of $Z$ is

$$ \label{eq:Z-cov}
\mathrm{Cov}(Z) = \left[ \begin{array}{ccc} 1 & \cdots & 0 \\ \vdots & \ddots & \vdots \\ 0 & \cdots & 1 \end{array} \right] = I_n \; .
$$

2) Next, consider an $n \times n$ matrix $A$ solving the equation $A A^\mathrm{T} = \Sigma$. Such a matrix exists, because $\Sigma$ [is defined to be positive definite](/D/mvn). Then, $X$ [can be represented as a linear transformation](/P/mvn-ltt) of $Z$:

$$ \label{eq:X-Z}
X = AZ + \mu \sim \mathcal{N}(A 0_n + \mu, A I_n A^\mathrm{T}) = \mathcal{N}(\mu, \Sigma) \; .
$$

Thus, the [covariance](/D/cov) of $X$ can be written as:

$$ \label{eq:X-mean}
\mathrm{Cov}(X) = \mathrm{Cov}(AZ + \mu) \; .
$$

With the [invariance of the covariance matrix under addition](/P/covmat-inv)

$$ \label{eq:cov-inv}
\mathrm{Cov}(X + a) = \mathrm{Cov}(X)
$$

and the [scaling of the covariance matrix upon multiplication](/P/covmat-scal)

$$ \label{eq:cov-scal}
\mathrm{Cov}(AX) = A \mathrm{Cov}(X) A^\mathrm{T} \; ,
$$

this becomes:

$$ \label{eq:mvn-cov-qed}
\begin{split}
   \mathrm{Cov}(X)
&= \mathrm{Cov}(AZ + \mu) \\
&\overset{\eqref{eq:cov-inv}}{=} \mathrm{Cov}(AZ) \\
&\overset{\eqref{eq:cov-scal}}{=} A \, \mathrm{Cov}(Z) A^\mathrm{T} \\
&\overset{\eqref{eq:Z-cov}}{=} A I_n A^\mathrm{T} \\
&= A A^\mathrm{T} \\
&= \Sigma \; .
\end{split}
$$