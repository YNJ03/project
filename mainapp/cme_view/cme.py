import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import numpy as np
plt.rc("font", family = "Malgun Gothic")

class Cme_View :
    ### 최초 실행되는 생성자 만들기
    def __init__(self) :
        ### 데이터 읽어들이는 함수 호출
        self.initDataFrame()
        
        ### 그래프 그리는 함수 호출
        self.Graph_init()
        
    ### 데이터 읽어들이는 함수 호출
    def initDataFrame(self) :
        self.cme_month = pd.read_csv('./mainapp/cme_view/cme_month_pre.csv')

    ### 그래프 그리는 함수 호출
    def Graph_init(self) :
        # 그래프 그리기
        fig, ax1 = plt.subplots(figsize=[20, 10])

        # 첫 번째 y축 그래프 (cme 속력)
        ax1.plot(pd.to_datetime(self.cme_month['년월']), self.cme_month['LineaSpeed [km/s]'], 
                color='blue', label='Linear speed(km/s)', alpha=0.5)
        ax1.set_ylabel('linear speed(km/s)', color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')


        # 두번째 y축 그래프 (mpa)
        ax2 = ax1.twinx()
        ax2.plot(pd.to_datetime(self.cme_month['년월']), self.cme_month['MPA [deg]'], 
                color='green', label='MPA(deg)', alpha=0.5)
        ax2.set_ylabel('MPA(deg)', color='green')
        ax2.tick_params(axis='y', labelcolor='green')


        # 세 번째 y축 그래프 (흑점수)
        ax3 = ax1.twinx()
        ax3.spines['right'].set_position(('outward', 60))  # 오른쪽 Y축의 위치를 조정
        ax3.plot(pd.to_datetime(self.cme_month['년월']), self.cme_month['흑점수'], 
                color='red', label='sunspot', alpha=0.5)
        ax3.set_ylabel('흑점수', color='red')
        ax3.tick_params(axis='y', labelcolor='red')


        # 그래프의 레이블 및 범례 추가
        lines = ax1.get_lines() + ax2.get_lines() + ax3.get_lines()
        labels = [line.get_label() for line in lines]
        ax1.legend(lines, labels, loc='upper left')


        # X축 레이블을 날짜 형식으로 표시
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        ## 1년 단위로 표시
        #plt.gca().xaxis.set_major_locator(mdates.YearLocator())
        ax1.set_xlabel('YearMonth')

        plt.title('CME의 linear speed 와 mpa 태양의 흑점수 비교')
        plt.grid(True)
        plt.show()

