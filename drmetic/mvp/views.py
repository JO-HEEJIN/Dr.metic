from django.http import HttpResponse
from django.shortcuts import render
from .extract_allergy import find_allergens

import pandas as pd 


allergy_list_ko = ['아밀신남알', '벤질알코올', '신나밀알코올', '시트랄', '유제놀', '하이드록시시트로넬알', '아이소유제놀', '아밀신나밀알코올', '벤질살리실레이트', '신남알', '쿠마린', '제라니올', '아니스알코올', '벤질신나메이트', '파네솔', '부틸페닐메틸프로피오날', '리날룰', '벤질벤조에이트', '시트로넬올', '헥실신남알', '리모넨', '메틸 2-옥티노에이트', '알파-아이소메틸아이오논', '참나무이끼추출물', '나무이끼추출물']


def search_view(request):
    query = request.GET.get('q')
    result = ""
    if query:
        sephora_data = pd.read_csv("/Users/mac/git/cosmetic/sephora_website_dataset.csv")
        allergy_list = ['Amyl cinnamal', 'Benzyl alcohol', 'Cinnamyl alcohol', 'Citral', 'Eugenol', 'Hydroxycitronellal', 'Isoeugenol', 'Amylcinnamyl alcohol', 'Benzyl salicylate', 'Cinnamal', 'Coumarin', 'Geraniol', 'Anisyl alcohol', 'Benzyl cinnamate', 'Farnesol', 'Butylphenyl methylpropional', 'Linalool', 'Benzyl benzoate', 'Citronellol', 'Hexyl cinnamal', 'Limonene', 'Methyl 2-octynoate', 'Alpha-isomethyl ionone', 'Evernia prunastri extract (Oakmoss)', 'Evernia furfuracea extract (Treemoss)']
        result, _ = find_allergens(query, sephora_data, allergy_list)
    return render(request, 'search.html', {'result': result})