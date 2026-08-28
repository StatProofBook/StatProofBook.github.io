---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-05-29 12:25:47

title: "Invariance of the sample correlation under linear transformation"
chapter: "General Theorems"
section: "Probability theory"
topic: "Correlation"
theorem: "Invariance of the sample correlation"

sources:
  - authors: "Ostwald D, Soch J"
    year: 2026
    title: "Korrelation"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (2), Folien 36-37"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2026/Allgemeines+Lineares+Modell/02_Korrelation.pdf"

proof_id: "P542"
shortcut: "corrsamp-inv"
username: "JoramSoch"
---


**Theorem:** Let $x = \left\lbrace x_1, \ldots, x_n \right\rbrace$ and $y = \left\lbrace y_1, \ldots, y_n \right\rbrace$ be [samples](/D/samp) from [random variables](/D/rvar) $X$ and $Y$. Further, let $\tilde{x} = \left\lbrace \tilde{x}_1, \ldots, \tilde{x}_n \right\rbrace$ and $\tilde{y} = \left\lbrace \tilde{y}_1, \ldots, \tilde{y}_n \right\rbrace$ be linearly transformed versions of this sample with

$$ \label{eq:samp-lin}
\begin{split}
\tilde{x}_i &= a x_i + b \\
\tilde{y}_i &= c y_i + d \; .
\end{split}
$$

Then, the absolute [sample correlation](/D/corr-samp) of $\tilde{x}$ and $\tilde{y}$ is equal to the absolute sample correlation of $x$ and $y$:

$$ \label{eq:corr-samp-inv}
|r_{\tilde{x}\tilde{y}}| = |r_{xy}| \; .
$$


**Proof:** The [sample correlation](/D/corr-samp) is defined in terms of the [sample means](/D/mean-samp) $\bar{x}$ and $\bar{y}$ as

$$ \label{eq:corr-samp}
r_{xy} = \frac{\sum_{i=1}^n (x_i-\bar{x}) (y_i-\bar{y})}{\sqrt{\sum_{i=1}^n (x_i-\bar{x})^2} \sqrt{\sum_{i=1}^n (y_i-\bar{y})^2}} \; .
$$

The [sample mean behaves linearly under linear transformation](/P/meansamp-lin):

$$ \label{eq:mean-samp-lin}
\begin{split}
\bar{\tilde{x}} &= a \bar{x} + b \\
\bar{\tilde{y}} &= c \bar{y} + d \; .
\end{split}
$$

Taking this together, we obtain:

$$ \label{eq:corr-samp-inv-s1}
\begin{split}
   r_{\tilde{x}\tilde{y}}
&\overset{\eqref{eq:corr-samp}}{=} \frac{\sum_{i=1}^n (\tilde{x}_i - \bar{\tilde{x}}) (\tilde{y}_i - \bar{\tilde{y}})}{\sqrt{\sum_{i=1}^n (\tilde{x}_i - \bar{\tilde{x}})^2} \sqrt{\sum_{i=1}^n (\tilde{y}_i - \bar{\tilde{y}})^2}} \\
&\overset{\eqref{eq:samp-lin}}{=} \frac{\sum_{i=1}^n \left( (a x_i + b) - \bar{\tilde{x}} \right) \left( (c y_i + d) - \bar{\tilde{y}} \right)}{\sqrt{\sum_{i=1}^n \left( (a x_i + b) - \bar{\tilde{x}} \right)^2} \sqrt{\sum_{i=1}^n \left( (c y_i + d) - \bar{\tilde{y}} \right)^2}} \\
&\overset{\eqref{eq:mean-samp-lin}}{=} \frac{\sum_{i=1}^n \left( (a x_i + b) - (a \bar{x} + b) \right) \left( (c y_i + d) - (c \bar{y} + d) \right)}{\sqrt{\sum_{i=1}^n \left( (a x_i + b) - (a \bar{x} + b) \right)^2} \sqrt{\sum_{i=1}^n \left( (c y_i + d) - (c \bar{y} + d) \right)^2}} \\
&= \frac{\sum_{i=1}^n \left( a x_i - a \bar{x} \right) \left( c y_i - c \bar{y} \right)}{\sqrt{\sum_{i=1}^n \left( a x_i - a \bar{x} \right)^2} \sqrt{\sum_{i=1}^n \left( c y_i - c \bar{y} \right)^2}} \\
&= \frac{\sum_{i=1}^n a (x_i-\bar{x}) c (y_i-\bar{y})}{\sqrt{\sum_{i=1}^n a^2 (x_i-\bar{x})^2} \sqrt{\sum_{i=1}^n c^2 (y_i-\bar{y})^2}} \\
&= \frac{a c}{\sqrt{a^2} \sqrt{c^2}} \frac{\sum_{i=1}^n (x_i-\bar{x}) (y_i-\bar{y})}{\sqrt{\sum_{i=1}^n (x_i-\bar{x})^2} \sqrt{\sum_{i=1}^n (y_i-\bar{y})^2}} \\
&\overset{\eqref{eq:corr-samp}}{=} \frac{a c}{|a| |c|} r_{xy} \; .
\end{split}
$$

Since $(a c)/(\lvert a \rvert \lvert c \rvert)$ is either $+1$ oder $-1$, we have

$$ \label{eq:corr-samp-inv-s2}
|r_{\tilde{x}\tilde{y}}| = |r_{xy}| \; .
$$