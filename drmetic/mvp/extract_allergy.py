# TODO: 유저가 입력을 했을 때 그 상품이 우리 데이터셋에 있어야 함. 없는 경우는 해당 제품을 저장하는 temp 리스트 만들기

# 1st: 입력된 상품의 name을 sort 방식으로 리스트에서 해당 value를 가진 index를 뽑아내기 
# 2nd: 뽑은 index와 매칭되는 ingredients feature의 row를 찾아 출력하기 
# 3rd:  allergy_list 라는 알레르기 list를 만들고 식약처에서 뽑았던 데이터의 영문 네임을 값으로 집어넣기
# 4th: ingredients[i].loc("성분이름") 의 형태를 for 문을 돌려서 name(상품명)_ingredients_list 라는 새 리스트에 담기
# 5th: set 함수와 pop 함수를 통해  allergy_list와 name_ingredients_list 사이에 중복되는 값이 있으면 그 값을 출력하기 

import pandas as pd

def find_allergens(product_name, dataset, allergy_list):
    # TODO: 유저가 입력을 했을 때 그 상품이 우리 데이터셋에 있어야 함. 없는 경우는 해당 제품을 저장하는 temp 리스트 만들기
    temp_list = []
    try:
        # Find all product names in the dataset that contain the input product_name
        matching_products = dataset[dataset['name'].str.contains(product_name)]
        if matching_products.empty:
            temp_list.append(product_name)
            return f"{product_name} not found in dataset. Added to temp list.", temp_list
        else:
            result_str = ""
            for _, row in matching_products.iterrows():
                product_name = row['name']
                ingredients = row['ingredients']
                name_ingredients_list = []
                for ingredient in ingredients:
                    name_ingredients_list.append(ingredient)

                common_allergens = set(allergy_list).intersection(set(name_ingredients_list))

                if common_allergens:
                    result_str += f"{product_name}: Common allergens found: {', '.join(common_allergens)}\n"
                else:
                    result_str += f"{product_name}: No common allergens found.\n"
            return result_str, temp_list
    except KeyError as e:
        return f"Error: {e}. Please make sure the dataset contains the required columns.", temp_list


