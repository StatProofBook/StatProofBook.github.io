---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-05-31 14:35:20

title: "Omnibus F-test for multiple regressors in multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "F-test for multiple regressors"

sources:
  - authors: "Ostwald, Dirk"
    year: 2023
    title: "F-Statistiken"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (8), Folien 20, 24"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2023/Allgemeines+Lineares+Modell/8_F_Statistiken-p-9972.pdf"

proof_id: "P454"
shortcut: "mlr-fomnibus"
username: "JoramSoch"
---


**Theorem:** Consider a [linear regression model](/D/mlr)

$$ \label{eq:mlr}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V)
$$

the design matrix and regression coefficients of which are partitioned as

$$ \label{eq:mlr-X-b}
\begin{split}
X = \left[ \begin{matrix} X_0 & X_1 \end{matrix} \right] \in \mathbb{R}^{n \times p}
\quad &\text{where} \quad
X_0 \in \mathbb{R}^{n \times p_0} \quad \text{and} \quad X_1 \in \mathbb{R}^{n \times p_1} \\
\beta = \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right] \in \mathbb{R}^{p \times 1}
\quad &\text{where} \quad
\beta_0 \in \mathbb{R}^{p_0 \times 1} \quad \text{and} \quad \beta_1 \in \mathbb{R}^{p_1 \times 1}
\end{split}
$$

with $p = p_0 + p_1$. Then, the [test statistic](/D/tstat)

$$ \label{eq:mlr-f-omnibus}
F = \frac{(\hat{\varepsilon}_0^\mathrm{T} V^{-1} \hat{\varepsilon}_0 - \hat{\varepsilon}^\mathrm{T} V^{-1} \hat{\varepsilon})/p_1}{\hat{\varepsilon}^\mathrm{T} V^{-1} \hat{\varepsilon}/(n-p)}
$$

follows an [F-distribution](/D/f)

$$ \label{eq:mlr-f-omnibus-dist}
F \sim \mathrm{F}(p_1, n-p)
$$

under the [null hypothesis](/D/h0) that all [regression coefficients](/D/mlr) $\beta_1$ are zero:

$$ \label{eq:mlr-f-omnibus-h0}
H_0: \; \beta_1 = 0_{p_1} \quad \Leftrightarrow \quad
\beta_j = 0 \quad \text{for all} \quad j = (p_0+1),\ldots,p \; .
$$

In \eqref{eq:mlr-f-omnibus}, $\hat{\varepsilon}$ and $\hat{\varepsilon}_0$ are the [residual vectors](/P/mlr-mat) when using either the full design matrix $X$ or the reduced design matrix $X_0$:

$$ \label{eq:mlr-e-e0}
\begin{split}
\hat{\varepsilon} = y - X \hat{\beta} \quad &\text{with} \quad
\hat{\beta} = (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \\
\hat{\varepsilon}_0 = y - X_0 \hat{\beta}_0 \quad &\text{with} \quad
\hat{\beta}_0 = (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} y \; .
\end{split}
$$


**Proof:** This is a special case of the [contrast-based F-test for multiple linear regression](/P/mlr-f) based on the [F-statistic](/D/tstat)

$$ \label{eq:mlr-f}
F = \hat{\beta}^\mathrm{T} C \left( \hat{\sigma}^2 C^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C \right)^{-1} C^\mathrm{T} \hat{\beta} / q
$$

which follows an [F-distribution](/D/f) under the [null hypothesis](/D/h0) that the product of the [contrast matrix](/D/fcon) $C \in \mathbb{R}^{p \times q}$ and the [regression coefficients](/D/mlr) equals zero: 

$$ \label{eq:mlr-f-dist-h0}
F \sim \mathrm{F}(q, n-p), \quad \text{if} \quad C^\mathrm{T} \beta = 0_q = \left[ \begin{matrix} 0 \\ \vdots \\ 0 \end{matrix} \right] \; .
$$

In \eqref{eq:mlr-f}, $\hat{\sigma}^2$ is an estimate of the [noise variance](/D/mlr) calculated as the [weighted](/P/mlr-wls) [residual sum of squares](/D/rss), divided by $n-p$:

$$ \label{eq:mlr-sig2-est}
\hat{\sigma}^2 = \frac{1}{n-p} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) \; .
$$

In the present case, in order to compare the full model specified by $X$ against the reduced model specified by $X_0$, we have to define the [contrast matrix](/D/fcon) as a vertical concatenation of a zero matrix on the first $p_0$ components and an identity matrix on the last $p_1$ components of $\beta$,

