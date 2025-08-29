---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-08-29 13:57:56

title: "Expectation of a bilinear form"
chapter: "General Theorems"
section: "Probability theory"
topic: "Expected value"
theorem: "Expectation of a bilinear form "

sources:

proof_id: "P513"
shortcut: "mean-blf"
username: "JoramSoch"
---


**Theorem:** Let $X$ be an $n$-dimensional [random vector](/D/rvec) with [mean](/D/mean) $\mu_X$ and let $Y$ be an $m$-dimensional [random vector](/D/rvec) with [mean](/D/mean) $\mu_Y$ where $X$ and $Y$ can or cannot be of equal of size ($n = m$ or $n \neq m$). Further, let $A$ be an $n \times m$ matrix and let $\Sigma_{XY}$ be the [cross-covariance matrix](/D/covmat-cross) of $X$ and $Y$. Then, the expectation of the bilinear form $X^\mathrm{T} A Y$ is

$$ \label{eq:mean-blf}
\mathrm{E}\left[ X^\mathrm{T} A Y \right] = \mu_X^\mathrm{T} A \mu_Y + \mathrm{tr}(A^\mathrm{T} \Sigma_{XY}) \; .
$$


**Proof:** Note that $X^\mathrm{T} A Y = Y^\mathrm{T} A^\mathrm{T} X$ is a $1 \times 1$ matrix. We can therefore write

$$ \label{eq:mean-blf-s1}
\mathrm{E}\left[ X^\mathrm{T} A Y \right] =  \mathrm{E}\left[ \mathrm{tr} \left( Y^\mathrm{T} A^\mathrm{T} X \right) \right] \; .
$$

Using the trace property $\mathrm{tr}(ABC) = \mathrm{tr}(BCA)$, this becomes

$$ \label{eq:mean-blf-s2}
\mathrm{E}\left[ X^\mathrm{T} A Y \right] =  \mathrm{E}\left[ \mathrm{tr} \left( A^\mathrm{T} X Y^\mathrm{T} \right) \right] \; .
$$

Because [mean and trace are linear operators](/P/mean-tr), we have

$$ \label{eq:mean-blf-s3}
\mathrm{E}\left[ X^\mathrm{T} A X \right] =  \mathrm{tr} \left( A^\mathrm{T} \mathrm{E}\left[ X Y^\mathrm{T} \right] \right) \; .
$$

Note that the [cross-covariance matrix can be partitioned into expected values](/P/covmatcross-mean)

$$ \label{eq:covmatcross-mean}
\mathrm{Cov}(X,Y) = \mathrm{E}(X Y^\mathrm{T}) - \mathrm{E}(X) \mathrm{E}(Y)^\mathrm{T} \; ,
$$

such that the expected value of the quadratic form becomes

$$ \label{eq:mean-blf-s4}
\mathrm{E}\left[ X^\mathrm{T} A Y \right] =  \mathrm{tr} \left( A \left[ \mathrm{Cov}(X,Y) + \mathrm{E}(X) \mathrm{E}(Y)^\mathrm{T} \right] \right) \; .
$$

Finally, applying [mean](/D/mean) and [covariance](/D/covmat) of $X$, we have

$$ \label{eq:mean-blf-s5}
\begin{split}
   \mathrm{E}\left[ X^\mathrm{T} A Y \right]
&= \mathrm{tr} \left( A^\mathrm{T} \left[ \Sigma_{XY} + \mu_X \mu_Y^\mathrm{T} \right] \right) \\
&= \mathrm{tr} \left( A^\mathrm{T} \Sigma_{XY} + A^\mathrm{T} \mu_X \mu_Y^\mathrm{T} \right) \\
&= \mathrm{tr}(A^\mathrm{T} \Sigma_{XY}) + \mathrm{tr}(A^\mathrm{T} \mu_X \mu_Y^\mathrm{T}) \\
&= \mathrm{tr}(A^\mathrm{T} \Sigma_{XY}) + \mathrm{tr}(\mu_Y^\mathrm{T} A^\mathrm{T} \mu_X) \\
&= \mathrm{tr}(A^\mathrm{T} \Sigma_{XY}) + \mathrm{tr}(\mu_X^\mathrm{T} A \mu_Y) \\
&= \mu_X^\mathrm{T} A \mu_Y + \mathrm{tr}(A^\mathrm{T} \Sigma_{XY}) \; .
\end{split}
$$