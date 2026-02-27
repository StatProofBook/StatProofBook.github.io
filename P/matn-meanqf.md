---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-01-23 12:01:00

title: "Expectation of quadratic forms for the matrix-normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Expectation of quadratic forms"

sources:
  - authors: "Wikipedia"
    year: 2026
    title: "Matrix normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2026-01-23"
    url: "https://en.wikipedia.org/wiki/Matrix_normal_distribution#Expected_values"

proof_id: "P523"
shortcut: "matn-meanqf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n \times p$ [random matrix](/D/rmat) following a [matrix-normal distribution](/D/matn):

$$ \label{eq:matn}
X \sim \mathcal{MN}(M, U, V) \; .
$$

Then, quadratic forms of $X$ have the following [expectations](/D/mean):

1) for a $p \times p$ matrix $A$, we have

$$ \label{eq:matn-mean-XAXT}
\mathrm{E}\left[ X A X^\mathrm{T} \right] = M A M^\mathrm{T} + U \, \mathrm{tr}(A^\mathrm{T} V) \; ;
$$

2) for an $n \times n$ matrix $B$, we have

$$ \label{eq:matn-mean-XTBX}
\mathrm{E}\left[ X^\mathrm{T} B X \right] = M^\mathrm{T} B M + V \, \mathrm{tr}(U B^\mathrm{T}) \; ;
$$

3) for a $p \times n$ matrix $C$, we have

$$ \label{eq:matn-mean-XCX}
\mathrm{E}\left[ X C X \right] = M C M + U C^\mathrm{T} V \; .
$$


**Proof:** The [expected value of a random matrix is equal to the matrix of expected values](/D/mean-rmat):

$$ \label{eq:mean-rmat}
  \mathrm{E}\left( \left[ \begin{array}{ccc} X_{11} & \ldots & X_{1p} \\ \vdots & \ddots & \vdots \\ X_{n1} & \ldots & X_{np} \end{array} \right] \right)
= \left[ \begin{array}{ccc} \mathrm{E}(X_{11}) & \ldots & \mathrm{E}(X_{1p}) \\ \vdots & \ddots & \vdots \\ \mathrm{E}(X_{n1}) & \ldots & \mathrm{E}(X_{np}) \end{array} \right] \; .
$$

The [expectation of a bilinear form](/P/mean-blf) $X^\mathrm{T} A Y$ with $X \in \mathbb{R}^{n}$, $Y \in \mathbb{R}^{m}$ and $A \in \mathbb{R}^{n \times m}$ [is equal to](/P/mean-blf)

$$ \label{eq:mean-blf}
\mathrm{E}\left[ X^\mathrm{T} A Y \right] = \mu_X^\mathrm{T} A \mu_Y + \mathrm{tr}(A^\mathrm{T} \Sigma_{XY})
$$

where $\mu_X = \mathrm{E}(X)$, $\mu_Y = \mathrm{E}(Y)$ and $\Sigma_{XY}$ is the $n \times m$ [cross-covariance matrix](/D/covmat-cross) of $X$ and $Y$.

When the matrix $X \in \mathbb{R}^{n \times p}$ follows a [matrix-normal distribution](/D/matn), we have [the following cross-covariance matrices](/P/matn-ccm) of rows and columns from $X$:

$$ \label{eq:matn-ccm-col}
\mathrm{Cov}(x_{\bullet i}, x_{\bullet j}) = v_{ij} \, U
\quad \text{where} \quad
i,j = 1,\ldots,p \; ;
$$

$$ \label{eq:matn-ccm-row}
\mathrm{Cov}(x_{i \bullet}^\mathrm{T}, x_{j \bullet}^\mathrm{T}) = u_{ij} \, V
\quad \text{where} \quad
i,j = 1,\ldots,n \; ;
$$

$$ \label{eq:matn-ccm-row-col}
\mathrm{Cov}(x_{i \bullet}^\mathrm{T}, x_{\bullet j}) = v_{\bullet j} \, u_{i \bullet}
\quad \text{where} \quad
i = 1,\ldots,n, \; j = 1,\ldots,p \; .
$$

With that, we are able to derive the above equations:

1) The $(i,j)$-th entry of the expectation $\mathrm{E}\left[ X A X^\mathrm{T} \right]$ is

