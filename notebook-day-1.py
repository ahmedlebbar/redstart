import marimo

__generated_with = "0.20.4"
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



    return np, plt, sci


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

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell
def _():
    g = 1.0      
    M = 1.0      
    l = 2.0      

    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Dans le repère propre du booster (axe pointant « vers le haut »), la poussée fait un angle $\phi$ (sens antihoraire) avec l'axe du booster, donc ses composantes locales sont $(-f\sin\phi,\; f\cos\phi)$.

    Le booster lui-même est incliné de $\theta$ par rapport à la verticale. En composant les deux rotations, la force exprimée dans le repère monde devient :

    $$
    \boxed{\;f_x = -f\,\sin(\theta + \phi), \qquad f_y =  f\,\cos(\theta + \phi).\;}
    $$

    Vérifications :
    - $\theta=0,\ \phi=0 \Rightarrow (f_x,f_y)=(0,f)$ — poussée verticale.
    - $\theta=0,\ \phi=\pi/2 \Rightarrow (f_x,f_y)=(-f,0)$ — poussée horizontale.
    """)
    return


@app.cell
def _(np):
    def force(f,teta,phi):
        return -f*np.sin(teta+phi), f*np.cos(teta+phi)


    print(force(1.0,0.0,0.0))           
    print(force(1.0,0.0,np.pi/2))   
    return (force,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Le centre de masse subit la résultante de la gravité (verticale, vers le bas) et de la poussée du réacteur. Le principe fondamental de la dynamique donne :

    $$
    M\,\ddot x = f_x, \qquad M\,\ddot y = f_y - M g.
    $$

    En substituant les expressions de $f_x$ et $f_y$ :

    $$
    \boxed{\;\ddot x = -\tfrac{f}{M}\sin(\theta+\phi), \qquad \ddot y = \tfrac{f}{M}\cos(\theta+\phi) - g.\;}
    $$
    """)
    return


@app.cell
def _(M, force, g):
    def centerofmass(f, teta, phi):
        fx, fy = force(f,teta, phi)
        ax = fx / M
        ay = fy / M - g
        return ax, ay

    print(centerofmass(M * g, 0.0, 0.0))

    return (centerofmass,)


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
    Pour une tige rigide de longueur totale $l$, de masse $M$ uniformément répartie, le moment d'inertie autour d'un axe passant par le centre de masse (perpendiculaire à la tige) est :

    $$
    J = \tfrac{1}{12} M l^2 .
    $$

    Avec $M = 1$ kg et $\ell = 2$ m, $J = \tfrac{1}{3}$ kg·m².
    """)
    return


@app.cell
def _(M, l):
    J = M * l**2 /12
    print(J)

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
    **Explication.**

    La gravité agit au centre de masse : son couple est nul. Seule la poussée du réacteur crée un couple.

    Dans le repère propre du booster, le point d'application de la force est la base, située en $(0,-\ell)$ par rapport au centre de masse, et la force est $(-f\sin\phi,\; f\cos\phi)$. Le couple (composante $z$ scalaire en 2D) vaut :

    $$
    \tau = r_x F_y - r_y F_x = 0 - (-\ell)(-f\sin\phi) = -\ell\, f \sin\phi.
    $$

    Le théorème du moment cinétique donne donc :

    $$
    \boxed{\;\ddot\theta = -\frac{\ell\, f\,\sin\phi}{2J} }
    $$

    Vérification du signe : si $\phi > 0$, la base est poussée vers la gauche, donc le sommet bascule vers la droite : $\theta$ diminue, cohérent avec $\ddot\theta<0$.
    """)
    return


