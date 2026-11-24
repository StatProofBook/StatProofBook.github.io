---
layout: proof
mathjax: true

author: "Ljx000888"
affiliation: ""
e_mail: ""
date: 2026-11-24 23:47:00

title: "Law of total cumulance"
chapter: "General Theorems"
section: "Probability theory"
topic: "Cumulant"
theorem: "Law of total cumulance"

sources:
  - authors: "Brillinger, D. R."
    year: 1969
    title: "The calculation of cumulants via conditioning"
    in: "Annals of the Institute of Statistical Mathematics"
    pages: "21, 215–218"
    doi: "10.1007/BF02532246"

proof_id: "P575"
shortcut: "cum-tot"
username: "Ljx000888"
---

**Theorem:** Let $X_1,\ldots,X_n$ be real random variables with $\mathbb{E}|X_i|^n<\infty$, where $n\geq1$, and let $\mathcal G$ be a sub-$\sigma$-algebra. Write $[n]=\{1,\ldots,n\}$ and let $\Pi(S)$ be the set of partitions of a finite set $S$ into nonempty blocks. For each nonempty $B\subseteq[n]$, let $C_B$ be the joint cumulant of $(X_i)_{i\in B}$ conditional on $\mathcal G$. Then

$$ \label{eq:cum-tot}
\kappa(X_1,\ldots,X_n)
=\sum_{\pi\in\Pi([n])}\kappa\bigl(C_B:B\in\pi\bigr).
$$

Each outer cumulant is taken under the original probability law, treating the conditional cumulants as random variables. For $n=2$, the one-block partition gives the expected conditional covariance and the two-block partition gives the covariance of the conditional means. This recovers the [law of total covariance](/P/cov-tot).

**Proof:** Recall that the joint cumulants of a family $(Y_i)_{i\in S}$ are determined by its moments through

$$ \label{eq:cum-tot-mom}
\mathbb E\!\left[\prod_{i\in S}Y_i\right]
=\sum_{\pi\in\Pi(S)}\prod_{B\in\pi}\kappa(Y_i:i\in B).
$$

Indeed, the one-block term is the cumulant of all variables in $S$, and every other term involves only cumulants of smaller sets. The conditional cumulants $C_B$ are defined by the same recursion with conditional expectations. The assumed moments and Hölder's inequality ensure that the products below are integrable.

Apply the conditional relation to $(X_i)_{i\in S}$, take expectations using the [tower property](/P/mean-tot), and then apply \eqref{eq:cum-tot-mom} to the family $(C_B)_{B\in\pi}$:

$$ \label{eq:cum-tot-expand}
\mathbb E\!\left[\prod_{i\in S} X_i\right]
=\sum_{\pi\in\Pi(S)} \mathbb E\!\left[\prod_{B\in\pi} C_B\right]
=\sum_{\pi\in\Pi(S)}\sum_{\rho\in\Pi(\pi)}
  \prod_{A\in\rho}\kappa(C_B:B\in A).
$$

Here $\rho$ partitions the *blocks* of $\pi$. Joining the blocks in each group $A\in\rho$ gives one block $D=\bigcup_{B\in A}B$ of a partition $\sigma$ of $S$. Conversely, choosing $\sigma$ and a partition of each $D\in\sigma$ recovers $\pi$ (collect all the smaller blocks) and $\rho$ (group them by their parent block). Thus the last sum in \eqref{eq:cum-tot-expand} equals

$$ \label{eq:cum-tot-regroup}
\sum_{\sigma\in\Pi(S)}\prod_{D\in\sigma}K(D),
\qquad
K(D)=\sum_{\tau\in\Pi(D)}\kappa(C_B:B\in\tau).
$$

This holds for every nonempty $S\subseteq[n]$. Hence $K(D)$ satisfies the same moment recursion as $\kappa(X_i:i\in D)$. Uniqueness in \eqref{eq:cum-tot-mom} gives equality for every $D$, in particular for $D=[n]$, which proves \eqref{eq:cum-tot}.
