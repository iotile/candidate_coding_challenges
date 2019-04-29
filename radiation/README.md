# Please do not publish a solution in either a fork or clone. Keep all of your work local! 
#### If you do want to store your work, we ask that you keep it in your own private repos (git lets everyone do this now!).

## Introduction
This project is designed to get you familiar with how to build and interact with IOTile hardware devices by creating a virtual hardware device and then controlling it. At Arch, we build industrial IOT solutions radically faster using a combination of modularity and automation. You'll use some of the open source tools that we've built to build your first IOTile device.

### What we're looking for

Think of this as an opportunity for you to show us how you approach solving a problem. Being more verbose than normal in describing what you're solving so that we can follow your process might help, but is not required. 


## Background Story
Arch is bringing to market a new radiation sensor (a POD-1R) that can monitor the radiation levels in the lab, allowing us to track changes over time and provide both metrics and alerts to those in the factory, protecting people's safety and preventing expensive repairs with early warning systems.
We're just starting the project which is going to include:

- Hardware engineers building the radiation sensor tile
- Firmware engineers programming the radiation tile and surrounding system
- Mobile engineers creating a mobile app that can receive data from the POD-1R and configure it in real time
- Cloud engineers creating a machine learning pipeline to learn how the overall factory radiation changes over time so we can accurately identify hotspots and provide robust analysis of the factory.
- A large amount of testing of each component so that we can be sure our solution will work.

Since the project is just getting started there's no hardware yet and no firmware, so nobody can do any work. Your job as the lone intrepid python engineer on the team is to:

- create a virtual radiation sensor in python using IOTile CoreTools that everyone else on the team can use to build their part until the actual device is ready in a few months
- Implement behaviors that would emulate the radiation sensor at a high, functional level.
- use your virtual device to create acceptance tests to make the sure the actual hardware device works when it's ready, by implementing convenience functions so that we can simulate real-world conditions.

If you're successful, everyone will look to you as a hero because you'll be the one who makes sure that everybody's part works together and you'll unblock the mobile and cloud engineers from having to wait until the hardware is ready before being able to work with it.

## Your Goal
- Use CoreTools to write a python module that acts as a virtual IOTile device (see the required behavior section below for what it needs to do)
- Test out your virtual device using the iotile command line tool to make sure that it works as you develop
- Write a series of unit tests using pytest and some of the built-in CoreTools functionality to make sure your virtual device is behaving properly.

## Getting Started
You'll need a computer running linux, MacOS or Windows with a Python 3.5+ installation. You can try to use Python2.7, but we have deprecated support for that and can't guarantee that everything still works. We made efforts to leave compatibility there, however.
Follow the instructions here to get the basic CoreTools installed on your computer:
- http://coretools.readthedocs.io/en/latest/introduction.html 
- **Important** : The docs may still say python2.7 is recommended, but that is outdated. It will be easier if you use Python3.
- You should also install pytest (pip install pytest)

Read up on how to build virtual devices, it will help you develop your own:
- https://coretools.readthedocs.io/en/latest/tutorials.html#creating-your-first-iotile-device
You can look at tutorials past this first section, but they might not be used for what we are asking in this exercise. However, you can generally use the concepts to further extend the behavior of your virtual device!

