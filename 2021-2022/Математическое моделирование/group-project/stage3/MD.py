import numpy as np
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches
import matplotlib.path as path

class MDSimulation:

    def __init__(self, pos, vel, r, m):
        # создаем симуляцию с частицами, одинаковыми по массе и радиусу
        # в массиве pos храним координаты частиц
        # в массиве vel храним скорости
        self.pos = np.asarray(pos, dtype=float)
        self.vel = np.asarray(vel, dtype=float)
        self.n = self.pos.shape[0]
        self.r = r
        self.m = m
        self.nsteps = 0

    def advance(self, dt):
        # функция, в которой мы находим, что происходит в симуляции в следующий момент времени
        self.nsteps += 1
        # обновляем координаты частиц, учитывая ускорение
        self.pos += self.vel * dt
        # находим все столкновения:
        # находим все расстояния между парами частиц
        dist = squareform(pdist(self.pos))
        # координаты частиц, которые находятся на расстоянии меньше своего диаметра от другой частицы
        iarr, jarr = np.where(dist < 2 * self.r)
        k = iarr < jarr
        iarr, jarr = iarr[k], jarr[k]

        # изменяем скорости частиц после столкновения
        # @ - умножение матриц (тут векторов)
        for i, j in zip(iarr, jarr):
            # находим координаты и скорости цастиц до столкновения
            pos_i, vel_i = self.pos[i], self.vel[i]
            pos_j, vel_j = self.pos[j], self.vel[j]
            # ????
            rel_pos, rel_vel = pos_i - pos_j, vel_i - vel_j
            r_rel = rel_pos @ rel_pos
            v_rel = rel_vel @ rel_pos
            v_rel = 2 * rel_pos * v_rel / r_rel - rel_vel
            v_cm = (vel_i + vel_j) / 2
            self.vel[i] = v_cm - v_rel / 2
            self.vel[j] = v_cm + v_rel / 2

        # Проверим, есть ли частицы чтолкнувшиеся со стеной, если да, то отразим их векторы скорости
        hit_left_wall = self.pos[:, 0] < self.r
        hit_right_wall = self.pos[:, 0] > 1 - self.r
        hit_bottom_wall = self.pos[:, 1] < self.r
        hit_top_wall = self.pos[:, 1] > 1 - self.r
        self.vel[hit_left_wall | hit_right_wall, 0] *= -1
        self.vel[hit_bottom_wall | hit_top_wall, 1] *= -1


# n - число частиц, rscale - коэффициент увеличения масштаба
n = 1000
rscale = 5.e6
# используем молекулы аргона, задаем их растояние Ван-дер-Ваальса
r = 2e-10 * rscale
time = 1e9  # задаем измерение времени в наносекундах
# считаем изменение скорости аргона за еденицу времени при 300 кельвин
sbar = 353 * rscale / time

# задаем всем частицам рандомное положение
pos = np.random.random((n, 2))
# задаем рандомную скорость и направление движения
theta = np.random.random(n) * 2 * np.pi
vel = (np.random.random(n) * np.array((np.cos(theta), np.sin(theta)))).T

# запускаем симуляцию
sim = MDSimulation(pos, vel, r, 1)

# создаем 2 диаграммы:
fig = plt.figure()
# поле частиц, показывает перемещение частиц с течением времени
sim_ax = fig.add_subplot(121, autoscale_on=False)
sim_ax.set_xticks([])
sim_ax.set_yticks([])
particles, = sim_ax.plot([], [], 'ko')
# гисторамма распределения скоростей
speed_ax = fig.add_subplot(122)

# т.к. в matplotlib нет реализации анимации гистограмм, будем использовать вспомогательный класс
class Histogram:
    # создаем гистограмму скоростей
    def __init__(self, data, xmax, nbars):
        self.nbars = nbars
        self.density = True
        self.bins = np.linspace(0, xmax, nbars)
        self.hist, bins = np.histogram(data, self.bins, density=True)

        # это не скриним = делаем вид что само работате потому что ну нафиг
        self.left = np.array(bins[:-1])
        self.right = np.array(bins[1:])
        self.bottom = np.zeros(len(self.left))
        self.top = self.bottom + self.hist
        nrects = len(self.left)
        self.nverts = nrects * 5
        self.verts = np.zeros((self.nverts, 2))
        self.verts[0::5, 0] = self.left
        self.verts[0::5, 1] = self.bottom
        self.verts[1::5, 0] = self.left
        self.verts[1::5, 1] = self.top
        self.verts[2::5, 0] = self.right
        self.verts[2::5, 1] = self.top
        self.verts[3::5, 0] = self.right
        self.verts[3::5, 1] = self.bottom

    # рисуем текущую гистограмму
    def draw(self, ax):
        codes = np.ones(self.nverts, int) * path.Path.LINETO
        codes[0::5] = path.Path.MOVETO
        codes[4::5] = path.Path.CLOSEPOLY
        barpath = path.Path(self.verts, codes)
        self.patch = patches.PathPatch(barpath, ec='k', lw=0.5, alpha=0.5)
        ax.add_patch(self.patch)

    # изменяем столбцы гисторгаммы, относительно новых значений
    def update(self, data):
        self.hist, bins = np.histogram(data, self.bins, density=self.density)
        self.top = self.bottom + self.hist
        self.verts[1::5, 1] = self.top
        self.verts[2::5, 1] = self.top


def get_speeds(vel):  # находим скорости частиц
    return np.hypot(vel[:, 0], vel[:, 1])


def get_KE(speeds):  # находим кинетическую энергию для всех частиц
    return 0.5 * sim.m * sum(speeds ** 2)

# создаем гистограмму по нашим данным
speeds = get_speeds(sim.vel)
speed_hist = Histogram(speeds, 2 * sbar, 50)
speed_hist.draw(speed_ax)
speed_ax.set_xlim(speed_hist.left[0], speed_hist.right[-1])

fig.tight_layout()

# находим распределение Максвелла
mean_KE = get_KE(speeds) / n
a = sim.m / 2 / mean_KE
# рисуем кривую поверх гистрограммы
sgrid_hi = np.linspace(0, speed_hist.bins[-1], 200)
f = 2 * a * sgrid_hi * np.exp(-a * sgrid_hi ** 2)
mb_line, = speed_ax.plot(sgrid_hi, f, c='0.7')

# вспомогательные функции для анимации
def init_anim():
    particles.set_data([], [])
    return particles, speed_hist.patch

def animate(i):
    global sim, verts
    sim.advance(1 / 30)

    particles.set_data(sim.pos[:, 0], sim.pos[:, 1])
    particles.set_markersize(0.5)

    speeds = get_speeds(sim.vel)
    speed_hist.update(speeds)
    return particles, speed_hist.patch

# запускаем анимации и выводим графики
anim = FuncAnimation(fig, animate, interval=10, blit=False, init_func=init_anim)
plt.show()
