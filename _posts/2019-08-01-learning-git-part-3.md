---
layout: post
title: Learning Git, Part 3
summary: Creating Branches & Reverting Changes
tags: GitHub
date: 2019-07-28
---
# Introduction
This is Part 3 of my practical guide to using Git and GitHub. This part covers some more advanced topics related to collaborating with others. If you are completely new to Git and GitHub, I would recommend reading the previous part: [Learning Git, Part 1]({{ post.url | relative_url }}/blog/learning-git-part-1)

# Recap
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

# Merging Aside
Merging is useful when you do a bunch of work on our test-branch, and want to combine it with master. There are a few ways to do this. The easiest is to simply use `git merge` to merge our test branch with master.

In the command line, we can type: `git merge test-branch master`. In general, this command will be:

`git merge <branch-we-want-to-merge> <final-output-branch>`

However, there are a few downsides to merging all the time. For example, your commit history (using `git log`) may start to look like this:

```git
commit 45d08300871f4ad239601072b850009daf61da42 (HEAD -> master)
Merge: dfddd52 0925c96
Author: Tyler Yep <tyep@cs.stanford.edu>
Date:   Sat Sep 12 12:27:08 2020 -0700

    Merge branch 'master' of https://github.com/TylerYep/learning-github

commit 0925c96c100a03a0bb8f0ade52ae933577688854 (origin/master, origin/HEAD)
Author: Tyler Yep <tyep@cs.stanford.edu>
Date:   Sat Sep 12 12:25:53 2020 -0700

    Update otherfiles.txt with correct header

commit 54911a03b0d16d56c67ff707d834f1fbb461da56
Merge: dfdee61 023dc71
Author: Tyler Yep <tyep@cs.stanford.edu>
Date:   Thu Aug 22 21:16:18 2019 -0400

    Merge branch 'master' of https://github.com/TylerYep/learning-github

commit dfddd5250b1a6c63a4891e1e4524ad6ad7134e67
Author: Tyler Yep <tyep@cs.stanford.edu>
Date:   Sat Sep 12 12:24:01 2020 -0700

    oops

commit 2778b752158446b7cc18bb51a89a43d6091379db
Author: Tyler Yep <tyep@cs.stanford.edu>
Date:   Sat Sep 12 12:23:50 2020 -0700

    Fix off-by-one bug in phantom generator

commit e7d41bd330585a9f2640e0f153be828ff2fb000a
Author: Tyler Yep <tyep@stanford.edu>
Date:   Sun Jul 21 01:49:54 2019 -0700

    Make changes to README and add otherfiles

```

The above log has many unnecessary merges that cause our output to look messy. Also, merges can make it difficult to revert back to those commits later.

We would much rather our commit history look something like this:

```git

commit 0925c96c100a03a0bb8f0ade52ae933577688854 (origin/master, origin/HEAD)
Author: Tyler Yep <tyep@cs.stanford.edu>
Date:   Sat Sep 12 12:25:53 2020 -0700

    Update otherfiles.txt with correct header

commit 2778b752158446b7cc18bb51a89a43d6091379db
Author: Tyler Yep <tyep@cs.stanford.edu>
Date:   Sat Sep 12 12:23:50 2020 -0700

    Fix off-by-one bug in phantom generator

commit e7d41bd330585a9f2640e0f153be828ff2fb000a
Author: Tyler Yep <tyep@stanford.edu>
Date:   Sun Jul 21 01:49:54 2019 -0700

    Make changes to README and add otherfiles

```
