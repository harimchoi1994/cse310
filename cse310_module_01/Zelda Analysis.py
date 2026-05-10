import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 현재 Python 파일이 있는 폴더 기준
folder = Path(__file__).parent

# Zelda 데이터 파일 불러오기
creatures = pd.read_csv(folder / "Creatures.csv")
materials = pd.read_csv(folder / "Material.csv")

print("Zelda Breath of the Wild Data Analysis")
print("--------------------------------------")

print("\nCreatures Data Preview:")
print(creatures.head())

print("\nMaterials Data Preview:")
print(materials.head())


# 질문 1
print("\nQuestion 1: Which creature types recover the most hearts on average?")

creatures_with_hearts = creatures[creatures["Hearts Recovered"] > 0]

creature_avg = creatures_with_hearts.groupby("Type")["Hearts Recovered"].mean()

creature_avg = creature_avg.sort_values(ascending=False)

print(creature_avg)


# 질문 2
print("\nQuestion 2: Which material types recover the most hearts on average?")

materials_with_hearts = materials[materials["Hearts Recovered"] > 0]

material_avg = materials_with_hearts.groupby("Type")["Hearts Recovered"].mean()

material_avg = material_avg.sort_values(ascending=False)

print(material_avg)


# Stretch Challenge: 그래프 만들기
material_avg.plot(kind="bar")
plt.title("Average Hearts Recovered by Material Type")
plt.xlabel("Material Type")
plt.ylabel("Average Hearts Recovered")

plt.tight_layout()
plt.show()