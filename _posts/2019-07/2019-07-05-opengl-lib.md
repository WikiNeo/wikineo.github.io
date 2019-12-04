---
title:  "OpenGL Libraries"
published: true
categories: tech
tags: OpenGL
---

The first thing we need to do create stunning graphics is to create an OpenGL context and an application window to draw in. However, those operations are specific per operating system and OpenGL purposefully tries to abstract from these operations. This means we have to create a window, define a context and handle user input all by ourselves.

There are quite a few libraries out there that already provide the functionality we seek, some specially aimed at OpenGL. hose librariessave us all the operation-system specific work and give us a window and an OpenGL context to render in.

## GLFW

GLFW is a libray, written in C, specifically targeted at OpengGL providing the base necessities required for rendering goodies to the screen. It allows us to create an OpenGL context, define window parameters and handle user input wihch is all that we need.

GLFW is a free, Open Source, multi-platform library for OpenGL, OpenGL ES and Vulkan appliccation development. It provides a simple, platform-independent API for creating windows, contexts and surfaces, reading input, handling events, etc.

## GLDA

Since OpenGL is a standard/specification it is up to the driver manufacturer to impement the specification to a driver that the specifi graphic card supports. Sine there are many different versions of OpenGL dirvers, the location of most of its functions is not know at compile-time and needs to be queried at run-time. It is then the task of the developer to retrieve the location of the functions he/she needs and store them in function pointers for later use. Retrieving those locations is OS-specific and in Windows it looks something like this:

```cpp
// define the function's prototype
typedef void (*GL_GENBUFFERS) (GLsizei, GLuint*);
// find the function and assign it to a function pointer
GL_GENBUFFERS glGenBuffers  = (GL_GENBUFFERS)wglGetProcAddress("glGenBuffers");
// function can now be called as normal
unsigned int buffer;
glGenBuffers(1, &buffer);
```

As you can see the code looks complex and it's a cumbersome process to do this for each function you might need that is not yet declared. Thankfully, there are libraries for this purpose as well where GLAD is a popular and up-to-date library.
