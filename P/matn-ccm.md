---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-01-23 11:07:00

title: "Cross-covariance matrices of the matrix-normal distribution"
chapter: "Probability Distributions"
section: "Matrix-variate continuous distributions"
topic: "Matrix-normal distribution"
theorem: "Cross-covariances"

sources:

proof_id: "P522"
shortcut: "matn-ccm"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n \times p$ [random matrix](/D/rmat) following a [matrix-normal distribution](/D/matn):

$$ \label{eq:matn}
X \sim \mathcal{MN}(M, U, V) \; .
$$

Then,

1) the [cross-covariance matrix](/D/covmat-cross) of any two columns of $X$ is equal to $U$, multiplied with the corresponding entry of $V$:

$$ \label{eq:matn-ccm-col}
\mathrm{Cov}(x_{\bullet i}, x_{\bullet j}) = v_{ij} \, U
\quad \text{where} \quad
i,j = 1,\ldots,p \; ;
$$

2) the [cross-covariance matrix](/D/covmat-cross) of any two rows of $X$ is equal to $V$, multiplied with the corresponding entry of $U$:

$$ \label{eq:matn-ccm-row}
\mathrm{Cov}(x_{i \bullet}^\mathrm{T}, x_{j \bullet}^\mathrm{T}) = u_{ij} \, V
\quad \text{where} \quad
i,j = 1,\ldots,n \; ;
$$

3) the [cross-covariance matrix](/D/covmat-cross) of a given row and column from $X$ is equal to the matrix product of the corresponding row and column from $V$ and $U$:

$$ \label{eq:matn-ccm-row-col}
\mathrm{Cov}(x_{i \bullet}^\mathrm{T}, x_{\bullet j}) = v_{\bullet j} \, u_{i \bullet}
\quad \text{where} \quad
i = 1,\ldots,n, \; j = 1,\ldots,p \; .
$$


**Proof:** When the matrix $X \in \mathbb{R}^{n \times p}$ follows a [matrix-normal distribution](/D/matn), the vector $\mathrm{vec}(X) \in \mathbb{R}^{np}$ [follows a multivariate normal distribution](/P/matn-mvn):

$$ \label{eq:matn-mvn}
\mathrm{vec}(X) \sim \mathcal{N}(\mathrm{vec}(M), V \otimes U)
$$

where $\mathrm{vec}(A)$ is the vectorization function which collects the entries of an $n \times m$ matrix $A$ into a single $(n \cdot m)$-dimensional vector column by column:

$$ \label{eq:vec}
\mathrm{vec}(A) =
\left[
\begin{matrix}
x_{11} \\ \vdots \\ x_{n1} \\
       \\ \vdots \\        \\
x_{1m} \\ \vdots \\ x_{nm}
\end{matrix}
\right] \; .
$$

Any [marginal distribution of a multivariate normal distribution](/P/mvn-marg) can be obtained by removing the corresponding entries (i.e. the ones marginalized out) from [mean vector and covariance matrix](/D/mvn):

$$ \label{eq:mvn-marg}
X \sim \mathcal{N}(\mu, \Sigma)
\quad \Rightarrow \quad
X_s \sim \mathcal{N}(\mu_s, \Sigma_s) \; .
$$

Moreover, the [covariance matrix of a multivariate normal distribution](/P/mvn-cov) is equal to the [second parameter of the distribution](/D/mvn):

$$ \label{eq:mvn-cov}
X \sim \mathcal{N}(\mu, \Sigma)
\quad \Rightarrow \quad
\mathrm{Cov}(X) = \Sigma \; .
$$

Thus, the above cross-covariance matrices can be read out from the non-diagonal entries of covariance matrices belonging to marginal distribution of corresponding rows and columns according to \eqref{eq:matn-mvn} and \eqref{eq:mvn-marg}.

1) The marginal distribution of two columns $x_{\bullet i}$ and $x_{\bullet j}$ is

$$ \label{eq:matn-marg-col}
\left[ \begin{matrix} x_{\bullet i} \\ x_{\bullet j} \end{matrix} \right]
\sim \mathcal{N} \left(
\left[ \begin{matrix} m_{\bullet i} \\ m_{\bullet j} \end{matrix} \right],
\left[ \begin{matrix} v_{ii} & v_{ij} \\ v_{ji} & v_{jj} \end{matrix} \right] \otimes U
\right) \; .
$$

Thus, the [cross-covariance](/D/covmat-cross) of $x_{\bullet i}$ and $x_{\bullet j}$ is

$$ \label{eq:matn-ccm-col-qed}
\mathrm{Cov}(x_{\bullet i}, x_{\bullet j}) = v_{ij} \, U \; .
$$

2) The marginal distribution of two rows $x_{i \bullet}$ and $x_{j \bullet}$ is

$$ \label{eq:matn-marg-row}
\left[ \begin{matrix} x_{i \bullet}^\mathrm{T} \\ x_{j \bullet}^\mathrm{T} \end{matrix} \right]
\sim \mathcal{N} \left(
\left[ \begin{matrix} m_{i \bullet}^\mathrm{T} \\ m_{j \bullet}^\mathrm{T} \end{matrix} \right],
V \otimes \left[ \begin{matrix} u_{ii} & u_{ij} \\ u_{ji} & u_{jj} \end{matrix} \right]
\right) \; .
$$

Thus, the [cross-covariance](/D/covmat-cross) of $x_{i \bullet}$ and $x_{j \bullet}$ is

$$ \label{eq:matn-ccm-row-qed}
\mathrm{Cov}(x_{i \bullet}^\mathrm{T}, x_{j \bullet}^\mathrm{T}) = u_{ij} \, V \; .
$$

3) The cross-covariance matrix of a row $x_{i \bullet}$ and a column $x_{\bullet j}$ can be obtained by extracting the rows $i, n+i, 2n+i, \ldots$ (i.e. belonging to $x_{i \bullet}$) and the columns $j, p+j, 2p+j, \ldots$ (i.e. belonging to $x_{\bullet j}$) from the matrix $V \otimes U$.

Thus, the [cross-covariance](/D/covmat-cross) of $x_{i \bullet}$ and $x_{\bullet j}$ is

$$ \label{eq:matn-ccm-row-col-qed}
\mathrm{Cov}(x_{i \bullet}^\mathrm{T}, x_{\bullet j}) = v_{\bullet j} \, u_{i \bullet} \; .
$$

Note that $v_{\bullet j} \in \mathbb{R}^{p \times 1}$ and $u_{i \bullet} \in \mathbb{R}^{1 \times n}$, such that $v_{\bullet j} \, u_{i \bullet} \in \mathbb{R}^{p \times n}$, compatible with $x_{i \bullet}^\mathrm{T} \in \mathbb{R}^p$ ($p$ entries per row) and $x_{\bullet j} \in \mathbb{R}^n$ ($n$ entries per column).