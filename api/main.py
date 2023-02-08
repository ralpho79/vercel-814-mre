import csv

def list_to_csv(list,name):
    
    with open(name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(list)


if __name__ == "__main__":
    my_bands=["Foo Fighters", "The Killers", "Greta Van Fleet"]
    list_to_csv(my_bands,"example.csv")
