import streamlit as st
import google.generativeai as genai

# إعداد الصفحة
st.set_page_config(page_title="مساعد مصطفى الذكي", layout="centered")

# إدخال الـ API Key 
# ملحوظة: لما تشغله على Streamlit هنعلمك تحط المفتاح في مكان آمن
API_KEY = "حط_المفتاح_بتاعك_هنا" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

st.title("🤖 مساعد بطل: نظامك الصحي المبتكر")
st.write("أنا هنا عشان أراقب صحتك وأقترح عليك الأفضل دايماً يا مصطفى.")

# مدخلات المستخدم
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("الوزن (كجم)", min_value=30.0, value=75.0)
        height = st.number_input("الطول (سم)", min_value=100.0, value=175.0)
    with col2:
        age = st.number_input("العمر", min_value=10, value=20)
        goal = st.selectbox("هدفك الحالي", ["تنشيف (Cutting)", "تضخيم (Bulking)", "لياقة عامة"])

st.subheader("حالتك دلوقتي؟")
user_input = st.text_area("قولي حاسس بإيه؟ أكلت إيه؟ الجو عندك إيه؟", 
                         placeholder="مثلاً: أنا أكلت سمك النهاردة والجو حر في المنوفية..")

if st.button("اطلب نصيحة بطل الذكية"):
    if user_input:
        with st.spinner('بفكرلك في أحسن حل...'):
            prompt = f"""
            أنت مساعد صحي ذكي جداً واسمك 'بطل'. 
            المستخدم مبرمج شاب اسمه مصطفى، وزنه {weight}، طوله {height}، عمره {age}، وهدفه {goal}.
            بياناته الحالية: {user_input}.
            المطلوب منك نصيحة أكل ورياضة ومبادرة ذكية بأسلوب مصري جدع.
            """
            try:
                response = model.generate_content(prompt)
                st.success("إليك خطتك المبتكرة:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"محتاج تحط الـ API Key بتاعك عشان أشتغل.")
    else:
        st.warning("قولي أي حاجة عشان أقدر أساعدك!")
