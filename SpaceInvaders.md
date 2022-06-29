# Space Invaders

​	Aqui é mostrado o modelo de um *framework* que facilita o desenvolvimento de jogos usando como exemplo o o jogo Space Invaders

# Organização do Projeto

* /GameSystem
  * g_system.py
  * input.py
  * collider.py
  * display.py
  * camera.py
  * timer.py
  * sound.py
  * global_vars.py
  * screen_manager.py
* /Bases
  * /Interfaces
    * screen_interface.py
    * sprite_interface.py
    * behavior_interface.py
    * collider_interface.py
    * display_interface.py
    * screen_inteface.py
    * object_interface.py
  * object.py
  * screen.py
  * sprite.py
  * animation.py
  * group.py
* /Behaviors
* /Screens
* /Objects
* /Resouces
  * /Images
  * /Sounds
* main.py

​	O projeto será organizado em pastas, que terão a estrutura apresentada acima. Esta estrutura é composta por um arquivo `main.py`, que será o primeiro código a ser executado, e pelas pastas *GameSystem*, *Bases*, *Behaviors*, *Screens*, *Objects* e *Resources*. Cada uma delas será explicada e detalhada assim como seus arquivos.

​	Para criarmos um projeto de um jogo usando essa organização, utilizaremos somente as pastas *Objects*, *Screens* e *Resources*. Todo as outras não deverão ser editadas, somente utilizadas.

​	Dentro da pasta *Objects*, serão criados todos os objetos do jogo. Eles serão, geralmente, *sprites*. Cada *sprite* diferente será representado como um objeto individual. Internamente, cada objeto conterá todos os seus comportamentos, como animações, movimentação, e colisão com outros objetos. A forma de se criar tudo isso será detalhado adiante.

​	Dentro da pasta *Screens*, serão criadas todas as telas do jogo. As telas serão responsáveis por criar os objetos e se comunicar com o sistema. Nela, os objetos serão declarados em suas posições.

​	Por fim, na pasta *Resources*, serão colocados todasas imagens e sons utilizados no jogo.

# Screen

```python
class Tela(Screen):
    def setup():
        # Criação dos objetos
        # 
        
```

```python
class Screen:
	def setup(): pass
    def mainloop(): pass
    def stop_loop(): pass
```

# GameSystem

## Input

​	Será responsável pela entrada de teclado, mouse e eventos de saída do sistema. A interface de acesso é a seguinte:

```python
class Input:
    def add_key(function, event, key)
    def remove_key(function, event, key)
    def add_click(function, event, button)
    def remove_click(function, event, button)
    def add_double_click(fucntion, event, button)
    def remove_double_click(function, event, button)
    def add_quit_request(function)
    def remove_quit_request(function)
```

## Collider

​	Será responsável pelas colisões entre objetos. Ele é formado por 2 interfaces: a primeira é a do objeto *Collider* e a segunda é a que o objeto que se deseja colidir deve seguir. As duas são listadas a seguir:

```python
class Collider:
    def add_on_collision(obj1, obj2)
    def is_colliding(obj1, obj2) -> bool
```

```python
class Object:
    def get_collider() -> list
    def on_collision(obj)
```

## Display

​	Será responsável pela exibição dos objetos na tela. A interface de acesso é a seguinte:

```python
class Display:
    def add_object(obj)
    def remove_object(obj)
```

```python
class Object:
    def get_surfaces() -> list
```

## Timer

​	Será responsável por controlar o tempo do jogo. A interface é a seguinte:

```python
class Timer:
    def add_clock(time, func)
    def add_clock_once(time, func)
    def add_everytime_clock(func)
    def remove_clock(func)
    def update()
```

​	Esta classe terá ainda o auxílio de outras duas classes: Clock e FunctionList. As duas são detalhadas abaixo:

```python
class Clock:
    def __init__(time)
    def check(delta)
```

```python
class FunctionList:
    def __init__(funcs)
    def add_func(func)
    def remove_func(func)
    def get_funcs() -> list
```