import arcade

largura_tela = 600
altura_tela = 600
titulo = "Exemplo"
raio = 150
arcade.open_window(largura_tela, altura_tela, titulo)
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()
arcade.draw_circle_filled(300, 300, raio, arcade.color.ROSE_GOLD)
arcade.finish_render()
arcade.run()