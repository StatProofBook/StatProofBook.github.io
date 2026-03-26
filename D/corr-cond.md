---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "OvGU Magdeburg"
e_mail: "joram.soch@ovgu.de"
date: 2026-03-26 10:03:40

title: "Conditional correlation"
chapter: "General Theorems"
section: "Probability theory"
topic: "Correlation"
definition: "Conditional correlation"

sources:
  - authors: "Ostwald D, Soch J"
    year: 2025
    title: "Partielle Korrelation"
    in: "Allgemeines Lineares Modell"
    pages: "Einheit (12), Folie 8"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Sommersemester+2025/Allgemeines+Lineares+Modell/12_Partielle_Korrelation.pdf"

def_id: "D226"
shortcut: "corr-cond"
username: "JoramSoch"
---


**Definition:** Let $X$, $Y$ and $Z$ be [random variables](/D/rvar) with the [joint probability distribution](/D/dist-joint) $p(X,Y,Z)$ and consider the [conditional probability distribution](/D/dist-cond) $p(X,Y \vert Z)$ as well as the [(marginal and)](/D/dist-marg) [conditional probability distributions](/D/dist-cond) $p(X \vert Z)$ and $p(Y \vert Z)$. Then, the conditional correlation of $X$ and $Y$ given $Z$ is defined as

$$ \label{eq:corr-cond}
\mathrm{Corr}(X,Y|Z) = \frac{\mathrm{Cov}(X,Y|Z)}{\sqrt{\mathrm{Var}(X|Z)} \sqrt{\mathrm{Var}(Y|Z)}}
$$

where $\mathrm{Cov}(X,Y \vert Z)$ is the [conditional covariance](/D/cov-cond) of $X$ and $Y$, i.e. the [covariance](/D/cov) of $p(X,Y \vert Z)$, and $\mathrm{Var}(X \vert Z)$ as well as $\mathrm{Var}(Y \vert Z)$ are the [conditional variances](/D/var-cond) of $X$ and $Y$, i.e. the [variances](/D/var) of $p(X \vert Z)$ and $p(Y \vert Z)$.