---
title: "Axis-aligned Bounding Boxes"
published: true
---

## Axis-aligned Bounding Boxes (AABBs)

The axis-aligned bounding box (AABB) is one of the most common bounding volumes. It is a
rectangular six-sided box (in 3D, four-sided in 2D) categorized by having its faces
oriented in such a way that its face normals are at all times parallel with the axes of
the given coordinate system. The best feature of the AABB is its fast overlap check, which
simply involves direct comparison of individual coordinate values.

There are three common representations of AABBs. One is by the minimum and maximum
coordinate values along each axis

```cpp
// region R = { (x, y, z) | min.x<=x<=max.x, min.y<=y<=max.y, min.z<=z<=max.z }
struct AABB {
    Point min;
    Point max;
};
```

## A C++ Implementation (with some variations)

```cpp
#ifndef BOUNDINGBOX_H
#define BOUNDINGBOX_H

#include <glm/vec3.hpp>
#include <glm/mat4x4.hpp>

namespace fly
{

    inline glm::vec3 component_wise_apply(const glm::vec3& a, const glm::vec3& b,
                                        const float& (*f)(const float&, const float&))
    {
        return {f(a.x, b.x), f(a.y, b.y), f(a.z, b.z)};
    }

    struct AABB
    {
        glm::vec3 position;
        glm::vec3 dimensions;
    };

    struct OBB
    {
        OBB(const glm::vec3& dimensions, const glm::mat4& transformation);
        AABB getAABB() const;

        glm::vec3 points[8];
    };

}
#endif //BOUNDINGBOX_H
```

```cpp
#include <glm/vec4.hpp>
#include "BoundingBox.h"
#include <algorithm>
#include <numeric>

namespace fly
{
    OBB::OBB(const glm::vec3& dimensions, const glm::mat4& transformation)
    {
        glm::vec4 half_extent {dimensions / 2.0f, 1.f};
        for (auto i = 0u; i < 8; ++i)
        {
            // get (x, y, z, w) here where
            // x = 1/-1
            // y = 1/-1
            // z = 1/-1
            // so in total 8 points
            glm::vec4 local_point {((i & 4) >> 1) - 1.f,
                                (i & 2) - 1.f,
                                ((i & 1) << 1) - 1.f,
                                1.f};
            // to get the bounding box
            local_point = local_point * half_extent;
            // do the transformation
            points[i] = transformation * local_point;
        }
    }

    AABB OBB::getAABB() const
    {
        // get min (x, y, z)
        auto min = std::accumulate(std::begin(points), std::end(points), points[0],
                        [](const glm::vec3& a, const glm::vec3& b){ return component_wise_apply(a, b, std::min); });
        // get max (x, y z)
        auto max = std::accumulate(std::begin(points), std::end(points), points[0],
                        [](const glm::vec3& a, const glm::vec3& b){ return component_wise_apply(a, b, std::max); });
        // get middle point (position)
        // get dimension
        return {(min + max) / 2.f, max - min};
    }
}
```

## References

- Real-Time Collision Detection by Christer Ericson
- [https://github.com/amhndu/fly](https://github.com/amhndu/fly)