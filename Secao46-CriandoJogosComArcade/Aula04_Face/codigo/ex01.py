import arcade

tela_largura = 600
tela_altura = 600
titulo = "Exemplo"

def tela():
    arcade.open_window(tela_largura, tela_altura, titulo)
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

def rosto():
    x = 300
    y = 300
    raio = 200
    arcade.draw_circle_filled(x, y, raio, arcade.color.YELLOW)

def olho_direito():
    x = 370
    y = 350
    raio = 20
    arcade.draw_circle_filled(x, y, raio, arcade.color.BLACK)

def olho_esquerdo():
    x = 230
    y = 350
    raio = 20
    arcade.draw_circle_filled(x, y, raio, arcade.color.BLACK)

def boca():
    x = 300
    y = 280
    largura = 120
    altura = 100
    inicio_angulo = 190
    final_angulo = 350
    arcade.draw_arc_outline(x, y, largura, altura, arcade.color.BLACK, inicio_angulo, final_angulo, 10)
    arcade.finish_render()
    arcade.run()


def main():
    tela()
    rosto()
    olho_direito()
    olho_esquerdo()
    boca()

if __name__ == '__main__':
    main()
