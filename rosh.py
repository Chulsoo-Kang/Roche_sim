# app.py

import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import time


# ============================================================
# Streamlit settings
# ============================================================
st.set_page_config(
    page_title="Roche Potential Simulator",
    layout="wide"
)

st.title("Roche Potential & Test Particle Simulator")

st.markdown(
    r"""
2天体と共に回転する座標系での有効ポテンシャル

$$
\psi_{\rm eff}(\mathbf r)
=
-\frac{GM_1}{|\mathbf r-\mathbf r_1|}
-\frac{GM_2}{|\mathbf r-\mathbf r_2|}
-\frac12 |\boldsymbol{\Omega}\times\mathbf r|^2
$$

とテスト粒子についてコリオリ力を含めた

$$
\ddot{\mathbf r}
=
-\nabla\psi_{\rm eff}
-2\boldsymbol{\Omega}\times\dot{\mathbf r}
$$

を用いて、テスト粒子の運動を計算する
"""
)


# ============================================================
# Sidebar parameters
# ============================================================
st.sidebar.header("Binary parameters")

G = 1.0

M1 = st.sidebar.number_input(
    "M1",
    min_value=0.01,
    value=1.0,
    step=0.1
)

M2 = st.sidebar.number_input(
    "M2",
    min_value=0.01,
    value=0.5,
    step=0.1
)

a = st.sidebar.number_input(
    "Binary separation a",
    min_value=0.1,
    value=1.0,
    step=0.1
)


st.sidebar.header("Initial conditions")

x0 = st.sidebar.number_input(
    "x0",
    value=0.24,
    step=0.05
)

y0 = st.sidebar.number_input(
    "y0",
    value=0.0,
    step=0.05
)

vx0 = st.sidebar.number_input(
    "vx0",
    value=0.0,
    step=0.05
)

vy0 = st.sidebar.number_input(
    "vy0",
    value=0.0,
    step=0.05
)


st.sidebar.header("Time evolution")

t_max = st.sidebar.number_input(
    "t max",
    min_value=0.1,
    value=20.0,
    step=1.0
)

n_frames = st.sidebar.slider(
    "Number of frames",
    min_value=100,
    max_value=2000,
    value=500,
    step=100
)

trail_length = st.sidebar.slider(
    "Trail length",
    min_value=10,
    max_value=500,
    value=100,
    step=10
)

animation_speed = st.sidebar.slider(
    "Animation speed",
    min_value=0.001,
    max_value=0.1,
    value=0.02,
    step=0.005
)


# ============================================================
# Binary geometry
# ============================================================
Mtot = M1 + M2

x1 = -M2 / Mtot * a
x2 = +M1 / Mtot * a

Omega = np.sqrt(G * Mtot / a**3)


# ============================================================
# Effective potential
# ============================================================
def psi_eff(x, y):

    d1 = np.sqrt((x - x1)**2 + y**2)
    d2 = np.sqrt((x - x2)**2 + y**2)

    psi_grav = (
        -G * M1 / d1
        -G * M2 / d2
    )

    psi_cent = (
        -0.5 * Omega**2 * (x**2 + y**2)
    )

    return psi_grav + psi_cent


# ============================================================
# d psi / dx on y = 0
# ============================================================
def dpsi_dx_axis(x):

    dx1 = x - x1
    dx2 = x - x2

    term1 = (
        G * M1 * dx1
        / np.abs(dx1)**3
    )

    term2 = (
        G * M2 * dx2
        / np.abs(dx2)**3
    )

    term_cent = -Omega**2 * x

    return term1 + term2 + term_cent


# ============================================================
# Find L1
# ============================================================
eps = 1e-6 * a

try:

    x_L1 = brentq(
        dpsi_dx_axis,
        x1 + eps,
        x2 - eps
    )

    psi_L1 = psi_eff(
        x_L1,
        0.0
    )

except Exception:

    x_L1 = None
    psi_L1 = None


# ============================================================
# Equation of motion
# ============================================================
def rhs(t, state):

    x, y, vx, vy = state

    dx1 = x - x1
    dy1 = y

    dx2 = x - x2
    dy2 = y

    d1 = np.sqrt(
        dx1**2 + dy1**2
    )

    d2 = np.sqrt(
        dx2**2 + dy2**2
    )

    ax_grav = (
        -G * M1 * dx1 / d1**3
        -G * M2 * dx2 / d2**3
    )

    ay_grav = (
        -G * M1 * dy1 / d1**3
        -G * M2 * dy2 / d2**3
    )

    ax_cent = Omega**2 * x
    ay_cent = Omega**2 * y

    ax_cor = 2.0 * Omega * vy
    ay_cor = -2.0 * Omega * vx

    ax = (
        ax_grav
        + ax_cent
        + ax_cor
    )

    ay = (
        ay_grav
        + ay_cent
        + ay_cor
    )

    return [
        vx,
        vy,
        ax,
        ay
    ]


# ============================================================
# Simulation button
# ============================================================
run = st.sidebar.button(
    "Run simulation",
    type="primary"
)


# ============================================================
# Information panel
# ============================================================
st.subheader("Binary geometry")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "M1 position",
    f"x₁ = {x1:.6f}"
)

col2.metric(
    "Center of mass",
    "x = 0"
)

col3.metric(
    "M2 position",
    f"x₂ = {x2:.6f}"
)

