---
title: "Lesson 1: Bresenham's Line Drawing Algorithm"
published: true
---

## First attempt

The simplest code that draws a line segment between `(x0, y0)` and `(x1, y1)`
points.

```cpp
void line(int x0, int y0, int x1, int y1, TGAImage &image, TGAColor color){
    for(float t = .0; t < 1.; t += .01){
        int x = x0 + (x1 - x0)*t;
        int y = y0 + (y1 - y0)*t;
        image.set(x, y, color)
    }
}
```

The idea here is to use the difference in x and y coordinate for two points as
the step value, and change it step by step.

## Second attempt

The problem with previous code (besides its inefficiency) is the choice of the
constant, which I took equal to .01.

We can easily find the necessary step: it's the number of pixels to be drawn.

```cpp
void line(int x0, int y0, int x1, int y1, TGAImage &image, TGAColor color){
    for( int x = x0; x < x1; x++){
        float t = (x - x0) / (float)(x1 - x0);
        int y = y0 + t*(y1 - y0);
        image.set(x, y, color);
    }
}
```

## Third attempt

We fix the missing red line by swapping the points so x0 is always lower than
x1.

There are holes in one of the line segments due to the fact that its height is
greater than the width.

```cpp
void line(int x0, int y0, int x1, int y1, TGAImage &image, TGAColor color){
    bool steep = false;

    // if line is steep, we transpose the image
    if (std::abs(x0 - x1) < std::abs(y0 - y1)){ 
        std::swap(x0, y0);
        std::swap(x1, y1);
        steep = true;
    }

    if (x0 > x1){   // make it left-to-right
        std::swap(x0, x1);
        std::swap(y0, y1);
    }

    for (int x = x0; x < x1; x++){
        float t = (x - x0)/(float)(x1 - x0);
        int y = y0 + t*(y1 - y0);
        if(steep){  
            image.set(y, x, color); // if transposed, de-transpose
        } else {
            image.set(x, y, color);
        }
    }
}
```

## Fourth attempt continued

We should note that each division has the same divisor. Let's take it out of the
loop. The error variable gives us the distance to the best straight line from
our current (x, y) pixel. Each time error is greater than one pixel,we increase
(or decrease) y by one, and decrease the error by one as well.

```cpp
void line(int x0, int y0, int x1, int y1, TGAImage &image, TGAColor color){
    bool steep = false;
    if(std::abs(x0 - x1) < std::abs(y0 - y1)){
        std::swap(x0, y0);
        std::swap(x1, y1);
        steep = true;
    }

    if (x0 > x1){
        std::swap(x0, x1);
        std::swap(y0, y1);
    }

    int dx = x1 - x0;
    int dy = y1 - y0;
    float derror = std::abs(dy/float(dx));
    float error = 0;
    int y = y0;
    for (int x = x0; x < x1; x++){
        if (steep){
            image.set(y, x, color);
        } else {
            image.set(x, y, color);
        }
        error += derror;
        if (error > 0.5){
            y += (y1 > y0 ? 1 : -1);
            error -= 1.;
        }
    }
}
```

## Timings: fifth and final attempt

Why do we need floating points? The only reason is one division by dx and
comparison with .5 in the loop body. We can get rid of the floating point by
replacing the error variable with another one. Let's call it error2, and assume
it is equal to error*dx*2.

```cpp
void line(int x0, int y0, int x1, int y1, TGAImage &image, TGAColor color){
    bool steep = false;
    if(std::abs(x0 - x1) < std::abs(y0 - y1)){
        std::swap(x0, y0);
        std::swap(x1, y1);
        steep = true;
    }

    if (x0 > x1){
        std::swap(x0, x1);
        std::swap(y0, y1);
    }

    int dx = x1 - x0;
    int dy = y1 - y0;
    int derror2 = std::abs(dy)*2
    int error2 = 0;
    int y = y0;
    for(int x = x0; x <= x1; x++){
        if(steep){
            image.set(x, y, color);
        } else {
            image.set(y, x, color);
        }
    }
    error2 += derror2;
    if(error2 > dx){
        y += (y1 > y0 ? 1 : -1);
        error2 -= dx*2;
    }

}
```

## References

- [https://github.com/ssloy/tinyrenderer/wiki/Lesson-1:-Bresenham%E2%80%99s-Line-Drawing-Algorithm](https://github.com/ssloy/tinyrenderer/wiki/Lesson-1:-Bresenham%E2%80%99s-Line-Drawing-Algorithm)