import re


def sum_profit(text: str):
    def generator_numbers():
        number = re.findall(r"\d+\.\d+", text)
        for num in number:
            yield float(num)
    return sum(generator_numbers())


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text)
print(f"Загальний дохід: {total_income}")