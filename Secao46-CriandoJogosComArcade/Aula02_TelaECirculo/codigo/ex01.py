import arcade

largura_tela = 600
altura_tela = 600
titulo = "Exemplo"
arcade.open_window(largura_tela, altura_tela, titulo)
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()
arcade.finish_render()
arcade.run()