---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2022-09-15 02:22:00

title: "Mean of the multivariate normal distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Mean"

sources:
  - authors: "Taboga, Marco"
    year: 2021
    title: "Multivariate normal distribution"
    in: "Lectures on probability theory and mathematical statistics"
    pages: "retrieved on 2022-09-15"
    url: "https://www.statlect.com/probability-distributions/multivariate-normal-distribution"

proof_id: "P339"
shortcut: "mvn-mean"
username: "JoramSoch"
---


**Theorem:** Let $x$ follow a [multivariate normal distribution](/D/mvn):

$$ \label{eq:mvn}
x \sim \mathcal{N}(\mu, \Sigma) \; .
$$

Then, the [mean or expected value](/D/mean) of $x$ is

$$ \label{eq:mvn-mean}
\mathrm{E}(x) = \mu \; .
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

By definition, the [expected value of a random vector is equal to the vector of all expected values](/D/mean-rvec):

$$ \label{eq:mean-rvec}
\mathrm{E}(z) = \mathrm{E}\left( \left[ \begin{array}{c} z_1 \\ \vdots \\ z_n \end{array} \right] \right) = \left[ \begin{array}{c} \mathrm{E}(z_1) \\ \vdots \\ \mathrm{E}(z_n) \end{array} \right] \; .
$$

Because the [expected value of all its entries is zero](/P/norm-mean), the expected value of the random vector is

$$ \label{eq:z-mean}
\mathrm{E}(z) = \left[ \begin{array}{c} \mathrm{E}(z_1) \\ \vdots \\ \mathrm{E}(z_n) \end{array} \right] = \left[ \begin{array}{c} 0 \\ \vdots \\ 0 \end{array} \right] = 0_n \; .
$$

2) Next, consider an $n \times n$ matrix $A$ solving the equation $A A^\mathrm{T} = \Sigma$. Such a matrix exists, because $\Sigma$ [is defined to be positive definite](/D/mvn). Then, $x$ [can be represented as a linear transformation of](/P/mvn-ltt) $z$:

$$ \label{eq:x-z}
x = Az + \mu \sim \mathcal{N}(A 0_n + \mu, A I_n A^\mathrm{T}) = \mathcal{N}(\mu, \Sigma) \; .
$$

Thus, the [expected value](/D/mean) of $x$ can be written as:

$$ \label{eq:x-mean}
\mathrm{E}(x) = \mathrm{E}( Az + \mu ) \; .
$$

With the [linearity of the expected value](/P/mean-lin), this becomes:

$$ \label{eq:mvn-mean-qed}
\begin{split}
\mathrm{E}(x) &= \mathrm{E}( Az + \mu ) \\
&= \mathrm{E}(Az) + \mathrm{E}(\mu) \\
&= A \, \mathrm{E}(z) + \mu \\
&\overset{\eqref{eq:z-mean}}{=} A \, 0_n + \mu \\
&= \mu \; .
\end{split}
$$