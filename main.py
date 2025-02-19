import pygame, math, time
# import settings
import scripts.player, scripts.enemies


def play(screen):
    doroga_data = pygame.image.load('data/doroga.png')
    doroga_raz = doroga_data.get_width()

    font = pygame.font.Font(None, 64)
    count = 0

    sd = False
    gameover = False

    q = math.ceil(screen.get_width() / doroga_raz) + 1
    scroll = 0

    player = scripts.player.Player()
    player.rect.y = screen.get_height() // 2
    player_group = pygame.sprite.Group()
    player_group.add(player)

    enemy_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_timer, 1000)

    clock = pygame.time.Clock()

    while not sd:
        while not gameover and not sd:

            events = pygame.event.get()
            keys = pygame.key.get_pressed()

            for i in range(0, q):
                screen.blit(doroga_data, (i * doroga_raz + scroll, 0))
            scroll -= 2
            if abs(scroll) > doroga_raz:
                scroll = 0

            for event in events:
                if event.type == pygame.QUIT:
                    sd = True
                if event.type == enemy_timer:
                    scripts.enemies.Enemy(player.rect.y)

            if keys[pygame.K_UP]:
                player.to_up()
            elif keys[pygame.K_DOWN]:
                player.to_down()

            if player.check_coll(scripts.enemies.enemies_group):
                gameover = True

            count += player.update_count(scripts.enemies.enemies_group)

            text = font.render(f"Points {count}", True, (0, 0, 0))

            text_rect = text.get_rect(x=70, y=40)

            player_group.update()
            scripts.enemies.enemies_group.update()

            screen.blit(text, text_rect)
            player_group.draw(screen)
            scripts.enemies.enemies_group.draw(screen)


            pygame.display.update()

        if gameover:
            [e.kill() for e in scripts.enemies.enemies_group]

            gameover_img = pygame.image.load('data/over.jpeg')
            gameover_img = pygame.transform.scale(gameover_img, (1280, 720))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sd = True
                if event.type == 1025:
                    gameover = False
                    player = None
                    play(screen)

            screen.blit(gameover_img, (0, 0))
            pygame.display.update()


def main():
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Game')

    play(screen)


if __name__ == '__main__':
    main()
