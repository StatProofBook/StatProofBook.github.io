---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-10-22 08:04:00

title: "Exceedance probabilities for the Dirichlet distribution"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Dirichlet distribution"
theorem: "Exceedance probabilities"

sources:
  - authors: "Soch J, Allefeld C"
    year: 2016
    title: "Exceedance Probabilities for the Dirichlet Distribution"
    in: "arXiv stat.AP"
    pages: "1611.01439"
    url: "https://arxiv.org/abs/1611.01439"

proof_id: "P181"
shortcut: "dir-ep"
username: "JoramSoch"
---


**Theorem:** Let $r = [r_1, \ldots, r_k]$ be a [random vector](/D/rvec) following a [Dirichlet distribution](/D/dir) with concentration parameters $\alpha = [\alpha_1, \ldots, \alpha_k]$:

$$ \label{eq:r-Dir}
r \sim \mathrm{Dir}(\alpha) \; .
$$

<br>
1) If $k = 2$, then the [exceedance probability](/D/prob-exc) for $r_1$ is

$$ \label{eq:Dir2-EP}
\varphi_1 = 1 - \frac{\mathrm{B}\left( \frac{1}{2};\alpha_1,\alpha_2 \right)}{\mathrm{B}(\alpha_1,\alpha_2)}
$$

where $\mathrm{B}(x,y)$ is the beta function and $\mathrm{B}(x;a,b)$ is the incomplete beta function.

<br>
2) If $k > 2$, then the [exceedance probability](/D/prob-exc) for $r_i$ is

$$ \label{eq:Dir-EP}
\varphi_i = \int_0^\infty \prod_{j \neq i} \left( \frac{\gamma(\alpha_j,q_i)}{\Gamma(\alpha_j)} \right) \, \frac{q_i^{\alpha_i-1} \exp[-q_i]}{\Gamma(\alpha_i)} \, \mathrm{d}q_i \; .
$$

where $\Gamma(x)$ is the gamma function and $\gamma(s,x)$ is the lowerr incomplete gamma function.


**Proof:** In the context of the [Dirichlet distribution](/D/dir), the [exceedance probability](/D/prob-exc) for a particular $r_i$ is defined as:

$$ \label{eq:Dir-EP-def}
\begin{split}
\varphi_i &= p \Bigl( \forall j \in \left\lbrace 1, \ldots, k \Bigm| j \neq i \right\rbrace: \, r_i > r_j |\alpha \bigr) \\
&= p \Bigl( \bigwedge_{j \neq i} r_i > r_j \Bigm| \alpha \Bigr) \; .
\end{split}
$$

The [probability density function of the Dirichlet distribution](/P/dir-pdf) is given by:

$$ \label{eq:Dir-pdf}
\mathrm{Dir}(r; \alpha) = \frac{\Gamma\left( \sum_{i=1}^k \alpha_i \right)}{\prod_{i=1}^k \Gamma(\alpha_i)} \, \prod_{i=1}^k {r_i}^{\alpha_i-1} \; .
$$

Note that the probability density function is only calculated, if

$$ \label{eq:Dir-req}
r_i \in [0,1] \quad \text{for} \quad i = 1,\ldots,k \quad \text{and} \quad \sum_{i=1}^k r_i = 1 \; ,
$$

and [defined to be zero otherwise](/D/dir).

<br>
1) If $k = 2$, the [probability density function of the Dirichlet distribution](/P/dir-pdf) reduces to

$$ \label{eq:Dir2-pdf}
p(r) = \frac{\Gamma(\alpha_1 + \alpha_2)}{\Gamma(\alpha_1) \, \Gamma(\alpha_2)} \, r_1^{\alpha_1-1} \, r_2^{\alpha_2-1}
$$

which is equivalent to the [probability density function of the beta distribution](/P/beta-pdf)

$$ \label{eq:Beta-pdf}
p(r_1) = \frac{r_1^{\alpha_1-1} \, (1-r_1)^{\alpha_2-1}}{\mathrm{B}(\alpha_1,\alpha_2)}
$$

with the beta function given by

$$ \label{eq:beta-fct}
\mathrm{B}(x,y) = \frac{\Gamma(x) \, \Gamma(y)}{\Gamma(x + y)} \; .
$$

With \eqref{eq:Dir-req}, the exceedance probability for this bivariate case simplifies to

$$ \label{eq:Dir2-EP-def}
\varphi_1 = p(r_1 > r_2) = p(r_1 > 1 - r_1) = p(r_1 > 1/2) = \int_{\frac{1}{2}}^1 p(r_1) \, \mathrm{d}r_1 \; .
$$

Using the [cumulative distribution function of the beta distribution](/P/beta-cdf), it evaluates to

$$ \label{eq:Dir2-EP-qed}
\varphi_1 = 1 - \int_0^{\frac{1}{2}} p(r_1) \, \mathrm{d}r_1 = 1 - \frac{\mathrm{B}\left( \frac{1}{2};\alpha_1,\alpha_2 \right)}{\mathrm{B}(\alpha_1,\alpha_2)}
$$

with the incomplete beta function

$$ \label{eq:inc-beta-fct}
\mathrm{B}(x; a, b) = \int_0^x x^{a-1} \, (1-x)^{b-1} \, \mathrm{d}x \; .
$$

<br>
2) If $k > 2$, there is no similarly simple expression, because in general

