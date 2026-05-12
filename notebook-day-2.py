import marimo

__generated_with = "0.23.5"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return la, np, plt, scipy


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
    J
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    controlled_landing_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return animate_transform, svg, transform


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box    
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
          xmlns="http://www.w3.org/2000/svg",
          viewBox=f"0 0 {width} {height}",
          style="max-height:80vh")(
              transform.translate(x=-x_min, y=y_max)(
                  transform.scale(y=-1.0)(
                      # Sky
                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),
                      # Ground
                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),
                      # Target 
                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),
                      *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4], 
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )    
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),                
                )
            )
        ],
        justify="space-around"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
def _(M, booster, g, l, mo, np, world):
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            theta = lambda t: theta_cst
        if not callable(phi):
            phi_cst = phi
            phi = lambda t: phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center() 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 
        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    À l'équilibre, toutes les dérivées temporelles sont nulles : $v_x = v_y = \omega = 0$ et $\ddot{x} = \ddot{y} = \ddot{\theta} = 0$. On reporte cela dans le système :

    \begin{align*}
    -f \sin(\theta + \phi) &= 0 \\
    f \cos(\theta + \phi) - Mg &= 0 \\
    -\tfrac{f\,\ell}{2 J}\sin\phi &= 0
    \end{align*}

    Comme $f > 0$ : la première équation donne $\sin(\theta + \phi) = 0$, donc (avec $|\theta|,|\phi| < \pi/2$ : la somme est dans $(-\pi,\pi)$) **$\theta + \phi = 0$**. La troisième donne $\sin\phi = 0$ donc **$\phi = 0$** et par conséquent **$\theta = 0$**. La deuxième impose alors $\cos(0) = Mg/f$, soit **$f = Mg$**.

    **Conclusion.** L'ensemble des équilibres est :
    $$
    s^* = (x^*,\;0,\;y^*,\;0,\;0,\;0),\quad f^* = Mg,\quad \phi^* = 0,
    $$
    où $(x^*, y^*) \in \mathbb{R}^2$ est arbitraire : le booster tient verticalement à n'importe quelle position, tuyère droite, poussée égale au poids.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On pose $f = Mg + \Delta f$, $\theta = \Delta\theta$, $\phi = \Delta\phi$ (petites perturbations autour de l'équilibre). On développe à l'ordre 1 :

    - $\sin(\theta+\phi) \approx \Delta\theta + \Delta\phi$,
    - $\cos(\theta+\phi) \approx 1$,
    - $\sin\phi \approx \Delta\phi$.

    **Équation en $x$ :**
    $$
    M\,\Delta\ddot{x} = -f \sin(\theta+\phi) \approx -Mg(\Delta\theta + \Delta\phi)
    \quad\Longrightarrow\quad \boxed{\Delta\ddot{x} = -g(\Delta\theta + \Delta\phi)}
    $$

    **Équation en $y$ :**
    $$
    M\,\Delta\ddot{y} = f\cos(\theta+\phi) - Mg \approx (Mg + \Delta f) - Mg
    \quad\Longrightarrow\quad \boxed{\Delta\ddot{y} = \Delta f / M}
    $$

    **Équation en $\theta$ :**
    $$
    J\,\Delta\ddot{\theta} = -\tfrac{f\,\ell}{2}\sin\phi \approx -\tfrac{Mg\,\ell}{2}\,\Delta\phi
    \quad\Longrightarrow\quad \boxed{\Delta\ddot{\theta} = -\tfrac{Mg\,\ell}{2J}\,\Delta\phi = -\tfrac{6g}{\ell}\,\Delta\phi}
    $$
    (on a utilisé $J = M\ell^2/12$).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On choisit l'état $\Delta s = (\Delta x,\ \Delta v_x,\ \Delta y,\ \Delta v_y,\ \Delta\theta,\ \Delta\omega)^{\!\top}\in\mathbb{R}^6$ et l'entrée $u = (\Delta f,\ \Delta\phi)^{\!\top}\in\mathbb{R}^2$. Le système $\dot{\Delta s} = A\,\Delta s + B\,u$ s'écrit :

    $$
    A = \begin{bmatrix}
    0 & 1 & 0 & 0 & 0  & 0\\
    0 & 0 & 0 & 0 & -g & 0\\
    0 & 0 & 0 & 1 & 0  & 0\\
    0 & 0 & 0 & 0 & 0  & 0\\
    0 & 0 & 0 & 0 & 0  & 1\\
    0 & 0 & 0 & 0 & 0  & 0
    \end{bmatrix},\qquad
    B = \begin{bmatrix}
    0       & 0\\
    0       & -g\\
    0       & 0\\
    1/M     & 0\\
    0       & 0\\
    0       & -\tfrac{6g}{\ell}
    \end{bmatrix}.
    $$

    Avec $g=1$, $M=1$, $\ell=2$ on obtient $-6g/\ell = -3$.
    """)
    return


@app.cell
def _(M, g, l, np):
    A = np.array([
        [0, 1, 0, 0,  0, 0],
        [0, 0, 0, 0, -g, 0],
        [0, 0, 0, 1,  0, 0],
        [0, 0, 0, 0,  0, 0],
        [0, 0, 0, 0,  0, 1],
        [0, 0, 0, 0,  0, 0],
    ], dtype=float)

    B = np.array([
        [0,      0          ],
        [0,     -g          ],
        [0,      0          ],
        [1/M,    0          ],
        [0,      0          ],
        [0,     -6*g/l      ],
    ], dtype=float)

    print("A =\n", A)
    print("B =\n", B)
    return A, B


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notre matrice $A$ est strictement triangulaire supérieure avec des 0 sur la diagonale → **toutes les valeurs propres valent 0**.

    On est dans le **cas limite**. En plus, la matrice n'est pas diagonalisable (La seule valeur propre est 0 avec multiplicité algébrique 6, mais dim ker(A) = 2 : il n'y a que 2 vecteurs propres indépendants.).

    Par conséquant, le système n'est pas asymptotiquement stable.
    """)
    return


