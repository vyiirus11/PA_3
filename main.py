import argparse
import time


def parse_input(path):
    with open(path, "r") as f:
        k = int(f.readline().strip())
        weights = {}

        for _ in range(k):
            char, value = f.readline().split()
            weights[char] = int(value)

        a = f.readline().strip()
        b = f.readline().strip()

    return a, b, weights


def hvlcs(a, b, weights):
    n = len(a)
    m = len(b)

    # dp[i][j] = maximum value of a common subsequence
    # using a[:i] and b[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + weights[a[i - 1]]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # backtrack to rebuild one optimal subsequence
    i = n
    j = m
    subsequence = []

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1] and dp[i][j] == dp[i - 1][j - 1] + weights[a[i - 1]]:
            subsequence.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    subsequence.reverse()
    return dp[n][m], "".join(subsequence)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to input file")
    parser.add_argument("-t", "--time", action="store_true", help="print runtime")
    parser.add_argument(
        "-m",
        "--multiplier",
        type=int,
        default=1,
        help="repeat both strings this many times for timing experiments",
    )
    args = parser.parse_args()

    a, b, weights = parse_input(args.path)

    a = a * args.multiplier
    b = b * args.multiplier

    start = time.perf_counter()
    value, subsequence = hvlcs(a, b, weights)
    end = time.perf_counter()

    print(value)
    print(subsequence)

    if args.time:
        print(f"Time: {end - start:.6f} seconds")


if __name__ == "__main__":
    main()