$$ \label{eq:matn-mean-XAXT-qed}
\begin{split}
   \left( \mathrm{E}\left[ X A X^\mathrm{T} \right] \right)_{ij}
&\overset{\eqref{eq:mean-rmat}}{=} \mathrm{E}\left[ \left( X A X^\mathrm{T} \right)_{ij} \right] \\
&= \mathrm{E}\left[ x_{i \bullet} A x_{j \bullet}^\mathrm{T} \right] \\
&\overset{\eqref{eq:mean-blf}}{=} m_{i \bullet} A m_{j \bullet}^\mathrm{T} + \mathrm{tr}(A^\mathrm{T} \mathrm{Cov}[x_{i \bullet}^\mathrm{T}, x_{j \bullet}^\mathrm{T}]) \\
&\overset{\eqref{eq:matn-ccm-row}}{=} m_{i \bullet} A m_{j \bullet}^\mathrm{T} + \mathrm{tr}(A^\mathrm{T} u_{ij} V) \\
&= m_{i \bullet} A m_{j \bullet}^\mathrm{T} + u_{ij} \, \mathrm{tr}(A^\mathrm{T} V) \\
   \Rightarrow \mathrm{E}\left[ X A X^\mathrm{T} \right]
&= M A M^\mathrm{T} + U \, \mathrm{tr}(A^\mathrm{T} V) \; .
\end{split}
$$

2) The $(i,j)$-th entry of the expectation $\mathrm{E}\left[ X^\mathrm{T} B X \right]$ is

$$ \label{eq:matn-mean-XTBX-qed}
\begin{split}
   \left( \mathrm{E}\left[ X^\mathrm{T} B X \right] \right)_{ij}
&\overset{\eqref{eq:mean-rmat}}{=} \mathrm{E}\left[ \left( X B X^\mathrm{T} \right)_{ij} \right] \\
&= \mathrm{E}\left[ x_{\bullet i}^\mathrm{T} B x_{\bullet j} \right] \\
&\overset{\eqref{eq:mean-blf}}{=} m_{\bullet i}^\mathrm{T} B m_{\bullet j} + \mathrm{tr}(B^\mathrm{T} \mathrm{Cov}[x_{\bullet i}^\mathrm{T}, x_{\bullet j}]) \\
&\overset{\eqref{eq:matn-ccm-col}}{=} m_{\bullet i}^\mathrm{T} B m_{\bullet j} + \mathrm{tr}(B^\mathrm{T} v_{ij} U) \\
&= m_{\bullet i}^\mathrm{T} B m_{\bullet j} + v_{ij} \, \mathrm{tr}(U B^\mathrm{T}) \\
   \Rightarrow \mathrm{E}\left[ X^\mathrm{T} B X \right]
&= M^\mathrm{T} B M + V \, \mathrm{tr}(U B^\mathrm{T}) \; .
\end{split}
$$

3) The $(i,j)$-th entry of the expectation $\mathrm{E}\left[ X C X \right]$ is

$$ \label{eq:matn-mean-XCX-qed}
\begin{split}
   \left( \mathrm{E}\left[ X C X \right] \right)_{ij}
&\overset{\eqref{eq:mean-rmat}}{=} \mathrm{E}\left[ \left( X C X \right)_{ij} \right] \\
&= \mathrm{E}\left[ x_{i \bullet} C x_{\bullet j} \right] \\
&\overset{\eqref{eq:mean-blf}}{=} m_{i \bullet} C m_{\bullet j} + \mathrm{tr}(C^\mathrm{T} \mathrm{Cov}[x_{i \bullet}^\mathrm{T}, x_{\bullet j}]) \\
&\overset{\eqref{eq:matn-ccm-row-col}}{=} m_{i \bullet} C m_{\bullet j} + \mathrm{tr}(C^\mathrm{T} v_{\bullet j} u_{i \bullet}) \\
&= m_{i \bullet} C m_{\bullet j} + \mathrm{tr}(u_{i \bullet} C^\mathrm{T} v_{\bullet j}) \\
&= m_{i \bullet} C m_{\bullet j} + u_{i \bullet} C^\mathrm{T} v_{\bullet j} \\
   \Rightarrow \mathrm{E}\left[ X C X \right]
&= M C M + U C^\mathrm{T} V \; .
\end{split}
$$