@app.cell
def _(A, la):
    eig = la.eigvals(A)
    print("Valeurs propres de A :", eig)
    print("rang de A :", la.matrix_rank(A))
    print("dim noyau :", 6 - la.matrix_rank(A))   
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Définition.** $\mathcal{C} = [B \;\; AB \;\; A^2 B \;\; A^3 B \;\; A^4 B \;\; A^5 B]$. Le système est commandable ssi $\operatorname{rang}(\mathcal{C}) = 6$.

    **Données** (avec $g=1$, $M=1$, $\ell=2$, donc $-6g/\ell = -3$) :

    $$
    A = \begin{bmatrix}
    0 & 1 & 0 & 0 & 0  & 0\\
    0 & 0 & 0 & 0 & -1 & 0\\
    0 & 0 & 0 & 1 & 0  & 0\\
    0 & 0 & 0 & 0 & 0  & 0\\
    0 & 0 & 0 & 0 & 0  & 1\\
    0 & 0 & 0 & 0 & 0  & 0
    \end{bmatrix},\qquad
    B = \begin{bmatrix}
    0 & 0\\ 0 & -1\\ 0 & 0\\ 1 & 0\\ 0 & 0\\ 0 & -3
    \end{bmatrix}
    $$

    **Calcul de $AB$.** La $i$-ème ligne de $AB$ = (ligne $i$ de $A$) $\cdot B$, ce qui revient à *sélectionner* des lignes de $B$ pondérées par les coefficients de $A$ :

    - ligne 1 de $A = (0,1,0,0,0,0)$ → ligne 2 de $B = (0,-1)$
    - ligne 2 de $A = (0,0,0,0,-1,0)$ → $-1\cdot$ ligne 5 de $B = (0,0)$
    - ligne 3 → ligne 4 de $B = (1,0)$
    - ligne 4 → $(0,0)$
    - ligne 5 → ligne 6 de $B = (0,-3)$
    - ligne 6 → $(0,0)$

    $$
    AB = \begin{bmatrix} 0 & -1\\ 0 & 0\\ 1 & 0\\ 0 & 0\\ 0 & -3\\ 0 & 0 \end{bmatrix}
    $$

    **Calcul de $A^2 B = A(AB)$** par la même méthode :

    $$
    A^2 B = \begin{bmatrix} 0 & 0\\ 0 & 3\\ 0 & 0\\ 0 & 0\\ 0 & 0\\ 0 & 0\end{bmatrix},\qquad
    A^3 B = A^4 B = A^5 B = 0
    $$

    (les chaînes d'intégrateurs s'éteignent : dès la 3ème itération, on ne « voit » plus que des lignes nulles).

    **Concaténation** (on ne garde que les colonnes non nulles utiles) :

    $$
    \mathcal{C} =
    \begin{bmatrix}
    \,B_1 & B_2 & AB_1 & AB_2 & A^2B_1 & A^2B_2\,
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 & 0  & 0 & -1 & 0 & 0\\
    0 & -1 & 0 & 0  & 0 & 3\\
    0 & 0  & 1 & 0  & 0 & 0\\
    1 & 0  & 0 & 0  & 0 & 0\\
    0 & 0  & 0 & -3 & 0 & 0\\
    0 & -3 & 0 & 0  & 0 & 0
    \end{bmatrix}
    $$

    **Rang.** On identifie six pivots : la colonne $B_1$ donne $e_4$, $AB_1$ donne $e_3$, $A^2B_2$ donne $e_2$, $B_2$ donne $e_6$ (après combinaison avec $AB_2$), $AB_2$ donne $e_5$, et $e_1$ vient de la combinaison restante. **Rang = 6 → COMMANDABLE.**

    Vérification numérique ci-dessous.
    """)
    return


@app.cell
def _(A, B, la, np):
    C = np.hstack([la.matrix_power(A, k) @ B for k in range(6)])
    rang = la.matrix_rank(C)
    print("Forme C :", C.shape)
    print("Rang de C :", rang, "  =>", "COMMANDABLE" if rang == 6 else "non commandable")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On garde l'état $\Delta s_{\text{lat}} = (\Delta x,\ \Delta v_x,\ \Delta\theta,\ \Delta\omega)^{\!\top}$ et l'unique entrée $\Delta\phi$ (puisque $f = Mg$ est figé, $\Delta f = 0$). Les équations linéarisées projetées sur ces composantes donnent :

    $$
    A_{\text{lat}} = \begin{bmatrix}
    0 & 1 & 0  & 0\\
    0 & 0 & -g & 0\\
    0 & 0 & 0  & 1\\
    0 & 0 & 0  & 0
    \end{bmatrix},\qquad
    B_{\text{lat}} = \begin{bmatrix} 0\\ -g\\ 0\\ -\tfrac{6g}{\ell}\end{bmatrix}.
    $$

    **Calcul détaillé de la matrice de commandabilité.** Avec $g=1$ et $\ell=2$ :

    $$
    A_{\text{lat}} = \begin{bmatrix} 0&1&0&0\\ 0&0&-1&0\\ 0&0&0&1\\ 0&0&0&0\end{bmatrix},\qquad B_{\text{lat}} = \begin{bmatrix} 0\\ -1\\ 0\\ -3\end{bmatrix}.
    $$

    On calcule les puissances une par une :

    - $B_{\text{lat}} = (0,\,-1,\,0,\,-3)^{\!\top}$
    - $A_{\text{lat}} B_{\text{lat}}$ : ligne 1 × $B$ = $-1$ ; ligne 2 = $-1\cdot 0 = 0$ ; ligne 3 = $-3$ ; ligne 4 = $0$ → $(-1,\,0,\,-3,\,0)^{\!\top}$
    - $A_{\text{lat}}^2 B_{\text{lat}} = A_{\text{lat}}(A_{\text{lat}} B_{\text{lat}})$ : ligne 1 = $0$ ; ligne 2 = $-1\cdot(-3) = 3$ ; ligne 3 = $0$ ; ligne 4 = $0$ → $(0,\,3,\,0,\,0)^{\!\top}$
    - $A_{\text{lat}}^3 B_{\text{lat}}$ : ligne 1 = $3$ ; autres = $0$ → $(3,\,0,\,0,\,0)^{\!\top}$

    D'où la matrice de commandabilité :

    $$
    \mathcal{C}_{\text{lat}} =
    \begin{bmatrix}
    0  & -1 & 0 & 3\\
    -1 & 0  & 3 & 0\\
    0  & -3 & 0 & 0\\
    -3 & 0  & 0 & 0
    \end{bmatrix}
    $$

    **Déterminant** (matrice anti-diagonale par blocs $2\times 2$) :

    $$
    \det \mathcal{C}_{\text{lat}} = (-3)\cdot(-3)\cdot 3 \cdot 3 = 81 \neq 0
    $$

    donc **rang $= 4$ → COMMANDABLE**. Vérification numérique ci-dessous.
    """)
    return