$$ \label{eq:mlr-f-omnibus-C}
\begin{split}
C_1 = \left[ \begin{matrix} 0_{p_0,p_1} \\ I_{p_1} \end{matrix} \right] \in \mathbb{R}^{p \times p_1} \; ,
\end{split}
$$

i.e. specify an omnibus F-contrast that tests the [alternative hypothesis](/D/h1) that any of the coefficients $\beta_1$ associated with the regressors $X_1$ is different from zero against the [null hypothesis](/D/h0) that all those coefficients are zero:

$$ \label{eq:mlr-f-omnibus-h0-C}
\begin{split}
&H_0: \; C_1^\mathrm{T} \beta
= \left[ \begin{matrix} 0_{p_0,p_1} \\ I_{p_1} \end{matrix} \right]^\mathrm{T} \left[ \begin{matrix} \beta_0 \\ \beta_1 \end{matrix} \right]
= \beta_1 = 0_{p_1} \quad \Leftrightarrow \quad \beta_{1j} = 0 \quad \text{for all} \quad j=1,\ldots,p_1 \\
\Rightarrow \; &H_1 \Leftrightarrow \neg H_0: \;  C_1^\mathrm{T} \beta
= \beta_1 \neq 0_{p_1} \quad \Leftrightarrow \quad  \beta_{1j} \neq 0 \quad \text{for at least one} \quad j=1,\ldots,p_1 \; .
\end{split}
$$

Thus, plugging $C = C_1$ and $q = p_1$ into \eqref{eq:mlr-f} and noting that $\hat{\sigma}^2$ from \eqref{eq:mlr-sig2-est} is a scalar, we obtain:

$$ \label{eq:mlr-f-s1}
\begin{split}
F
&= \hat{\beta}^\mathrm{T} C_1 \left( \hat{\sigma}^2 C_1^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C_1 \right)^{-1} C_1^\mathrm{T} \hat{\beta} / p_1 \\
&\overset{\eqref{eq:mlr-sig2-est}}{=} \frac{\hat{\beta}^\mathrm{T} C_1 \left( C_1^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C_1 \right)^{-1} C_1^\mathrm{T} \hat{\beta} / p_1}{(y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) / (n-p)} \; .
\end{split}
$$

Here, we take note of the fact that the denominator in \eqref{eq:mlr-f-s1} is already equal to the denominator in \eqref{eq:mlr-f-omnibus}:

$$ \label{eq:mlr-f-den}
(y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) / (n-p) \overset{\eqref{eq:mlr-e-e0}}{=} \hat{\varepsilon}^\mathrm{T} V^{-1} \hat{\varepsilon}/(n-p) \; .
$$

Therefore, what remains to be shown is that the numerator in \eqref{eq:mlr-f-s1} is equal to the numerator in \eqref{eq:mlr-f-omnibus}:

$$ \label{eq:mlr-f-num}
\hat{\beta}^\mathrm{T} C_1 \left( C_1^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C_1 \right)^{-1} C_1^\mathrm{T} \hat{\beta} / p_1 = (\hat{\varepsilon}_0^\mathrm{T} V^{-1} \hat{\varepsilon}_0 - \hat{\varepsilon}^\mathrm{T} V^{-1} \hat{\varepsilon})/p_1 \; .
$$

To do this, we start with the inner-most matrix:

$$ \label{eq:mlr-f-s2}
\begin{split}
X^\mathrm{T} V^{-1} X
&\overset{\eqref{eq:mlr-X-b}}{=} \left[ \begin{matrix} X_0 & X_1 \end{matrix} \right]^\mathrm{T} V^{-1} \left[ \begin{matrix} X_0 & X_1 \end{matrix} \right] \\
&= \left[ \begin{matrix} X_0^\mathrm{T} \\ X_1^\mathrm{T} \end{matrix} \right] V^{-1} \left[ \begin{matrix} X_0 & X_1 \end{matrix} \right] \\
&= \left[ \begin{matrix} X_0^\mathrm{T} V^{-1} X_0 & X_0^\mathrm{T} V^{-1} X_1 \\ X_1^\mathrm{T} V^{-1} X_0 & X_1^\mathrm{T} V^{-1} X_1 \end{matrix} \right] \; .
\end{split}
$$

The inverse of a block matrix is:

$$ \label{eq:block-inv}
\begin{bmatrix}
A & B \\
C & D
\end{bmatrix}^{-1} =
\begin{bmatrix}
A^{-1} + A^{-1}B(D-CA^{-1}B)^{-1}CA^{-1} & -A^{-1}B(D-CA^{-1}B)^{-1} \\
-(D-CA^{-1}B)^{-1}CA^{-1}                & (D-CA^{-1}B)^{-1}
\end{bmatrix} \; .
$$

