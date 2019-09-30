import random


class Base_info:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor


class Player(Base_info):

    def attack(self, enemy):
        enemy.health = enemy.health - self._damage(enemy)
        return \
            '{} наносит: {} ед. урона\n' \
            'Здоровье {}: {} ед. \n' \
            'Здоровье {}: {} ед.'.format(self.name, self._damage(enemy),
                                         self.name, self.health, enemy.name,
                                         enemy.health)

    def _damage(self, enemy):
        percent_armor = enemy.armor - 1
        damage_after = int(self.damage - (self.damage * percent_armor))
        return damage_after


class Enemy(Player):
    pass


class Fight:

    def round(self, player, enemy):
        round_count = 0
        while player.health > 0 and enemy.health > 0:
            round_count += 1
            print('Round: {}'.format(round_count))
            rand = random.randint(1, 2)
            if rand == 1:
                print(player.attack(enemy))
                answer = input('Нажмите q для выхода, для перехода в следующий раунд: Enter.')
                if answer == 'q':
                    break
            else:
                print(enemy.attack(player))
                answer = input('Нажмите q для выхода, для перехода в следующий раунд: Enter.')
                if answer == 'q':
                    break
        if player.health <= 0:
            print('{} - Потерпел поражение.'.format(player.name))
        else:
            print('{} - Одержал победу!'.format(player.name))


player = Player(input('Дайте игроку имя: '), 100, 18, 1.5)
enemy = Enemy(input('Назовите своего врага: '), 100, 32, 1.1)
fight = Fight()

fight.round(player, enemy)
