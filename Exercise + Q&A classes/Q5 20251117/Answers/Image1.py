import numpy as np
import matplotlib.pyplot as plt

# 设置物理参数 (归一化处理)
G = 1.0    # 万有引力常量
M = 1.0    # 地球质量
m = 1.0    # 测试质点质量
R = 1.0    # 地球半径

# 定义引力势能函数
def gravitational_potential(r, R):
    V = np.zeros_like(r)

    # 地球内部 (0 <= r < R)
    internal_mask = (r >= 0) & (r < R)
    V[internal_mask] = -G*M*m/(2*R**3) * (3*R**2 - r[internal_mask]**2)
    
    # 地球外部 (r >= R)
    external_mask = (r >= R)
    V[external_mask] = -G*M*m/r[external_mask]
    
    return V

# 生成数据点
r_internal = np.linspace(0, R, 500, endpoint=False)
r_external = np.linspace(R, 10*R, 1000)
r = np.concatenate([r_internal, r_external])
V = gravitational_potential(r, R)

# 计算关键点
V_center = -3*G*M*m/(2*R)  # 地心处势能
V_surface = -G*M*m/R       # 地表处势能

# 创建图形
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(r, V, 'b-', linewidth=2.5, label=r'$V(r)$')

# 标记重要点
plt.scatter([0, R], [V_center, V_surface], color='red', s=80, zorder=5)

# 添加参考线
plt.axhline(y=0, color='k', linestyle='--', alpha=0.3)
plt.axvline(x=R, color='g', linestyle='--', alpha=0.5)

# 设置坐标轴范围，精确到整数点
plt.xlim(0, 10)
plt.ylim(-1.6, 0)

# 设置横轴刻度为R的倍数
x_ticks = np.arange(0, 11, 1)
plt.xticks(x_ticks, [f'${i}R$' if i > 0 else '0' for i in x_ticks])

# 设置纵轴刻度为-GMm/R的倍数
y_ticks = np.arange(-1.5, 0.5, 0.5)
plt.yticks(y_ticks, [f'${i}\\frac{{GMm}}{{R}}$' if i != 0 else '0' for i in y_ticks])

# 添加标签和标题
plt.xlabel(r'Distance from Earth center, $r/R$', fontsize=14)
plt.ylabel(r'Gravitational Potential Energy, $V(r)/(GMm/R)$', fontsize=14)
plt.title('Earth\'s Gravitational Potential Energy Profile', fontsize=16, fontweight='bold')

# 添加网格
plt.grid(True, linestyle='--', alpha=0.7)

# 精心安排标注位置，确保不重叠
plt.annotate(r'$(0, -\frac{3GMm}{2R})$', 
             xy=(0, V_center), xytext=(0.3, -1.45),
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=12, color='red')

plt.annotate(r'$(R, -\frac{GMm}{R})$', 
             xy=(R, V_surface), xytext=(1.2, -0.7),
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=12, color='red')

plt.text(0.3, -1.15, r'$V(r) = -\frac{GMm}{2R^3}(3R^2-r^2)$', 
         fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

plt.text(6.0, -0.15, r'$V(r) = -\frac{GMm}{r}$', 
         fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

# 添加图例
plt.legend(loc='lower right', fontsize=12)

# 调整布局
plt.tight_layout()

# 显示图像
plt.show()