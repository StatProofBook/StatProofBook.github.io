---
layout: proof
mathjax: true

author: "AtticKnight (AI-assisted)"
affiliation: ""
e_mail: ""
date: 2026-11-23 12:53:00

title: "Maximum likelihood estimation for beta-distributed data"
chapter: "Statistical Models"
section: "Frequency data"
topic: "Beta-distributed data"
theorem: "Maximum likelihood estimation"

sources:
  - authors: "R. Gnanadesikan, R. S. Pinkham and L. P. Hughes"
    year: 1967
    title: "Maximum Likelihood Estimation of the Parameters of the Beta Distribution from Smallest Order Statistics"
    in: "Technometrics"
    pages: "9(4), section 3, equations (5) and (6)"
    doi: "10.1080/00401706.1967.10490509"

proof_id: "P577"
shortcut: "beta-mle"
username: "AtticKnight"
---


**Theorem:** Let $x_1,\ldots,x_n$ be independent [beta-distributed observations](/D/beta-data) in $(0,1)$ with unknown shape parameters $a,b>0$. Write $u$ and $v$ for the geometric means of the observations and their complements, respectively,

$$ \label{eq:beta-mle-stat}
u=\left(\prod_{i=1}^n x_i\right)^{1/n},
\qquad
v=\left(\prod_{i=1}^n (1-x_i)\right)^{1/n}.
$$

If at least two observations differ, the [maximum likelihood estimate](/D/mle) is the unique positive pair satisfying

$$ \label{eq:beta-mle-score}
\begin{aligned}
\psi(\hat a)-\psi(\hat a+\hat b)&=\log u,\\
\psi(\hat b)-\psi(\hat a+\hat b)&=\log v,
\end{aligned}
$$

where $\psi(z)=\frac{\mathrm{d}}{\mathrm{d}z}\log\Gamma(z)$. If all observations are equal, the likelihood is unbounded.


**Proof:** Multiplying the [beta densities](/P/beta-pdf) gives the log-likelihood per observation

$$ \label{eq:beta-mle-ll}
\frac{\ell(a,b)}{n}=(a-1)\log u+(b-1)\log v-\log \mathrm{B}(a,b).
$$

Substitute $\mathrm{B}(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)$. Setting the two partial derivatives of \eqref{eq:beta-mle-ll} to zero gives \eqref{eq:beta-mle-score}.

To prove uniqueness, differentiate the integral defining $\mathrm{B}(a,b)$. For $X\sim\mathrm{Bet}(a,b)$ and a direction $(h,k)$, this gives

$$ \label{eq:beta-mle-curvature}
\left.\frac{\mathrm{d}^2}{\mathrm{d}s^2}
\log\mathrm{B}(a+sh,b+sk)\right|_{s=0}
=\mathrm{Var}\!\left(h\log X+k\log(1-X)\right).
$$

Indeed, the first derivative is the expectation of the log expression, and the second subtracts the square of that expectation from its second moment. Differentiation under the integral is valid because positive shape parameters remain positive in a neighborhood of $s=0$, and the endpoint powers there are integrable even after multiplication by squared logarithms. The variance can vanish only if $h\log x+k\log(1-x)$ is constant throughout $(0,1)$. Differentiating in $x$ gives $h(1-x)-kx=0$ for every $x$, hence $h=k=0$. Thus $\ell$ is strictly concave.

It remains to show that a maximum is attained. For a nonconstant sample the strict arithmetic–geometric mean inequality gives $u<\bar x$ and $v<1-\bar x$. Choose $c,d$ with $u<c<d<1-v$. Restricting the beta integral to $[c,d]$ gives

$$ \label{eq:beta-mle-large}
\begin{aligned}
\mathrm{B}(a,b)
&\geq\int_c^d\frac{x^a(1-x)^b}{x(1-x)}\,\mathrm{d}x
\geq (d-c)c^a(1-d)^b,\\
\exp\{\ell(a,b)/n\}
&\leq \frac{1}{uv(d-c)}
       \left(\frac{u}{c}\right)^a
       \left(\frac{v}{1-d}\right)^b .
\end{aligned}
$$

Both ratios are less than one, so the likelihood tends to zero as $a+b\to\infty$. If $a+b$ stays bounded and $a\downarrow 0$, then $(1-x)^{b-1}$ has a uniform positive lower bound for $0<x<1/2$, while $\int_0^{1/2}x^{a-1}\,\mathrm{d}x=2^{-a}/a\to\infty$. Thus $\mathrm{B}(a,b)\to\infty$ and the likelihood tends to zero. The same argument applies when $b\downarrow 0$. Continuity now gives an interior maximum, and strict concavity makes it the unique solution of \eqref{eq:beta-mle-score}.

Finally, suppose $x_i=r$ for every $i$. Take $a=1+tr$, $b=1+t(1-r)$ with $t>0$. The reciprocal of the resulting density at $r$ is

$$ \label{eq:beta-mle-constant}
\int_0^1
\left[\left(\frac{x}{r}\right)^r
      \left(\frac{1-x}{1-r}\right)^{1-r}\right]^t
\,\mathrm{d}x .
$$

The function $x^r(1-x)^{1-r}$ has its unique maximum at $x=r$. The bracket is therefore at most one and is strictly smaller away from $r$. Dominated convergence sends the integral to zero as $t\to\infty$, so the density at $r$ and the sample likelihood grow without bound.
