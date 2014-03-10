Pyglet on Rails, Kinda
======================

[![Build Status](https://travis-ci.org/tredfern/pygsty.png?branch=master)](https://travis-ci.org/tredfern/pygsty)

*Temporarily all development is being done to support the terralien project.*

Pygsty is a pretty strange idea I had after drinking a bunch of wine and
waking up early in the morning with a dull throb in my head. The basic
concept is to organize the framework in an MVC kind of format in order
to allow game logic and interaction to rise to the surface of an actual
game project. Similar to what Rails has done in web applications.

I'm going to follow the principles of convention over configuration, DRY,
and also the testability of game logic by removing complexities that rendering
and user input provide.

MVC
---

The stateless web version of MVC obviously won't work in this context, at
the same time they still provide a good foundation of where things go:

*Models* are everything from your bad and good guys, bullets, etc... to
your levels, to your high score list. Long term goal is to provide some
persistable format. Basically, the blocks of your game.

*Controllers* do more than traditional rails controllers. These are where
the game is played. They control the interaction of models and will receive
information on user input. This is the interactions of your game.

*Views* can be screens, images, 3D models, animations, etc... Again we are
be flexible in the definition but we are still segmenting things that are
drawn to here. This is the visualization of your game. Might include sound
for the aural view.

PygstyRack
--------

The backend engine. Ok, maybe having too much fun with sharing terminology,
but here is where the engine is really running and utilizes your controllers
to provide input about what is happening on the current state of your game.

Development
-----------

Python frightens and confuses me at this point. Here are the steps I think
necessary to use and work with the code

For the main requirements

    pip install -r Packages

For the development requirements

    pip install -r Development

Unit testing is just unittest/nosetests/rednose
