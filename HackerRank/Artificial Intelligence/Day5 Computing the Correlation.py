import sys


def main():
    data = sys.stdin.read().split()

    if not data:
        return

    n = int(data[0])

    mathematics_sum = physics_sum = chemistry_sum = 0.0
    mathematics_sum2 = physics_sum2 = chemistry_sum2 = 0.0
    mathematics_physics_sum = physics_chemistry_sum = chemistry_mathematics_sum = 0.0

    for i in range(n):
        idx = 1 + i*3

        mathematics_score = float(data[idx])
        physics_score = float(data[idx+1])
        chemistry_score = float(data[idx+2])

        mathematics_sum += mathematics_score
        physics_sum += physics_score
        chemistry_sum += chemistry_score

        mathematics_sum2 += mathematics_score * mathematics_score
        physics_sum2 += physics_score * physics_score
        chemistry_sum2 += chemistry_score * chemistry_score

        mathematics_physics_sum += mathematics_score * physics_score
        physics_chemistry_sum += physics_score * chemistry_score
        chemistry_mathematics_sum += chemistry_score * mathematics_score


    def corr(sz, s_x, s_y, s_x2, s_y2, s_xy):
        numerator = (sz * s_xy) - (s_x * s_y)
        denomiator = (
            (sz * s_x2 - s_x**2) *
            (sz * s_y2 - s_y**2)
        ) ** 0.5

        if denomiator == 0:
            return 0.0

        return numerator / denomiator

    corr_mp = corr(
        n,
        mathematics_sum, physics_sum,
        mathematics_sum2, physics_sum2,
        mathematics_physics_sum,
    )
    corr_pc = corr(
        n,
        physics_sum, chemistry_sum,
        physics_sum2, chemistry_sum2,
        physics_chemistry_sum,
    )
    corr_cm = corr(
        n,
        chemistry_sum, mathematics_sum,
        chemistry_sum2, mathematics_sum2,
        chemistry_mathematics_sum,
    )

    print(f'{corr_mp:.2f}')
    print(f'{corr_pc:.2f}')
    print(f'{corr_cm:.2f}')


if __name__ == '__main__':
    main()