$$ \label{eq:Dir-EP-ineq}
\varphi_i = p(r_i = \mathrm{max}(r)) > p(r_i > 1/2) \quad \text{for} \quad i = 1, \ldots, k \; ,
$$

i.e. exceedance probabilities cannot be evaluated using a simple threshold on $r_i$, because $r_i$ might be the maximal element in $r$ without being larger than $1/2$. Instead, we make use of the [relationship between the Dirichlet and the gamma distribution](/P/gam-dir) which states that

$$ \label{eq:Gam-Dir}
\begin{split}
& Y_1 \sim \mathrm{Gam}(\alpha_1,\beta), \, \ldots, \, Y_k \sim \mathrm{Gam}(\alpha_k,\beta), \, Y_s = \sum_{i=1}^k Y_j \\
\Rightarrow \; & X = (X_1, \ldots, X_k) = \left( \frac{Y_1}{Y_s}, \ldots, \frac{Y_k}{Y_s} \right) \sim \mathrm{Dir}(\alpha_1, \ldots, \alpha_k) \; .
\end{split}
$$

The [probability density function of the gamma distribution](/P/gam-pdf) is given by

$$ \label{eq:Gam-pdf}
\mathrm{Gam}(x; a, b) = \frac{ {b}^{a} }{\Gamma(a)} \, x^{a-1} \, \exp[-b x] \quad \text{for} \quad x > 0 \; .
$$

Consider the [gamma random variables](/D/gam)

$$ \label{eq:Gam-Dir-A}
q_1 \sim \mathrm{Gam}(\alpha_1,1), \, \ldots, \, q_k \sim \mathrm{Gam}(\alpha_k,1), \, q_s = \sum_{j=1}^k q_j
$$

and the [Dirichlet random vector](/D/dir)

$$ \label{eq:Gam-Dir-B}
r = (r_1, \ldots, r_k) = \left( \frac{q_1}{q_s}, \ldots, \frac{q_k}{q_s} \right) \sim \mathrm{Dir}(\alpha_1, \ldots, \alpha_k) \; .
$$

Obviously, it holds that

$$ \label{eq:Gam-Dir-eq}
r_i > r_j \; \Leftrightarrow \; q_i > q_j \quad \text{for} \quad i,j = 1, \ldots, k \quad \text{with} \quad j \neq i \; .
$$

Therefore, consider the probability that $q_i$ is larger than $q_j$, given $q_i$ is known. This probability is equal to the probability that $q_j$ is smaller than $q_i$, given $q_i$ is known

$$ \label{eq:Gam-EP0}
p(q_i > q_j|q_i) = p(q_j < q_i|q_i)
$$

which can be expressed in terms of the [cumulative distribution function of the gamma distribution](/P/gam-cdf) as

$$ \label{eq:Gam-EP1}
p(q_j < q_i|q_i) = \int_0^{q_i} \mathrm{Gam}(q_j;\alpha_j,1) \, \mathrm{d}q_j = \frac{\gamma(\alpha_j,q_i)}{\Gamma(\alpha_j)}
$$

where $\Gamma(x)$ is the gamma function and $\gamma(s,x)$ is the lower incomplete gamma function. Since the gamma variates are independent of each other, these probabilties factorize:

$$ \label{eq:Gam-EP2}
p(\forall_{j \neq i} \left[ q_i > q_j \right]|q_i) = \prod_{j \neq i} p(q_i > q_j|q_i) = \prod_{j \neq i} \frac{\gamma(\alpha_j,q_i)}{\Gamma(\alpha_j)} \; .
$$

In order to obtain the exceedance probability $\varphi_i$, the dependency on $q_i$ in this probability still has to be removed. From equations \eqref{eq:Dir-EP-def} and \eqref{eq:Gam-Dir-eq}, it follows that

$$ \label{eq:Dir-EP2a}
\varphi_i = p(\forall_{j \neq i} \left[ r_i > r_j \right]) = p(\forall_{j \neq i} \left[ q_i > q_j \right]) \; .
$$

Using the [law of marginal probability](/D/prob-marg), we have

$$ \label{eq:Dir-EP2b}
\varphi_i = \int_0^\infty p(\forall_{j \neq i} \left[ q_i > q_j \right]|q_i) \, p(q_i) \, \mathrm{d}q_i \; .
$$

With \eqref{eq:Gam-EP2} and \eqref{eq:Gam-Dir-A}, this becomes

$$ \label{eq:Dir-EP2c}
\varphi_i = \int_0^\infty \prod_{j \neq i} \left( p(q_i > q_j|q_i) \right) \cdot \mathrm{Gam}(q_i;\alpha_i,1) \, \mathrm{d}q_i \; .
$$

And with \eqref{eq:Gam-EP1} and \eqref{eq:Gam-pdf}, it becomes

$$ \label{eq:Dir-EP-qed}
\varphi_i = \int_0^\infty \prod_{j \neq i} \left( \frac{\gamma(\alpha_j,q_i)}{\Gamma(\alpha_j)} \right) \cdot \frac{q_i^{\alpha_i-1} \exp[-q_i]}{\Gamma(\alpha_i)} \, \mathrm{d}q_i \; .
$$

In other words, the [exceedance probability](/D/prob-exc) for one element from a [Dirichlet-distributed](/D/dir) [random vector](/D/rvec) is an integral from zero to infinity where the first term in the integrand conforms to a product of [gamma](/D/gam) [cumulative distribution functions](/D/cdf) and the second term is a [gamma](/D/gam) [probability density function](/D/pdf).
