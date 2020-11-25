---
layout: definition
mathjax: true

author: "Joram Soch"
affiliation: "BCCN Berlin"
e_mail: "joram.soch@bccn-berlin.de"
date: 2020-11-19 04:55:00

title: "Cross-validated log model evidence"
chapter: "Model Selection"
section: "Bayesian model selection"
topic: "Log model evidence"
definition: "Cross-validated log model evidence"

sources:
  - authors: "Soch J, Allefeld C, Haynes JD"
    year: 2016
    title: "How to avoid mismodelling in GLM-based fMRI data analysis: cross-validated Bayesian model selection"
    in: "NeuroImage"
    pages: "vol. 141, pp. 469-489, eqs. 13-15"
    url: "https://www.sciencedirect.com/science/article/pii/S1053811916303615"
    doi: "10.1016/j.neuroimage.2016.07.047"
  - authors: "Soch J, Meyer AP, Allefeld C, Haynes JD"
    year: 2017
    title: "How to improve parameter estimates in GLM-based fMRI data analysis: cross-validated Bayesian model averaging"
    in: "NeuroImage"
    pages: "vol. 158, pp. 186-195, eq. 6"
    url: "https://www.sciencedirect.com/science/article/pii/S105381191730527X"
    doi: "10.1016/j.neuroimage.2017.06.056"
  - authors: "Soch J, Allefeld C"
    year: 2018
    title: "MACS – a new SPM toolbox for model assessment, comparison and selection"
    in: "Journal of Neuroscience Methods"
    pages: "vol. 306, pp. 19-31, eqs. 14-15"
    url: "https://www.sciencedirect.com/science/article/pii/S0165027018301468"
    doi: "10.1016/j.jneumeth.2018.05.017"
  - authors: "Soch J"
    year: 2018
    title: "cvBMS and cvBMA: filling in the gaps"
    in: "arXiv stat.ME"
    pages: "arXiv:1807.01585"
    url: "https://arxiv.org/abs/1807.01585"

def_id: "D111"
shortcut: "cvlme"
username: "JoramSoch"
---


**Definition:** Let there be a [data set](/D/data) $y$ with mutually exclusive and collectively exhaustive subsets $y_1, \ldots, y_S$. Assume a [generative model](/D/gm) $m$ with model parameters $\theta$ implying a [likelihood function](/D/lf) $p(y \vert \theta, m)$ and a [non-informative](/D/prior-inf) [prior density](/D/prior) $p_{\mathrm{ni}}(\theta \vert m)$.

Then, the cross-validated log model evidence of $m$ is given by

$$ \label{eq:cvLME}
\mathrm{cvLME}(m) = \sum_{i=1}^{S} \log \int p( y_i \vert \theta, m ) \, p( \theta \vert y_{\neg i}, m ) \, \mathrm{d}\theta
$$

where $y_{\neg i} = \bigcup_{j \neq i} y_j$ is the union of all data subsets except $y_i$ and $p( \theta \vert y_{\neg i}, m )$ is the [posterior distribution](/D/post) obtained from $y_{\neg i}$ when using the [prior distribution](/D/prior) $p_{\mathrm{ni}}(\theta \vert m)$:

$$ \label{eq:post}
p( \theta \vert y_{\neg i}, m ) = \frac{p( y_{\neg i} \vert \theta, m ) \, p_{\mathrm{ni}}(\theta \vert m)}{p( y_{\neg i} \vert m )} \; .
$$