@app.cell
def _(g, l, la, np):
    A_lat = np.array([
        [0, 1,  0, 0],
        [0, 0, -g, 0],
        [0, 0,  0, 1],
        [0, 0,  0, 0],
    ], dtype=float)

    B_lat = np.array([[0], [-g], [0], [-6*g/l]], dtype=float)

    C_lat = np.hstack([la.matrix_power(A_lat, k) @ B_lat for k in range(4)])
    rang_lat = la.matrix_rank(C_lat)
    print("A_lat =\n", A_lat)
    print("B_lat =\n", B_lat.ravel())
    print("Rang de la matrice de commandabilite :", rang_lat,
          "=>", "COMMANDABLE" if rang_lat == 4 else "non commandable")
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Avec $\phi = 0$, l'équation de rotation linéarisée donne $\Delta\ddot{\theta} = 0$, donc $\Delta\theta(t) = \Delta\theta_0 = \pi/4$ (constant). Cela génère une accélération horizontale constante $\Delta\ddot{x} = -g\,\Delta\theta_0$, d'où $\Delta x(t) = -\tfrac{g\pi}{8} t^2.$ Sans commande, le système est donc instable (divergence de $x$).
    """)
    return


@app.cell
def _(g, np, plt):
    import scipy.integrate as sci2

    def sim_linear_freefall(theta0, t_end=20.0):
        def dyn(t, s):
            dx, dvx, dtheta, domega = s
            d2x     = -g * dtheta        # φ = 0
            d2theta =  0.0               # φ = 0
            return [dvx, d2x, domega, d2theta]
        sol = sci2.solve_ivp(dyn, [0, t_end], [0, 0, theta0, 0], dense_output=True)
        return sol.sol

    sol_ff = sim_linear_freefall(np.pi / 4)
    t = np.linspace(0, 20, 1000)
    s = sol_ff(t)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(t, s[0], label=r"$\Delta x(t)$")
    axes[0].set_xlabel("t (s)"); axes[0].set_ylabel("m"); axes[0].set_title(r"Dérive latérale $\Delta x$")
    axes[0].grid(True); axes[0].legend()

    axes[1].plot(t, np.degrees(s[2]), color="tab:orange", label=r"$\Delta\theta(t)$")
    axes[1].set_xlabel("t (s)"); axes[1].set_ylabel("degrés"); axes[1].set_title(r"Inclinaison $\Delta\theta$")
    axes[1].grid(True); axes[1].legend()
    plt.tight_layout(); plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Comme l'énoncé l'autorise, on prend $K = \begin{bmatrix} 0 & 0 & k_\theta & k_\omega \end{bmatrix}$. La loi
    $\Delta\phi = -K\,\Delta s_{\text{lat}} = -k_\theta\,\Delta\theta - k_\omega\,\Delta\omega$
    n'agit que sur la dynamique de $\theta$ :
    $$
    \Delta\ddot{\theta} = -\tfrac{6g}{\ell}\,\Delta\phi = \tfrac{6g}{\ell}\,(k_\theta\,\Delta\theta + k_\omega\,\Delta\omega).
    $$
    Avec $\beta := 6g/\ell = 3$, l'équation caractéristique est
    $$
    \lambda^2 \;-\; \beta k_\omega\,\lambda \;-\; \beta k_\theta = 0.
    $$
    On identifie à $\lambda^2 + 2\zeta\omega_n\lambda + \omega_n^2 = 0$ : il faut
    $$
    k_\theta = -\omega_n^2/\beta,\qquad k_\omega = -2\zeta\omega_n/\beta.
    $$

    **Choix.** On vise un amortissement critique $\zeta = 1$ et un temps de réponse à 5 % d'environ $4/(\zeta\omega_n) \approx 4\text{ s}$, donc $\omega_n = 1$. Cela donne
    $$
    k_\theta = -1/3 \approx -0.333,\qquad k_\omega = -2/3 \approx -0.667.
    $$

    **Vérifications.** $|\Delta\theta(0)| = \pi/4 \approx 0.785$ et $|\Delta\phi|_{\max} \leq |k_\theta|\cdot\pi/4 \approx 0.26 < \pi/2$. Le système $\theta$ seul est stable, donc $\Delta\theta \to 0$. En revanche $\Delta x$ dérive (boucle ouverte sur $x$), ce qui est accepté par l'énoncé.
    """)
    return