Note that, with the contrast matrix $C_1$, we only extract the lower-right part of the inverse block matrix, so that we have:

$$ \label{eq:mlr-f-s3}
\begin{split}
\left( C_1^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C_1 \right)^{-1}
&\overset{\eqref{eq:mlr-f-omnibus-C}}{=} \left( \left[ \begin{matrix} 0_{p_1,p_0} & I_{p_1} \end{matrix} \right] (X^\mathrm{T} V^{-1} X)^{-1} \left[ \begin{matrix} 0_{p_0,p_1} \\ I_{p_1} \end{matrix} \right] \right)^{-1} \\
&\overset{\eqref{eq:block-inv}}{=} \left( \left( X_1^\mathrm{T} V^{-1} X_1 - X_1^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} X_1 \right)^{-1} \right)^{-1} \\
&= X_1^\mathrm{T} V^{-1} X_1 - X_1^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} X_1 \; .
\end{split}
$$

We call this $p_1 \times p_1$ matrix $E$ and note that it can be written as

$$ \label{eq:mlr-f-E}
\begin{split}
E
&\overset{\eqref{eq:mlr-f-s3}}{=} X_1^\mathrm{T} \left( V^{-1} - V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} \right) X_1 \\
&= X_1^\mathrm{T} \left( V^{-1} - F \right) X_1
\end{split}
$$

where the $n \times n$ matrix $F$ is given as follows:

$$ \label{eq:mlr-f-F}
F
= V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} \; .
$$

Let $\hat{\beta}_{0(X)}$ denote the first $p_0$ entries of $\hat{\beta}$, i.e. estimates of the coefficients belonging to $X_0$, but estimated with $X$ (as opposed to $\hat{\beta}_0$ estimated with $X_0$ given by \eqref{eq:mlr-e-e0}):

$$ \label{eq:hat-b-b0X-b1}
\hat{\beta} = \left[ \begin{matrix} \hat{\beta}_{0(X)} \\ \hat{\beta}_1 \end{matrix} \right] \; .
$$

Then, it obviously holds that

$$ \label{eq:mlr-f-s4}
\begin{split}
X \hat{\beta}
&\overset{\eqref{eq:hat-b-b0X-b1}}{=} \left[ \begin{matrix} X_0 & X_1 \end{matrix} \right] \left[ \begin{matrix} \hat{\beta}_{0(X)} \\ \hat{\beta}_1 \end{matrix} \right] \\
&= X_0 \hat{\beta}_{0(X)} + X_1 \hat{\beta}_1 \\
&\Leftrightarrow \\
X_1 \hat{\beta}_1 &= X \hat{\beta} - X_0 \hat{\beta}_{0(X)} \; .
\end{split}
$$

Next, we focus on $C_1^\mathrm{T} \hat{\beta}$ which simply extracts $\hat{\beta}_1$:

$$ \label{eq:mlr-f-s5}
\begin{split}
C_1^\mathrm{T} \hat{\beta}
&\overset{\eqref{eq:hat-b-b0X-b1}}{=} \left[ \begin{matrix} 0_{p_1,p_0} & I_{p_1} \end{matrix} \right] \left[ \begin{matrix} \hat{\beta}_{0(X)} \\ \hat{\beta}_1 \end{matrix} \right] \\
&= \hat{\beta}_1 \; .
\end{split}
$$

With these identities in mind, we can get back to our main quantity of interest from \eqref{eq:mlr-f-num}:

