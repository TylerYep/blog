---
layout: post
title: Learning Git, Part 2
summary: Branching, Reverting, and Merging vs. Rebasing.
date: 2019-07-28
---
# Introduction
This is part 2 of my practical guide to using Git and Github. This part covers some more advanced topics related to collaborating with others. If you are completely new to Git and Github, I would recommend reading the previous part: [Learning Git, Part 1]({{ post.url | relative_url }}/blog/learning-git-part-1)

## Recap
Last part, we described a simple workflow you can do on your cloned project:

`git add <new_file>` → `git commit -m "..."` → `git push`

These commands add your changes to a staging area, commits them, and then pushes your changes up to origin, which is stored in the cloud.

This works well when you're working on your own project, but what about if you are collaborating on a project with others? If you are working in any tech company, there are going to be tens to hundreds of people editing the same project at any given time. How do we manage these changes?

# Branching
**Branches** are separate versions of your code. Think of a branch as an experimental feature, or some changes you are working on that shouldn't interact with other changes. This is especially useful if you are working on a team and don't want other people to interfere with your work. With a branch, you can work in isolation until you are ready to rejoin the master branch.

The **master branch** is usually the final, master copy of the code. All branches eventually merge into the master branch once their work is finished.

![Git Branch](/blog/images/github-tutorial/branch.svg)

Let's create a branch! In the command line, type in the following command:

`git checkout -b test-feature`

This command is an abbreviation for a couple commands: `git branch test-feature` → `git checkout test-feature`. I think it's more intuitive to do them in a single step, though.

Okay, let's check what branch we're on:

`git branch`

![Check what branch you are on with `git branch`](/blog/images/github-tutorial/git-branch.png)

You can see that we have switched over to our new branch! This is a yet another version of our code that can be modified independently of the master branch version. If we are done experimenting with this feature, we can return back to the master branch with: `git checkout master`

# Merging & Rebasing
Alright, let's pretend that we did a bunch of work on our test-branch, and want to combine it with master! There are a few ways to do this. The easiest is to simply merge our test branch with master.

In the command line, we can type: `git merge test-branch master`. In general, this command will be:

`git merge <branch-we-want-to-merge> <final-output-branch>`

However, there are a few downsides to merging all the time. For example, your commit history (using `git log`) may start to look like this:

![Ouch.](/blog/images/github-tutorial/git-branch.png)

We would much rather our commit history look something like this:

![Better!!](/blog/images/github-tutorial/git-branch.png)

