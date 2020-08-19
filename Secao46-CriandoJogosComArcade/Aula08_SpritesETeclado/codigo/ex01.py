# importando o arcade
import arcade

# Definindo as constantes
LARGURA_JANELA = 800
ALTURA_JANELA = 600
TITULO = "Jogo de Nave"
ESCALA = 1.0

# Definindo as Classes
class FlyingSprite(arcade.Sprite):
    """Classe base para nosso sprite
    """

    def update(self):
        """Atualiza a posição do sprite
        """

        # Move o sprite
        super().update()

class Game(arcade.Window):
    """Nesse jogo vamos movimentar
    nosso sprite dentro da área da janela
    """

    def __init__(self, width: int, height: int, title: str):
        """Inicializa o jogo
        """
        super().__init__(width, height, title)

        # Limpa a lista de sprites
        self.all_sprites = arcade.SpriteList()

    def setup(self):
        """Prepara o jogo
        """

        # Define a cor de fundo
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Configura o player (nave)
        self.player = arcade.Sprite("images/nave.png", ESCALA)
        self.player.center_y = self.height / 2
        self.player.left = 10
        self.all_sprites.append(self.player)
        self.paused = False

    def on_key_press(self, symbol: int, modifiers: int):
        """Manipular a entrada do teclado
        Q: Sai do jogo
        P: Pausa o Jogo
        Setas: Move para cima, para a esquerda,
        para baixo e para a direita

        Argumentos:
            symbol {int} -- Qual tecla foi pressionada
            modifiers {int} -- Quais modificadores foram
             pressionados (shift, ctrl, alt)
        """
        if symbol == arcade.key.Q:
            arcade.close_window()

        if symbol == arcade.key.P:
            self.paused = not self.paused

        if symbol == arcade.key.UP:
            self.player.change_y = 250

        if symbol == arcade.key.DOWN:
            self.player.change_y = -250

        if symbol == arcade.key.LEFT:
            self.player.change_x = -250

        if symbol == arcade.key.RIGHT:
            self.player.change_x = 250

    def on_key_release(self, symbol: int, modifiers: int):
        """Desfazer os vetores de movimento quando as
        teclas de movimento são liberadas

        Arguments:
            symbol {int} -- Qual tecla foi pressionada
            modifiers {int} -- Quais modificadores foram
             pressionados (shift, ctrl, alt)
        """
        if (symbol == arcade.key.UP or
                symbol == arcade.key.DOWN):
            self.player.change_y = 0

        if (symbol == arcade.key.LEFT or
                symbol == arcade.key.RIGHT):
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        """Atualiza as posições e status dos objetos
        do jogo. Se estiver em pausa, não faz nada

        Argumentos:
            delta_time {float} -- Tempo deste a última atualização
        """

        # Se o jogo estiver em pausa, não fazer nada
        if self.paused:
            return

        # Atualiza todos sprites
        for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )

    def on_draw(self):
        """Desenha os objetos do jogo
        """

        arcade.start_render()
        self.all_sprites.draw()
        if self.paused:
            arcade.draw_text("EM PAUSA", 120, 0,
                             arcade.color.BRICK_RED, 100)


if __name__ == "__main__":
    jogo = Game(
        int(LARGURA_JANELA * ESCALA),
        int(ALTURA_JANELA * ESCALA),
        TITULO
    )
    jogo.setup()
    arcade.run()
