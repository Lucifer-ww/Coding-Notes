import matplotlib.pyplot as plt

xr = [255, 255, 0, 0, 150]
yr = [1, 3, 4, 6, 7]
# 0, 100, 200, 300, 400, 500, 600, 700

plt.plot(yr, xr, color="tomato", label="Red")
xg = [0, 150, 255, 255, 0, 0]
yg = [1, 2, 3, 5, 6, 7]
plt.plot(yg, xg, color="ForestGreen", label="Green")
xb = [0, 0, 255, 255]
yb = [1, 4, 5, 7]
plt.plot(yb, xb, color="Royalblue", label="Blue")
plt.legend()
plt.show()
