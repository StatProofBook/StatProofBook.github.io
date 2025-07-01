---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2025-05-22 15:59:00

title: "Construction of a bivariate normal distribution from univariate standard normal random variables"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Bivariate normal distribution"
theorem: "Construction from standard normal distributions"

sources:
  - authors: "Ostwald, Dirk"
    year: 2023
    title: "Normalverteilungen"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (4), Folie 15"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2023/Allgemeines+Lineares+Modell/4_Normalverteilungen.pdf"
  - authors: "Wikipedia"
    year: 2025
    title: "Multivariate normal distribution"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2025-05-23"
    url: "https://en.wikipedia.org/wiki/Multivariate_normal_distribution#Bivariate_case"

proof_id: "P502"
shortcut: "bvn-snorm"
username: "JoramSoch"
---


**Theorem:** Let $Y_1$ and $Y_2$ be [independent](/D/ind) [random variables](/D/rvar) following a [standard normal distribution](/D/snorm):

$$ \label{eq:Y12}
Y_1 \sim \mathcal{N}(0,1) \quad \text{and} \quad
Y_2 \sim \mathcal{N}(0,1) \quad \text{ind.}
$$

and define the two [random variables](/D/rvar) $X_1$ and $X_2$

$$ \label{eq:X12}
\begin{split}
X_1 &= \sigma_1 Y_1 + \mu_1 \\
X_2 &= \sigma_2 \left( \rho Y_1 + \sqrt{1-\rho^2} Y_2 \right) + \mu_2
\end{split}
$$

where $\mu_1, \mu_2 \in \mathbb{R}$, $\sigma_1, \sigma_2 \in \mathbb{R}_{>0}$ and $\rho \in [-1,+1]$. Then, the [random vector](/D/rvec) with entries $X_1$ and $X_2$ follows a [bivariate normal distribution](/D/bvn)

$$ \label{eq:bvn-snorm}
\begin{split}
X =  \left[ \begin{matrix} X_1 \\ X_2 \end{matrix} \right]
\sim \mathcal{N}\left( \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right],
					   \left[ \begin{matrix} \sigma_1^2 & \rho \sigma_1 \sigma_2 \\
					                         \rho \sigma_1 \sigma_2 & \sigma_2^2 \end{matrix} \right] \right)
\end{split}
$$

where [mean and covariance](/D/bvn) are functions of the parameters $\mu_1$, $\mu_2$, $\sigma_1$, $\sigma_2$ and $\rho$.


**Proof:** The [probability density function of the standard normal distribution](/P/norm-pdf) is

$$ \label{eq:snorm-pdf}
Y \sim \mathcal{N}(0,1)
\quad \Rightarrow \quad
f_Y(y) = \frac{1}{\sqrt{2 \pi}} \cdot \exp \left[ -\frac{1}{2} y^2 \right] \; .
$$

The random variables $X_1$ and $X_2$ are functions of $Y_1$ and $Y_2$

$$ \label{eq:X12-Y12}
\begin{split}
X_1 &= \sigma_1 Y_1 + \mu_1 \\
X_2 &= \sigma_2 \left( \rho Y_1 + \sqrt{1-\rho^2} Y_2 \right) + \mu_2 \; ,
\end{split}
$$

such that the inverse functions $Y_1$ and $Y_2$ in terms of $X_1$ and $X_2$ are

$$ \label{eq:Y12-X12}
\begin{split}
Y_1 &= (X_1 - \mu_1)/\sigma_1 \\
Y_2 &= \left[ (X_2-\mu_2)/\sigma_2 - \rho Y_1 \right] / \sqrt{1-\rho^2} \\
    &= \left[ (X_2-\mu_2)/\sigma_2 - \rho (X_1-\mu_1)/\sigma_1 \right] / \sqrt{1-\rho^2} \; .
\end{split}
$$

This implies the following Jacobian matrix

$$ \label{eq:Y12-X12-jac}
  J
= \left[ \begin{matrix}
\frac{\mathrm{d}Y_1}{\mathrm{d}X_1} & \frac{\mathrm{d}Y_1}{\mathrm{d}X_2} \\
\frac{\mathrm{d}Y_2}{\mathrm{d}X_1} & \frac{\mathrm{d}Y_2}{\mathrm{d}X_2}
\end{matrix} \right]
= \left[ \begin{matrix}
\frac{1}{\sigma_1}                    & 0                                  \\
\frac{\rho}{\sigma_1 \sqrt{1-\rho^2}} & \frac{1}{\sigma_2 \sqrt{1-\rho^2}}
\end{matrix} \right]
$$

and determinant of the Jacobian matrix

$$ \label{eq:Y12-X12-jac-det}
\begin{split}
   \lvert J \rvert
