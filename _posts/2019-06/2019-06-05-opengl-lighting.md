---
title:  "OpenGL Lighting"
published: true
categories: tech
---

# Colors

Colors are digitally represented using a red, green and blue component commonly abbreviated as RGB.

```cpp
glm::vec3 coral(1.0f, 0.5f, 0.31f);
```

The colors we see in real life are not the colors the objects actually have, but are the colors reflected from the object; the colors that are not absorbed (rejected) by the objects are the colors we perceive of them.

When we define a light source in OpenGL we want to give this light source a color. 
If we would then multiply the light source's color with an object's color value, the resulting color is the reflected color of the object (and thus its perceived color)

```cpp
glm::vec3 lightColor(1.0f, 1.0f, 1.0f);
glm::vec3 toyColor(1.0f, 0.5f, 0.31f);
glm::vec3 result = lightColor * toyColor; // = (1.0f, 0.5f, 0.31f);
```

## A lighting scene

Fragment Shader deals with the color.

```glsl
#version 330 core
out vec4 FragColor;
  
uniform vec3 objectColor;
uniform vec3 lightColor;

void main()
{
    FragColor = vec4(lightColor * objectColor, 1.0);
}
```

[code](https://github.com/mintwzy/my-opengl/blob/master/src/learn/lighting/colors/colors.cpp)

# Basic Lighting

The major building blocks of the Phong model consist of 3 components: 

- Ambient lighting: even when it is dark there is usually still some light somewhere in the world (the moon, a distant light) so objects are almost never completely dark. To simulate this we use an ambient lighting constant that always gives the object some color.
- Diffuse lighting: simulates the directional impact a light object has on an object. This is the most visually significant component of the lighting model. The more a part of an object faces the light source, the brighter it becomes.
- Specular lighting: simulates the bright spot of a light that appears on shiny objects. Specular highlights are often more inclined to the color of the light than the color of the object.

## Ambient lighting

Adding ambient lighting to the scene is really easy. We take the light's color, multiply it with a small constant ambient factor, multiply this with the object's color and use it as the fragment's color: 

```glsl
void main()
{
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColor;

    vec3 result = ambient * objectColor;
    FragColor = vec4(result, 1.0);
}  
```

## Diffuse lighting

Diffuse lighting gives the object more brightness the closer its fragments are aligned to the light rays from a light source. 



# References

[LEARN OpenGL](https://learnopengl.com/Lighting/Colors)
