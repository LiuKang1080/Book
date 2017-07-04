
from random import randint


class Game():


    def __init__(self):

        self.attempts = 1
        self.max_attempts = 8
        self.secret = self.set_secret_combo()


    def compare_combos(self, attempt, secret):

        secret_copy = secret[:]
        attempt_copy = attempt[:]
        
        full = 0
        partial = 0

        for i in range(4):
            if attempt_copy[i] == secret_copy[i]:
                secret_copy[i] = 'x'
                attempt_copy[i] = 'x'
                full += 1

        for i in range(4):
            if secret_copy[i] != 'x':
                for j in range(4):
                    if attempt_copy[j] != 'x':
                        if secret_copy[i] == attempt_copy[j]:
                            secret_copy[i] = 'x'
                            attempt_copy[j] = 'x'
                            partial += 1

        self.attempts += 1

        return [full, partial]


    def set_secret_combo(self):

        secret = list()
        
        for _ in range(4):
            secret.append(randint(1, 8))

        return secret
            


def main():

    game = Game()

    secret = game.set_secret_combo()
    attempt = secret
    print(secret)
    print(attempt)
    print(game.compare_combos(secret, attempt))

    secret = game.set_secret_combo()
    attempt = secret[::-1]
    print(secret)
    print(attempt)
    print(game.compare_combos(secret, attempt))

    secret = game.set_secret_combo()
    attempt = [8, 4, 3, 3]
    print(secret)
    print(attempt)
    print(game.compare_combos(secret, attempt))

    secret = game.set_secret_combo()
    attempt = [1, 6, 8, 2]
    print(secret)
    print(attempt)
    print(game.compare_combos(secret, attempt))            

    

if __name__ == '__main__':
    main()
