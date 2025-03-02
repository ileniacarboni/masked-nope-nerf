import matplotlib.pyplot as plt
import numpy as np
import torch
import cv2

h, w = 640, 640
n_points = 1024
device = 'mps'

target_mask = cv2.imread('masks/greendino/0.png', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('colmap_dataset/greendino/0.png', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img = torch.from_numpy(img)
t_mask = torch.from_numpy(target_mask.reshape(-1)).float()
t_mask[t_mask == 0] = 0.2

ray_idx = torch.multinomial(t_mask, n_points, replacement=False)
ray_idx = ray_idx.cpu().numpy()
print(ray_idx.max(), ray_idx.min())


ys, xs = np.unravel_index(ray_idx, (h, w))
print(ys.shape, xs.shape)

activation_map = np.zeros((h, w))
activation_map[xs, ys] = 1

plt.figure(figsize=(10, 10))
plt.imshow(img, interpolation='nearest')
plt.scatter(xs, ys, color='blue', s=1, marker='s', label="Sampled Points")  # Overlay sampled points
plt.title("Ray Index Activation Map")
plt.legend()

output_path = "sampled_pixels_overlay.png"
plt.savefig(output_path, dpi=300)

plt.show()

