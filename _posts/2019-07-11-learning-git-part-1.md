---
layout: post
title: Learning Git, Part 1
summary: A Practical Introduction to Git and Github.
date: 2019-07-11
---
# Introduction
This is a practical guide to using Git and Github. I struggled a lot when I first started learning how to use Git, so this is the guide I wish I had when I first started. This guide reflects my current (but constantly evolving) workflow. I hope this step-by-step story helps you manage your code better and gives you a good sense of how to navigate version control.

This tutorial requires you to have signed up on Github and downloaded Git (there are plenty of other tutorials explaining how to do this). This tutorial also assumes you have basic knowledge of moving around using the command line. Good luck!

# The Beginning: Your First Project
The first step is to create a repository on Github to contain all of your files. Think of this as a Google Drive folder - this is a space where you can upload all of your files in order to keep them up to date.

![Creating the repository](/blog/images/github-tutorial/create-repo.png)
*Make sure you select "Initialize this repository with a README".*

You will get to a landing page with your empty repository. The next step is to create a local copy of this repository on your local machine. Go to your command line and type:

`git clone https://github.com/<YOUR USERNAME>/learning-github.git`

If your repository is named differently, you can find the url on the repo homepage:

![Repository](/blog/images/github-tutorial/repo.png)
*You can click the clipboard icon in order to easily copy+paste the repo url.*

This will create a copy of the contents of the repository onto your computer. You should see a folder on your computer with a README.md file.

Now, an important distinction: there are now TWO copies of your files. One is the **local version**, which we will work on and make changes to. The other is an **origin version**, which exists on the Github servers. Once we make changes to the local copy, we will push it up to the Github servers to store in the **origin**.

![How Github Works](/blog/images/github-tutorial/github.png)
*Quick diagram of origin vs local copy.*

# Making Changes
Let's make some changes to our repository. Go make some changes to *README.md* and add some extra files to the folder. Now, let's pretend we are now ready to save our work. First, let's see an overview of our changes. In the command line, type:

`git status`

We should now see an overview like this. We can see the files we have modified/edited.

![Git Status](/blog/images/github-tutorial/git-status.png)

Now, we want to specify these are the files that we want to save our progress on. This is called making a **commit**, which basically means saving the differences between the previous version and the current version. Let's add all of the current files to a **staging area**.

`git add .`

*(You can also add files individually: `git add README.md`; `git add otherfiles.txt`)*

![Git Add](/blog/images/github-tutorial/git-add.png)

This **staging area** contains all of the changes we want included in this commit. This is a helpful feature because we don't necessarily want all of our changes to be included in the new version. Once we have finalized the staging area (which you can verify with another `git status`), we can make a commit with a commit message:

`git commit -m "Add new features to the bork bork"`

At this point, it's a good idea to check that `git status` does not contain those changes anymore, and that typing `git log` shows the commit you just made.

![Git Log](/blog/images/github-tutorial/git-log.png)

At this point, we've successfully made a commit, and are now ready to push our changes to the Github servers to save. We can use the following command to send our changes up to the Github servers.

`git push`

*(Note: this command is an abbreviation for `git push origin master`. It is often better practice to type the entire command out so you push changes to the right place!)*

After running this command, going back to the Github page for this repository should show your new commit!

![First Commit](/blog/images/github-tutorial/first-commit.png)

# Summary
If are working on a solo project and just want some basic version control, these steps should be all you need to get started. Every time you want to save a snapshot of your work, simply add to the staging area with with `git add .`, commit with `git commit -m "example commit"`, and then push to Github with `git push`!

In the next part, we'll explore features of Git that make collaboration easy, such as **branching**, as well as ways to undo your mistakes through **reverting**.
