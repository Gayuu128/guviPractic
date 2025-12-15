total = 10

count = 0

for rs1 in range(0, total + 1):
    for rs2 in range(0, total // 2 + 1):
        for rs5 in range(0, total // 5 + 1):
            for rs10 in range(0, total // 10 + 1):
                if (rs1*1 + rs2*2 + rs5*5 + rs10*10) == total:
                    print("1Rs:", rs1,
                          "2Rs:", rs2,
                          "5Rs:", rs5,
                          "10Rs:", rs10)
                    count = count + 1

print("Total ways:", count)
