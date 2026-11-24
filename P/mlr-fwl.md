---
layout: proof
mathjax: true

author: "Artemis Data Desk"
affiliation: ""
e_mail: ""
date: 2026-11-24 13:11:28

title: "Frisch-Waugh-Lovell theorem for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Frisch-Waugh-Lovell theorem"

sources:
  - authors: "Frisch, Ragnar and Waugh, Frederick V."
    year: 1933
    title: "Partial Time Regressions as Compared with Individual Trends"
    in: "Econometrica"
    pages: "vol. 1, no. 4, pp. 387-401"
    doi: "10.2307/1907330"
  - authors: "Lovell, Michael C."
    year: 1963
    title: "Seasonal Adjustment of Economic Time Series and Multiple Regression Analysis"
    in: "Journal of the American Statistical Association"
    pages: "vol. 58, no. 304, pp. 993-1010"
    doi: "10.1080/01621459.1963.10480682"
  - authors: "Lovell, Michael C."
    year: 2008
    title: "A Simple Proof of the FWL Theorem"
    in: "The Journal of Economic Education"
    pages: "vol. 39, no. 1, pp. 88-91"
    url: "https://repec.wesleyan.edu/pdf/mlovell/2005012_lovell.pdf"
    doi: "10.3200/JECE.39.1.88-91"

proof_id: "P571"
shortcut: "mlr-fwl"
username: "theyounganimation-rgb"
---


**Theorem:** Let $y \in \mathbb{R}^n$ and let $X=[A \; B]$ have full column rank, with $A \in \mathbb{R}^{n \times p}$ and $B \in \mathbb{R}^{n \times q}$. Write $\hat a$ and $\hat b$ for the two coefficient vectors obtained by [ordinary least squares](/P/mlr-ols) in the joint regression of $y$ on $A$ and $B$. Define the residuals of the response and of each column of $B$ using the [residual-forming matrix](/D/rfmat) for $A$,

$$ \label{eq:fwl-project}
R_A = I_n - A(A^\mathrm{T}A)^{-1}A^\mathrm{T}, \qquad
\tilde y = R_A y, \qquad \tilde B = R_A B .
$$

Regressing $\tilde y$ on $\tilde B$ without adding an intercept gives the same coefficient vector for $B$ and the same residual vector as the joint regression. In symbols,

$$ \label{eq:fwl-result}
\hat b = (\tilde B^\mathrm{T}\tilde B)^{-1}\tilde B^\mathrm{T}\tilde y,
\qquad
\tilde y-\tilde B\hat b = y-A\hat a-B\hat b .
$$

If an intercept is among the controls, its column of ones belongs in $A$ when forming both $\tilde y$ and $\tilde B$.


**Proof:** Fix a candidate $b$. Minimizing the [residual sum of squares](/D/rss) over $a$ amounts to regressing $y-Bb$ on $A$. The minimizing coefficient $a(b)$ and the residual at that minimum are

$$ \label{eq:fwl-fixed}
a(b)=(A^\mathrm{T}A)^{-1}A^\mathrm{T}(y-Bb), \qquad
y-Aa(b)-Bb=R_A(y-Bb)=\tilde y-\tilde B b .
$$

It follows that minimizing over both coefficient vectors reduces to minimizing $\|\tilde y-\tilde B b\|^2$ over $b$. This last regression has a unique solution. Indeed, if $\tilde B v=0$, then $Bv$ lies in the column space of $A$, so $Bv=Au$ for some $u$. The full column rank of $[A \; B]$ forces $u=0$ and $v=0$. Thus $\tilde B$ has full column rank, and its least squares formula gives the first equality in \eqref{eq:fwl-result}. Substituting $b=\hat b$ and $a(\hat b)=\hat a$ in \eqref{eq:fwl-fixed} gives the residual equality.