@app.cell
def _(J, l, np):
    def accel_teta(f, phi):
        return -l * f * np.sin(phi) / 2*J

    # Verif : phi > 0 implique teta diminue
    print(accel_teta(1.0,  0.1))   
    print(accel_teta(1.0, -0.1))   

    return (accel_teta,)


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
    Le booster possède 3 degrés de liberté ($x,\, y,\, \theta$) ; en doublant pour inclure les vitesses, l'état est de dimension :

    $$
    n = 6, \qquad s = (x,\, v_x,\, y,\, v_y,\, \theta,\, \omega) \in \mathbb{R}^6.
    $$

    En empilant toutes les EDO trouvées précédemment, le champ de vecteurs s'écrit :

    $$
    \dot s = F(s, f, \phi) =
    \begin{pmatrix}
    v_x \\[2pt]
    -\dfrac{f}{M}\sin(\theta+\phi) \\[6pt]
    v_y \\[2pt]
    \dfrac{f}{M}\cos(\theta+\phi) - g \\[6pt]
    \omega \\[2pt]
    -\dfrac{\ell\, f\,\sin\phi}{2J}
    \end{pmatrix}.
    $$
    """)
    return


@app.cell
def _(accel_teta, centerofmass, np):
    # Dimension n = 6 :  s = [x, vx, y, vy, teta, omega]
    def F(s, f, phi):
        x, vx, y, vy, teta, omega = s
        ax, ay = centerofmass(f, teta, phi)
        acc_teta = accel_teta(f, phi)
        return np.array([vx, ax, vy, ay, omega, acc_teta])



    return (F,)


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


@app.cell
def _(F, sci):
    def redstart_solve(t_span, y0, f_phi):
        def s_point(t, y):
            f, phi = f_phi(t, y)
            return F(y, f, phi)

        res = sci.solve_ivp(
            s_point,
            t_span,
            y0,
            dense_output=True,
            max_step=0.05,
        )
        return res.sol



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
    En chute libre ($f = 0$), $\ddot y = -g$. Avec $y(0)=10$ et $\dot y(0)=0$ :

    $$
    y(t) = 10 - \tfrac{1}{2} g\, t^2 = 10 - \tfrac{1}{2} t^2.
    $$

    L'instant $t^\star$ où le centre de masse traverse $y = \ell = 2$ vérifie :

    $$
    10 - \tfrac{1}{2}(t^\star)^2 = 2 \quad\Longrightarrow\quad t^\star = 4 \text{s}.
    $$

    Le tracé suivant superpose la solution numérique de `redstart_solve` et la droite $y = \ell$ : on vérifie visuellement qu'elles se croisent en $t = t^\star$ (ligne rouge pointillée).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell
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
        plt.plot(t, l * np.ones_like(t), color="red", ls="--", label=r"$y=\ell$")
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
    mo.md(r"""
    Comme $\theta \equiv 0$ et $\phi \equiv 0$, la dynamique se réduit à l'axe vertical :

    $$
    M\,\ddot y(t) = f(t) - M g \quad\Longleftrightarrow\quad f(t) = M\bigl(\ddot y(t) + g\bigr).
    $$

    On choisit pour $y(t)$ une trajectoire **polynomiale cubique** (4 coefficients = juste assez pour 4 conditions aux limites) :

    $$
    y(t) = a + b\,t + c\,t^2 + d\,t^3,
    \qquad
    \begin{cases} y(0)=10 \\ \dot y(0)=-2 \\ y(5)=1 \\ \dot y(5)=0. \end{cases}
    $$

    Ce système linéaire est résolu numériquement avec `np.linalg.solve`.
    """)
    return


@app.cell
def _(M, g, np):

    T = 5.0
    A = np.array([
        [1, 0,   0,    0],     # y(0)  = a = 10
        [0, 1,   0,    0],     # y'(0) = b = -2
        [1, T, T**2, T**3],    # y(T)  = a+bT+cT^2+dT^3 = 1
        [0, 1, 2*T,  3*T**2],  # y'(T) = b+2cT+3dT^2    = 0
    ])
    conditions = np.array([10.0, -2.0, 1.0, 0.0])
    a, b, c, d = np.linalg.solve(A, conditions)
    print(f"a={a}, b={b}, c={c}, d={d}")

    def y_ref(t):  return a + b*t + c*t**2 + d*t**3
    def ddy_ref(t): return 2*c + 6*d*t
    def f_landing(t): return M * (ddy_ref(t) + g)

    print(f"f(t) = {M*(2*c + g):.3f} + {M*6*d:.3f} * t")
    print("f(0) =", f_landing(0.0), "   f(5) =", f_landing(5.0))
    return T, f_landing


@app.cell
def _(T, f_landing, l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, T]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]   # [x, vx, y, vy, theta, omega]

        def f_phi(t, y):
            return np.array([f_landing(t), 0.0])  # f(t) trouve plus haut, phi = 0

        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(0.0, T, 500)
        states = sol(t)
        y_t, vy_t = states[2], states[3]

        fig, ax = plt.subplots(2, 1, figsize=(7, 5), sharex=True)
        ax[0].plot(t, y_t, label="$y(t)$")
        ax[0].axhline(l, color="grey", ls="--", label=r"$y=\ell$")
        ax[0].set_ylabel("hauteur (m)"); ax[0].grid(True); ax[0].legend()

        ax[1].plot(t, vy_t, color="tab:orange", label=r"$\dot y(t)$")
        ax[1].axhline(0, color="grey", ls="--")
        ax[1].set_xlabel("temps $t$ (s)"); ax[1].set_ylabel("vitesse (m/s)")
        ax[1].grid(True); ax[1].legend()

        print(f"y(T)  = {y_t[-1]:.6f}   (cible = {l})")
        print(f"vy(T) = {vy_t[-1]:.6f}   (cible = 0)")
        return fig

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
    mo.md(r"""
    **Idée.** SVG a son axe $y$ vers le bas. On enveloppe tout dans deux groupes :

    1. `translate(-x_min, y_max)` pour mettre l'origine au bon endroit ;
    2. `scale(1, -1)` pour inverser l'axe $y$.

    À l'intérieur on peut alors utiliser directement les coordonnées cartésiennes.
    """)
    return


@app.cell
def _(svg, transform):
    from IPython.display import HTML

    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box
        w = x_max - x_min
        h = y_max - y_min
        sky    = svg.rect(x=x_min, y=0,     width=w, height=y_max,  fill='#87CEEB')
        ground = svg.rect(x=x_min, y=y_min, width=w, height=-y_min, fill='#8B4513')
        target = svg.rect(x=-1,    y=-0.05, width=2, height=0.1,    fill='#22aa22')
        inner = transform.translate(x=-x_min, y=y_max)(
            transform.scale(x=1, y=-1)(
                sky, ground, target, *objects
            )
        )
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {w} {h}" width="360">{inner}</svg>'
        )


    return HTML, world


@app.cell
def _(HTML, svg, world):
    # Tests : monde vide, monde avec un carré noir sur la cible, monde avec 2 carrés colorés.
    html = (
        '<div style="display:flex;justify-content:space-around;gap:10px">'
        + world([-3, 3, -2, 4])
        + world([-3, 3, -2, 4], svg.rect(x=-1, y=0, width=2, height=2, fill='black'))
        + world([-3, 3, -2, 4],
                svg.rect(x=-3, y=2, width=2, height=2, fill='red'),
                svg.rect(x=1,  y=2, width=2, height=2, fill='blue'))
        + '</div>'
    )
    HTML(html)

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
    mo.md(r"""
    **Construction.**

    Dans le repère propre du booster (origine au centre de masse, axe propre +y) :

    - Corps : rectangle centré, largeur 0.2, hauteur $\ell$, soit $x\in[-0.1,0.1]$, $y\in[-\ell/2,\,\ell/2]$.
    - Base : point $(0,\,-\ell/2)$.
    - Flamme : triangle sortant de la base, longueur $L_\text{flamme} = \dfrac{\ell}{2}\cdot\dfrac{f}{Mg}$ (donc $L_\text{flamme} = \ell/2$ lorsque $f = M g$). Le triangle est ensuite tourné de $\phi$ autour de la base.

    On applique enfin `rotate(theta)` autour de $(0,0)$ puis `translate(x, y)` pour placer le booster dans le monde. Comme on travaille dans le repère interne après le `scale(1,-1)`, un `rotate(θ degrés)` correspond bien à une rotation antihoraire dans le repère cartésien.
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_len = (l / 2) * (f / (M * g)) if f > 0 else 0.0
        body  = svg.rect(x=-0.1, y=-l/2, width=0.2, height=l, fill='#222222')
        flame = transform.translate(x=0, y=-l/2)(
            transform.rotate(a=np.degrees(phi))(
                svg.polygon(
                    points=f'-0.12,0 0.12,0 0,{-flame_len}',
                    fill='orange'
                )
            )
        )
        return transform.translate(x=x, y=y)(
            transform.rotate(a=np.degrees(theta))(body, flame)
        )


    return (booster,)


