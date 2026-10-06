# 近接連星系におけるテスト粒子軌道の数値計算

## 1. 目的

2天体からなる近接連星系について、連星と共回転する座標系を考え、

- 2天体の重力
- 遠心力
- コリオリ力

を考慮したテスト粒子の運動を数値的に計算する。

また、

- 有効ポテンシャル
- Roche lobe
- L1 点
- Jacobi 定数
- zero-velocity curve

との関係を調べる。

---

# 2. 座標系と基本設定

2天体の質量を

\[
M_1,\qquad M_2
\]

とし、2天体間距離を

\[
a
\]

とする。

2天体は円軌道を描いて公転しており、
その角速度ベクトルを

\[
\boldsymbol{\Omega}
\]

とする。

計算では、2天体と共に回転する座標系を用いる。

---

## 2.1 重心を原点にとる

2天体の重心を

\[
(x,y)=(0,0)
\]

とする。

2天体を \(x\) 軸上に置き、

\[
\mathbf r_1=(x_1,0),
\qquad
\mathbf r_2=(x_2,0)
\]

とする。

重心条件

\[
M_1x_1+M_2x_2=0
\]

および

\[
x_2-x_1=a
\]

より、

\[
\boxed{
x_1=-\frac{M_2}{M_1+M_2}a
}
\]

\[
\boxed{
x_2=+\frac{M_1}{M_1+M_2}a
}
\]

となる。

---

# 3. 連星の公転角速度

2天体は円軌道を描くものとし、Kepler 則より

\[
\boxed{
\Omega^2
=
\frac{G(M_1+M_2)}{a^3}
}
\]

とする。

したがって

\[
\boxed{
\Omega
=
\sqrt{
\frac{G(M_1+M_2)}{a^3}
}
}
\]

である。

---

# 4. 有効ポテンシャル

2天体と共に回転する座標系におけるテスト粒子の有効ポテンシャルを

\[
\psi_{\rm eff}(\mathbf r)
=
\psi_{\rm grav}
+
\psi_{\rm cent}
\]

とする。

---

## 4.1 重力ポテンシャル

テスト粒子の位置を

\[
\mathbf r=(x,y)
\]

とすると、

\[
\boxed{
\psi_{\rm grav}
=
-\frac{GM_1}{|\mathbf r-\mathbf r_1|}
-\frac{GM_2}{|\mathbf r-\mathbf r_2|}
}
\]

である。

2次元では

\[
r_1
=
\sqrt{(x-x_1)^2+y^2}
\]

\[
r_2
=
\sqrt{(x-x_2)^2+y^2}
\]

なので、

\[
\psi_{\rm grav}(x,y)
=
-\frac{GM_1}
{\sqrt{(x-x_1)^2+y^2}}
-\frac{GM_2}
{\sqrt{(x-x_2)^2+y^2}}.
\]

---

## 4.2 遠心ポテンシャル

回転軸を \(z\) 軸とすると、

\[
|\boldsymbol{\Omega}\times\mathbf r|^2
=
\Omega^2(x^2+y^2)
\]

である。

遠心力に対応するポテンシャルは

\[
\boxed{
\psi_{\rm cent}
=
-\frac12
|\boldsymbol{\Omega}\times\mathbf r|^2
}
\]

したがって

\[
\boxed{
\psi_{\rm cent}
=
-\frac12
\Omega^2(x^2+y^2)
}
\]

である。

---

## 4.3 有効ポテンシャル全体

以上より、

\[
\boxed{
\psi_{\rm eff}(x,y)
=
-\frac{GM_1}
{\sqrt{(x-x_1)^2+y^2}}
-\frac{GM_2}
{\sqrt{(x-x_2)^2+y^2}}
-\frac12
\Omega^2(x^2+y^2)
}
\]

となる。

---

# 5. 有効力

有効ポテンシャルから得られる加速度は

\[
\boxed{
\mathbf a_{\rm eff}
=
-\nabla\psi_{\rm eff}
}
\]

である。

したがって、速度が 0 の瞬間には
テスト粒子は等ポテンシャル面に対して法線方向に加速する。

等ポテンシャル面は

\[
\psi_{\rm eff}(x,y)
=
{\rm const.}
\]

で定義され、その法線方向は

\[
\nabla\psi_{\rm eff}
\]

である。

したがって粒子の初期加速度は

\[
-\nabla\psi_{\rm eff}
\]

すなわちポテンシャルが低下する方向となる。

---

# 6. 回転座標系での運動方程式

2天体と共に回転する座標系では、有効ポテンシャルからの力に加えてコリオリ力を考える必要がある。

運動方程式は

\[
\boxed{
\ddot{\mathbf r}
=
-\nabla\psi_{\rm eff}
-
2\boldsymbol{\Omega}\times\dot{\mathbf r}
}
\]

である。

---

## 6.1 x 成分

\[
\boxed{
\ddot{x}
=
-\frac{GM_1(x-x_1)}{r_1^3}
-\frac{GM_2(x-x_2)}{r_2^3}
+\Omega^2x
+2\Omega\dot{y}
}
\]

---

## 6.2 y 成分

\[
\boxed{
\ddot{y}
=
-\frac{GM_1y}{r_1^3}
-\frac{GM_2y}{r_2^3}
+\Omega^2y
-2\Omega\dot{x}
}
\]

ここで

\[
r_1
=
\sqrt{(x-x_1)^2+y^2}
\]

\[
r_2
=
\sqrt{(x-x_2)^2+y^2}
\]

