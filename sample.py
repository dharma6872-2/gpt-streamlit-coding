# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
df = pd.read_csv('./data/titanic.csv')

# 기본 스타일 설정
plt.style.use('fivethirtyeight')
sns.set_theme(style="whitegrid")

# 페이지 구성 설정
st.set_page_config(page_title="Titanic Data Analysis", page_icon=":ship:", layout="wide")

# 경고 메시지 무시
st.set_option('deprecation.showPyplotGlobalUse', False)

# Sidebar
st.sidebar.title("타이타닉 데이터 분석")
chart_option = st.sidebar.selectbox("차트 선택", ['생존률 파이차트', '성별 생존률', '객실 등급별 생존률', '객실 등급 및 성별에 따른 나이 분포', '나이에 따른 생존 여부 히스토그램'])

# 차트 선택에 따라 해당하는 차트를 표시
if chart_option == '생존률 파이차트':
    st.subheader('타이타닉 생존률')
    fig, ax = plt.subplots(1, 2, figsize=(18, 8))
    df['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
    ax[0].set_title('Survived')
    ax[0].set_ylabel('')
    sns.countplot(x='Survived', data=df, ax=ax[1])
    ax[1].set_title('Survived')
    st.pyplot(fig)

elif chart_option == '성별 생존률':
    st.subheader('성별 생존률')
    fig, ax = plt.subplots(1, 2, figsize=(18, 8))
    df[['Sex', 'Survived']].groupby(['Sex']).mean().plot.bar(ax=ax[0])
    ax[0].set_title('Survived vs Sex')
    sns.countplot(x='Sex', hue='Survived', data=df, ax=ax[1])
    ax[1].set_title('Sex:Survived vs Dead')
    st.pyplot(fig)

elif chart_option == '객실 등급별 생존률':
    st.subheader('객실 등급별 생존률')
    fig, ax = plt.subplots(1, 2, figsize=(18, 8))
    df['Pclass'].value_counts().plot.bar(color=['#CD7F32', '#FFDF00', '#D3D3D3'], ax=ax[0])
    ax[0].set_title('Number Of Passengers By Pclass')
    ax[0].set_ylabel('Count')
    sns.countplot(x='Pclass', hue='Survived', data=df, ax=ax[1])
    ax[1].set_title('Pclass:Survived vs Dead')
    st.pyplot(fig)

elif chart_option == '객실 등급 및 성별에 따른 나이 분포':
    st.subheader('객실 등급 및 성별에 따른 나이 분포')
    fig, ax = plt.subplots(1, 2, figsize=(18, 8))
    sns.violinplot(x='Pclass', y='Age', hue='Survived', data=df, split=True, ax=ax[0])
    ax[0].set_title('Pclass and Age vs Survived')
    ax[0].set_yticks(range(0, 110, 10))
    sns.violinplot(x='Sex', y='Age', hue='Survived', data=df, split=True, ax=ax[1])
    ax[1].set_title('Sex and Age vs Survived')
    ax[1].set_yticks(range(0, 110, 10))
    st.pyplot(fig)

elif chart_option == '나이에 따른 생존 여부 히스토그램':
    st.subheader('나이에 따른 생존 여부 히스토그램')
    fig, ax = plt.subplots(1, 2, figsize=(18, 8))
    df[df.Survived == 0].Age.plot.hist(ax=ax[0], bins=20, edgecolor='black', color='red')
    ax[0].set_title('Not Survived')
    x1 = list(range(0, 85, 5))
    ax[0].set_xticks(x1)
    df[df.Survived == 1].Age.plot.hist(ax=ax[1], bins=20, color='green', edgecolor='black')
    ax[1].set_title('Survived')
    ax[1].set_xticks(range(0, 85, 5))
    st.pyplot(fig)
