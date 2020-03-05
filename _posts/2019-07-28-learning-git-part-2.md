---
layout: post
title: Learning Git, Part 2
summary: Pulling, Merging, Stashing
date: 2019-07-28
---
# Introduction
This is Part 2 of my practical guide to using Git and Github. This part covers some topics related to collaborating with others. If you are completely new to Git and Github, I would recommend reading the previous part: [Learning Git, Part 1]({{ post.url | relative_url }}/blog/learning-git-part-1)

# Recap
Last part, we described a simple workflow you can do on your cloned project:

→ `git add <new_file>`

→ `git commit -m "..."`

→ `git push`

These commands add your changes to a staging area, commits them, and then pushes your changes up to origin, which is stored in the cloud.

This works well when you're working on your own project, but what about if you are collaborating on a project with others? How do we merge their changes in?

# Pulling in Changes
Assuming you haven't made any changes to the repository, all you need to do is run:
```git
$ git pull
```

What if we have already made changes? This can give us a *merge conflict*. Sometimes Git will try to resolve these merge conflicts for you, but other times the pull will simply fail. In this case, you can simply execute the following commands:

```git
$ git stash
$ git pull
$ git stash pop
```

Stashing is a process that temporarily hides all of your visible changes. This is really useful for when you want to temporarily hide all of your local changes, but still want to bring them back easily.



# Merging
Alright, let's pretend that we did a bunch of work on our test-branch, and want to combine it with master! There are a few ways to do this. The easiest is to simply merge our test branch with master.

In the command line, we can type: `git merge test-branch master`. In general, this command will be:

`git merge <branch-we-want-to-merge> <final-output-branch>`

However, there are a few downsides to merging all the time. For example, your commit history (using `git log`) may start to look like this:

![Ouch.](/blog/images/github-tutorial/git-branch.png)

We would much rather our commit history look something like this:

![Better!!](/blog/images/github-tutorial/git-branch.png)
