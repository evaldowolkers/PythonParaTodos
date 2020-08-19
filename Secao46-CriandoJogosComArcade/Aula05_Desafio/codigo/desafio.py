import arcade

LARGURA = 800
ALTURA = 600
TITULO = "WingSec"

def criar_tela():
    arcade.open_window(LARGURA, ALTURA, TITULO)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.start_render()

def criar_texto(texto):
    arcade.draw_text(texto, 150, 300, arcade.color.YELLOW, 50)
    arcade.finish_render()
    arcade.run()

def main():
    texto = input("Digite uma frase: ")
    criar_tela()
    criar_texto(texto)

if __name__ == "__main__":
    main()