"""Generates a SYNTHETIC EV market dataset (replace with your real data if you have it)."""
import csv, random
random.seed(42)
MAKERS = {"Tesla":"USA","BYD":"China","Hyundai":"South Korea","Volkswagen":"Germany","Tata Motors":"India",
          "Nissan":"Japan","Kia":"South Korea","BMW":"Germany","NIO":"China","Ola Electric":"India"}
CATS = {"Hatchback":(35,60,300,0.7),"Sedan":(55,90,450,1.0),"SUV":(60,110,480,1.2),
        "Bus":(150,300,250,0.2),"Truck":(100,250,300,0.25),"Two-Wheeler":(2,8,120,2.0)}
BATT = ["LFP","NMC","NCA","Sodium-Ion","Solid-State"]
W = [0.38,0.34,0.14,0.08,0.06]
rows = []
for year in range(2021, 2026):
    for maker, country in MAKERS.items():
        for cat,(lo,hi,rng,vol) in CATS.items():
            if random.random() < 0.25: continue
            b = random.choices(BATT, W)[0]
            cap = round(random.uniform(lo,hi),1)
            growth = 1 + (year-2021)*random.uniform(0.1,0.35)
            rows.append([year,maker,f"{maker} {cat} {random.randint(1,9)}",cat,b,cap,
                round(rng*random.uniform(.8,1.3)*(cap/((lo+hi)/2))**.3),
                round(cap*random.uniform(450,800)*(1.6 if cat in("Bus","Truck") else 1)),
                int(random.uniform(2000,90000)*vol*growth),
                round(random.uniform(3.4,4.9),1), country])
with open("data/ev_dataset.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["Year","Manufacturer","Model","Category","Battery_Type","Battery_Capacity_kWh",
                "Range_km","Price_USD","Annual_Sales","Customer_Rating","Manufacturing_Country"])
    w.writerows(rows)
print(len(rows),"rows written")
