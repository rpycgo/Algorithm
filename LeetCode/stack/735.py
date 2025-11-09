class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            alive = True

            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()

                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()

                alive = False

                break

            if alive:
                stack.append(asteroid)

        return stack
