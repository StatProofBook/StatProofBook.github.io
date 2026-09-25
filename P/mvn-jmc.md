---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-08-28 12:02:10

title: "Joint distribution of marginally and conditionally multivariate normal random vectors"
chapter: "Probability Distributions"
section: "Multivariate continuous distributions"
topic: "Multivariate normal distribution"
theorem: "Joint distribution"

sources:
  - authors: "Ostwald D, Soch J"
    year: 2026
    title: "Normalverteilungen"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (4), Folien 34-39"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre/Sommersemester+2026/Allgemeines+Lineares+Modell/04_Normalverteilungen-p-13695.pdf"
  - authors: "Wikipedia"
    year: 2026
    title: "Methods of matrix inversion"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2026-08-28"
    url: "https://en.wikipedia.org/wiki/Methods_of_matrix_inversion#Blockwise_inversion"
  - authors: "Wikipedia"
    year: 2026
    title: "Determinant"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2026-08-28"
    url: "https://en.wikipedia.org/wiki/Determinant#Block_matrices"

proof_id: "P548"
shortcut: "mvn-jmc"
username: "JoramSoch"
---


**Theorem:** Let $X = [X_1,\ldots,X_m]^\mathrm{T}$ be an $m$-dimensional [multivariate normal](/D/mvn) [random vector](/D/rvec)

$$ \label{eq:mvn-marg}
X \sim N(\mu_X, \Sigma_{XX})
\quad \mbox{with} \quad
\mu_X \in \mathbb{R}^m
\quad \mbox{and} \quad
\Sigma_{XX} \in \mathbb{R}^{m \times m}
$$

and let $Y = [Y_1,\ldots,Y_n]^\mathrm{T}$ be an $n$-dimensional [conditionally](/D/dist-cond) [multivariate normal distributed](/D/mvn)

$$ \label{eq:mvn-cond}
Y|X \sim N(AX+b, \Sigma_{YY})
\quad \mbox{with} \quad
\Sigma_{YY} \in \mathbb{R}^{n \times n}
\quad \mbox{as well as} \quad
A \in \mathbb{R}^{n \times m}
\quad \mbox{and} \quad
b \in \mathbb{R}^n \; .
$$

Then, the $(m+n)$-dimensional random vector $Z = \begin{pmatrix} X \\ Y \end{pmatrix}$ is [jointly](/D/dist-joint) [multivariate normal distributed](/D/mvn)

$$ \label{eq:mvn-joint}
Z \sim N(\mu_{X,Y}, \Sigma_{X,Y})
$$

with the [multivariate mean](/D/mvn)

$$ \label{eq:mvn-joint-mean}
\mu_{X,Y} = \begin{pmatrix} \mu_X \\ A\mu_X + b \end{pmatrix} \in \mathbb{R}^{m+n}
$$

and the [covariance matrix](/D/mvn)

$$ \label{eq:mvn-joint-cov}
\Sigma_{X,Y} =
\begin{pmatrix}
\Sigma_{XX}   & \Sigma_{XX} A^\mathrm{T} \\
A \Sigma_{XX} & \Sigma_{YY} + A \Sigma_{XX} A^\mathrm{T}
\end{pmatrix} \in \mathbb{R}^{(m+n) \times (m+n)} \; .
$$


**Proof:** The [probability density function for the maginal distribution](/P/mvn-pdf) of $X$ is

$$ \label{eq:mvn-marg-pdf}
p(x) = \frac{1}{\sqrt{(2\pi)^m |\Sigma_{XX}|}} \exp\left(-\frac{1}{2} (x-\mu_X)^\mathrm{T} \Sigma_{XX}^{-1} (x-\mu_X)\right) \; .
$$

The [probability density function for the conditional distribution](/P/mvn-pdf) of $Y$ given $X$ is

$$ \label{eq:mvn-cond-pdf}
p(y|x) = \frac{1}{\sqrt{(2\pi)^n |\Sigma_{YY}|}} \exp\left(-\frac{1}{2} (y-(Ax+b))^\mathrm{T} \Sigma_{YY}^{-1} (y-(Ax+b))\right) \; .
$$

According to the [law of conditional probability](/D/prob-cond), we have

$$ \label{eq:prob-cond}
p(y|x) = \frac{p(x,y)}{p(x)} \; ,
$$

such that

$$ \label{eq:prob-joint}
p(x,y) = p(y|x) \cdot p(x) \; .
$$

