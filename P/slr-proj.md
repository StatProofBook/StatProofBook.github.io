---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2021-11-09 10:16:00

title: "Projection of a data point to the regression line"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Simple linear regression"
theorem: "Projection of data point to regression line"

sources:
  - authors: "Penny, William"
    year: 2006
    title: "Projections"
    in: "Mathematics for Brain Imaging"
    pages: "ch. 1.4.10, pp. 34-35, eqs. 1.87/1.88"
    url: "https://ueapsylabs.co.uk/sites/wpenny/mbi/mbi_course.pdf"

proof_id: "P283"
shortcut: "slr-proj"
username: "JoramSoch"
---


**Theorem:** Consider [simple linear regression](/D/slr) and an [estimated regression line](/D/regline) specified by

$$ \label{eq:slr-regline}
y = \hat{\beta}_0 + \hat{\beta}_1 x \quad \text{where} \quad x,y \in \mathbb{R} \; .
$$

For any given data point $O(x_o \vert y_o)$, the point on the regression line $P(x_p \vert y_p)$ that is closest to this data point is given by:

$$ \label{eq:slr-proj}
P\left(w \mid \hat{\beta}_0 + \hat{\beta}_1 w\right) \quad \text{with} \quad w = \frac{x_0 + (y_o - \hat{\beta}_0) \hat{\beta}_1}{1 + \hat{\beta}_1^2} \; .
$$


**Proof:** The intersection point of the [regression line](/D/regline) with the y-axis is

$$ \label{eq:S}
S(0 \vert \hat{\beta}_0) \; .
$$

Let $a$ be a vector describing the direction of the regression line, let $b$ be the vector pointing from $S$ to $O$ and let $p$ be the vector pointing from $S$ to $P$.

Because $\hat{\beta}_1$ is the slope of the regression line, we have

$$ \label{eq:a}
a = \left( \begin{matrix} 1 \\ \hat{\beta}_1 \end{matrix} \right) \; .
$$

Moreover, with the points $O$ and $S$, we have

$$ \label{eq:b}
b = \left( \begin{matrix} x_o \\ y_o \end{matrix} \right) - \left( \begin{matrix} 0 \\ \hat{\beta}_0 \end{matrix} \right) = \left( \begin{matrix} x_o \\ y_o - \hat{\beta}_0 \end{matrix} \right) \; .
$$

Because $P$ is located on the regression line, $p$ is collinear with $a$ and thus a scalar multiple of this vector:

$$ \label{eq:p}
p = w \cdot a \; .
$$

Moreover, as $P$ is the point on the regression line which is closest to $O$, this means that the vector $b-p$ is orthogonal to $a$, such that the inner product of these two vectors is equal to zero:

$$ \label{eq:a-b-p-orth}
a^\mathrm{T} (b-p) = 0 \; .
$$

Rearranging this equation gives

$$ \label{eq:w}
\begin{split}
a^\mathrm{T} (b-p) &= 0 \\
a^\mathrm{T} (b - w \cdot a) &= 0 \\
a^\mathrm{T} b - w \cdot a^\mathrm{T} a &= 0 \\
w \cdot a^\mathrm{T} a &= a^\mathrm{T} b \\
w &= \frac{a^\mathrm{T} b}{a^\mathrm{T} a} \; .
\end{split}
$$

With \eqref{eq:a} and \eqref{eq:b}, $w$ can be calculated as

$$ \label{eq:w-qed}
\begin{split}
w &= \frac{a^\mathrm{T} b}{a^\mathrm{T} a} \\
w &= \frac{\left( \begin{matrix} 1 \\ \hat{\beta}_1 \end{matrix} \right)^\mathrm{T} \left( \begin{matrix} x_o \\ y_o - \hat{\beta}_0 \end{matrix} \right)}{\left( \begin{matrix} 1 \\ \hat{\beta}_1 \end{matrix} \right)^\mathrm{T} \left( \begin{matrix} 1 \\ \hat{\beta}_1 \end{matrix} \right)} \\
w &= \frac{x_0 + (y_o - \hat{\beta}_0) \hat{\beta}_1}{1 + \hat{\beta}_1^2}
\end{split}
$$

Finally, with the point $S$ \eqref{eq:S} and the vector $p$ \eqref{eq:p}, the coordinates of $P$ are obtained as

$$ \label{eq:P-qed}
\left( \begin{matrix} x_p \\ y_p \end{matrix} \right) = \left( \begin{matrix} 0 \\ \hat{\beta}_0 \end{matrix} \right) + w \cdot \left( \begin{matrix} 1 \\ \hat{\beta}_1 \end{matrix} \right) = \left( \begin{matrix} w \\ \hat{\beta}_0 + \hat{\beta}_1 w \end{matrix} \right) \; .
$$

Together, \eqref{eq:P-qed} and \eqref{eq:w-qed} constitute the proof of equation \eqref{eq:slr-proj}.