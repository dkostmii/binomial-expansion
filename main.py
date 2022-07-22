from math import factorial


a_term = "a"
b_term = "b"


def coeffs(n: int) -> list[int]:
    coeffs: list[int] = []
    factorial_n = factorial(n)
    factorial_k = 1

    for k in range(n + 1):
        if (k > 0):
            factorial_k *= k

        # calculate the binomial coefficient
        # n choose k = n! / k! * (n - k)!
        coefficient = int(factorial_n / (factorial_k * factorial(n - k)))
        coeffs.append(coefficient)

    return coeffs


def powers(n: int) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []

    for i in range(n + 1):
        # make list of powers
        # a^n * b^0 + a^(n-1) * b^1 + ... + a^0 * b^n
        result.append( (n - i, i) )

    return result


# represents term for coefficient,
# a power and b power given
def repr_terms(coeff: int, a: int, b: int) -> str:
    # return f'{coeff} * {a_term}^{a} * {b_term}^{b}'

    buffer: list[str] = []

    if (coeff > 1):
        buffer.append(f'{coeff}')
    elif (coeff == 0):
        return ''

    if (a == 1):
        buffer.append(f'{a_term}')
    elif (a > 0):
        buffer.append(f'{a_term}^{a}')

    if (b == 1):
        buffer.append(f'{b_term}')
    elif (b > 0):
        buffer.append(f'{b_term}^{b}')

    return " * ".join(buffer)


def expansion(n: int) -> str:
    cs = coeffs(n)
    pwr = powers(n)
    result: str = f'({a_term} + {b_term})^{n} = '
    buffer: list[str] = []

    if (len(cs) != len(pwr)):
        raise Exception(f'Expected cs and pwr to have same length. Got len(cs) = {len(cs)}; len(pwr) = {len(pwr)}')

    for coeff, pwrs in zip(cs, pwr):
        a, b = pwrs

        buffer.append(repr_terms(coeff, a, b))

    result += " + ".join(buffer)
    return result


def main():
    print(expansion(3))


if __name__ == "__main__":
    main()