$$ \label{eq:mlr-f-s6}
\begin{split}
&\quad\quad \hat{\beta}^\mathrm{T} C_1 \left( C_1^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C_1 \right)^{-1} C_1^\mathrm{T} \hat{\beta} \\
&\overset{\eqref{eq:mlr-f-s5}}{=} \hat{\beta}_1^\mathrm{T} \; E \; \hat{\beta}_1 \\
&\overset{\eqref{eq:mlr-f-E}}{=} \hat{\beta}_1^\mathrm{T} X_1^\mathrm{T} \left( V^{-1} - V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} \right) X_1 \hat{\beta}_1 \\
&\overset{\eqref{eq:mlr-f-s4}}{=} \left( \hat{\beta}^\mathrm{T} X^\mathrm{T} - \hat{\beta}_{0(X)}^\mathrm{T} X_0^\mathrm{T} \right) \left( V^{-1} - V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} \right) \left( X \hat{\beta} - X_0 \hat{\beta}_{0(X)} \right) \\
&\overset{\eqref{eq:mlr-f-F}}{=} \left( \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} - \hat{\beta}^\mathrm{T} X^\mathrm{T} F - \hat{\beta}_{0(X)}^\mathrm{T} X_0^\mathrm{T} V^{-1} + \hat{\beta}_{0(X)}^\mathrm{T} X_0^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} \right) \left( X \hat{\beta} - X_0 \hat{\beta}_{0(X)} \right) \\
&= \left( \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} - \hat{\beta}^\mathrm{T} X^\mathrm{T} F - \hat{\beta}_{0(X)}^\mathrm{T} X_0^\mathrm{T} V^{-1} + \hat{\beta}_{0(X)}^\mathrm{T} X_0^\mathrm{T} V^{-1} \right) \left( X \hat{\beta} - X_0 \hat{\beta}_{0(X)} \right) \\
&= \left( \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} - \hat{\beta}^\mathrm{T} X^\mathrm{T} F \right) \left( X \hat{\beta} - X_0 \hat{\beta}_{0(X)} \right) \\
&\overset{\eqref{eq:mlr-f-F}}{=} \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X \hat{\beta} - \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X_0 \hat{\beta}_{0(X)} - \hat{\beta}^\mathrm{T} X^\mathrm{T} F X \hat{\beta} + \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} X_0 \hat{\beta}_{0(X)} \\
&= \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X \hat{\beta} - \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X_0 \hat{\beta}_{0(X)} - \hat{\beta}^\mathrm{T} X^\mathrm{T} F X \hat{\beta} + \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X_0 \hat{\beta}_{0(X)} \\
&= \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X \hat{\beta} - \hat{\beta}^\mathrm{T} X^\mathrm{T} F X \hat{\beta} \\
&\overset{\eqref{eq:mlr-f-F}}{=} \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X \hat{\beta} - \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} X \hat{\beta} \; .
\end{split}
$$

Let the residual vector of the full model be defined as given by \eqref{eq:mlr-e-e0}

$$ \label{eq:hat-e}
\hat{\varepsilon} = y - X \hat{\beta} \quad \Leftrightarrow \quad y = X \hat{\beta} + \hat{\varepsilon}
$$

and consider the term $X^\mathrm{T} V^{-1} \hat{\varepsilon}$. Using the [residual-forming matrix expression of the residual vector](/P/mlr-mat), we can show that this matrix product is zero:

$$ \label{eq:mlr-f-s7a}
\begin{split}
X^\mathrm{T} V^{-1} \hat{\varepsilon}
&= X^\mathrm{T} V^{-1} \left( I_n - X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} \right) y \\
&= X^\mathrm{T} V^{-1} y - X^\mathrm{T} V^{-1} X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \\
&= X^\mathrm{T} V^{-1} y - X^\mathrm{T} V^{-1} y \\
&= 0_p \; .
\end{split}
$$

From this, it follows that the product $X_0^\mathrm{T} V^{-1} \hat{\varepsilon}$ is also zero:

$$ \label{eq:mlr-f-s7b}
\begin{split}
X^\mathrm{T} V^{-1} \hat{\varepsilon} &= 0_p \\
\left[ \begin{matrix} X_0^\mathrm{T} \\ X_1^\mathrm{T} \end{matrix} \right] V^{-1} \hat{\varepsilon} &= 0_p \\
\left[ \begin{matrix} X_0^\mathrm{T} V^{-1} \hat{\varepsilon} \\ X_1^\mathrm{T} V^{-1} \hat{\varepsilon} \end{matrix} \right] &= \left[ \begin{matrix} 0_{p_0} \\ 0_{p_1} \end{matrix} \right] \\
&\Leftrightarrow \\
X_0^\mathrm{T} V^{-1} \hat{\varepsilon} &= 0_{p_0} \; .
\end{split}
$$

Thus, any term containing $X_0^\mathrm{T} V^{-1} \hat{\varepsilon} = 0_{p_0}$ can be added to a sum without changing the value of this sum. Continuing from above, we therefore write:

