from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time


class WeatherCrawler:

    def __init__(self, stn, year, obs):
        # 요소(obs): 평균기온, 최저기온, 최고기온, 강수량, 신적설, 평균풍속, 상대습도, 일조시간, 운량, 날씨
        # 풍속이랑 날씨 조회는 안된다,,,

        url = "https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-element.do"

        chrome_options = Options()

        with webdriver.Chrome(options=chrome_options) as driver:
            driver.get(url)
            driver.implicitly_wait(3)

            # 지점, 년도, 월을 입력
            stn_input = driver.find_element(By.ID, "select-stn")
            ActionChains(driver).send_keys_to_element(stn_input, stn).perform()
            time.sleep(0.5)

            year_input = driver.find_element(By.ID, "select-yy")
            ActionChains(driver).send_keys_to_element(year_input, year).perform()
            time.sleep(0.5)

            obs_input = driver.find_element(By.ID, "select-obs")
            ActionChains(driver).send_keys_to_element(obs_input, obs).perform()
            time.sleep(0.5)

            # 조회 버튼 클릭
            button_search = driver.find_element(
                By.XPATH, '//*[@id="default-form"]/div/div[1]/input'
            )
            ActionChains(driver).click(button_search).perform()
            time.sleep(0.5)

            months = [i for i in range(1, 13)]

            df = pd.DataFrame(columns=months)

            data_table = driver.find_elements(By.TAG_NAME, "tr")

            for idx, table_row in enumerate(data_table):

                # 첫째 행 (칼럼명) 스킵
                if idx == 0:
                    # info_list = table_row.text.split("\n")
                    continue

                # 32번 째 행 (평균값) 스킵
                elif idx == len(data_table) - 1:
                    continue

                else:
                    # print(':' + table_row.text + ':')
                    t = table_row.text + '            '
                    temp = t.replace("   ", " 0 ").split()
                    # print(temp)
                    info_list = [e if e != "0" else " " for e in temp]
                    # print(info_list)
                    # info_list = table_row.text.split(' ')
                df.loc[idx] = info_list[1:13]

            df.to_csv(f"{year}_{stn}_{obs}_data.csv")  # csv 파일로 저장
            # return df


if __name__ == "__main__":

    stn = "대구"
    year = "2022"
    obs = "운량"

    # WeatherCrawler('서울', '2024', '평균기온')
    crawler = WeatherCrawler(stn, year, obs)



