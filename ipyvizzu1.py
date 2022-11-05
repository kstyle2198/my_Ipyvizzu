import pandas as pd
# import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

from ipyvizzu import Data, Config, Style
from ipyvizzustory import Slide, Step
from ipyvizzustory import Story  # or
# from ipyvizzustory.env.st.story import Story

# create data and initialize Story with the created data
df = pd.read_excel("./src/fruits.xlsx")
df["expected_income"] = df["price"] * df["quantity"]
print(df)


st.title("Ipyvizzu Test1")
st.markdown("---")
st.subheader("See DataFrame")
df

data = Data()
data.add_data_frame(df)
story = Story(data = data)

# create Slides and Steps and add them to the Story

slide1 = Slide(
    Step(
        Data.filter("record.origin == 'KOR'"),# 데이터 필터링
        Config({"x": ["item"], "y": ["quantity"], "label":"quantity",
                "title": "오렌지와 사과의 총생산량- 한국으로 필터건 상태"}),
    )
)
story.add_slide(slide1)

slide2 = Slide(
    Step(
        Data.filter(None),  # 이전 스텝에서 필터를 걸은 것을 풀어주기
        Config({"x": ["origin","item"], "y": ["quantity"],"color":"item","label":"quantity",
                "title": "국가별 오렌지와 사과 생산량"}),
    )
)
story.add_slide(slide2)

slide3 = Slide(
    Step(
        Config({"x": ["origin", "item"], "y": ["price"], "color":"item","label":"price",
                "title": "국가별 오렌지와 사과 가격2"}),
    )
)
story.add_slide(slide3)

# Step 1 - let's get back to the previous view
slide1.add_step(Step(Config({"split": False})))
# Step 2 - Add the defense function to the chart by removing it from the filter
# slide1.add_step(
#     Step(
#         Data.filter(None),
#         Config({"title": "Add New Category While Keeping the Context"}),
#     )
# )
# Add the multi-step slide to the story, just like any other slide.
story.add_slide(slide1)

slide4 = Slide(
    Step(
        Data.filter(None),  # 이전 스텝에서 필터를 걸은 것을 풀어주기
        Config({"x": ["expected_income"], "y": ["origin","item"], "color":"item","label":"expected_income",
               "title": "국가별 오렌지 및 사과의 예상 판매 수익"})
    )
)
story.add_slide(slide4)


# Switch on the tooltip that appears
# when the user hovers the mouse over a chart element.
story.set_feature("tooltip", True)


# note: in Streamlit,
# you need to set the width and height in pixels as int

story.set_size(width=800, height=480)
story.play()





# pr = df.profile_report()
# st_profile_report(pr)