With \eqref{eq:mvn-marg-pdf} and \eqref{eq:mvn-cond-pdf}, we get:

$$ \label{eq:mvn-joint-pdf-s1}
\begin{split}
   p(x,y)
&= \frac{1}{\sqrt{(2\pi)^n |\Sigma_{YY}|}} \exp\left(-\frac{1}{2} (y-(Ax+b))^\mathrm{T} \Sigma_{YY}^{-1} (y-(Ax+b))\right) \cdot \\
&\hphantom{=}\; \frac{1}{\sqrt{(2\pi)^m |\Sigma_{XX}|}} \exp\left(-\frac{1}{2} (x-\mu_X)^\mathrm{T} \Sigma_{XX}^{-1} (x-\mu_X)\right) \\
&= \frac{1}{\sqrt{(2\pi)^{m+n} |\Sigma_{XX}| |\Sigma_{YY}|}} \exp\left(-\frac{1}{2} \left[ (x-\mu_X)^\mathrm{T} \Sigma_{XX}^{-1} (x-\mu_X) + (y-(Ax+b))^\mathrm{T} \Sigma_{YY}^{-1} (y-(Ax+b)) \right] \right) \; .
\end{split}
$$

The determinant of a block matrix is:

$$ \label{eq:block-det}
  \left| \begin{pmatrix} A & B \\ C & D \end{pmatrix} \right|
= |A| \cdot | D - C A^{-1} B | \; .
$$

Thus, we get

$$ \label{eq:Sigma-yy-det}
\begin{split}
\left| \begin{pmatrix}
\Sigma_{XX}   & \Sigma_{XX} A^\mathrm{T} \\
A \Sigma_{XX} & \Sigma_{YY} + A \Sigma_{XX} A^\mathrm{T}
\end{pmatrix} \right|
&= |\Sigma_{XX}| \cdot | \Sigma_{YY} + A \Sigma_{XX} A^\mathrm{T} - A \Sigma_{XX} \Sigma_{XX}^{-1} \Sigma_{XX} A^\mathrm{T} | \\
&= |\Sigma_{XX}| \cdot | \Sigma_{YY} + A \Sigma_{XX} A^\mathrm{T} - A \Sigma_{XX} A^\mathrm{T} | \\
&= |\Sigma_{XX}| \cdot | \Sigma_{YY} + 0_{nn} | \\
&= |\Sigma_{XX}| \cdot |\Sigma_{YY}| \; ,
\end{split}
$$

such that

$$ \label{eq:mvn-joint-pdf-s2}
|\Sigma_{XX}| |\Sigma_{YY}| = |\Sigma_{X,Y}| \; .
$$

The inverse of a block matrix is:

$$ \label{eq:block-inv}
  \begin{pmatrix} A & B \\ C & D \end{pmatrix}^{-1}
= \begin{pmatrix} 
A^{-1} + A^{-1}B (D - CA^{-1}B)^{-1} CA^{-1} & -A^{-1}B (D - CA^{-1}B)^{-1} \\
-(D - CA^{-1}B)^{-1} CA^{-1}                 & (D - CA^{-1}B)^{-1}
\end{pmatrix} \; .
$$

With

$$ \label{eq:Sigma-yy-inv-D}
  D - CA^{-1}B
= \Sigma_{YY} + A \Sigma_{XX} A^\mathrm{T} - A \Sigma_{XX} \Sigma_{XX}^{-1} \Sigma_{XX} A^\mathrm{T}
= \Sigma_{YY} \; ,
$$

we obtain

$$ \label{eq:Sigma-yy-inv}
\begin{split}
\begin{pmatrix}
\Sigma_{XX}   & \Sigma_{XX} A^\mathrm{T} \\
A \Sigma_{XX} & \Sigma_{YY} + A \Sigma_{XX} A^\mathrm{T}
\end{pmatrix}^{-1}
&=\begin{pmatrix}
  \Sigma_{XX}^{-1} + \Sigma_{XX}^{-1} \Sigma_{XX} A^\mathrm{T} \Sigma_{YY}^{-1} A \Sigma_{XX} \Sigma_{XX}^{-1}
& -\Sigma_{XX}^{-1} \Sigma_{XX} A^\mathrm{T} \Sigma_{YY}^{-1} \\
  -\Sigma_{YY}^{-1} A \Sigma_{XX} \Sigma_{XX}^{-1}
& \Sigma_{YY}^{-1}
  \end{pmatrix} \\
