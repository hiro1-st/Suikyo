import streamlit as st

# 分別ルールの辞書
garbage_categories = {
    "紙": "資源ごみ",
    "段ボール": "資源ごみ",
    "ペットボトル": "資源ごみ",
    "アルミ缶": "資源ごみ",
    "ガラス瓶": "資源ごみ",
    "プラスチック": "資源ごみ",
    "食べ残し": "燃えるごみ",
    "野菜くず": "燃えるごみ",
    "肉骨": "燃えるごみ",
    "ティッシュ": "燃えるごみ",
    "電子機器": "燃えないごみ",
    "金属": "燃えないごみ",
    "電池": "燃えないごみ",
    "ガラス": "燃えないごみ",
    "石": "燃えないごみ",
    "割れた食器": "燃えないごみ",
    "タバコの吸い殻": "燃えないごみ",
}

# タイトル
st.title("ごみの分別アプリ")

# アイテム名を入力させる
item = st.text_input("分別したいごみのアイテム名を入力してください:")

# アイテムが入力された場合
if item:
    # 分別の判断
    item_lower = item.lower()
    found_category = None
    for key in garbage_categories:
        if key.lower() in item_lower:
            found_category = garbage_categories[key]
            break
    
    if found_category:
        st.success(f"「{item}」は「{found_category}」に分類されます。")
    else:
        st.error(f"「{item}」の分類が見つかりませんでした。")