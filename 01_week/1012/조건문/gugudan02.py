for i in range(1, 10):
    # 한 줄로 2~9단 출력
    print(
        f"2x{i}={2*i}\t3x{i}={3*i}\t4x{i}={4*i}\t"
        f"5x{i}={5*i}\t6x{i}={6*i}\t7x{i}={7*i}\t"
        f"8x{i}={8*i}\t9x{i}={9*i}"
    )

for i in range(2,10):
    print(f"\n==== {i}단 ===")
    for j in range(1,10):
        print(f"{i} x {j} = {i*j:2}")