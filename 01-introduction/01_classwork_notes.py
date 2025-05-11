# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Week 1 Class notes
#
# ## 1.1 Introduction
# * MLOps is Machine Learning Operations which is a set of best practices for putting machine learning in production
# * As an example problem for this course, we will look at predicting the duration of a taxi ride in New York City. 
#   * Imagine you get an Uber/Lyft and the app gives an estimate of the ride duration. It's this given ride duration that we would like to predict using some data.
#
# ## Stages of a ML project (a simplified set of steps)
# 1. Design: Determine if ML the right solution to solve the problem and formulate a solvable problem.
# 2. Train: Build the model, do experiements
# 3. Operate: Deploy the model perhaps to an API, monitor the model so that it's performance doesn't degrade and, instead, it performs reliably over time.
#    
#

# %%