$$ \label{eq:mlr-f-s8}
\begin{split}
&\quad\quad \hat{\beta}^\mathrm{T} C_1 \left( C_1^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C_1 \right)^{-1} C_1^\mathrm{T} \hat{\beta} \\
&\overset{\eqref{eq:mlr-f-s6}}{=} \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X \hat{\beta} - \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} X \hat{\beta} \\
&\overset{\eqref{eq:mlr-f-s7b}}{=} \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X \hat{\beta} - \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} X \hat{\beta} \\
&+ 2 \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} \hat{\varepsilon} + \hat{\varepsilon}^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} \hat{\varepsilon} \\
&= \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X \hat{\beta} - \left( X \hat{\beta} + \hat{\varepsilon} \right)^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} \left( X \hat{\beta} + \hat{\varepsilon} \right) \\
&\overset{\eqref{eq:hat-e}}{=} \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X \hat{\beta} - y^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} y \; .
\end{split}
$$

In the next transformations, we will make use of the [weighted least squares parameter estimates](/P/mlr-wls)

$$ \label{eq:mlr-b-b0}
\begin{split}
\hat{\beta} &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \\
\hat{\beta}_0 &= (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} y
\end{split}
$$

and the fact that matrices and their inverses cancel out:

$$ \label{eq:mlr-inv}
\begin{split}
X^\mathrm{T} V^{-1} X (X^\mathrm{T} V^{-1} X)^{-1} = (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} X &= I_p \\
X_0^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} = (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} X_0 &= I_{p_0} \; .
\end{split}
$$

Continuing from above, we have:

$$ \label{eq:mlr-f-s9}
\begin{split}
&\quad\quad \hat{\beta}^\mathrm{T} C_1 \left( C_1^\mathrm{T} (X^\mathrm{T} V^{-1} X)^{-1} C_1 \right)^{-1} C_1^\mathrm{T} \hat{\beta} \\
&\overset{\eqref{eq:mlr-f-s8}}{=} \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X \hat{\beta} - y^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} y \\
&\overset{\eqref{eq:mlr-b-b0}}{=} y^\mathrm{T} V^{-1} X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y - y^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} y \\
&= y^\mathrm{T} V^{-1} X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y - y^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} y \\
&= y^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} y - 2 y^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} y \\
&- y^\mathrm{T} V^{-1} X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y + 2 y^\mathrm{T} V^{-1} X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \\
&\overset{\eqref{eq:mlr-inv}}{=} y^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} y - 2 y^\mathrm{T} V^{-1} X_0 (X_0^\mathrm{T} V^{-1} X_0)^{-1} X_0^\mathrm{T} V^{-1} y \\
&- y^\mathrm{T} V^{-1} X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y + 2 y^\mathrm{T} V^{-1} X (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \\
&\overset{\eqref{eq:mlr-b-b0}}{=} \hat{\beta}_0^\mathrm{T} X_0^\mathrm{T} V^{-1} X_0 \hat{\beta}_0 - 2 y^\mathrm{T} V^{-1} X_0 \hat{\beta}_0 - \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X \hat{\beta} + 2 y^\mathrm{T} V^{-1} X \hat{\beta} \\
&= y^\mathrm{T} V^{-1} y - 2 y^\mathrm{T} V^{-1} X_0 \hat{\beta}_0 + \hat{\beta}_0^\mathrm{T} X_0^\mathrm{T} V^{-1} X_0 \hat{\beta}_0 - y^\mathrm{T} V^{-1} y + 2 y^\mathrm{T} V^{-1} X \hat{\beta} - \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X \hat{\beta} \\
&= \left( y^\mathrm{T} V^{-1} y - 2 y^\mathrm{T} V^{-1} X_0 \hat{\beta}_0 + \hat{\beta}_0^\mathrm{T} X_0^\mathrm{T} V^{-1} X_0 \hat{\beta}_0 \right) - \left( y^\mathrm{T} V^{-1} y - 2 y^\mathrm{T} V^{-1} X \hat{\beta} + \hat{\beta}^\mathrm{T} X^\mathrm{T} V^{-1} X \hat{\beta} \right) \\
&= (y - X_0 \hat{\beta}_0)^\mathrm{T} V^{-1} (y - X_0 \hat{\beta}_0) - (y - X \hat{\beta})^\mathrm{T} V^{-1} (y - X \hat{\beta}) \\
&\overset{\eqref{eq:mlr-e-e0}}{=} \hat{\varepsilon}_0^\mathrm{T} V^{-1} \hat{\varepsilon}_0 - \hat{\varepsilon}^\mathrm{T} V^{-1} \hat{\varepsilon} \; .
\end{split}
$$

With that, it is shown that \eqref{eq:mlr-f-num} is true which, together with \eqref{eq:mlr-f-den}, finally demonstrates that the F-value in \eqref{eq:mlr-f-s1} is equal to the test statistic given by \eqref{eq:mlr-f-omnibus}. This completes the proof.