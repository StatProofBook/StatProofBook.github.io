---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2024-11-01 14:26:04

title: "Estimand, estimator and estimate"
chapter: "General Theorems"
section: "Estimation theory"
topic: "Basic concepts of estimation"
definition: "Estimator"

sources:
  - authors: "Ostwald, Dirk"
    year: 2023
    title: "Punktschätzung"
    in: "Wahrscheinlichkeitstheorie und Frequentistische Inferenz"
    pages: "Einheit (9), Folie 7"
    url: "https://www.ipsy.ovgu.de/ipsy_media/Methodenlehre+I/Wintersemester+2324/Wahrscheinlichkeitstheorie+und+Frequentistische+Inferenz/9_Punktsch%C3%A4tzung.pdf"
  - authors: "Wikipedia"
    year: 2024
    title: "Estimator"
    in: "Wikipedia, the free encyclopedia"
    pages: "retrieved on 2024-11-01"
    url: "https://en.wikipedia.org/wiki/Estimator#Definition"

def_id: "D208"
shortcut: "est"
username: "JoramSoch"
---


**Definition:** Let $y \in \mathcal{Y}$ be [measured data](/D/data), governed by a [probability distribution](/D/dist) described by some [statistical parameter](/D/para) $\theta \in \Theta$. Then, a function $\hat{\theta}: \mathcal{Y} \rightarrow \Theta$ exemplifying a rule for calculating an estimate of $\theta$ from $y$ is called an "estimator". Estimation theory distinguishes:

* the quantify of interest $\theta$ is called the "estimand";

* the rule $\hat{\theta}$ for estimating it is called "estimator";

* the result of estimation $\hat{\theta}(y)$ is called "estimate".