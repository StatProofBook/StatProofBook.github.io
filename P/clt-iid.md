---
layout: proof
mathjax: true

author: "AtticKnight (AI-assisted)"
affiliation: ""
e_mail: ""
date: 2026-11-25 11:48:00

title: "Classical central limit theorem for independent and identically distributed observations"
chapter: "General Theorems"
section: "Probability theory"
topic: "Central limit theorems"
theorem: "Classical central limit theorem"

sources:
  - authors: "Durrett, Rick"
    year: 2019
    title: "Probability: Theory and Examples"
    in: "Cambridge University Press, fifth edition"
    pages: "Theorems 3.3.17 and 3.4.1"
    url: "https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf"

proof_id: "P579"
shortcut: "clt-iid"
username: "AtticKnight"
---


**Theorem:** Let $X_1,X_2,\ldots$ be [independent and identically distributed](/D/iid) real random variables with [mean](/D/mean) $\mu$ and [variance](/D/var) $0<\sigma^2<\infty$. Let $\bar X_n$ denote their [sample mean](/D/mean-samp) and $\Phi$ the [standard normal](/D/snorm) distribution function. For every real $x$,

$$ \label{eq:clt-iid}
\lim_{n\to\infty}\Pr\!\left\{\frac{\sqrt n(\bar X_n-\mu)}{\sigma}\leq x\right\}=\Phi(x).
$$


**Proof:** Set $Y_j=(X_j-\mu)/\sigma$. The $Y_j$ have mean zero, second moment one and common [characteristic function](/D/cf) $\varphi(u)=\mathrm E[\exp(iuY_j)]$. Taylor's formula with integral remainder, applied to the complex exponential along the real line, gives

$$ \label{eq:clt-iid-rem}
e^{iw}=1+iw-w^2\int_0^1(1-s)e^{isw}\,\mathrm ds.
$$

Use $w=uY_1$ in \eqref{eq:clt-iid-rem} and take expectations. The integral has magnitude at most $1/2$ and tends to $1/2$ for every value of $Y_1$ as $u\to0$. The integrable bound $Y_1^2/2$ therefore gives, by dominated convergence,

$$ \label{eq:clt-iid-exp}
\lim_{u\to0}\frac{\varphi(u)-1}{u^2}=-\tfrac12\,\mathrm E[Y_1^2]=-\tfrac12.
$$

The standardized sample mean equals $(Y_1+\cdots+Y_n)/\sqrt n$. Independence makes its characteristic function at $t$ equal to $\varphi(t/\sqrt n)^n$. For fixed $t$, \eqref{eq:clt-iid-exp} gives $n(\varphi(t/\sqrt n)-1)\to-t^2/2$. The logarithm defined by its power series near $1$ satisfies $\log(1+z)=z+O(|z|^2)$ as $z\to0$. Thus

$$ \label{eq:clt-iid-limit}
\varphi(t/\sqrt n)^n=\exp\!\left(n\log\varphi(t/\sqrt n)\right)\longrightarrow e^{-t^2/2}.
$$

The limit is the characteristic function of a standard normal variable. Lévy's continuity theorem gives convergence in distribution, and continuity of $\Phi$ at every real $x$ gives \eqref{eq:clt-iid}.