@app.cell
def _(HTML, M, booster, g, l, np, world):
    # Tests : booster posé, booster en hover (flamme = l/2), booster tilté avec poussée latérale.
    html2 = (
        '<div style="display:flex;justify-content:space-around;gap:10px">'
        + world([-3, 3, -2, 4], booster(0, l/2, 0, 0, 0))
        + world([-3, 3, -2, 4], booster(0, l, 0, M * g, 0))
        + world([-3, 3, -2, 4], booster(-l/2, l, np.pi/4, 2 * M * g, np.pi/2))
        + '</div>'
    )
    HTML(html2)

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
    mo.md(r"""
    **Idée.**

    On reprend la composition statique du booster, mais chaque transformation devient animée :

    - `animate_transform.translate(x(t), y(t))` pour la position,
    - `animate_transform.rotate(theta(t))` pour l'inclinaison,
    - `animate_transform.rotate(phi(t))` autour de la base pour la tuyère,
    - `animate_transform.scale(1, flame_len(t))` pour rallonger la flamme proportionnellement à $f(t)$.

    Astuce pour la flamme : on dessine un triangle « unitaire » de hauteur 1 et on l'étire par un `scale(1, flame_len(t))` ; comme la pointe est à $y = -1$, après le scale la pointe est à $y = -L_\text{flamme}(t)$.
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg, transform):
    def booster_anim(x, y, theta, f, phi, T):
        theta_deg = lambda t: np.degrees(theta(t))
        phi_deg   = lambda t: np.degrees(phi(t))
        flame_len = lambda t: (l / 2) * f(t) / (M * g)

        body = svg.rect(x=-0.1, y=-l/2, width=0.2, height=l, fill='#222222')

        flame_unit = svg.polygon(points='-0.12,0 0.12,0 0,-1', fill='orange')
        flame_group = transform.translate(x=0, y=-l/2)(
            animate_transform.rotate(a=phi_deg, x=0, y=0, T=T)(
                animate_transform.scale(x=1, y=flame_len, T=T)(
                    flame_unit
                )
            )
        )

        return animate_transform.translate(x=x, y=y, T=T)(
            animate_transform.rotate(a=theta_deg, x=0, y=0, T=T)(
                body, flame_group
            )
        )


    return (booster_anim,)


@app.cell
def _(HTML, M, booster_anim, g, l, np, world):
    def booster_anim_0():
        T = 5.0
        def x(t):     return -l/2 + l * (t / T)
        def y(t):     return l/2 + l/2 * (t / T)
        def theta(t): return (t / T) * 2 * np.pi
        def f(t):     return M * g * (t / T)
        def phi(t):   return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    HTML(world([-3, 3, -2, 4], booster_anim_0()))

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


@app.cell
def _(booster_anim, redstart_solve):
    def simulate_and_animate(t_span, y0, f_phi):
        sol = redstart_solve(t_span, y0, f_phi)
        T = t_span[1] - t_span[0]

        def x_t(t):     return float(sol(t)[0])
        def y_t(t):     return float(sol(t)[2])
        def theta_t(t): return float(sol(t)[4])
        def f_t(t):     return float(f_phi(t, sol(t))[0])
        def phi_t(t):   return float(f_phi(t, sol(t))[1])

        return booster_anim(x_t, y_t, theta_t, f_t, phi_t, T=T)


    return (simulate_and_animate,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On utilise `redstart_solve` pour intégrer les EDO, puis on extrait les fonctions $x(t)$, $y(t)$, $\theta(t)$, $f(t)$, $\phi(t)$ depuis la solution dense.

    ### Scénario 1 – Chute libre
    $(x,\dot x,y,\dot y,\theta,\dot\theta)=(0,0,10,0,0,0)$, $f=0$, $\phi=0$.

    Le booster tombe sans poussée. Il croise $y=\ell$ à $t=4$ s et s'enfonce dans le sol.
    """)
    return


