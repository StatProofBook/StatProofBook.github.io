---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2024-07-18 09:34:13

title: "Ordinary least squares for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Ordinary least squares"

sources:
  - authors: "Ostwald, Dirk"
    year: 2023
    title: "Parameterschätzung"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (6), Folien 10-12"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2023/Allgemeines+Lineares+Modell/6_Parametersch%C3%A4tzung.pdf"

proof_id: "P462"
shortcut: "mlr-ols3"
username: "JoramSoch"
---


**Theorem:** Given a [linear regression model](/D/mlr) with independent observations

$$ \label{eq:MLR}
y = X\beta + \varepsilon, \; \varepsilon_i \overset{\mathrm{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2) \; ,
$$

the parameters minimizing the [residual sum of squares](/D/rss) are given by

$$ \label{eq:OLS}
\hat{\beta} = (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \; .
$$


**Proof:** We consider the sum of squared differences between $y$ and $X\beta$:

$$ \label{eq:mlr-rss}
\sum_{i=1}^n \varepsilon_i^2
= \varepsilon^\mathrm{T} \varepsilon
= (y - X\beta)^\mathrm{T} (y - X\beta) \; .
$$

First, we note that the residual vector $\hat{\varepsilon}$ implied by the ordinary least squares solution $\hat{\beta}$ is orthogonal to the columns of the design matrix, such that the result of their multiplication is the $p$-dimensional zero vector (where $X \in \mathbb{R}^{n \times p}$):

$$ \label{eq:XTe}
\begin{split}
X^\mathrm{T} (y - X \hat{\beta})
&= X^\mathrm{T} y - X \hat{\beta} \\
&= X^\mathrm{T} y - X^\mathrm{T} X (X^\mathrm{T} X)^{-1} X^\mathrm{T} y \\
&= X^\mathrm{T} y - X^\mathrm{T} y \\
&= 0_p \; .
\end{split}
$$

Second, since $X^\mathrm{T} X$ [is a positive semi-definite matrix](/P/covmat-psd), the following product is non-negative for each $p$-dimensional real vector $z$:

$$ \label{eq:XTX-psd}
z^\mathrm{T} X^\mathrm{T} X z \geq 0 \quad \text{for each} \quad z \in \mathbb{R}^p \; .
$$

We continue developping the sum of squared differences from \eqref{eq:mlr-rss}:

$$ \label{eq:rss-s1}
\begin{split}
(y - X\beta)^\mathrm{T} (y - X\beta)
&= (y - X\hat{\beta} + X\hat{\beta} - X\beta)^\mathrm{T} (y - X\hat{\beta} + X\hat{\beta} - X\beta) \\
&= \left( (y - X\hat{\beta}) + X(\hat{\beta} - \beta) \right)^\mathrm{T} \left( (y - X\hat{\beta}) + X(\hat{\beta} - \beta) \right) \\
&= (y - X\hat{\beta})^\mathrm{T} (y - X\hat{\beta}) + (y - X\hat{\beta})^\mathrm{T} X (\hat{\beta} - \beta) + (\hat{\beta} - \beta)^\mathrm{T} X^\mathrm{T} (y - X\hat{\beta}) + (\hat{\beta} - \beta)^\mathrm{T} X^\mathrm{T} X (\hat{\beta} - \beta) \\
&\overset{\eqref{eq:XTe}}{=} (y - X\hat{\beta})^\mathrm{T} (y - X\hat{\beta}) + 0_p^\mathrm{T} (\hat{\beta} - \beta) + (\hat{\beta} - \beta)^\mathrm{T} 0_p + (\hat{\beta} - \beta)^\mathrm{T} X^\mathrm{T} X (\hat{\beta} - \beta) \\
&= (y - X\hat{\beta})^\mathrm{T} (y - X\hat{\beta}) + (\hat{\beta} - \beta)^\mathrm{T} X^\mathrm{T} X (\hat{\beta} - \beta) \; .
\end{split}
$$

By virtue of \eqref{eq:XTX-psd}, the second term on the right-hand side must be non-zero:

$$ \label{eq:bbTXTXbb}
(\hat{\beta} - \beta)^\mathrm{T} X^\mathrm{T} X (\hat{\beta} - \beta) \geq 0 \; .
$$

Thus, the residual sum of squares must be greater than or equal to the first term

$$ \label{eq:rss-s2}
(y - X\beta)^\mathrm{T} (y - X\beta) \geq (y - X\hat{\beta})^\mathrm{T} (y - X\hat{\beta})
$$

and its minimum value is reached when the the second term is zero:

$$ \label{eq:rss-s3}
\begin{split}
(\hat{\beta} - \beta)^\mathrm{T} X^\mathrm{T} X (\hat{\beta} - \beta) &= 0 \\
\Leftrightarrow \quad
(\hat{\beta} - \beta) &= 0 \\
\Leftrightarrow \quad
\beta &= \hat{\beta} \; .
\end{split}
$$

Thus, the residual sum of squares is minimized when $\beta = \hat{\beta}$:

$$ \label{eq:mlr-ols-qed}
\hat{\beta} = (X^\mathrm{T} X)^{-1} X^\mathrm{T} y = \operatorname*{arg\,min\,}_\beta (y - X\beta)^\mathrm{T} (y - X\beta) \; .
$$