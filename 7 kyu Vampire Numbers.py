def vampire_test(x, y):
    pass


print(vampire_test(21, 6) == True, "Basic: 21 * 6 = 126 should return True")
print(vampire_test(204, 615) == True, "Basic: 204 * 615 = 125460 should return True")
print(vampire_test(30, -51) == True, "One Negative: 30 * -51 = -1530 should return True")
print(vampire_test(-246, -510) == False,
      "Double Negatives: -246 * -510 = 125460 should return False (The negative signs aren't present on the product)")
print(vampire_test(210, 600) == True, "Trailing Zeroes: 210 * 600 = 126000 should return True")
