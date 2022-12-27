# Geoguessr AI Player

> Work in progress

## Introduction

[GeoGuessr](https://www.geoguessr.com/) is a geographical game where players are presented random street view imaginary and the goal is to guess its location. To achieve this players need to use their geographical knowledge to infere location-specific hints: language, soil type etc. and then pinpoint their guess on the map.

## Goal

The goal of this project is to create ML model for image classification to their location using convolutional neural network ([CNN](https://en.wikipedia.org/wiki/Convolutional_neural_network)) in [Tensoflow](https://www.tensorflow.org/) framework.

## Technologies and libraries

- Python 3.10+
- Tensorflow 2.10
- Matplotlib 3.6
- JS (web extension)

## Todo list

- [x] Create script that gathers raw images, and their locations from [GeoGuessr](https://www.geoguessr.com/)
- [x] Collect initial training set
- [X] Create basic sequencial model that would classified images to countries
- [ ] Create model that would classify images with better accuracy by dividing world map into smaller regions
- [ ] Use reinforcement learning to constantly improve the model based on geoguessr points rewarded