&=\begin{pmatrix}
  \Sigma_{XX}^{-1} + A^\mathrm{T} \Sigma_{YY}^{-1} A
& -A^\mathrm{T} \Sigma_{YY}^{-1} \\
  -\Sigma_{YY}^{-1} A
& \Sigma_{YY}^{-1}
  \end{pmatrix} \; ,
\end{split}
$$

such that

$$ \label{eq:mvn-joint-pdf-s3a}
\begin{split}
&\hphantom{=}\;
\left( \begin{pmatrix} x \\ y \end{pmatrix} - \begin{pmatrix} \mu_X \\ A\mu_X + b \end{pmatrix} \right)^\mathrm{T}
\begin{pmatrix}
\Sigma_{XX}   & \Sigma_{XX} A^\mathrm{T} \\
A \Sigma_{XX} & \Sigma_{YY} + A \Sigma_{XX} A^\mathrm{T}
\end{pmatrix}^{-1}
\left( \begin{pmatrix} x \\ y \end{pmatrix} - \begin{pmatrix} \mu_X \\ A\mu_X + b \end{pmatrix} \right) \\
&=
\begin{pmatrix} x - \mu_X \\ y - (A\mu_X + b) \end{pmatrix}^\mathrm{T}
\begin{pmatrix}
  \Sigma_{XX}^{-1} + A^\mathrm{T} \Sigma_{YY}^{-1} A
& -A^\mathrm{T} \Sigma_{YY}^{-1} \\
  -\Sigma_{YY}^{-1} A
& \Sigma_{YY}^{-1}
\end{pmatrix}
\begin{pmatrix} x - \mu_X \\ y - (A\mu_X + b) \end{pmatrix} \\
&=
\begin{pmatrix}
  (x - \mu_X)^\mathrm{T} (\Sigma_{XX}^{-1} + A^\mathrm{T} \Sigma_{YY}^{-1} A)
- (y - (A\mu_X + b))^\mathrm{T} \Sigma_{YY}^{-1} A \\
- (x - \mu_X)^\mathrm{T} A^\mathrm{T} \Sigma_{YY}^{-1}
+ (y - (A\mu_X + b))^\mathrm{T} \Sigma_{XX}^{-1}
\end{pmatrix}^\mathrm{T}
\begin{pmatrix} x - \mu_X \\ y - A\mu_X + b \end{pmatrix} \\
&= (x - \mu_X)^\mathrm{T} (\Sigma_{XX}^{-1} + A^\mathrm{T} \Sigma_{YY}^{-1} A) (x - \mu_X) - (y - (A\mu_X + b))^\mathrm{T} \Sigma_{YY}^{-1} A (x - \mu_X) \\
&- (x - \mu_X)^\mathrm{T} A^\mathrm{T} \Sigma_{YY}^{-1} (y - (A\mu_X + b)) + (y - (A\mu_X + b))^\mathrm{T} \Sigma_{XX}^{-1} (y - (A\mu_X + b)) \; .
\end{split}
$$

With

$$ \label{eq:Sigma-yy-inv-equiv}
\begin{split}
&\hphantom{=}\; \left[ (x - \mu_X)^\mathrm{T} A^\mathrm{T} \Sigma_{YY}^{-1} (y - (A\mu_X + b)) \right]^\mathrm{T} \\
&= \left[ (y - (A\mu_X + b))^\mathrm{T} \Sigma_{YY}^{-1} A (x - \mu_X) \right] \in \mathbb{R}^{1 \times 1} \; ,
\end{split}
$$

we thus obtain

