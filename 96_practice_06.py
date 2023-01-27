# Can you change the self parameters inside a class to something else (say "harry") . Try changing self to "slf" or "harry" and see the effect . 

class Sample:
    def __init__(slf , name):
        slf.name = name

obj = Sample("Sumit")
print(obj.name)        