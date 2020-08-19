import arcade

arcade.open_window(600, 600, "Exemplo")
arcade.set_background_color(arcade.color.SKY_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 600, 250, 0, arcade.color.DARK_GREEN)
arcade.draw_circle_filled(5, 590, 60, arcade.color.YELLOW)
arcade.draw_lrtb_rectangle_filled(20, 37, 300, 220, arcade.color.DARK_BROWN)
arcade.draw_circle_filled(28, 300, 30, arcade.color.DARK_GREEN)
arcade.draw_text("WingSec", 158, 155, arcade.color.BRICK_RED, 50)
arcade.finish_render()
arcade.run()