&= \frac{1}{\sigma_1} \cdot \frac{1}{\sigma_2 \sqrt{1-\rho^2}} - 0 \cdot \frac{\rho}{\sigma_1 \sqrt{1-\rho^2}} \\
&= \frac{1}{\sigma_1 \sigma_2 \sqrt{1-\rho^2}} \\
&= \frac{1}{\sqrt{\sigma_1^2 \sigma_2^2 (1-\rho^2)}} \; .
\end{split}
$$

Because $Y_1$ and $Y_2$ are [independent](/D/ind), the [joint density](/D/dist-joint) of $Y_1$ and $Y_2$ is [equal to the product](/P/prob-ind) of the [marginal densities](/D/dist-marg):

$$ \label{eq:f-Y12-s1}
f_{Y_1,Y_2}(y_1,y_2) = f_{Y_1}(y_1) \cdot f_{Y_2}(y_2) \; .
$$

Substituting \eqref{eq:snorm-pdf} into \eqref{eq:f-Y12-s1}, we get:

$$ \label{eq:f-Y12-s2}
\begin{split}
   f_{Y_1,Y_2}(y_1,y_2)
&= \frac{1}{\sqrt{2 \pi}} \exp \left[ -\frac{1}{2} y_1^2 \right] \cdot \frac{1}{\sqrt{2 \pi}} \exp \left[ -\frac{1}{2} y_2^2 \right] \\
&= \frac{1}{\sqrt{(2 \pi)^2}} \cdot \exp \left[ -\frac{1}{2} \left( y_1^2 + y_2^2 \right) \right] \; .
\end{split}
$$

With the [probability density function of an invertible function](/P/pdf-invfct), the [joint density](/D/dist-joint) of $X_1$ and $X_2$ can be derived as:

$$ \label{eq:f-X12-s1}
f_{X_1,X_2}(x_1,x_2) = f_{Y_1,Y_2}(y_1,y_2) \cdot \lvert J \rvert \; .
$$

Substituting \eqref{eq:f-Y12-s2}, \eqref{eq:Y12-X12} and \eqref{eq:Y12-X12-jac-det} into \eqref{eq:f-X12-s1}, we get:

$$ \label{eq:f-XY12-s2}
\begin{split}
   f_{X_1,X_2}(x_1,x_2)
&= \frac{1}{\sqrt{(2 \pi)^2}} \cdot \exp \left[ -\frac{1}{2} \left( \left( \frac{x_1-\mu_1}{\sigma_1} \right)^2 + \left( \left[ \frac{x_2-\mu_2}{\sigma_2} - \rho \frac{x_1-\mu_1}{\sigma_1} \right] / \sqrt{1-\rho^2} \right)^2 \right) \right] \cdot \frac{1}{\sqrt{\sigma_1^2 \sigma_2^2 (1-\rho^2)}} \\
&= \frac{1}{\sqrt{(2 \pi)^2 \sigma_1^2 \sigma_2^2 (1-\rho^2)}} \cdot \exp \left[ -\frac{1}{2} \left( \left( \frac{x_1-\mu_1}{\sigma_1} \right)^2 + \frac{1}{1-\rho^2} \left[ \left( \frac{x_2-\mu_2}{\sigma_2} \right)^2 - 2 \rho \left( \frac{x_1-\mu_1}{\sigma_1} \right) \left( \frac{x_2-\mu_2}{\sigma_2} \right) + \rho^2 \left( \frac{x_1-\mu_1}{\sigma_1} \right)^2 \right] \right) \right] \\
&= \frac{1}{2 \pi \sigma_1 \sigma_2 \sqrt{1-\rho^2}} \cdot \exp \left[ -\frac{1}{2(1-\rho^2)} \left( \left( \frac{x_1-\mu_1}{\sigma_1} \right)^2 - 2 \rho \frac{(x_1-\mu_1)(x_2-\mu_2)}{\sigma_1 \sigma_2} + \left( \frac{x_2-\mu_2}{\sigma_2} \right)^2 \right) \right] \; .
\end{split}
$$

This is the [probability density function of the bivariate normal distribution](/P/bvn-pdfcorr) with parameters

$$ \label{eq:bvn-mu-Sigma}
\mu    = \left[ \begin{matrix} \mu_1 \\ \mu_2 \end{matrix} \right] \quad \text{and} \quad
\Sigma = \left[ \begin{matrix} \sigma_1^2 & \rho \sigma_1 \sigma_2 \\
							   \rho \sigma_1 \sigma_2 & \sigma_2^2 \end{matrix} \right] \; .
$$

Thus, it follows that

$$ \label{eq:bvn-snorm-qed}
\begin{split}
X \sim \mathcal{N}(\mu, \Sigma) \; .
\end{split}
$$