$$ \label{eq:mvn-joint-pdf-s3b}
\begin{split}
&\hphantom{=}\;
\left( \begin{pmatrix} x \\ y \end{pmatrix} - \begin{pmatrix} \mu_X \\ A\mu_X + b \end{pmatrix} \right)^\mathrm{T}
\begin{pmatrix}
\Sigma_{XX}   & \Sigma_{XX} A^\mathrm{T} \\
A \Sigma_{XX} & \Sigma_{YY} + A \Sigma_{XX} A^\mathrm{T}
\end{pmatrix}^{-1}
\left( \begin{pmatrix} x \\ y \end{pmatrix} - \begin{pmatrix} \mu_X \\ A\mu_X + b \end{pmatrix} \right) \\
&= (x - \mu_X)^\mathrm{T} \Sigma_{XX}^{-1} (x - \mu_X) + (x - \mu_X)^\mathrm{T} A^\mathrm{T} \Sigma_{YY}^{-1} A (x - \mu_X) \\
&- 2 (y - (A\mu_X + b))^\mathrm{T} \Sigma_{YY}^{-1} A (x - \mu_X) + (y - (A\mu_X + b))^\mathrm{T} \Sigma_{XX}^{-1} (y - (A\mu_X + b)) \\
&= (x - \mu_X)^\mathrm{T} \Sigma_{XX}^{-1} (x - \mu_X) + (Ax - A\mu_X)^\mathrm{T} \Sigma_{YY}^{-1} (Ax - A\mu_X) \\
&- 2 (y - (A\mu_X + b))^\mathrm{T} \Sigma_{YY}^{-1} A (x - \mu_X) + (y - (A\mu_X + b))^\mathrm{T} \Sigma_{XX}^{-1} (y - (A\mu_X + b)) \\
&= (x - \mu_X)^\mathrm{T} \Sigma_{XX}^{-1} (x - \mu_X) \\
&+ \left[ Ax - A\mu_X - 2(y - (A\mu_X + b) + (y - (A\mu_X + b) \right]^\mathrm{T} \Sigma_{XX}^{-1} \left[  Ax - A\mu_X - 2(y - (A\mu_X + b) + (y - (A\mu_X + b) \right] \\
&= (x - \mu_X)^\mathrm{T} \Sigma_{XX}^{-1} (x - \mu_X) \\
&+ \left[ Ax - A\mu_X - (y - (A\mu_X + b) \right]^\mathrm{T} \Sigma_{XX}^{-1} \left[  Ax - A\mu_X - (y - (A\mu_X + b) \right] \\
&= (x - \mu_X)^\mathrm{T} \Sigma_{XX}^{-1} (x - \mu_X) \\
&+ \left[ Ax - A\mu_X - (y - (A\mu_X + b) \right]^\mathrm{T} \Sigma_{XX}^{-1} \left[  Ax - A\mu_X - (y - (A\mu_X + b) \right] \\
&= (x - \mu_X)^\mathrm{T} \Sigma_{XX}^{-1} (x - \mu_X) + (y - (Ax + b))^\mathrm{T} \Sigma_{XX}^{-1} (y - (Ax + b)) \; ,
\end{split}
$$

such that

$$ \label{eq:mvn-joint-pdf-s3c}
\begin{split}
&\hphantom{=}\; (x-\mu_X)^\mathrm{T} \Sigma_{XX}^{-1} (x-\mu_X) + (y-(Ax+b))^\mathrm{T} \Sigma_{YY}^{-1} (y-(Ax+b)) \\
&= \left( \begin{pmatrix} x \\ y \end{pmatrix} - \begin{pmatrix} \mu_X \\ A\mu_X + b \end{pmatrix} \right)^\mathrm{T}
\begin{pmatrix}
\Sigma_{XX}   & \Sigma_{XX} A^\mathrm{T} \\
A \Sigma_{XX} & \Sigma_{YY} + A \Sigma_{XX} A^\mathrm{T}
\end{pmatrix}^{-1}
\left( \begin{pmatrix} x \\ y \end{pmatrix} - \begin{pmatrix} \mu_X \\ A\mu_X + b \end{pmatrix} \right) \\
&= (z-\mu_{X,Y})^\mathrm{T} \Sigma_{X,Y}^{-1} (z-\mu_{X,Y}) \; .
\end{split}
$$

Plugging \eqref{eq:mvn-joint-pdf-s2} and \eqref{eq:mvn-joint-pdf-s3c} into \eqref{eq:mvn-joint-pdf-s1}, we finally get

$$ \label{eq:mvn-joint-pdf-s4}
\begin{split}
   p(z)
&= \frac{1}{\sqrt{(2\pi)^{m+n} |\Sigma_{X,Y}|}} \exp\left(-\frac{1}{2} (z-\mu_{X,Y})^\mathrm{T} \Sigma_{X,Y}^{-1} (z-\mu_{X,Y}) \right)
\end{split}
$$

which is the [probability density function of a multivariate normal distribution](/P/mvn-pdf) for the random vector $Z \in \mathbb{R}^{m+n}$ with multivariate mean $\mu_{X,Y}$ from \eqref{eq:mvn-joint-mean} and covariance matrix $\Sigma_{X,Y}$ from \eqref{eq:mvn-joint-cov}.