である。

---

# 7. コリオリ力

コリオリ加速度は

\[
\boxed{
\mathbf a_{\rm Cor}
=
-2\boldsymbol{\Omega}
\times
\mathbf v
}
\]

である。

\[
\boldsymbol{\Omega}
=
(0,0,\Omega)
\]

\[
\mathbf v
=
(v_x,v_y,0)
\]

とすると、

\[
\boxed{
a_{{\rm Cor},x}
=
2\Omega v_y
}
\]

\[
\boxed{
a_{{\rm Cor},y}
=
-2\Omega v_x
}
\]

となる。

コリオリ力は速度に垂直なので、

\[
\mathbf v\cdot
\mathbf a_{\rm Cor}
=
0
\]

であり、仕事をしない。

したがって、

- 軌道の向きは曲げる
- 速度の大きさを直接変化させない

という性質を持つ。

---

# 8. 初期条件

2次元運動を解くためには、

\[
\boxed{
x_0,\quad
y_0,\quad
v_{x,0},\quad
v_{y,0}
}
\]

の4つが必要である。

初期状態を

\[
\mathbf X_0
=
(x_0,y_0,v_{x,0},v_{y,0})
\]

とする。

静止状態から粒子を放す場合は

\[
v_{x,0}=0,
\qquad
v_{y,0}=0
\]

とする。

---

# 9. L1 点

L1 点は2天体間に存在するラグランジュ点であり、
有効ポテンシャルの鞍点となる。

\(y=0\) 上で

\[
\boxed{
\frac{\partial\psi_{\rm eff}}{\partial x}
=
0
}
\]

を満たす、
\(x_1<x<x_2\) の解を数値的に求める。

具体的には

\[
\frac{\partial\psi_{\rm eff}}{\partial x}
=
\frac{GM_1(x-x_1)}
{|x-x_1|^3}
+
\frac{GM_2(x-x_2)}
{|x-x_2|^3}
-
\Omega^2x
\]

なので、

\[
\boxed{
\frac{GM_1(x-x_1)}
{|x-x_1|^3}
+
\frac{GM_2(x-x_2)}
{|x-x_2|^3}
-
\Omega^2x
=
0
}
\]

を解く。

数値計算では `scipy.optimize.brentq` を用いる。

---

# 10. Roche lobe

L1 点を通る等ポテンシャル面

\[
\boxed{
\psi_{\rm eff}(x,y)
=
\psi_{\rm eff}(L_1)
}
\]

が Roche lobe の境界に対応する。

2次元プロットでは、この等ポテンシャル線を強調して描画する。

---

# 11. Jacobi 定数

2天体と共に回転する座標系で保存される量として Jacobi 定数を考える。

運動方程式

\[
\ddot{\mathbf r}
=
-\nabla\psi_{\rm eff}
-
2\boldsymbol{\Omega}
\times
\dot{\mathbf r}
\]

に \(\dot{\mathbf r}\) を内積すると、

\[
\frac{d}{dt}
\left(
\frac12v^2
+
\psi_{\rm eff}
\right)
=
0
\]

となる。

したがって

\[
\frac12v^2
+
\psi_{\rm eff}
=
{\rm const.}
\]

である。

Jacobi 定数を

\[
\boxed{
C_J
=
-2\psi_{\rm eff}
-
v^2
}
\]

と定義する。

2次元では

\[
\boxed{
C_J
=
-2\psi_{\rm eff}(x,y)
-
(v_x^2+v_y^2)
}
\]

である。

理想的な数値積分では

\[
C_J(t)
=
{\rm const.}
\]

であるため、Jacobi 定数の時間変化を
数値計算精度のチェックとして用いることができる。

---

# 12. Zero-velocity curve

Jacobi 定数より

\[
v^2
=
-2\psi_{\rm eff}
-
C_J
\]

である。

物理的には

\[
v^2\geq0
\]

でなければならないため、

\[
\boxed{
\psi_{\rm eff}
\leq
-\frac{C_J}{2}
}
\]

を満たす領域のみ粒子が到達可能である。

境界

\[
v=0
\]

では

\[
\boxed{
\psi_{\rm eff}
=
-\frac{C_J}{2}
}
\]

となり、これを zero-velocity curve と呼ぶ。

---

## 12.1 L1 との関係

L1 点で静止している粒子に対応する Jacobi 定数は

\[
\boxed{
C_{J,L1}
=
-2\psi_{\rm eff}(L_1)
}
\]

である。

一般に、

\[
C_J>C_{J,L1}
\]

では L1 周辺の通路が閉じ、

\[
C_J<C_{J,L1}
\]

では L1 周辺の通路が開く。

したがって、
一方の Roche lobe からもう一方へ粒子が移動可能かどうかを
Jacobi 定数から判断できる。

---

# 13. 数値積分

運動方程式を1階連立常微分方程式に書き換える。

\[
\mathbf X
=
(x,y,v_x,v_y)
\]

とすると、

\[
\dot{x}=v_x
\]

\[
\dot{y}=v_y
\]

\[
\dot{v}_x
=
-\frac{GM_1(x-x_1)}{r_1^3}
-\frac{GM_2(x-x_2)}{r_2^3}
+\Omega^2x
+2\Omega v_y
\]

\[
\dot{v}_y
=
-\frac{GM_1y}{r_1^3}
-\frac{GM_2y}{r_2^3}
+\Omega^2y
-2\Omega v_x
\]

を解く。

Python では

```python
scipy.integrate.solve_ivp
```
