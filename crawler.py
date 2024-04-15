from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pandas as pd
import time


class WeatherCrawler:

    def __init__(self, stn, year, obs):
        # 요소(obs): 평균기온, 최저기온, 최고기온, 강수량, 신적설, 평균풍속, 상대습도, 일조시간, 운량, 날씨

        url = "https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-element.do"

        with webdriver.Chrome() as driver:
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

            df = pd.DataFrame()

            months = [i for i in range(1, 13)]

            df = pd.DataFrame(columns=months)

            for idx, table_row in enumerate(driver.find_elements(By.TAG_NAME, "tr")):

                if idx == 0:
                    info_list = table_row.text.split("\n")
                    continue
                else:
                    info_list = table_row.text.split(" ")
                #     print(len(info_list[1:13]))
                df.loc[idx] = info_list[1:13]

            df.to_csv(f"{year}_{stn}_{obs}_data.csv")


if __name__ == "__main__":

    stn = "서울"
    year = "2024"
    obs = "평균기온"

    # WeatherCrawler('서울', '2024', '평균기온')
    crawler = WeatherCrawler(stn, year, obs)