@app.cell
def _(A_lat, B_lat, la, np, plt):
    def manual_controller():
        k_theta, k_omega = -1/3, -2/3
        K = np.array([[0, 0, k_theta, k_omega]])
        A_cl = A_lat - B_lat @ K
        print("Poles boucle fermee :", la.eigvals(A_cl))

        s0 = np.array([0.0, 0.0, np.pi/4, 0.0])
        t = np.linspace(0, 25, 1000)
        from scipy.linalg import expm
        s_t = np.array([expm(A_cl * ti) @ s0 for ti in t])
        phi_t = -(K @ s_t.T).ravel()

        fig, axes = plt.subplots(2, 2, figsize=(10, 6))
        axes[0,0].plot(t, s_t[:, 2]); axes[0,0].set_title(r"$\Delta\theta(t)$"); axes[0,0].grid(True)
        axes[0,0].axhline(np.pi/4, color="r", ls=":"); axes[0,0].axhline(-np.pi/4, color="r", ls=":")
        axes[0,1].plot(t, phi_t);    axes[0,1].set_title(r"$\Delta\phi(t)$");    axes[0,1].grid(True)
        axes[0,1].axhline(np.pi/4, color="r", ls=":"); axes[0,1].axhline(-np.pi/4, color="r", ls=":")
        axes[1,0].plot(t, s_t[:, 0]); axes[1,0].set_title(r"$\Delta x(t)$ (derive acceptee)"); axes[1,0].grid(True)
        axes[1,1].plot(t, s_t[:, 1]); axes[1,1].set_title(r"$\Delta\dot x(t)$"); axes[1,1].grid(True)
        for ax in axes.ravel(): ax.set_xlabel("t")
        fig.tight_layout()
        return fig, K

    _fig, K_manual = manual_controller()
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


if __name__ == "__main__":
    app.run()
