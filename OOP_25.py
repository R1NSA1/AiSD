class DecimalFraction:
    def __init__(self, wholepart, fractionalpart):
        self.wholepart = wholepart
        self.fractionalpart = fractionalpart

    def sum(self, other):
        newwholepart = self.wholepart + other.wholepart
        newfractionalpart = self.fractionalpart
        return DecimalFraction(newwholepart, newfractionalpart)

    def diff(self, other):
        newwholepart = self.wholepart - other.wholepart
        newfractionalpart = self.fractionalpart - other.fractionalpart
        return DecimalFraction(newwholepart, newfractionalpart)

    def сomposition(self, other):
        newwholepart = self.wholepart * other.wholepart
        newfractionalpart = self.fractionalpart * other.fractionalpart
        return DecimalFraction(newwholepart, newfractionalpart)

    def quotient(self, other):
        newwholepart = self.wholepart / other.wholepart
        newfractionalpart = self.fractionalpart / other.fractionalpart
        return DecimalFraction(newwholepart, newfractionalpart)


df1 = DecimalFraction(1, 10)
df2 = DecimalFraction(1, 10)

result_sum = df1.sum(df2)
print(f"Сумма: {result_sum.wholepart}/{result_sum.fractionalpart} ")

result_diff = df1.diff(df2)
print(f"Разность: {result_diff.wholepart}/{result_diff.fractionalpart}")

result_composition = df1.сomposition(df2)
print(f"Произведение: {result_composition.wholepart}/{result_composition.fractionalpart}")

result_quotient = df1.quotient(df2)
print(f"Частное: {result_quotient.wholepart}/{result_quotient.fractionalpart}")


