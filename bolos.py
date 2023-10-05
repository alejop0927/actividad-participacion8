class Frame:
    def __init__(self):
        self.rolls = []

    def is_strike(self):
        return len(self.rolls) == 1 and sum(self.rolls) == 10

    def is_spare(self):
        return len(self.rolls) == 2 and sum(self.rolls) == 10

    def score(self, next_frame, next_next_frame=None):
        frame_score = sum(self.rolls)
        if self.is_strike():
            if next_frame:
                frame_score += sum(next_frame.rolls)
                if next_frame.is_strike() and next_next_frame:
                    frame_score += next_next_frame.rolls[0]
        elif self.is_spare() and next_frame:
            frame_score += next_frame.rolls[0]
        return frame_score


class BowlingGame:
    def __init__(self):
        self.frames = [Frame() for _ in range(10)]
        self.current_frame = 0

    def roll(self, pins):
        if self.current_frame == 10:
            print("Game over. Cannot roll anymore.")
            return

        frame = self.frames[self.current_frame]
        frame.rolls.append(pins)

        if frame.is_strike() or len(frame.rolls) == 2:
            self.current_frame += 1

    def calculate_score(self):
        total_score = 0
        for i in range(10):
            frame = self.frames[i]
            if i < 8:
                next_frame = self.frames[i + 1]
                next_next_frame = self.frames[i + 2] if not next_frame.is_strike() else None
            elif i == 8:
                next_frame = self.frames[i + 1]
                next_next_frame = None
            else:
                next_frame = None
                next_next_frame = None

            total_score += frame.score(next_frame, next_next_frame)
            print(f"Frame {i+1} score: {total_score}")

        print("Total score:", total_score)


# Ejemplo de uso
game = BowlingGame()
game.roll(10)  # Strike
game.roll(5)   # Segundo frame
game.roll(5)   # Segundo frame
game.roll(9)   # Tercer frame
game.roll(0)   # Tercer frame

game.calculate_score()
