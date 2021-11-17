---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-03-11 12:27:00

title: "Maximum likelihood estimation for multiple linear regression"
chapter: "Statistical Models"
section: "Univariate normal data"
topic: "Multiple linear regression"
theorem: "Maximum likelihood estimation"

sources:

proof_id: "P78"
shortcut: "mlr-mle"
username: "JoramSoch"
---


**Theorem:** Given a [linear regression model](/D/mlr) with correlated observations

$$ \label{eq:MLR}
y = X\beta + \varepsilon, \; \varepsilon \sim \mathcal{N}(0, \sigma^2 V) \; ,
$$

the [maximum likelihood estimates](/D/mle) of $\beta$ and $\sigma^2$ are given  by

$$ \label{eq:MLE-MLE}
\begin{split}
\hat{\beta} &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} y \\
\hat{\sigma}^2 &= \frac{1}{n} (y-X\hat{\beta})^\mathrm{T} V^{-1} (y-X\hat{\beta}) \; .
\end{split}
$$


**Proof:** With the [probability density function of the multivariate normal distribution](/P/mvn-pdf), the linear regression equation \eqref{eq:MLR} implies the following [likelihood function](/D/lf)

$$ \label{eq:MLR-LF}
\begin{split}
p(y|\beta,\sigma^2) &= \mathcal{N}(y; X\beta, \sigma^2 V) \\
&= \sqrt{\frac{1}{(2\pi)^n |\sigma^2 V|}} \cdot \exp\left[ -\frac{1}{2} (y - X\beta)^\mathrm{T} (\sigma^2 V)^{-1} (y - X\beta) \right]
\end{split}
$$

and, using $\lvert \sigma^2 V \rvert = (\sigma^2)^n \lvert V \rvert$, the [log-likelihood function](/D/llf)

$$ \label{eq:MLR-LL1}
\begin{split}
\mathrm{LL}(\beta,\sigma^2) = &\log p(y|\beta,\sigma^2) \\
= &- \frac{n}{2} \log(2\pi) - \frac{n}{2} \log (\sigma^2) - \frac{1}{2} \log |V| \\
&- \frac{1}{2 \sigma^2} (y - X\beta)^\mathrm{T} V^{-1} (y - X\beta) \; .
\end{split}
$$

Substituting the precision matrix $P = V^{-1}$ into \eqref{eq:MLR-LL1} to ease notation, we have:

$$ \label{eq:MLR-LL2}
\begin{split}
\mathrm{LL}(\beta,\sigma^2) = &- \frac{n}{2} \log(2\pi) - \frac{n}{2} \log(\sigma^2) - \frac{1}{2} \log(|V|) \\
&- \frac{1}{2 \sigma^2} \left( y^\mathrm{T} P y - 2 \beta^\mathrm{T} X^\mathrm{T} P y + \beta^\mathrm{T} X^\mathrm{T} P X \beta \right) \; .
\end{split}
$$

<br>
The derivative of the log-likelihood function \eqref{eq:MLR-LL2} with respect to $\beta$ is

$$ \label{eq:dLL-dbeta}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\beta,\sigma^2)}{\mathrm{d}\beta} &= \frac{\mathrm{d}}{\mathrm{d}\beta} \left( - \frac{1}{2 \sigma^2} \left( y^\mathrm{T} P y - 2 \beta^\mathrm{T} X^\mathrm{T} P y + \beta^\mathrm{T} X^\mathrm{T} P X \beta \right) \right) \\
&= \frac{1}{2 \sigma^2} \, \frac{\mathrm{d}}{\mathrm{d}\beta} \left( 2 \beta^\mathrm{T} X^\mathrm{T} P y - \beta^\mathrm{T} X^\mathrm{T} P X \beta \right) \\
&= \frac{1}{2 \sigma^2} \left( 2 X^\mathrm{T} P y - 2 X^\mathrm{T} P X \beta \right) \\
&= \frac{1}{\sigma^2} \left( X^\mathrm{T} P y - X^\mathrm{T} P X \beta \right)
\end{split}
$$

and setting this derivative to zero gives the MLE for $\beta$:

$$ \label{eq:beta-MLE}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\beta},\sigma^2)}{\mathrm{d}\beta} &= 0 \\
0 &= \frac{1}{\sigma^2} \left( X^\mathrm{T} P y - X^\mathrm{T} P X \hat{\beta} \right) \\
0 &= X^\mathrm{T} P y - X^\mathrm{T} P X \hat{\beta} \\
X^\mathrm{T} P X \hat{\beta} &= X^\mathrm{T} P y \\
\hat{\beta} &= \left( X^\mathrm{T} P X \right)^{-1} X^\mathrm{T} P y
\end{split}
$$

<br>
The derivative of the log-likelihood function \eqref{eq:MLR-LL1} at $\hat{\beta}$ with respect to $\sigma^2$ is

$$ \label{eq:dLL-ds2}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\beta},\sigma^2)}{\mathrm{d}\sigma^2} &= \frac{\mathrm{d}}{\mathrm{d}\sigma^2} \left( - \frac{n}{2} \log (\sigma^2) - \frac{1}{2 \sigma^2} (y - X\hat{\beta})^\mathrm{T} V^{-1} (y - X\hat{\beta}) \right) \\
&= - \frac{n}{2} \, \frac{1}{\sigma^2} + \frac{1}{2 (\sigma^2)^2} (y - X\hat{\beta})^\mathrm{T} V^{-1} (y - X\hat{\beta}) \\
&= - \frac{n}{2 \sigma^2} + \frac{1}{2 (\sigma^2)^2} (y - X\hat{\beta})^\mathrm{T} V^{-1} (y - X\hat{\beta})
\end{split}
$$

and setting this derivative to zero gives the MLE for $\sigma^2$:

$$ \label{eq:s2-MLE}
\begin{split}
\frac{\mathrm{d}\mathrm{LL}(\hat{\beta},\hat{\sigma}^2)}{\mathrm{d}\sigma^2} &= 0 \\
0 &= - \frac{n}{2 \hat{\sigma}^2} + \frac{1}{2 (\hat{\sigma}^2)^2} (y - X\hat{\beta})^\mathrm{T} V^{-1} (y - X\hat{\beta}) \\
\frac{n}{2 \hat{\sigma}^2} &= \frac{1}{2 (\hat{\sigma}^2)^2} (y - X\hat{\beta})^\mathrm{T} V^{-1} (y - X\hat{\beta}) \\
\frac{2 (\hat{\sigma}^2)^2}{n} \cdot \frac{n}{2 \hat{\sigma}^2} &= \frac{2 (\hat{\sigma}^2)^2}{n} \cdot \frac{1}{2 (\hat{\sigma}^2)^2} (y - X\hat{\beta})^\mathrm{T} V^{-1} (y - X\hat{\beta}) \\
\hat{\sigma}^2 &= \frac{1}{n} (y - X\hat{\beta})^\mathrm{T} V^{-1} (y - X\hat{\beta})
\end{split}
$$

<br>
Together, \eqref{eq:beta-MLE} and \eqref{eq:s2-MLE} constitute the MLE for multiple linear regression.