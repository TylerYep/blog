---
layout: post
title: Self-Driving with High Level Commands
summary: Branched Architecture Self-Driving Imitation Learning
date: 2019-08-04
---
# Introduction
I took CS 231N: Convolutional Neural Networks for Visual Recognition during the Spring quarter of my 3rd year at Stanford, and had the opportunity to work on a super cool project with Woody Wang, my project partner.

Our project was on Branched Architecture Self-driving Imitation Learning (affectionately called BASIL). The basic problem we wanted to solve was how to train a network to drive a car in a simulator using high-level human input.

![Intersection Course](/blog/images/self-driving/intersection.png)
<center><i>Intersection Course</i></center><br>

# High Level Commands
In a self-driving scenario, we want to be able to supply **high-level commands** to a car, and then have the car flawlessly execute those commands without human guidance. For example, if I am in a self-driving car, I might want the car to take the **next available left turn**. This is a high-level command because the car may not need to turn left immediately. It may continue straight for a few miles before the first available left turn appears. Or, it may need to sharply turn left in order to complete the turn.

Thus, the challenge is how to allow a network to take in this high-level command as input and perform the correct actions over the correct time interval.

**This problem is difficult because, given an image of an intersection, there are several possible "correct" answers for actions to take.** For example, the car could turn the steering wheel right, left, or not change the steering wheel angle at all. However, if a car only accepts a single image as input, how does it know which of the three actions it should do?

This means that it is not enough for a car to be able to predict the action for the next time step - it must also be able to keep track of where it wants to go and execute these actions over a given timeframe.

# Udacity Car Simulator
To simulate our solution to the problem, we adapted the Udacity Self-Driving Car Simulator, built for Udacity's Self-Driving Nano-degree course. The vanilla simulator provides a simple interface to drive the car and save a recording. The recordings are saved as a series of RGB images along with labels of the current throttle and steer angle.

![Modified Udacity Simulator](/blog/images/self-driving/simulator.png)
<center><i>Modified Udacity Simulator</i></center><br>

The simulator was originally designed to solve the lane-following problem - to see if students could create a model to follow a simple road and train the car to stay within its lane. We built on top of the basic lane-following model in order to accomplish our new task. Below, we see the original Lake Track provided by the simulator, and compare it to the custom Intersection Track we built from scratch to provide a testing environment for our model.

![Lake Track](/blog/images/self-driving/lake.png) ![Intersection Track](/blog/images/self-driving/intersection.png)
<center><i>Modified Udacity Simulator</i></center><br>

# Intersection Track
The custom track we designed comprises of a grid-world of identical intersections, with the only difference in each one the trees and hills in the background. We trained our model in this world by simply driving around the world and noting the keypress whenever we were about to take a certain action.

# Nvidia's Conditioned Model

# ResNet with Branching

# Analysis