# Coding Expectations & Honor Statement
We can't watch everything you do, so we are trusting you to follow these coding guidelines so that everyone gets a fair assessment:
- All code submitted must be your own. You are expected to work on this without the assistance of other people.
- You can reference Python syntax materials (i.e. https://docs.python.org/3/library/), and Arch reference documentation, but don't look up solutions to algorithmic challenges you face.
- You shouldn't need any third party libraries that aren't included in the `requirements.txt`. 

Remember, this is your opportunity to demonstrate how you approach and implement solutions to features that you might encounter during your work at Arch. Use that in judging the appropriate methods of implementation. You are welcome (and encouraged) to verbosely comment your work so we can understand what you did better. 

# Required Device Behavior
**PROTIP** : Completing the Getting Started section should make this section much easier to understand.

The goal of your device is 
- to provide RPC definitions that let you input simulated data, 
- to more effectively provoke test scenarios, and 
- implement the RPCs that would actually be used on the physical devices (the "emulation" part)

To get started, we've provided this repository with a skeleton to help you get started on development.

You should clone this repository to get going, or you can manually create the same structure. **It is important to keep the structure identical to what is here!**

If you are using the same virtual-env from the "Getting Started" tutorial, you don't need to install the `requirements.txt`. You should make sure that you have pytest installed, though, with `pip install pytest`. Otherwise, you can install the entire requirements, `pip install -r requirements.txt`. This should also work with your virtualenv if you want to be safe.

The files should do a sufficient job explaining what you need to implement. All unfinished parts are marked with a TODO.
- `radiation_device.py` defines RPCs that you need to implement
- `radiation_proxy.py` provides function definitions that you need to complete

### Boundary Conditions
- All radiation readings are expected to be 0 < reading <= 0xFFFF. You do not need to handle values outside of this range.


### Example commands that you should be able to run successfully to validate your solution
```
(radiation_venv) Matts-Macbook-Pro:radiation mrunchey$ pytest test_basic.py 
================================================================ test session starts ================================================================
platform darwin -- Python 2.7.15, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
rootdir: /Users/mrunchey/gitrepos/candidate_challenge_solutions/radiation, inifile:
plugins: timeout-1.3.3
collected 5 items                                                                                                                                   

test_basic.py .....                                                                                                                           [100%]

============================================================= 5 passed in 0.49 seconds ==============================================================
```

### Helpful Hints
- The basic tests provided are not meant to validate all of the required behavior. You should consider adding more tests to validate your solutions meet the specification defined in `radiation_device.py` RPC signatures.
- You can write helper functions in `radiation_device.py`, not everything has to be an RPC signature.
- Before you submit your challenge, **make sure** you can successfully pass `test_basic.py`.




## BONUS CHALLENGE: 
Have the device output the current average radiation reading via the realtime streaming interface. To do this, learn how to have your virtual device output real time data:
- https://coretools.readthedocs.io/en/latest/tutorials.html#simulating-realtime-data
- https://github.com/iotile/coretools/blob/master/iotiletest/iotile/mock/devices/realtime_test_device.py

If you implement this behavior, you should be able to demonstrate the functionality in the same way demonstrated on the link above, in a python file (you will need to extend the example to actually add radiation readings, play around with it) included with your submission. Here's a hint of what you might use to show that:
```
(radiation_env) Matts-Macbook-Pro:radiation mrunchey$ python radiation_realtime_test.py 
Received Stream 4096: 0 at 2019-01-24 22:39:51.085910
Received Stream 4096: 59 at 2019-01-24 22:39:52.235488
Received Stream 4096: 226 at 2019-01-24 22:39:53.392914
Received Stream 4096: 173 at 2019-01-24 22:39:54.533378
Received Stream 4096: 211 at 2019-01-24 22:39:55.697972
Received Stream 4096: 292 at 2019-01-24 22:39:56.835747
Received Stream 4096: 370 at 2019-01-24 22:39:57.990320
```

You may see hex values instead of integers for the Stream ID (i.e. 4096 showing up as 0x1000, and the value after the colon as well) depending on which version of Python you are using.

## NOTES
- Please do not create a public fork or public solution to this repo. If you do want to store your work, we ask that you keep it in your own private repos (git lets everyone do this now!).
- If you are submitting your solution, it's easiest if you can zip/tar the "radiation" directory and send us just the one file.


## Reference Information
The best reference for writing python scripts that can test your device is in the CoreTools documentation:
- http://coretools.readthedocs.io/en/latest/introduction.html#writing-scripts

If you're going to write unit tests using py.test, the best reference for a fixture that can give you an instance of your virtual device for each test is in iotile-test:
- https://github.com/iotile/coretools/blob/master/iotiletest/iotile/fixture/device_fixture.py