@app.cell
def _(HTML, np, simulate_and_animate, world):
    # Scénario 1 : chute libre (f = 0)
    y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
    anim_1 = simulate_and_animate(
        [0.0, 5.0], y0,
        lambda t, y: np.array([0.0, 0.0]),
    )
    HTML(world([-3, 3, -2, 12], anim_1))

    return (y0,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Scénario 2 – Poussée d'équilibre ($f=Mg$, $\phi=0$)
    $(x,\dot x,y,\dot y,\theta,\dot\theta)=(0,0,10,0,0,0)$, $f=Mg$, $\phi=0$.

    La poussée compense exactement la gravité : le booster est en sustentation parfaite à $y=10$.
    """)
    return


@app.cell
def _(HTML, M, g, np, simulate_and_animate, world, y0):
    # Scénario 2 : poussée constante f = M*g, phi = 0 (hover -> reste immobile en y)
    anim_2 = simulate_and_animate(
        [0.0, 5.0], y0,
        lambda t, y: np.array([M * g, 0.0]),
    )
    HTML(world([-3, 3, -2, 12], anim_2))

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Scénario 3 – Poussée déviée ($f=Mg$, $\phi=\pi/8$)
    $(x,\dot x,y,\dot y,\theta,\dot\theta)=(0,0,10,0,0,0)$, $f=Mg$, $\phi=\pi/8$.

    La poussée n'est pas alignée avec le booster. Un couple $\tau = -\frac{\ell f\sin\phi}{2}$ fait basculer le booster ; la poussée a aussi une composante horizontale qui le déplace latéralement.
    """)
    return


