import arcade

LARGURA = 600
ALTURA = 800
TITULO = "Bem-vindo ao Arcade"
RAIO = 150

class Jogo(arcade.Window):
    # Vamos adicionar duas variáveis para armazenar
    # as coordenadas x e y
    x = 0
    y = 0

    def __init__(self):
        super().__init__(LARGURA, ALTURA, TITULO)

        arcade.set_background_color(arcade.color.BLUE)

    def on_draw(self):
        arcade.start_render()

        # No exemplo anterior o valor de x e y eram fixos,
        # Desenhando o círculo no centro da tela
        # Agora vamos desenhar o círculo usando as
        # variáveis x e y que iniciam com zero.
        arcade.draw_circle_filled(
            self.x, self.y, RAIO, arcade.color.YELLOW
        )

        # Após desenhar o círculo, incrementamos x e y
        self.x += 1
        self.y += 1

        if(self.x == 800):
            self.x = 0
            self.y = 0

if __name__ == "__main__":
    app = Jogo()
    arcade.run()