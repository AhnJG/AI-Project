# Pillow

### Image

#### - Resize

```python
# use nearest neighbour
im2 = im1.resize((width, height), Image.NEAREST)      
# linear interpolation in a 2x2 environment
im3 = im1.resize((width, height), Image.BILINEAR)
# cubic spline interpolation in a 4x4 environment
im4 = im1.resize((width, height), Image.BICUBIC)      
## best down-sizing filter
im5 = im1.resize((width, height), Image.ANTIALIAS)    
```