@app.cell
def _(HTML, M, g, np, simulate_and_animate, world, y0):
    # Scénario 3 : f = M*g, phi = pi/8 -> couple non nul, le booster bascule
    anim_3 = simulate_and_animate(
        [0.0, 5.0], y0,
        lambda t, y: np.array([M * g, np.pi / 8]),
    )
    HTML(world([-6, 6, -2, 12], anim_3))

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Scénario 4 – Atterrissage contrôlé

    $(x,\dot x,y,\dot y,\theta,\dot\theta)=(0,0,10,-2,0,0)$, $f=f_{\rm landing}(t)$, $\phi=0$.

    La force polynomiale $f(t)=M(\ddot y_{\rm ref}(t)+g)$ guide le booster de $y=10$ à $y=\ell/2=1$ avec vitesse nulle en $t=5$ s.
    """)
    return


@app.cell
def _(HTML, T, f_landing, np, simulate_and_animate, world):
    # Scénario 4 : atterrissage contrôlé (cf. plus haut)
    y0_land = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
    anim_4 = simulate_and_animate(
        [0.0, T], y0_land,
        lambda t, y: np.array([f_landing(t), 0.0]),
    )
    HTML(world([-3, 3, -2, 12], anim_4))

    return


if __name__ == "__main__":
    app.run()
