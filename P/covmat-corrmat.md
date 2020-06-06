---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-06-06 06:02:00

title: "Relationship between covariance matrix and correlation matrix"
chapter: "General Theorems"
section: "Probability theory"
topic: "Covariance"
theorem: "Covariance matrix and correlation matrix"

sources:
  - authors: "Penny, William"
    year: 2006
    title: "The correlation matrix"
    in: "Mathematics for Brain Imaging"
    pages: "ch. 1.4.5, p. 28, eq. 1.60"
    url: "https://ueapsylabs.co.uk/sites/wpenny/mbi/mbi_course.pdf"

proof_id: "P121"
shortcut: "covmat-corrmat"
username: "JoramSoch"
---


**Theorem:** Let $X$ be a [random vector](/D/rvec). Then, the [covariance matrix](/D/covmat) of $X$ can be expressed in terms of its [correlation matrix](/D/corrmat) as follows

$$ \label{eq:covmat-corrmat}
\Sigma_{XX} = \mathrm{D}_X \cdot \mathrm{C}_{XX} \cdot \mathrm{D}_X \; ,
$$

where $\mathrm{D}_X$ is a diagonal matrix with the [standard deviations](/D/std) of $X_1, \ldots, X_n$ as entries on the diagonal:

$$ \label{eq:diagmat}
\mathrm{D}_X = \mathrm{diag}(\sigma_{X_1},\ldots,\sigma_{X_n}) =
\begin{bmatrix}
\sigma_{X_1} & \ldots & 0 \\
\vdots & \ddots & \vdots \\
0 & \ldots & \sigma_{X_n}
\end{bmatrix} \; .
$$


**Proof:** Reiterating \eqref{eq:covmat-corrmat} and applying \eqref{eq:diagmat}, we have:

$$ \label{eq:covmat-corrmat-s1}
\Sigma_{XX} =
\begin{bmatrix}
\sigma_{X_1} & \ldots & 0 \\
\vdots & \ddots & \vdots \\
0 & \ldots & \sigma_{X_n}
\end{bmatrix} \cdot
\mathrm{C}_{XX} \cdot
\begin{bmatrix}
\sigma_{X_1} & \ldots & 0 \\
\vdots & \ddots & \vdots \\
0 & \ldots & \sigma_{X_n}
\end{bmatrix} \; .
$$

Together with the [definition of the correlation matrix](/D/corrmat), this gives

$$ \label{eq:covmat-corrmat-s2}
\begin{split}
\Sigma_{XX} &=
\begin{bmatrix}
\sigma_{X_1} & \ldots & 0 \\
\vdots & \ddots & \vdots \\
0 & \ldots & \sigma_{X_n}
\end{bmatrix} \cdot
\begin{bmatrix}
\frac{\mathrm{E}\left[(X_1-\mathrm{E}[X_1]) (X_1-\mathrm{E}[X_1])\right]}{\sigma_{X_1} \, \sigma_{X_1}} & \ldots & \frac{\mathrm{E}\left[(X_1-\mathrm{E}[X_1]) (X_n-\mathrm{E}[X_n])\right]}{\sigma_{X_1} \, \sigma_{X_n}} \\
\vdots & \ddots & \vdots \\
\frac{\mathrm{E}\left[(X_n-\mathrm{E}[X_n]) (X_1-\mathrm{E}[X_1])\right]}{\sigma_{X_n} \, \sigma_{X_1}} & \ldots & \frac{\mathrm{E}\left[(X_n-\mathrm{E}[X_n]) (X_n-\mathrm{E}[X_n])\right]}{\sigma_{X_n} \, \sigma_{X_n}}
\end{bmatrix} \cdot
\begin{bmatrix}
\sigma_{X_1} & \ldots & 0 \\
\vdots & \ddots & \vdots \\
0 & \ldots & \sigma_{X_n}
\end{bmatrix} \\
&=
\begin{bmatrix}
\frac{\sigma_{X_1} \cdot \mathrm{E}\left[(X_1-\mathrm{E}[X_1]) (X_1-\mathrm{E}[X_1])\right]}{\sigma_{X_1} \, \sigma_{X_1}} & \ldots & \frac{\sigma_{X_1} \cdot \mathrm{E}\left[(X_1-\mathrm{E}[X_1]) (X_n-\mathrm{E}[X_n])\right]}{\sigma_{X_1} \, \sigma_{X_n}} \\
\vdots & \ddots & \vdots \\
\frac{\sigma_{X_n} \cdot \mathrm{E}\left[(X_n-\mathrm{E}[X_n]) (X_1-\mathrm{E}[X_1])\right]}{\sigma_{X_n} \, \sigma_{X_1}} & \ldots & \frac{\sigma_{X_n} \cdot \mathrm{E}\left[(X_n-\mathrm{E}[X_n]) (X_n-\mathrm{E}[X_n])\right]}{\sigma_{X_n} \, \sigma_{X_n}}
\end{bmatrix} \cdot
\begin{bmatrix}
\sigma_{X_1} & \ldots & 0 \\
\vdots & \ddots & \vdots \\
0 & \ldots & \sigma_{X_n}
\end{bmatrix} \\
&=
\begin{bmatrix}
\frac{\sigma_{X_1} \cdot \mathrm{E}\left[(X_1-\mathrm{E}[X_1]) (X_1-\mathrm{E}[X_1])\right] \cdot \sigma_{X_1}}{\sigma_{X_1} \, \sigma_{X_1}} & \ldots & \frac{\sigma_{X_1} \cdot \mathrm{E}\left[(X_1-\mathrm{E}[X_1]) (X_n-\mathrm{E}[X_n])\right] \cdot \sigma_{X_n}}{\sigma_{X_1} \, \sigma_{X_n}} \\
\vdots & \ddots & \vdots \\
\frac{\sigma_{X_n} \cdot \mathrm{E}\left[(X_n-\mathrm{E}[X_n]) (X_1-\mathrm{E}[X_1])\right] \cdot \sigma_{X_1}}{\sigma_{X_n} \, \sigma_{X_1}} & \ldots & \frac{\sigma_{X_n} \cdot \mathrm{E}\left[(X_n-\mathrm{E}[X_n]) (X_n-\mathrm{E}[X_n])\right] \cdot \sigma_{X_n}}{\sigma_{X_n} \, \sigma_{X_n}}
\end{bmatrix} \\
&=
\begin{bmatrix}
\mathrm{E}\left[ (X_1-\mathrm{E}[X_1]) (X_1-\mathrm{E}[X_1]) \right] & \ldots & \mathrm{E}\left[ (X_1-\mathrm{E}[X_1]) (X_n-\mathrm{E}[X_n]) \right] \\
\vdots & \ddots & \vdots \\
\mathrm{E}\left[ (X_n-\mathrm{E}[X_n]) (X_1-\mathrm{E}[X_1]) \right] & \ldots & \mathrm{E}\left[ (X_n-\mathrm{E}[X_n]) (X_n-\mathrm{E}[X_n]) \right]
\end{bmatrix}
\end{split}
$$

which is nothing else than the [definition of the covariance matrix](/D/covmat).