if x_L1 is not None:
    col4.metric(
        "L1 point",
        f"x = {x_L1:.6f}"
    )

    st.write(
        rf"""
        **L1 coordinates**

        $$
        (x_{{L1}},y_{{L1}})
        =
        ({x_L1:.8f},0)
        $$

        $$
        \psi_{{\rm eff}}(L_1)
        =
        {psi_L1:.8f}
        $$
        """
    )
else:
    col4.metric(
        "L1 point",
        "not found"
    )


# ============================================================
# Potential grid
# ============================================================
x_grid = np.linspace(
    -1.7 * a,
    1.7 * a,
    600
)

y_grid = np.linspace(
    -1.3 * a,
    1.3 * a,
    500
)

X, Y = np.meshgrid(
    x_grid,
    y_grid
)

Psi = psi_eff(
    X,
    Y
)


# mask singularity regions
r_mask = 0.03 * a

mask1 = (
    (X - x1)**2 + Y**2
    < r_mask**2
)

mask2 = (
    (X - x2)**2 + Y**2
    < r_mask**2
)

Psi_masked = np.ma.array(
    Psi,
    mask=(mask1 | mask2)
)


# ============================================================
# Static potential figure
# ============================================================
st.subheader("Effective potential")

fig, ax = plt.subplots(
    figsize=(9, 7)
)

finite_values = Psi_masked.compressed()

levels = np.linspace(
    np.percentile(
        finite_values,
        5
    ),
    np.percentile(
        finite_values,
        80
    ),
    30
)

ax.contour(
    X,
    Y,
    Psi_masked,
    levels=levels,
    linewidths=0.7
)

# Roche-lobe boundary
if psi_L1 is not None:

    ax.contour(
        X,
        Y,
        Psi_masked,
        levels=[psi_L1],
        linewidths=2.0
    )

    ax.scatter(
        x_L1,
        0.0,
        marker="x",
        s=120,
        label="L1"
    )


ax.scatter(
    x1,
    0.0,
    s=150,
    label="M1"
)

ax.scatter(
    x2,
    0.0,
    s=150,
    label="M2"
)

ax.scatter(
    x0,
    y0,
    marker="*",
    s=120,
    label="Initial position"
)

ax.set_xlabel("x")
ax.set_ylabel("y")

ax.set_aspect("equal")

ax.legend()

ax.set_xlim(
    x_grid.min(),
    x_grid.max()
)

ax.set_ylim(
    y_grid.min(),
    y_grid.max()
)

st.pyplot(fig)


# ============================================================
# Orbit integration
# ============================================================
if run:

    t_eval = np.linspace(
        0.0,
        t_max,
        n_frames
    )

    state0 = [
        x0,
        y0,
        vx0,
        vy0
    ]

    sol = solve_ivp(
        rhs,
        (0.0, t_max),
        state0,
        t_eval=t_eval,
        rtol=1e-9,
        atol=1e-11,
        max_step=t_max / n_frames
    )

    xp = sol.y[0]
    yp = sol.y[1]

    vxp = sol.y[2]
    vyp = sol.y[3]


    # ========================================================
    # Jacobi constant
    # ========================================================
    C = (
        -2.0 * psi_eff(
            xp,
            yp
        )
        -(
            vxp**2
            + vyp**2
        )
    )

    st.subheader(
        "Jacobi constant"
    )

    st.write(
        f"""
        Initial:
        {C[0]:.8f}

        Final:
        {C[-1]:.8f}

        Relative variation:
        {(C[-1]-C[0])/C[0]:.3e}
        """
    )


    # ========================================================
    # Animation
    # ========================================================
    st.subheader(
        "Particle motion"
    )

    plot_area = st.empty()

    for i in range(
        len(sol.t)
    ):

        fig, ax = plt.subplots(
            figsize=(9, 7)
        )

        ax.contour(
            X,
            Y,
            Psi_masked,
            levels=levels,
            linewidths=0.5
        )

        # Roche-lobe contour
        if psi_L1 is not None:

            ax.contour(
                X,
                Y,
                Psi_masked,
                levels=[psi_L1],
                linewidths=2.0
            )

            ax.scatter(
                x_L1,
                0.0,
                marker="x",
                s=100,
                label="L1"
            )


        # Binary
        ax.scatter(
            x1,
            0.0,
            s=150,
            label="M1"
        )

        ax.scatter(
            x2,
            0.0,
            s=150,
            label="M2"
        )


        # Trail
        i0 = max(
            0,
            i - trail_length
        )

        ax.plot(
            xp[i0:i+1],
            yp[i0:i+1],
            linewidth=1.5
        )


        # Particle
        ax.scatter(
            xp[i],
            yp[i],
            s=60
        )


        # Initial position
        ax.scatter(
            x0,
            y0,
            marker="*",
            s=100
        )


        ax.set_title(
            f"t = {sol.t[i]:.3f}"
        )

        ax.set_xlabel("x")
        ax.set_ylabel("y")

        ax.set_xlim(
            x_grid.min(),
            x_grid.max()
        )

        ax.set_ylim(
            y_grid.min(),
            y_grid.max()
        )

        ax.set_aspect(
            "equal"
        )

        ax.legend(
            loc="upper right"
        )

        plot_area.pyplot(
            fig,
            clear_figure=True
        )

        plt.close(fig)

        time.sleep(
            animation_speed
        )