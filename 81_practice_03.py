# write a program to generate multiplication table from 2 to 20 and write it to the differed files . Place these files in a folder for a 13-years old.

for i in range(2,21):
    with open(f"tables/Multiplication_table_of_{i}.txt" , 'w') as f:
        for j in range(1,11):
            f.write(f"{i}x{j}={i*j}")
            if j!=10:
                f.write('\n')



