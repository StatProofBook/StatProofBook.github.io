---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-08-29 13:44:11

title: "Partition of a cross-covariance matrix into expected values"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance matrix"
theorem: "Cross-covariance and expected values"

sources:

proof_id: "P512"
shortcut: "covmatcross-mean"
username: "JoramSoch"
---


**Theorem:** Let $X$ and $Y$ be a [random vectors](/D/rvec). Then, the [cross-covariance matrix](/D/covmat-cross) of $X$ and $Y$ is equal to the [mean](/D/mean) of the outer product of $X$ with $Y$ minus the outer product of the [means](/D/mean) of $X$ and $Y$:

$$ \label{eq:covmatcross-mean}
\Sigma_{XY} = \mathrm{E}(X Y^\mathrm{T}) - \mathrm{E}(X) \mathrm{E}(Y)^\mathrm{T} \; .
$$


**Proof:** The [cross-covariance matrix](/D/covmat-cross) of $X$ and $Y$ is defined as

$$ \label{eq:covmat-cross1}
\Sigma_{XY} =
\begin{bmatrix}
\mathrm{E}\left[ (X_1-\mathrm{E}[X_1]) (Y_1-\mathrm{E}[Y_1]) \right] & \ldots & \mathrm{E}\left[ (X_1-\mathrm{E}[X_1]) (Y_m-\mathrm{E}[Y_m]) \right] \\
\vdots & \ddots & \vdots \\
\mathrm{E}\left[ (X_n-\mathrm{E}[X_n]) (Y_1-\mathrm{E}[Y_1]) \right] & \ldots & \mathrm{E}\left[ (X_n-\mathrm{E}[X_n]) (Y_m-\mathrm{E}[Y_m]) \right]
\end{bmatrix}
$$

which can also be expressed using matrix multiplication as

$$ \label{eq:covmat-cross2}
\Sigma_{XY} = \mathrm{E}\left[ (X-\mathrm{E}[X]) (Y-\mathrm{E}[Y])^\mathrm{T} \right] \; .
$$

Due to the [linearity of the expected value](/P/mean-lin), this can be rewritten as

$$ \label{eq:covmatcross-mean-qed}
\begin{split}
   \Sigma_{XY}
&= \mathrm{E}\left[ (X-\mathrm{E}[X]) (Y-\mathrm{E}[Y])^\mathrm{T} \right] \\
&= \mathrm{E}\left[ X Y^\mathrm{T} - X \, \mathrm{E}(Y)^\mathrm{T} - \mathrm{E}(X) \, Y^\mathrm{T} + \mathrm{E}(X) \mathrm{E}(Y)^\mathrm{T} \right] \\
&= \mathrm{E}(X Y^\mathrm{T}) - \mathrm{E}(X) \mathrm{E}(Y)^\mathrm{T} - \mathrm{E}(X) \mathrm{E}(Y)^\mathrm{T} + \mathrm{E}(X) \mathrm{E}(Y)^\mathrm{T} \\
&= \mathrm{E}(X Y^\mathrm{T}) - \mathrm{E}(X) \mathrm{E}(Y)^\mathrm{T} \; .
\end{split}
$$