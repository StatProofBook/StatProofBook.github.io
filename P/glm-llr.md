---
layout: proof
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-06-07 12:14:31

title: "Log-likelihood ratio for the general linear model"
chapter: "Statistical Models"
section: "Multivariate normal data"
topic: "General linear model"
theorem: "Log-likelihood ratio"

sources:

proof_id: "P455"
shortcut: "glm-llr"
username: "JoramSoch"
---


**Theorem:** Let $Y = \left[ y_1, \ldots, y_v \right]$ be an $n \times v$ [data matrix](/D/data) and consider two [general linear models](/D/glm) with [design matrices](/D/glm) $X_1, X_2$ and [row-by-row covariance matrices](/D/glm) $V_1, V_2$, entailing potentially different [regression coefficients](/D/glm) $B_1, B_2$ and [column-by-column covariance matrices](/D/glm) $\Sigma_1, \Sigma_2$:

$$ \label{eq:m1-m2}
\begin{split}
m_1: \; Y &= X_1 B_1 + E_1, \; E_1 \sim \mathcal{N}(0, V_1, \Sigma_1) \\
m_2: \; Y &= X_2 B_2 + E_2, \; E_2 \sim \mathcal{N}(0, V_2, \Sigma_2) \; .
\end{split}
$$

Then, if the models assume the same covariance matrix across observations, i.e. if $V_1 = V_2$, the [log-likelihood ratio](/D/llr) for comparing $m_1$ vs. $m_2$ is given by

$$ \label{eq:glm-llr}
\ln \Lambda_{12} = \frac{n}{2} \ln \frac{|\hat{\Sigma}_2|}{|\hat{\Sigma}_1|}
$$

where $\hat{\Sigma}_1$ and $\hat{\Sigma}_2$ are the [maximum likelihood estimates](/D/mle) of $\Sigma_1$ and $\Sigma_2$.


**Proof:** The [likelihood ratio](/D/lr) between two models $m_1$ and $m_2$ with model parameters $\theta_1$ and $\theta_2$ and parameter spaces $\Theta_1$ and $\Theta_2$ is defined as the quotient of their [maximized](/D/mle) [likelihood functions](/D/lf):

$$ \label{eq:lr}
\Lambda_{12} = \frac{\operatorname*{max}_{\theta_1 \in \Theta_1} p(y|\theta_1,m_1)}{\operatorname*{max}_{\theta_2 \in \Theta_2} p(y|\theta_2,m_2)} \; .
$$

Thus, the [log-likelihood ratio](/D/llr) is equal to the difference of the [maximum log-likelihoods](/D/mll) of the two models:

$$ \label{eq:llr}
\ln \Lambda_{12} = \ln p(y|\hat{\theta}_1,m_1) - \ln p(y|\hat{\theta}_2,m_2) \; .
$$

The [likelihood function](/D/lf) of the [general linear model](/D/glm) is a [matrix-normal probability density function](/P/matn-pdf):

$$ \label{eq:glm-lf}
\begin{split}
p(Y|B,\Sigma)
&= \mathcal{MN}(Y; XB, V, \Sigma) \\
&= \sqrt{\frac{1}{(2\pi)^{nv} |\Sigma|^n |V|^v}} \cdot \exp\left[ -\frac{1}{2} \, \mathrm{tr}\left( \Sigma^{-1} (Y - XB)^\mathrm{T} V^{-1} (Y - XB) \right) \right] \; .
\end{split}
$$

Thus, the [log-likelihood function](/D/llf) is equal to a logarithmized [matrix-normal](/D/matn) [density](/D/pdf):

$$ \label{eq:glm-llf}
\begin{split}
\ln p(Y|B,\Sigma)
&= \ln \mathcal{MN}(Y; XB, V, \Sigma) \\
&= - \frac{nv}{2} \ln(2\pi) - \frac{n}{2} \ln |\Sigma| - \frac{v}{2} \ln |V| - \frac{1}{2} \, \mathrm{tr}\left[ \Sigma^{-1} (Y - XB)^\mathrm{T} V^{-1} (Y - XB) \right] \; .
\end{split}
$$

The [maximum likelihood estimates for the general linear model](/P/glm-mle) are given by

$$ \label{eq:glm-mle}
\begin{split}
\hat{B}      &= (X^\mathrm{T} V^{-1} X)^{-1} X^\mathrm{T} V^{-1} Y \\
\hat{\Sigma} &= \frac{1}{n} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \; .
\end{split}
$$

such that the last term in the maximum log-likelihood function \eqref{eq:glm-llf} becomes

$$ \label{eq:glm-mll-tr}
\begin{split}
&\quad\; \frac{1}{2} \, \mathrm{tr}\left[ \hat{\Sigma}^{-1} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \right] \\
&= \frac{1}{2} \, \mathrm{tr}\left[ \left( \frac{1}{n} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \right)^{-1} (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \right] \\
&= \frac{1}{2} \, \mathrm{tr}\left[ n \left( (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \right)^{-1} \left( (Y - X\hat{B})^\mathrm{T} V^{-1} (Y - X\hat{B}) \right) \right] \\
&= \frac{n}{2} \, \mathrm{tr}\left[ I_v \right] \\
&= \frac{nv}{2} \; .
\end{split}
$$

Thus, the [maximum log-likelihood for the general linear model](/P/glm-mll) is equal to

$$ \label{eq:glm-mll}
\ln p(Y|\hat{B},\hat{\Sigma}) = - \frac{nv}{2} \ln(2\pi) - \frac{n}{2} \ln |\hat{\Sigma}| - \frac{v}{2} \ln |V| - \frac{nv}{2} \; .
$$

Evaluating \eqref{eq:glm-mll} for $m_1$ and $m_2$ and plugging into \eqref{eq:llr}, we obtain:

$$ \label{eq:glm-llr-m1-m2}
\begin{split}
\ln \Lambda_{12}
&= \ln p(Y|\hat{B}_1,\hat{\Sigma}_1,m_1) - \ln p(Y|\hat{B}_2,\hat{\Sigma}_2,m_2) \\
&= \left( - \frac{nv}{2} \ln(2\pi) - \frac{n}{2} \ln |\hat{\Sigma}_1| - \frac{v}{2} \ln |V_1| - \frac{nv}{2} \right) \\
&- \left( - \frac{nv}{2} \ln(2\pi) - \frac{n}{2} \ln |\hat{\Sigma}_2| - \frac{v}{2} \ln |V_2| - \frac{nv}{2} \right) \\
&= - \frac{n}{2} \ln \frac{|\hat{\Sigma}_1|}{|\hat{\Sigma}_2|} - \frac{v}{2} \ln \frac{|V_1|}{|V_2|} \\
&= + \frac{n}{2} \ln \frac{|\hat{\Sigma}_2|}{|\hat{\Sigma}_1|} + \frac{v}{2} \ln \frac{|V_2|}{|V_1|} \; .
\end{split}
$$

Thus, if $V_1 = V_2$, such that $\ln(\vert V_2 \vert / \vert V_1 \vert) = \ln(1) = 0$, the log-likelihood ratio is equal to

$$ \label{eq:glm-llr-qed}
\ln \Lambda_{12} = \frac{n}{2} \ln \frac{|\hat{\Sigma}_2|}{|\hat{\Sigma}_1|} \; .
$$