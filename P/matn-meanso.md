---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-01-23 13:49:00

title: "Second-order expectations for the matrix-normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Second-order expectations"

sources:
  - authors: "Wikipedia"
    year: 2026
    title: "Matrix normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2026-01-23"
    url: "https://en.wikipedia.org/wiki/Matrix_normal_distribution#Expected_values"

proof_id: "P524"
shortcut: "matn-meanso"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n \times p$ [random matrix](/D/rmat) following a [matrix-normal distribution](/D/matn):

$$ \label{eq:matn}
X \sim \mathcal{MN}(M, U, V) \; .
$$

Then, we have the following [second-order](/D/covmat) [expectations](/D/mean) for $X$:

1) the second-order expectation across rows is

$$ \label{eq:matn-mean-XMXMT}
\mathrm{E}\left[ (X-M) (X-M)^\mathrm{T} \right] = U \, \mathrm{tr}(V) \; ;
$$

2) the second-order expectation across columns is

$$ \label{eq:matn-mean-XMTXM}
\mathrm{E}\left[ (X-M)^\mathrm{T} (X-M) \right] = V \, \mathrm{tr}(U) \; .
$$


**Proof:** The [linear transformation theorem for the matrix-normal distribution](/P/matn-ltt) states that any linear transformation of a [normal random matrix](/D/matn) is again matrix-normally distributed:

$$ \label{eq:matn-ltt}
X \sim \mathcal{MN}(M, U, V)
\quad \Rightarrow \quad
Y = AXB + C \sim \mathcal{MN}(AMB+C, AUA^\mathrm{T}, B^\mathrm{T}VB) \; .
$$

Applying \eqref{eq:matn-ltt} to \eqref{eq:matn}, we get:

$$ \label{eq:XM-dist}
\begin{split}
   Y
 = X - M = I_n X \, I_p - M
&\sim \mathcal{MN}(I_n M I_p - M, I_n U I_n^\mathrm{T}, I_p^\mathrm{T} V I_p) \\
&\sim \mathcal{MN}(0_{np}, U, V) \; .
\end{split}
$$

Moreover, when the matrix $X \in \mathbb{R}^{n \times p}$ follows a [matrix-normal distribution](/D/matn), we have [the following expectations of quadratic forms](/P/matn-qf) for $X$:

$$ \label{eq:matn-mean-XAXT}
\mathrm{E}\left[ X A X^\mathrm{T} \right] = M A M^\mathrm{T} + U \, \mathrm{tr}(A^\mathrm{T} V) \; ;
$$

$$ \label{eq:matn-mean-XTBX}
\mathrm{E}\left[ X^\mathrm{T} B X \right] = M^\mathrm{T} B M + V \, \mathrm{tr}(U B^\mathrm{T}) \; ;
$$

$$ \label{eq:matn-mean-XCX}
\mathrm{E}\left[ X C X \right] = M C M + U C^\mathrm{T} V \; .
$$

With that, we are able to derive the above equations:

1) The second-order expectation across rows obtains as

$$ \label{eq:matn-mean-XMXMT-qed}
\begin{split}
   \mathrm{E}\left[ (X-M) (X-M)^\mathrm{T} \right]
&\overset{\eqref{eq:XM-dist}}{=} \mathrm{E}\left[ Y Y^\mathrm{T} \right] \\
&= \mathrm{E}\left[ Y I_p Y^\mathrm{T} \right] \\
&\overset{\eqref{eq:matn-mean-XAXT}}{=} 0_{np} I_p 0_{np}^\mathrm{T} + U \, \mathrm{tr}(I_p^\mathrm{T} V) \\
&= U \, \mathrm{tr}(V) \; .
\end{split}
$$

2) The second-order expectation across columns obtains as

$$ \label{eq:matn-mean-XMTXM-qed}
\begin{split}
   \mathrm{E}\left[ (X-M)^\mathrm{T} (X-M) \right]
&\overset{\eqref{eq:XM-dist}}{=} \mathrm{E}\left[ Y^\mathrm{T} Y \right] \\
&= \mathrm{E}\left[ Y^\mathrm{T} I_n Y \right] \\
&\overset{\eqref{eq:matn-mean-XTBX}}{=} 0_{np}^\mathrm{T} I_n 0_{np} + V \, \mathrm{tr}(I_n^\mathrm{T} U) \\
&= V \, \mathrm{tr}(U) \; .
\end{split}
$$