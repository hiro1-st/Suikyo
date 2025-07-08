import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# ページ設定
st.set_page_config(
    page_title="4ページWebアプリ",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# カスタムCSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    
    .page-header {
        background: linear-gradient(90deg, #56ccf2 0%, #2f80ed 100%);
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        color: white;
    }
    
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #4299e1;
        margin-bottom: 1rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        color: white;
        margin-bottom: 1rem;
    }
    
    .stButton > button {
        width: 100%;
        height: 3rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .nav-button {
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# セッション状態の初期化
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False
if 'visitor_count' not in st.session_state:
    st.session_state.visitor_count = 142

# サイドバーナビゲーション
st.sidebar.markdown("""
<div class="main-header">
    <h2>🌟 Navigation</h2>
    <p>ページを選択してください</p>
</div>
""", unsafe_allow_html=True)

# ナビゲーションボタン
nav_buttons = {
    'home': {'label': '🏠 ホーム', 'color': '#56ccf2'},
    'about': {'label': '👥 会社について', 'color': '#6c5ce7'},
    'services': {'label': '🚀 サービス', 'color': '#00b894'},
    'contact': {'label': '📞 お問い合わせ', 'color': '#fd79a8'}
}

for page_key, page_info in nav_buttons.items():
    if st.sidebar.button(page_info['label'], key=f"nav_{page_key}"):
        st.session_state.page = page_key
        st.rerun()

# 現在のページ表示
st.sidebar.markdown(f"""
<div style="background: #e8f4f8; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
    <strong>現在のページ:</strong><br>
    {nav_buttons[st.session_state.page]['label']}
</div>
""", unsafe_allow_html=True)

# 訪問者カウンター
st.sidebar.markdown(f"""
<div style="background: #fff3cd; padding: 1rem; border-radius: 8px; margin-top: 1rem;">
    <strong>📊 訪問者数:</strong><br>
    <span style="font-size: 1.5rem; color: #e67e22;">{st.session_state.visitor_count:,}</span>
</div>
""", unsafe_allow_html=True)

# メイン関数
def main():
    # ヘッダー
    st.markdown("""
    <div class="main-header">
        <h1>🌟 Streamlit Multi-Page Application</h1>
        <p>インタラクティブな4ページWebアプリケーション</p>
    </div>
    """, unsafe_allow_html=True)
    
    # ページルーティング
    if st.session_state.page == 'home':
        show_home_page()
    elif st.session_state.page == 'about':
        show_about_page()
    elif st.session_state.page == 'services':
        show_services_page()
    elif st.session_state.page == 'contact':
        show_contact_page()

def show_home_page():
    st.markdown("""
    <div class="page-header">
        <h2>🏠 ホームページ</h2>
        <p>Streamlitアプリケーションへようこそ！</p>
    </div>
    """, unsafe_allow_html=True)
    
    # メトリクス表示
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📈 総プロジェクト数", "127", "12")
    
    with col2:
        st.metric("👥 アクティブユーザー", "1,234", "234")
    
    with col3:
        st.metric("🚀 デプロイ数", "89", "7")
    
    with col4:
        st.metric("⭐ 満足度", "4.8/5", "0.2")
    
    # 機能紹介
    st.markdown("## 🎯 主な機能")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>📊 データ可視化</h3>
            <p>Plotlyを使用したインタラクティブなグラフとチャート</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>🎨 カスタマイズ可能</h3>
            <p>柔軟なレイアウトとスタイリングオプション</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>⚡ 高速処理</h3>
            <p>効率的なデータ処理とリアルタイム更新</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>📱 レスポンシブ</h3>
            <p>モバイルフレンドリーなデザイン</p>
        </div>
        """, unsafe_allow_html=True)
    
    # サンプルチャート
    st.markdown("## 📈 サンプルダッシュボード")
    
    # データ生成
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    data = pd.DataFrame({
        'date': dates,
        'visitors': np.random.randint(100, 1000, len(dates)),
        'revenue': np.random.randint(1000, 10000, len(dates))
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = px.line(data, x='date', y='visitors', title='日別訪問者数')
        fig1.update_layout(height=300)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = px.bar(data.tail(30), x='date', y='revenue', title='月末売上推移')
        fig2.update_layout(height=300)
        st.plotly_chart(fig2, use_container_width=True)

def show_about_page():
    st.markdown("""
    <div class="page-header">
        <h2>👥 会社について</h2>
        <p>私たちの会社とビジョンをご紹介します</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 会社概要
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("## 🎯 私たちのミッション")
        st.write("""
        私たちは最先端の技術を使って、データサイエンスとWebアプリケーション開発の分野で
        革新的なソリューションを提供しています。Streamlitを活用することで、
        複雑なデータ分析を直感的で使いやすいインターフェースで提供します。
        """)
        
        st.markdown("## 📊 会社データ")
        company_data = {
            '項目': ['設立年', '従業員数', 'オフィス数', 'プロジェクト数'],
            '値': [2020, 45, 3, 127],
            '前年比': ['-', '+15%', '+50%', '+23%']
        }
        df_company = pd.DataFrame(company_data)
        st.dataframe(df_company, use_container_width=True)
    
    with col2:
        st.markdown("## 🏆 実績")
        achievements = [
            "🥇 Best Startup Award 2023",
            "🌟 Innovation Prize 2024",
            "📈 Growth Company Award",
            "👥 Best Workplace 2024"
        ]
        
        for achievement in achievements:
            st.success(achievement)
    
    # チーム情報
    st.markdown("## 👨‍💼 チーム構成")
    
    team_data = {
        'department': ['開発', '営業', 'マーケティング', '管理'],
        'members': [20, 10, 8, 7]
    }
    
    fig = px.pie(team_data, values='members', names='department', 
                 title='部署別人員構成')
    st.plotly_chart(fig, use_container_width=True)
    
    # タイムライン
    st.markdown("## 📅 会社の歴史")
    
    timeline_data = {
        '年': [2020, 2021, 2022, 2023, 2024],
        '出来事': [
            '会社設立',
            '初のWebアプリリリース',
            'シリーズA資金調達',
            '海外展開開始',
            'AI機能統合'
        ],
        '従業員数': [5, 15, 25, 35, 45]
    }
    
    fig = px.line(timeline_data, x='年', y='従業員数', 
                  title='従業員数の推移', markers=True)
    st.plotly_chart(fig, use_container_width=True)

def show_services_page():
    st.markdown("""
    <div class="page-header">
        <h2>🚀 サービス</h2>
        <p>私たちが提供するサービスの詳細</p>
    </div>
    """, unsafe_allow_html=True)
    
    # サービス選択
    service_tabs = st.tabs(["💻 Web開発", "📱 モバイル", "🤖 AI/ML", "☁️ クラウド"])
    
    with service_tabs[0]:
        st.markdown("### 💻 Webアプリケーション開発")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **主要技術:**
            - Streamlit
            - Django/Flask
            - React/Vue.js
            - FastAPI
            """)
            
            st.markdown("""
            **特徴:**
            - 高速開発
            - レスポンシブデザイン
            - SEO最適化
            - 保守性の高いコード
            """)
        
        with col2:
            # プロジェクト例
            projects = pd.DataFrame({
                'プロジェクト': ['ECサイト', 'ダッシュボード', 'CRM', 'LMS'],
                '期間(月)': [6, 3, 8, 5],
                '技術': ['Django', 'Streamlit', 'FastAPI', 'Flask'],
                '満足度': [4.8, 4.9, 4.7, 4.6]
            })
            
            fig = px.scatter(projects, x='期間(月)', y='満足度', 
                           size='満足度', color='技術', 
                           hover_data=['プロジェクト'])
            st.plotly_chart(fig, use_container_width=True)
    
    with service_tabs[1]:
        st.markdown("### 📱 モバイルアプリ開発")
        
        mobile_stats = {
            'プラットフォーム': ['iOS', 'Android', 'Cross-platform'],
            'プロジェクト数': [25, 30, 20],
            'ダウンロード数': [150000, 200000, 100000]
        }
        
        fig = px.bar(mobile_stats, x='プラットフォーム', y='プロジェクト数',
                     title='プラットフォーム別プロジェクト数')
        st.plotly_chart(fig, use_container_width=True)
    
    with service_tabs[2]:
        st.markdown("### 🤖 AI・機械学習")
        
        # AIサービスの実演
        st.markdown("#### 🔮 予測モデルデモ")
        
        # 簡単な予測デモ
        input_value = st.slider("入力値", 0, 100, 50)
        
        # 簡単な予測計算（実際にはMLモデルを使用）
        prediction = input_value * 1.5 + np.random.normal(0, 5)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("予測値", f"{prediction:.2f}")
        with col2:
            st.metric("信頼度", f"{np.random.uniform(0.8, 0.95):.2%}")
    
    with service_tabs[3]:
        st.markdown("### ☁️ クラウドサービス")
        
        cloud_services = {
            'サービス': ['AWS', 'Azure', 'GCP', 'その他'],
            '利用率': [40, 30, 25, 5]
        }
        
        fig = px.pie(cloud_services, values='利用率', names='サービス',
                     title='クラウドサービス利用率')
        st.plotly_chart(fig, use_container_width=True)

def show_contact_page():
    st.markdown("""
    <div class="page-header">
        <h2>📞 お問い合わせ</h2>
        <p>お気軽にお問い合わせください</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📧 お問い合わせフォーム")
        
        with st.form("contact_form"):
            name = st.text_input("お名前 *", placeholder="山田太郎")
            email = st.text_input("メールアドレス *", placeholder="example@email.com")
            
            inquiry_type = st.selectbox(
                "お問い合わせ種別",
                ["一般的なお問い合わせ", "サービスについて", "技術的な質問", "採用について", "その他"]
            )
            
            subject = st.text_input("件名", placeholder="お問い合わせの件名")
            message = st.text_area("メッセージ *", placeholder="お問い合わせ内容をご記入ください", height=150)
            
            submitted = st.form_submit_button("📤 送信", use_container_width=True)
            
            if submitted:
                if name and email and message:
                    st.success("✅ お問い合わせありがとうございました！担当者からご連絡いたします。")
                    st.balloons()
                    
                    # お問い合わせ情報の表示
                    st.markdown("**送信された内容:**")
                    st.write(f"**名前:** {name}")
                    st.write(f"**メール:** {email}")
                    st.write(f"**種別:** {inquiry_type}")
                    st.write(f"**件名:** {subject}")
                    st.write(f"**メッセージ:** {message}")
                    
                else:
                    st.error("❌ 必須項目をすべて入力してください。")
    
    with col2:
        st.markdown("### 📍 会社情報")
        
        company_info = {
            "🏢 会社名": "株式会社テックソリューション",
            "📍 住所": "東京都渋谷区渋谷1-1-1",
            "📞 電話": "03-1234-5678",
            "📧 メール": "info@techsolution.co.jp",
            "🕒 営業時間": "平日 9:00-18:00",
            "🌐 Website": "https://techsolution.co.jp"
        }
        
        for key, value in company_info.items():
            st.markdown(f"**{key}**  \n{value}")
        
        st.markdown("### 📊 お問い合わせ統計")
        
        # 月別お問い合わせ数のグラフ
        months = ['1月', '2月', '3月', '4月', '5月', '6月']
        inquiries = [23, 35, 28, 42, 38, 51]
        
        fig = px.bar(x=months, y=inquiries, title='月別お問い合わせ数')
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
        
        # レスポンス時間
        st.metric("平均レスポンス時間", "2.4時間", "-0.3時間")

# アプリケーション実行
if __name__ == "__main__":
    main()

# フッター
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>© 2024 Streamlit Multi-Page App. All rights reserved.</p>
    <p>Made with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)