def bilinear_resize(image: list, new_h: int, new_w: int) -> list:
    H = len(image)
    W = len(image[0])
    
    resized_image = []
    
    for i in range(new_h):
        row = []
        # Compute source y-coordinate
        if new_h == 1:
            y = 0.0
        else:
            y = i * (H - 1) / (new_h - 1)
            
        y0 = int(y)
        y1 = min(y0 + 1, H - 1)
        dy = y - y0
        
        for j in range(new_w):
            # Compute source x-coordinate
            if new_w == 1:
                x = 0.0
            else:
                x = j * (W - 1) / (new_w - 1)
                
            x0 = int(x)
            x1 = min(x0 + 1, W - 1)
            dx = x - x0
            
            # Retrieve corner values
            I_y0_x0 = image[y0][x0]
            I_y0_x1 = image[y0][x1]
            I_y1_x0 = image[y1][x0]
            I_y1_x1 = image[y1][x1]
            
            # Horizontal interpolations
            V0 = I_y0_x0 * (1 - dx) + I_y0_x1 * dx
            V1 = I_y1_x0 * (1 - dx) + I_y1_x1 * dx
            
            # Vertical interpolation
            O_ij = V0 * (1 - dy) + V1 * dy
            
            row.append(O_ij)
            
        resized_image.append(row)
        
    return resized_image